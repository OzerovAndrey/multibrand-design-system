#!/usr/bin/env python3
"""
Casino illustrations as code. Every fill is a colour *role* (art.primary.base, art.accent.dark …),
so the same drawing re-skins with the brand tokens.

Outputs
  site/src/art/illustrations.ts   SVG bodies whose fills are CSS variables (--illustration-primary-base …)
  --figma <file>                  the same SVGs with grey placeholder fills, one per role (for Figma import)

Run:  python3 tools/build-art.py [--figma /tmp/art_figma.json]
"""
import json, math, sys, os

ROLES = ["ink", "night", "cream", "white", "p.light", "p.base", "p.dark", "p.deep",
         "a.light", "a.base", "a.dark", "a.deep", "i.light", "i.base", "i.dark", "i.deep"]
CSSVAR = {r: "--illustration-" + r.replace("p.", "primary-").replace("a.", "accent-").replace("i.", "info-") for r in ROLES}
FIGMA_NAME = {r: "illustration/" + r.replace("p.", "primary/").replace("a.", "accent/").replace("i.", "info/") for r in ROLES}

def T(tf): return f' transform="{tf}"' if tf else ""
EO = ' fill-rule="evenodd" clip-rule="evenodd"'

def n(v): return ("%.1f" % v).rstrip("0").rstrip(".")
def n2(v): return ("%.2f" % v).rstrip("0").rstrip(".")
def fl(role, op=1):
    return f'fill="@@{role}@@"' + (f' fill-opacity="{n2(op)}"' if op != 1 else "")

def rect(x, y, w, h, r, role, op=1, tf=""):
    return f'<rect x="{n(x)}" y="{n(y)}" width="{n(w)}" height="{n(h)}" rx="{n(r)}" {fl(role, op)}{T(tf)}/>'
def circle(cx, cy, r, role, op=1):
    return f'<circle cx="{n(cx)}" cy="{n(cy)}" r="{n(r)}" {fl(role, op)}/>'
def ellipse(cx, cy, rx, ry, role, op=1, tf=""):
    return f'<ellipse cx="{n(cx)}" cy="{n(cy)}" rx="{n(rx)}" ry="{n(ry)}" {fl(role, op)}{T(tf)}/>'
def path(d, role, op=1, tf="", eo=False):
    return f'<path d="{d}" {fl(role, op)}{EO if eo else ""}{T(tf)}/>'
def poly(pts, role, op=1, tf=""):
    return path("M" + " L".join(f"{n(x)} {n(y)}" for x, y in pts) + "Z", role, op, tf)
def group(items, tf=""):
    return f'<g{T(tf)}>' + "".join(items) + "</g>"

TOKENIZE = False

def sparkle(cx, cy, r, role, op=1):
    if TOKENIZE: return "{{s:%s,%s,%s,%s,%s}}" % (n(cx), n(cy), n(r), role, n2(op))
    k = r * 0.16
    d = (f"M{n(cx)} {n(cy-r)} Q{n(cx+k)} {n(cy-k)} {n(cx+r)} {n(cy)} Q{n(cx+k)} {n(cy+k)} {n(cx)} {n(cy+r)} "
         f"Q{n(cx-k)} {n(cy+k)} {n(cx-r)} {n(cy)} Q{n(cx-k)} {n(cy-k)} {n(cx)} {n(cy-r)}Z")
    return path(d, role, op)

def coin(cx, cy, r, tone="p"):
    if TOKENIZE: return "{{c:%s,%s,%s,%s}}" % (n(cx), n(cy), n(r), tone)
    return group([
        circle(cx, cy + r * 0.12, r, "ink", 0.22),
        circle(cx, cy, r, f"{tone}.dark"), circle(cx, cy, r * 0.86, f"{tone}.base"), circle(cx, cy, r * 0.62, f"{tone}.dark", 0.55),
        circle(cx, cy, r * 0.52, f"{tone}.light", 0.85), sparkle(cx, cy, r * 0.34, f"{tone}.dark", 0.9),
        path(f"M{n(cx-r*0.7)} {n(cy-r*0.15)} A{n(r*0.72)} {n(r*0.72)} 0 0 1 {n(cx+r*0.1)} {n(cy-r*0.72)} L{n(cx+r*0.02)} {n(cy-r*0.55)} A{n(r*0.58)} {n(r*0.58)} 0 0 0 {n(cx-r*0.55)} {n(cy-r*0.12)}Z", "white", 0.5),
    ])

def rounded_poly(pts, r):
    out = []
    m = len(pts)
    for i in range(m):
        p0, p1, p2 = pts[i - 1], pts[i], pts[(i + 1) % m]
        def toward(a, b, d):
            L = math.hypot(b[0] - a[0], b[1] - a[1]); t = min(d / L, 0.5)
            return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
        a = toward(p1, p0, r); b = toward(p1, p2, r)
        out.append(("M" if i == 0 else "L") + f"{n(a[0])} {n(a[1])} Q{n(p1[0])} {n(p1[1])} {n(b[0])} {n(b[1])}")
    return " ".join(out) + "Z"

def suit(kind, cx, cy, s):
    if kind == "heart":
        return f"M{n(cx)} {n(cy+0.95*s)} C{n(cx-1.6*s)} {n(cy-0.05*s)} {n(cx-1.0*s)} {n(cy-1.1*s)} {n(cx)} {n(cy-0.35*s)} C{n(cx+1.0*s)} {n(cy-1.1*s)} {n(cx+1.6*s)} {n(cy-0.05*s)} {n(cx)} {n(cy+0.95*s)}Z"
    if kind == "diamond":
        return f"M{n(cx)} {n(cy-1.15*s)} L{n(cx+0.8*s)} {n(cy)} L{n(cx)} {n(cy+1.15*s)} L{n(cx-0.8*s)} {n(cy)}Z"
    if kind == "spade":
        return (f"M{n(cx)} {n(cy-0.95*s)} C{n(cx-1.6*s)} {n(cy+0.05*s)} {n(cx-1.0*s)} {n(cy+1.1*s)} {n(cx)} {n(cy+0.35*s)} C{n(cx+1.0*s)} {n(cy+1.1*s)} {n(cx+1.6*s)} {n(cy+0.05*s)} {n(cx)} {n(cy-0.95*s)}Z "
                f"M{n(cx)} {n(cy+0.25*s)} L{n(cx-0.5*s)} {n(cy+1.25*s)} L{n(cx+0.5*s)} {n(cy+1.25*s)}Z")
    r = 0.55 * s  # club
    return (f"M{n(cx)} {n(cy-1.1*s)} A{n(r)} {n(r)} 0 1 1 {n(cx+0.5*s)} {n(cy-0.2*s)} A{n(r)} {n(r)} 0 1 1 {n(cx+0.9*s)} {n(cy+0.5*s)} A{n(r)} {n(r)} 0 1 1 {n(cx+0.15*s)} {n(cy+0.55*s)} L{n(cx+0.5*s)} {n(cy+1.3*s)} H{n(cx-0.5*s)} L{n(cx-0.15*s)} {n(cy+0.55*s)} "
            f"A{n(r)} {n(r)} 0 1 1 {n(cx-0.9*s)} {n(cy+0.5*s)} A{n(r)} {n(r)} 0 1 1 {n(cx-0.5*s)} {n(cy-0.2*s)} A{n(r)} {n(r)} 0 1 1 {n(cx)} {n(cy-1.1*s)}Z")

def rank_A(x, y, s):
    d = "M0 14 L6 0 L12 14 H9.4 L8.6 11.4 H3.4 L2.6 14 Z M4.1 9.2 H7.9 L6 3.6 Z"
    return path(d, "ink", 1, f"translate({n(x)} {n(y)}) scale({n(s)})", eo=True)

def star5(cx, cy, R, r):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5; rad = R if i % 2 == 0 else r
        pts.append((cx + rad * math.cos(a), cy + rad * math.sin(a)))
    return pts

# ------------------------------------------------------------------ illustrations (240 × 240 unless noted)
def slots():
    b = [ellipse(120, 224, 86, 8, "ink", 0.35),
         rect(34, 26, 172, 190, 20, "p.dark"), rect(40, 32, 160, 178, 16, "p.base"), rect(40, 32, 160, 10, 5, "white", 0.25),
         rect(60, 40, 120, 26, 13, "ink")]
    for i, x in enumerate([76, 98, 120, 142, 164]): b.append(circle(x, 53, 4.5, "p.light" if i % 2 == 0 else "a.light"))
    b += [rect(50, 74, 140, 92, 10, "p.deep"), rect(56, 80, 128, 80, 7, "ink")]
    for x in (60, 102, 144):
        b += [rect(x, 85, 36, 70, 5, "cream"), rect(x, 85, 36, 12, 5, "ink", 0.12), rect(x, 143, 36, 12, 5, "ink", 0.12)]
    b.append(rect(56, 118.5, 128, 3, 1.5, "p.deep", 0.9))
    seven = "M0 0 H24 V7 L12 36 H2 L14 8 H0 Z"
    for x in (60, 102, 144):
        tx = x + 6; ty = 102
        b += [path(seven, "a.deep", 1, f"translate({n(tx+1.5)} {n(ty+2)})"), path(seven, "a.base", 1, f"translate({n(tx)} {n(ty)})"),
              rect(tx + 1, ty + 1, 20, 2.5, 1.2, "white", 0.45, f"translate(0 0)")]
    b += [rect(212, 78, 9, 60, 4, "p.deep"), rect(204, 120, 14, 10, 3, "p.deep"), circle(216.5, 72, 12, "a.dark"), circle(216.5, 72, 10, "a.base"), circle(213, 68, 4, "white", 0.45)]
    for x, r in ((80, "a.base"), (120, "p.light"), (160, "a.base")): b += [circle(x, 187, 8, "p.deep"), circle(x, 186, 6.5, r), circle(x - 2, 184, 2, "white", 0.5)]
    b += [rect(64, 199, 112, 14, 7, "ink"), coin(84, 207, 9), coin(104, 211, 9), coin(150, 208, 9), coin(24, 116, 10), coin(222, 196, 9),
          sparkle(24, 48, 10, "p.light"), sparkle(224, 26, 8, "white"), sparkle(16, 160, 6, "white"), sparkle(226, 168, 8, "p.light")]
    return 240, 240, "".join(b)

def roulette():
    cx, cy = 120, 122
    b = [ellipse(120, 226, 80, 7, "ink", 0.35), circle(cx, cy, 92, "p.dark"), circle(cx, cy, 88, "p.light"), circle(cx, cy, 84, "p.base"), circle(cx, cy, 80, "ink")]
    N = 24; r1, r2 = 56, 78
    for i in range(N):
        a0 = 2 * math.pi * i / N - math.pi / 2; a1 = 2 * math.pi * (i + 1) / N - math.pi / 2
        p = lambda r, a: (cx + r * math.cos(a), cy + r * math.sin(a))
        x1, y1 = p(r2, a0); x2, y2 = p(r2, a1); x3, y3 = p(r1, a1); x4, y4 = p(r1, a0)
        d = f"M{n(x1)} {n(y1)} A{r2} {r2} 0 0 1 {n(x2)} {n(y2)} L{n(x3)} {n(y3)} A{r1} {r1} 0 0 0 {n(x4)} {n(y4)}Z"
        role = "i.base" if i == 0 else ("a.base" if i % 2 == 1 else "night")
        b.append(path(d, role))
        px, py = p(80, a0); b.append(circle(px, py, 1.6, "white", 0.9))
    b += [circle(cx, cy, 55, "p.dark"), circle(cx, cy, 51, "p.base"), circle(cx, cy, 46, "night"), circle(cx, cy, 38, "p.dark"), circle(cx, cy, 34, "p.light", 0.6)]
    for a in (0, 45, 90, 135): b.append(rect(cx - 3, cy - 46, 6, 92, 3, "p.light", 1, f"rotate({a} {cx} {cy})"))
    b += [circle(cx, cy, 13, "p.dark"), circle(cx, cy, 10.5, "p.base"), circle(cx, cy, 6, "p.light"), circle(cx - 1.5, cy - 1.5, 2.6, "white", 0.8)]
    ba = math.radians(-40); bx, by = cx + 68 * math.cos(ba), cy + 68 * math.sin(ba)
    b += [circle(bx + 1.5, by + 2, 6, "ink", 0.35), circle(bx, by, 6, "white"), circle(bx - 1.6, by - 1.8, 2, "cream")]
    b += [path(f"M{cx-70} {cy-58} A92 92 0 0 1 {cx+10} {cy-90} L{cx+6} {cy-80} A84 84 0 0 0 {cx-62} {cy-52}Z", "white", 0.28),
          sparkle(20, 40, 10, "p.light"), sparkle(224, 44, 8, "white"), sparkle(214, 196, 9, "p.light"), sparkle(22, 200, 6, "white"), coin(214, 108, 8)]
    return 240, 240, "".join(b)

def cards():
    def card(rot, kind, red):
        role = "a.base" if red else "ink"
        items = [rect(81, 96, 84, 120, 10, "ink", 0.28), rect(78, 90, 84, 120, 10, "cream"), rect(82, 94, 76, 112, 7, "white", 0.55),
                 rank_A(86, 99, 0.8), path(suit(kind, 92, 122, 4.6), role),
                 path(suit(kind, 120, 150, 21), role), path(suit(kind, 120, 150, 21), "white", 0.12)]
        items[3] = path("M0 14 L6 0 L12 14 H9.4 L8.6 11.4 H3.4 L2.6 14 Z M4.1 9.2 H7.9 L6 3.6 Z", role, 1, "translate(86 99) scale(0.8)", eo=True)
        return group(items, f"translate(0 -8) rotate({rot} 120 222)")
    b = [ellipse(120, 224, 84, 7, "ink", 0.3), card(-38, "spade", False), card(0, "heart", True), card(38, "diamond", True)]
    def chip(cx, cy, r, tone):
        s = [circle(cx, cy + 2, r, "ink", 0.3), circle(cx, cy, r, f"{tone}.dark"), circle(cx, cy, r * 0.9, f"{tone}.base")]
        for k in range(8): s.append(rect(cx - r * 0.13, cy - r * 0.92, r * 0.26, r * 0.28, 1.5, "cream", 1, f"rotate({k*45} {n(cx)} {n(cy)})"))
        s += [circle(cx, cy, r * 0.58, f"{tone}.dark"), circle(cx, cy, r * 0.5, f"{tone}.light"), sparkle(cx, cy, r * 0.32, f"{tone}.dark")]
        return group(s)
    b += [chip(46, 190, 24, "p"), chip(198, 196, 20, "i"), sparkle(28, 60, 10, "p.light"), sparkle(214, 40, 9, "white"), sparkle(226, 130, 6, "p.light"), coin(206, 86, 9), coin(24, 118, 8)]
    return 240, 240, "".join(b)

def chips():
    def stack(cx, base, cnt, rx, ry, t, tone, stripe):
        s = []
        for i in range(cnt):
            y = base - i * t
            s += [ellipse(cx, y, rx, ry, f"{tone}.deep"), rect(cx - rx, y - t, rx * 2, t, 0, f"{tone}.dark"), ellipse(cx, y - t, rx, ry, f"{tone}.base")]
            for k in (-0.66, -0.33, 0, 0.33, 0.66):
                px = cx + rx * k; py = y - t * 0.5 + ry * math.sqrt(max(0, 1 - k * k)) * 0.98
                s.append(rect(px - 5, py - t * 0.42, 10, t * 0.8, 2, stripe, 0.95))
            s.append(ellipse(cx, y - t, rx * 0.8, ry * 0.8, f"{tone}.light", 0.5))
            s.append(ellipse(cx, y - t, rx * 0.66, ry * 0.66, f"{tone}.base"))
        s += [ellipse(cx, base - (cnt - 1) * t - t, rx * 0.34, ry * 0.34, f"{tone}.dark", 0.9), ellipse(cx, base - (cnt - 1) * t - t - 0.5, rx * 0.2, ry * 0.2, f"{tone}.light")]
        return group(s)
    b = [ellipse(120, 214, 100, 12, "ink", 0.32), stack(122, 168, 5, 46, 16, 13, "p", "cream"), stack(60, 200, 3, 38, 14, 13, "a", "cream"), stack(184, 204, 4, 38, 14, 13, "i", "cream")]
    cx, cy, r = 120, 62, 32
    f = [circle(cx + 2, cy + 4, r, "ink", 0.3), circle(cx, cy, r, "a.dark"), circle(cx, cy, r * 0.93, "a.base")]
    for k in range(12): f.append(rect(cx - 4, cy - r * 0.93, 8, 10, 2, "cream", 1, f"rotate({k*30} {cx} {cy})"))
    f += [circle(cx, cy, r * 0.62, "a.dark"), circle(cx, cy, r * 0.54, "a.light")]
    f.append(poly(star5(cx, cy, r * 0.4, r * 0.17), "a.dark"))
    f.append(path(f"M{cx-26} {cy-8} A28 28 0 0 1 {cx+2} {cy-27} L{cx} {cy-21} A22 22 0 0 0 {cx-21} {cy-7}Z", "white", 0.4))
    b.append(group(f, f"rotate(-14 {cx} {cy})"))
    b += [coin(30, 96, 10), coin(210, 112, 9), coin(200, 40, 8), sparkle(30, 40, 10, "p.light"), sparkle(214, 76, 10, "white"), sparkle(178, 20, 6, "p.light"), sparkle(20, 140, 6, "white")]
    return 240, 240, "".join(b)

def cube(cx, cy, s, faces, pip, pips, edge):
    w, h = s * 0.866, s * 0.5
    P0 = (cx, cy); ex = (w, -h); ey = (-w, -h)
    top = [P0, (P0[0] + ex[0], P0[1] + ex[1]), (P0[0] + ex[0] + ey[0], P0[1] + ex[1] + ey[1]), (P0[0] + ey[0], P0[1] + ey[1])]
    left = [P0, (P0[0] + ey[0], P0[1] + ey[1]), (P0[0] + ey[0], P0[1] + ey[1] + s), (P0[0], P0[1] + s)]
    right = [P0, (P0[0] + ex[0], P0[1] + ex[1]), (P0[0] + ex[0], P0[1] + ex[1] + s), (P0[0], P0[1] + s)]
    rr = s * 0.09
    out = [path(rounded_poly(left, rr), faces[1]), path(rounded_poly(right, rr), faces[2]), path(rounded_poly(top, rr), faces[0])]
    if edge: out += [path(rounded_poly(right, rr), "ink", edge), path(rounded_poly(left, rr), "ink", edge / 2)]
    def face_pips(origin, u, v, plist):
        res = []
        K = 0.5523
        def T(a, b): return (origin[0] + u[0] * a + v[0] * b, origin[1] + u[1] * a + v[1] * b)
        for (a, b) in plist:
            r = 0.085
            seg = f"M{n(T(a + r, b)[0])} {n(T(a + r, b)[1])}"
            # cubic circle approximation in unit space, mapped through the affine transform
            c = [((a + r, b), (a + r, b + K * r), (a + K * r, b + r), (a, b + r)),
                 ((a, b + r), (a - K * r, b + r), (a - r, b + K * r), (a - r, b)),
                 ((a - r, b), (a - r, b - K * r), (a - K * r, b - r), (a, b - r)),
                 ((a, b - r), (a + K * r, b - r), (a + r, b - K * r), (a + r, b))]
            for _, p1, p2, p3 in c:
                q1, q2, q3 = T(*p1), T(*p2), T(*p3)
                seg += f" C{n(q1[0])} {n(q1[1])} {n(q2[0])} {n(q2[1])} {n(q3[0])} {n(q3[1])}"
            res.append(path(seg + "Z", pip))
        return res
    def grid(k):
        pts = {1: [(.5, .5)], 2: [(.28, .28), (.72, .72)], 3: [(.26, .26), (.5, .5), (.74, .74)], 4: [(.28, .28), (.72, .28), (.28, .72), (.72, .72)],
               5: [(.27, .27), (.73, .27), (.5, .5), (.27, .73), (.73, .73)], 6: [(.3, .25), (.7, .25), (.3, .5), (.7, .5), (.3, .75), (.7, .75)]}
        return pts[k]
    out += face_pips(P0, ey, (0, s), grid(pips[1]))
    out += face_pips(P0, ex, (0, s), grid(pips[2]))
    # top face: affine from unit square (u along ex, v along ey) with origin P0
    out += face_pips(P0, ex, ey, grid(pips[0]))
    return group(out)

def dice():
    b = [ellipse(112, 226, 92, 9, "ink", 0.3)]
    b.append(cube(98, 122, 70, ("white", "cream", "cream"), "a.base", (5, 3, 2), 0.22))
    b.append(cube(172, 186, 50, ("a.light", "a.base", "a.dark"), "white", (2, 4, 3), 0.0))
    b += [coin(34, 190, 11), coin(50, 205, 9, "p"), coin(208, 96, 9), sparkle(32, 56, 10, "p.light"), sparkle(206, 44, 9, "white"), sparkle(224, 140, 6, "p.light"), sparkle(20, 130, 6, "white")]
    return 240, 240, "".join(b)

def gem():
    cx, cy = 120, 126
    b = []
    for k in range(14):
        a = 2 * math.pi * k / 14; R = 112 if k % 2 == 0 else 84; dl = math.radians(6)
        b.append(poly([(cx, cy), (cx + R * math.cos(a - dl), cy + R * math.sin(a - dl)), (cx + R * math.cos(a + dl), cy + R * math.sin(a + dl))], "p.light", 0.16))
    b.append(ellipse(120, 222, 72, 8, "ink", 0.32))
    A, B, C, D, E = (80, 76), (160, 76), (200, 112), (120, 200), (40, 112)
    M, G, H = (120, 76), (96, 112), (144, 112)
    facets = [([A, M, G], "a.light"), ([M, B, H], "a.light"), ([A, G, E], "a.base"), ([B, C, H], "a.dark"), ([M, G, H], "white"),
              ([E, G, D], "a.base"), ([G, H, D], "a.light"), ([H, C, D], "a.dark")]
    for pts, role in facets: b.append(poly(pts, role, 1 if role != "white" else 0.42))
    b += [poly([M, G, H], "a.light", 0.9), poly([A, M, G], "white", 0.38), poly([E, G, D], "white", 0.14), poly([H, C, D], "ink", 0.18), poly([B, C, H], "ink", 0.12)]
    b += [poly([(96, 112), (120, 200), (108, 112)], "white", 0.22)]
    b += [sparkle(200, 60, 13, "white"), sparkle(44, 72, 10, "p.light"), sparkle(214, 160, 8, "p.light"), sparkle(34, 168, 7, "white"), coin(214, 116, 9), coin(24, 130, 8)]
    return 240, 240, "".join(b)

def chest():
    W, Hh = 400, 300
    b = [circle(200, 140, 130, "p.base", 0.06), circle(200, 140, 100, "p.base", 0.07), circle(200, 140, 70, "p.light", 0.08), ellipse(200, 276, 160, 14, "ink", 0.33)]
    b += [path("M66 156 L66 112 C66 70 110 48 200 48 C290 48 334 70 334 112 L334 156 Z", "p.deep"), path("M80 156 L80 116 C80 82 118 62 200 62 C282 62 320 82 320 116 L320 156 Z", "a.deep"),
          rect(96, 56, 22, 100, 0, "p.dark", 0.7), rect(282, 56, 22, 100, 0, "p.dark", 0.7)]
    b += [group([rect(88, 110, 44, 64, 5, "cream"), rect(92, 114, 36, 56, 3, "white", 0.6), rect(96, 124, 28, 4, 2, "a.base"), rect(96, 134, 20, 4, 2, "ink", 0.4)], "rotate(-18 110 140)"),
          group([rect(268, 106, 44, 64, 5, "cream"), rect(272, 110, 36, 56, 3, "white", 0.6), path(suit("heart", 290, 138, 9), "a.base")], "rotate(16 290 140)")]
    coins = []
    rows = [(150, 9, 92, 24), (134, 8, 104, 24), (118, 7, 116, 24), (102, 5, 140, 24), (88, 3, 164, 24)]
    for ri, (y, cnt, x0, gap) in enumerate(rows):
        for i in range(cnt):
            x = x0 + i * gap + ((ri * 7 + i * 5) % 9 - 4)
            coins.append(coin(x + 8, y + ((i * 3 + ri) % 5 - 2), 15, "p" if (i + ri) % 4 else "p"))
    b += coins
    def gem_s(cx, cy, s, role):
        return group([poly([(cx - s, cy - s * 0.4), (cx - s * 0.5, cy - s * 0.9), (cx + s * 0.5, cy - s * 0.9), (cx + s, cy - s * 0.4), (cx, cy + s)], role + ".base"),
                      poly([(cx - s, cy - s * 0.4), (cx, cy - s * 0.25), (cx, cy + s)], role + ".dark", 0.7), poly([(cx - s * 0.5, cy - s * 0.9), (cx + s * 0.5, cy - s * 0.9), (cx, cy - s * 0.25)], role + ".light")])
    b += [gem_s(160, 84, 15, "a"), gem_s(232, 78, 17, "a"), gem_s(198, 62, 13, "i")]
    b += [rect(60, 150, 280, 110, 14, "a.dark"), rect(60, 150, 280, 18, 6, "p.base"), rect(60, 150, 280, 6, 3, "p.light", 0.8), rect(60, 176, 280, 8, 0, "p.deep", 0.55),
          rect(92, 150, 22, 110, 0, "p.base"), rect(286, 150, 22, 110, 0, "p.base"), rect(92, 150, 6, 110, 0, "p.light", 0.5), rect(286, 150, 6, 110, 0, "p.light", 0.5),
          rect(60, 252, 280, 8, 4, "ink", 0.3)]
    for x in (103, 297):
        for y in (192, 222): b.append(circle(x, y, 4.5, "p.light")); b.append(circle(x - 1, y - 1, 1.6, "white", 0.7))
    b += [rect(170, 168, 60, 60, 12, "p.dark"), rect(174, 172, 52, 52, 9, "p.base"), circle(200, 194, 8, "ink"), rect(197, 196, 6, 16, 3, "ink"), rect(174, 172, 52, 8, 4, "white", 0.3)]
    b += [coin(60, 258, 13), coin(80, 268, 10, "p"), coin(334, 262, 12),
          sparkle(40, 60, 16, "p.light"), sparkle(360, 70, 18, "white"), sparkle(58, 190, 9, "white"), sparkle(346, 190, 10, "p.light"), sparkle(200, 24, 12, "white"),
          coin(110, 30, 11), coin(300, 26, 10), coin(52, 110, 9), coin(350, 120, 9)]
    return W, Hh, "".join(b)

def trophy():
    cx = 120
    b = []
    for k in range(12):
        a = 2 * math.pi * k / 12; R = 112 if k % 2 == 0 else 86; dl = math.radians(7)
        b.append(poly([(cx, 118), (cx + R * math.cos(a - dl), 118 + R * math.sin(a - dl)), (cx + R * math.cos(a + dl), 118 + R * math.sin(a + dl))], "p.light", 0.15))
    b.append(ellipse(120, 226, 76, 8, "ink", 0.32))
    for side in (-1, 1):
        for i in range(9):
            a = math.radians(105 + i * 16); r = 92
            x = cx + side * r * math.cos(a) * -1; y = 118 + r * math.sin(a) * 0.98
            b.append(ellipse(x, y, 5, 11, "p.light" if i % 2 else "p.base", 1, f"rotate({n(side * (a * 180 / math.pi - 90) * -1)} {n(x)} {n(y)})"))
    b += [path("M38 76 a24 28 0 1 0 48 0 a24 28 0 1 0 -48 0 Z M48 76 a14 18 0 1 0 28 0 a14 18 0 1 0 -28 0Z", "p.dark", 1, "translate(6 0)", eo=True),
          path("M38 76 a24 28 0 1 0 48 0 a24 28 0 1 0 -48 0 Z M48 76 a14 18 0 1 0 28 0 a14 18 0 1 0 -28 0Z", "p.dark", 1, "translate(102 0)", eo=True)]
    b += [path("M68 40 H172 C172 98 154 134 120 140 C86 134 68 98 68 40 Z", "p.base"), path("M68 40 H100 C100 100 108 130 120 140 C86 134 68 98 68 40 Z", "p.dark", 0.8),
          path("M78 46 C80 88 90 118 106 132 L101 133 C86 118 76 90 74 46Z", "white", 0.42), rect(60, 32, 120, 14, 7, "p.light"), rect(60, 32, 120, 5, 2.5, "white", 0.45)]
    b += [poly(star5(120, 82, 24, 10), "cream"), poly(star5(120, 82, 17, 7), "a.base"), path("M104 44 H136 L120 62Z", "white", 0)]
    b += [rect(107, 138, 26, 34, 4, "p.dark"), ellipse(120, 156, 22, 9, "p.base"), ellipse(120, 154, 22, 8, "p.light", 0.6),
          rect(84, 170, 72, 16, 6, "p.base"), rect(72, 184, 96, 28, 9, "a.dark"), rect(72, 184, 96, 8, 4, "white", 0.15), rect(92, 192, 56, 14, 4, "p.light"), rect(98, 196, 44, 3, 1.5, "a.dark", 0.6)]
    conf = [(30, 40, "a.light", 20), (210, 36, "i.light", -30), (44, 150, "p.light", 55), (204, 156, "a.light", -20), (18, 110, "white", 10), (226, 100, "p.light", 70), (52, 20, "white", -40), (188, 14, "a.light", 25), (24, 196, "i.light", 30), (218, 196, "white", 50)]
    for x, y, role, a in conf: b.append(rect(x, y, 9, 4, 1.4, role, 1, f"rotate({a} {x+4} {y+2})"))
    b += [sparkle(22, 76, 10, "p.light"), sparkle(220, 66, 12, "white"), sparkle(196, 208, 8, "p.light"), sparkle(40, 200, 7, "white"), coin(212, 134, 9), coin(26, 170, 8)]
    return 240, 240, "".join(b)

ART = {"slots": slots, "roulette": roulette, "cards": cards, "chips": chips, "dice": dice, "gem": gem, "chest": chest, "trophy": trophy}


USE_SYMBOLS = False

def emb(name, x, y, k):
    w, h, body = ART[name]()
    if USE_SYMBOLS:
        return f'<use href="#ill-{name}" x="{n(x)}" y="{n(y)}" width="{n(w * k)}" height="{n(h * k)}"/>'
    return group([body], f"translate({n(x)} {n(y)}) scale({n(k)})")

def rays(cx, cy, W, H, cnt=16):
    out = []
    R = math.hypot(W, H)
    for i in range(cnt):
        a = 2 * math.pi * i / cnt; dl = math.pi / cnt * 0.55
        out.append(poly([(cx, cy), (cx + R * math.cos(a - dl), cy + R * math.sin(a - dl)), (cx + R * math.cos(a + dl), cy + R * math.sin(a + dl))], "white", 0.10 if i % 2 else 0.05))
    return out

SCENES = {}

def scene(fn):
    def body():
        W, H, back, embeds, front = fn()
        mid = "".join(emb(nm, x, y, k) for nm, x, y, k in embeds)
        return W, H, "".join(back) + mid + "".join(front)
    SCENES[fn.__name__] = fn
    return body

@scene
def jackpot():
    W, H = 560, 240
    back = rays(280, 150, W, H) + [circle(280, 150, 120, "p.light", 0.16), circle(280, 150, 84, "white", 0.10)]
    embeds = [("chips", -16, 28, 0.86), ("cards", 350, 22, 0.88), ("chest", 116, -6, 0.84)]
    front = [coin(x, y, r) for x, y, r in ((70, 30, 11), (496, 170, 12), (262, 12, 9), (520, 60, 9), (36, 176, 10))]
    front += [sparkle(x, y, r, c) for x, y, r, c in ((120, 24, 12, "white"), (446, 30, 14, "p.light"), (540, 120, 9, "white"), (24, 100, 9, "p.light"), (300, 220, 10, "white"), (200, 226, 7, "p.light"))]
    return W, H, back, embeds, front

@scene
def arena():
    W, H = 360, 180
    back = rays(180, 90, W, H, 14) + [circle(180, 96, 84, "p.light", 0.14)]
    for x, y, w, h, t in ((88, 142, 62, 38, "a"), (149, 124, 62, 56, "p"), (210, 154, 62, 26, "i")):
        back += [rect(x, y, w, h, 4, f"{t}.dark"), rect(x, y, w, 9, 4, f"{t}.light"), rect(x, y, w, 3, 1.5, "white", 0.55), rect(x + w - 8, y + 9, 8, h - 9, 0, "ink", 0.18)]
    back += [poly(star5(180, 152, 12, 5), "cream"), poly(star5(119, 160, 9, 4), "cream"), poly(star5(241, 166, 7, 3), "cream")]
    embeds = [("trophy", 101, -18, 0.66), ("gem", 6, 44, 0.38), ("chips", 262, 60, 0.4)]
    front = [coin(x, y, r) for x, y, r in ((40, 30, 9), (326, 120, 10), (300, 24, 8), (40, 150, 8))]
    front += [sparkle(x, y, r, c) for x, y, r, c in ((72, 16, 11, "white"), (330, 60, 12, "p.light"), (20, 96, 8, "white"), (346, 168, 8, "white"))]
    return W, H, back, embeds, front

ART.update({"jackpot": jackpot, "arena": arena})

def render(name, mode):
    w, h, body = ART[name]()
    def sub(m):
        r = m.group(1)
        if mode == "figma":
            i = ROLES.index(r) + 1; v = i * 8
            return "#%02X%02X%02X" % (v, v, v)
        return f"var({CSSVAR[r]})"
    import re
    body = re.sub(r"@@([a-z.]+)@@", sub, body)
    return w, h, body

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    USE_SYMBOLS = True
    out = {k: {"w": render(k, "css")[0], "h": render(k, "css")[1], "body": render(k, "css")[2]} for k in ART}
    KITS = [k for k in ART if k not in SCENES]
    sprite = "".join(f'<symbol id="ill-{k}" viewBox="0 0 {out[k]["w"]} {out[k]["h"]}">{out[k]["body"]}</symbol>' for k in KITS)
    for k in KITS: out[k]["body"] = f'<use href="#ill-{k}" width="{out[k]["w"]}" height="{out[k]["h"]}"/>'
    ts = "// GENERATED by tools/build-art.py — casino illustrations; every fill is an --illustration-* component token variable.\nexport type IllusKey = " + " | ".join(f'"{k}"' for k in ART) + ";\n"
    ts += "export const ILLUSTRATIONS: Record<IllusKey, { w: number; h: number; body: string }> = " + json.dumps(out, ensure_ascii=False) + ";\n"
    ts += "export const SPRITE = " + json.dumps(sprite, ensure_ascii=False) + ";\n"
    dst = os.path.join(here, "..", "site", "src", "art"); os.makedirs(dst, exist_ok=True)
    open(os.path.join(dst, "illustrations.ts"), "w").write(ts)
    print("site/src/art/illustrations.ts", len(ts), "bytes")
    if "--figma" in sys.argv:
        f = sys.argv[sys.argv.index("--figma") + 1]
        import re
        TOKENIZE = True
        USE_SYMBOLS = False
        def figma_body(body):
            def sub(m):
                v = (ROLES.index(m.group(1)) + 1) * 8
                return "#%02X%02X%02X" % (v, v, v)
            return re.sub(r"@@([a-z.]+)@@", sub, body)
        def svg(w, h, body): return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{figma_body(body)}</svg>'
        data = {}
        for k, fn in ART.items():
            if k in SCENES:
                W, H, back, embeds, front = SCENES[k]()
                data[k] = {"w": W, "h": H, "back": svg(W, H, "".join(back)), "front": svg(W, H, "".join(front)), "embeds": embeds}
            else:
                w, h, body = fn(); data[k] = {"w": w, "h": h, "svg": svg(w, h, body)}
        data["_roles"] = {("#%02X%02X%02X" % (((i + 1) * 8,) * 3)): FIGMA_NAME[r] for i, r in enumerate(ROLES)}
        json.dump(data, open(f, "w"), ensure_ascii=False, separators=(",", ":"))
        print(f, {k: (len(v.get("svg", "")) or len(v["back"]) + len(v["front"])) for k, v in data.items() if k != "_roles"})
