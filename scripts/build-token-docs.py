#!/usr/bin/env python3
"""
Multibrand Design System — генератор документації токенів.

Читає Token Studio JSON (tokens/*.json, $themes.json, $metadata.json)
і пише skill-подібні записи в docs/tokens/:
  SKILL.md                      індекс: шари, сети, теми, правила, карта файлів
  references/core.md            примітиви
  references/brand.md           3 бренди поруч
  references/map.md             рампи
  references/theme.md           light / dark поруч
  references/typography.md      text styles
  references/components/<c>.md  по файлу на компонент

Запуск:  python3 scripts/build-token-docs.py [tokens_dir] [out_dir]
За замовчуванням: tokens/  →  docs/tokens/
Ручні частини (мапінг text styles, анатомія) — у COMPONENT_NOTES нижче.
"""
import json, re, sys, os, datetime
from collections import OrderedDict

TOK = sys.argv[1] if len(sys.argv) > 1 else "tokens"
OUT = sys.argv[2] if len(sys.argv) > 2 else "docs/tokens"
BRANDS = ["aurum", "nova", "fiesta"]
MODES = ["light", "dark"]

# ---------------------------------------------------------------- ручні нотатки
COMPONENT_NOTES = {
    "button": {
        "title": "Button",
        "figma": "Button (component set) · Variant × Size × State × Label",
        "anatomy": "Контейнер (auto-layout H) → `Icon left` (instance) · `Label` (text) · `Icon right` (instance). "
                   "Icon-only варіант = `Label=False`.",
        "variants": "Variant: Primary / Secondary / Text · Size: xs–xl · State: Default / Hover / Active / Disabled",
        "text_styles": [("xs", "label/sm"), ("sm", "label/md"), ("md", "label/md"), ("lg", "label/lg"), ("xl", "label/xl")],
        "notes": [
            "Власних typography-токенів немає — текст бере text style зі шкали.",
            "Іконки за замовчуванням: left `plus`, right `chevron-right` (Static — Icons).",
        ],
    },
    "input": {
        "title": "Input",
        "figma": "Input (component set) · Size × State",
        "anatomy": "Wrapper (auto-layout V, gap `input.wrapper.gap`) → `Label` (text) · `Field` (auto-layout H) · `Helper` (text). "
                   "Field → `Icon left` · `Placeholder` · `Value` · `Icon right`.",
        "variants": "Size: sm / md / lg · State: Default / Hover / Active / Disabled (focus не робимо)",
        "text_styles": [("sm", "value/placeholder body/sm/regular · label label/sm · helper caption/md"),
                        ("md", "value/placeholder body/md/regular · label label/md · helper caption/md"),
                        ("lg", "value/placeholder body/lg/regular · label label/md · helper caption/md")],
        "notes": [
            "Placeholder і Value фарбуються одним токеном `input.color.*` — окремого `placeholder.color` немає.",
            "Властивості: ✏️ Label / Placeholder / Value / Helper · booleans Label, Helper, Placeholder, Value, ⬅️ Icon, Icon ➡️ · swap 💠 Icon left / right.",
            "Іконки за замовчуванням: left `search`, right `close` (Static — Icons).",
            "Висоти sm/md/lg = Button sm/md/lg (32/40/48) — стають в один ряд.",
        ],
    },
    "card": {
        "title": "Card Default",
        "figma": "Card Default (component set) · Size",
        "anatomy": "Контейнер (auto-layout V, padding `card.default.paddingH/V.{size}`, gap `card.default.gap.{size}`) → "
                   "`Slot 1` · `Slot 2` · `Slot 3` (інстанси `_Card slot`).",
        "variants": "Size: xs (mobile) / sm (tablet) / md (desktop). Станів немає — статичний контейнер",
        "notes": [
            "Власного контенту немає — вміст підставляється через instance swap 💠 Slot 1–3; Slot 2 і Slot 3 вмикаються булеанами.",
            "Ширина в сеті — референс (320 / 400 / 480); у макеті картка тягнеться (Fill) по колонці сітки.",
            "Padding: xs 12 · sm 16 · md 24; gap: xs 8 · sm 10 · md 12 — з існуючої брендової шкали `space.*`.",
        ],
    },
    "media": {
        "title": "Media",
        "figma": "Media (component set) · Ratio × State",
        "anatomy": "Контейнер (fill `media.bg`, radius `media.borderRadius`, clip) → `image` (rectangle, image fill) · `overlay` (`media.overlay.bg`) · "
                   "`icon` (fallback, `media.fallback.iconSize`) · `Content` (slot, padding `media.padding`, gap `media.gap`).",
        "variants": "Ratio: 1:1 / 4:3 / 16:9 / 3:4 · State: Loaded / Loading / Error",
        "notes": [
            "Медіа-примітив: зображення з брендовим радіусом і станами завантаження; основа для Thumb, PromoCard, банерів.",
            "Loading — фон `media.skeleton.bg`; Error — іконка `placeholder-default` кольору `media.fallback.iconColor`.",
            "Властивості: boolean Overlay · swap 💠 Fallback icon · slot Content (бейджі, кнопки).",
            "Ratio — фіксовані пропорції; у макеті Fill по ширині, висота за пропорцією. Картинка міняється заливкою шару image.",
        ],
    },
    "header": {
        "title": "Header",
        "figma": "Header (component set) · State  ·  частини: Logo (component set · Brand), Balance (component)",
        "anatomy": "Контейнер (auto-layout H, space-between, padding `header.paddingH/V`, нижній бордер `header.br` × `header.borderWidth`) → "
                   "`Logo` (instance) · `Actions` (auto-layout H, gap `header.gap`) → `Tools` (gap `header.actions.gap`: Search · Support) · `Balance`.",
        "variants": "State: Logged in / Search open / Logged out",
        "notes": [
            "Організм: збирається з Button, Input, Logo і Balance — власних кольорів у контролах немає, тільки контейнер і лого.",
            "Logged in: Search і Support = Button Secondary md icon-only (іконки `search`, `support`), далі Balance.",
            "Search open: замість кнопки пошуку — Input md State=Active, Label off, іконки `search` / `close`, ширина 320 (референс, у макеті — Fill).",
            "Logged out: тільки Log in (Button Secondary md) і Sign up (Button Primary md).",
            "Висота 72 не токен: `header.paddingV` 16 × 2 + control md 40.",
            "Logo — asset, не токен: Brand-варіант (Aurum / Nova / Fiesta) обирається разом із Brand-mode; кольори — `header.logo.iconColor` (марка) і `header.logo.color` (wordmark), тому лого саме перемикається light/dark.",
            "Logo, Balance, Search, Support, Log in, Sign up — exposed instances: властивості вкладених компонентів доступні з панелі хедера.",
        ],
    },
    "balance": {
        "title": "Balance",
        "figma": "Balance (component) · молекула всередині Header",
        "anatomy": "Контейнер (auto-layout H, bg `balance.bg`, radius `balance.borderRadius`, paddingL `balance.paddingL`, paddingR 0, gap `balance.gap`) → "
                   "`Icon` (instance `wallet`, `balance.iconSize`, `balance.iconColor`) · `Amount` (text) · `Deposit` (Button Primary md).",
        "variants": "Без варіантів. Властивості: ✏️ Amount · 💰 Icon (boolean) · 💠 Icon (swap)",
        "text_styles": [("Amount", "label/md")],
        "notes": [
            "Висота = висота кнопки Deposit (control md 40): контейнер hug, кнопка впритул праворуч.",
            "Deposit — exposed instance Button: розмір/іконку/текст можна міняти з панелі.",
        ],
    },
}

# ---------------------------------------------------------------- завантаження
def load(p):
    with open(os.path.join(TOK, p), encoding="utf-8") as f:
        return json.load(f, object_pairs_hook=OrderedDict)

def flat(d, p=""):
    out = OrderedDict()
    for k, v in d.items():
        if isinstance(v, dict) and "value" in v and "type" in v:
            out[p + k] = v
        elif isinstance(v, dict):
            out.update(flat(v, p + k + "."))
    return out

meta = load("$metadata.json")
themes = load("$themes.json")
SETS = OrderedDict((s, flat(load(s + ".json"))) for s in meta["tokenSetOrder"])

REF = re.compile(r"\{([^}]+)\}")
MAP_FLAT = len({v["value"] for k, v in SETS.get("map", {}).items() if k.startswith("color.product1.")}) <= 1

def pool(brand="aurum", mode="light"):
    p = OrderedDict()
    for s in ["core", f"brand/{brand}", "map", f"theme/{mode}", "typography", "components"]:
        p.update(SETS.get(s, {}))
    return p

def resolve(val, pl, depth=0):
    if depth > 20:
        return "⟳"
    if isinstance(val, dict):
        return {k: resolve(v, pl, depth + 1) for k, v in val.items()}
    s = str(val)
    m = REF.fullmatch(s)
    if m:
        t = pl.get(m.group(1))
        return resolve(t["value"], pl, depth + 1) if t else f"⚠ {m.group(1)}"
    return REF.sub(lambda m: str(resolve("{" + m.group(1) + "}", pl, depth + 1)), s)

def fmt(v):
    if isinstance(v, dict):
        return " · ".join(f"{k}: {v[k]}" for k in v)
    return str(v)

def code(v):
    return f"`{v}`"

def figma_name(path):
    return path.replace(".", "/")

def swatch(v):
    s = str(v)
    return f"`{s}`"

def count_refs(set_name):
    """скільки токенів сету посилаються на інші (а не мають сирих значень)"""
    t = SETS[set_name]
    return sum(1 for v in t.values() if REF.search(json.dumps(v["value"])))

def group_of(path):
    return path.split(".")[0]

def table(rows, head):
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    for r in rows:
        out.append("| " + " | ".join(str(c).replace("|", "\\|") for c in r) + " |")
    return "\n".join(out)

def write(rel, text):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.rstrip() + "\n")

TODAY = datetime.date.today().isoformat()
HEADER = f"> Згенеровано `scripts/build-token-docs.py` з Token Studio JSON · {TODAY}. Не редагувати вручну — правити JSON і перегенерувати.\n"

# ---------------------------------------------------------------- core
def doc_core():
    t = SETS["core"]
    parts = [f"# Core — примітиви\n", HEADER,
             "Словник сирих значень. **Ніколи не прив'язується до шару в Figma** — на core посилаються brand/map/theme/typography.",
             f"Figma: колекція **Base** (mode Default). Токенів: **{len(t)}**.\n"]
    groups = OrderedDict()
    for k, v in t.items():
        groups.setdefault(group_of(k), []).append((k, v))
    for g, items in groups.items():
        parts.append(f"## {g}\n")
        parts.append(table([(code(k), v["type"], code(fmt(v["value"])), figma_name(k)) for k, v in items],
                           ["Токен", "Тип", "Значення", "Figma variable"]))
        parts.append("")
    write("references/core.md", "\n".join(parts))

# ---------------------------------------------------------------- brand
def doc_brand():
    b = {x: SETS[f"brand/{x}"] for x in BRANDS}
    keys = list(b["aurum"].keys())
    parts = ["# Brand — Aurum / Nova / Fiesta\n", HEADER,
             "Бренд = набір значень. Ключі в усіх трьох файлах **ідентичні**, різняться лише значення.",
             "Figma: колекція **Brand** (modes Aurum / Nova / Fiesta). Разом із брендом у цю колекцію потрапляє `map` (enabled у темах Brand).",
             f"Токенів у бренді: **{len(keys)}**.\n",
             "Що живе в бренді:",
             "- **Кольори** — одиничні базові (`product1–3`, `onProduct1/2`, `success`, `warning`, `danger`, `ink`). Без рамп: відтінки — у `map`.",
             "- **Шрифти** — `fontFamily.display` (display/title), `fontFamily.base` (решта тексту).",
             "- **Розмірна семантика** — `space.padding.*`, `space.gap.*`, `size.control.*`, `iconSize.*`, `borderRadius.control|surface`, `borderWidth.none|control`. "
             "Живе в бренді, а не в темі: бренд може мати інші радіуси/щільність, тема (light/dark) міняє тільки кольори.\n"]
    groups = OrderedDict()
    for k in keys:
        g = k.split(".")[0] if not k.startswith("space.") else ".".join(k.split(".")[:2])
        groups.setdefault(g, []).append(k)
    for g, ks in groups.items():
        parts.append(f"## {g}\n")
        rows = []
        for k in ks:
            vals = []
            for x in BRANDS:
                raw = b[x][k]["value"]
                res = resolve(raw, pool(x))
                vals.append(code(raw) + ("" if str(res) == str(raw) else f" → `{res}`"))
            rows.append([code(k), b["aurum"][k]["type"]] + vals)
        parts.append(table(rows, ["Токен", "Тип", "Aurum", "Nova", "Fiesta"]))
        parts.append("")
    write("references/brand.md", "\n".join(parts))

# ---------------------------------------------------------------- map
def doc_map():
    t = SETS["map"]
    parts = ["# Map — рампи\n", HEADER,
             "Міст між брендом і темою: кроки `100…900` (і `neutral.0…900`) для кожного базового кольору бренду.",
             "Figma: колекція **Brand** (map enabled у темах Brand).",
             f"Токенів: **{len(t)}**.\n",
             "> ⚠ Зараз кожен крок рампи посилається на **той самий** базовий колір бренду (`color.product1.100…900 → {color.product1}`). "
             "Hover / Active / фони / бордери візуально не розрізняються, доки кроки не отримають власних значень.\n"]
    groups = OrderedDict()
    for k, v in t.items():
        groups.setdefault(".".join(k.split(".")[:2]), []).append((k, v))
    rows = []
    for g, items in groups.items():
        steps = ", ".join(k.split(".")[-1] for k, _ in items)
        refs = sorted(set(v["value"] for _, v in items))
        rows.append([code(g), steps, ", ".join(code(r) for r in refs)])
    parts.append(table(rows, ["Група", "Кроки", "Посилається на"]))
    write("references/map.md", "\n".join(parts))

# ---------------------------------------------------------------- theme
def doc_theme():
    L, D = SETS["theme/light"], SETS["theme/dark"]
    parts = ["# Theme — Light / Dark\n", HEADER,
             "Семантика кольорів. Тут калькулюється логіка тем: той самий ключ у light і dark дивиться в різні кроки `map`.",
             "Figma: колекція **Theme** (modes Light / Dark). **Тільки кольори** — розміри живуть у бренді.",
             f"Токенів: **{len(L)}** (ключі light і dark ідентичні).\n",
             "Колонки «Aurum» — значення, до якого резолвиться токен у бренді Aurum.\n"]
    groups = OrderedDict()
    for k in L:
        groups.setdefault(".".join(k.split(".")[:2]), []).append(k)
    for g, ks in groups.items():
        parts.append(f"## {g}\n")
        rows = []
        for k in ks:
            lv, dv = L[k]["value"], D[k]["value"]
            rows.append([code(k), code(lv), swatch(resolve(lv, pool("aurum", "light"))),
                         code(dv), swatch(resolve(dv, pool("aurum", "dark")))])
        parts.append(table(rows, ["Токен", "Light", "Aurum light", "Dark", "Aurum dark"]))
        parts.append("")
    write("references/theme.md", "\n".join(parts))

# ---------------------------------------------------------------- typography
def doc_typography():
    t = SETS["typography"]
    tr = lambda r: str(r).strip("{}").split(".")[-1]
    parts = ["# Typography — text styles\n", HEADER,
             "Окремий шар. Сет `typography` → тема **Typography / Default** → Figma **text styles** `typography/…`.",
             "Компоненти **не мають** власних typography-токенів: текстовий шар бере стиль зі шкали. Той самий набір — для вільного тексту.",
             f"Стилів: **{len(t)}**.\n",
             "Експорт: Styles & Variables → Export styles → тільки тема Typography/Default, галочка Typography, "
             "**Create styles with variable references** (fontFamily/fontSize/lineHeight/fontWeight прив'язані до змінних → шрифт перемикається з брендом).\n"]
    rows = []
    for k, v in t.items():
        val = v["value"]
        pl = pool("aurum")
        r = lambda f: resolve(val.get(f, ""), pl)
        rows.append([code(k.replace("typography.", "")), figma_name(k), tr(val.get("fontFamily")),
                     f'{r("fontSize")}/{r("lineHeight")}', r("fontWeight"), r("letterSpacing"),
                     r("textCase"), v.get("description", "")])
    parts.append(table(rows, ["Стиль", "Figma", "Family", "Size/LH", "Weight", "LS", "Case", "Для чого"]))
    parts.append("\nFamily: `display` → `fontFamily.display`, `base` → `fontFamily.base` (значення — у brand.md).")
    write("references/typography.md", "\n".join(parts))

# ---------------------------------------------------------------- components
def doc_components():
    t = SETS["components"]
    comps = OrderedDict()
    for k, v in t.items():
        comps.setdefault(group_of(k), OrderedDict())[k] = v
    for c, toks in comps.items():
        n = COMPONENT_NOTES.get(c, {})
        parts = [f"# {n.get('title', c.capitalize())}\n", HEADER]
        if n:
            parts += [f"**Figma:** {n['figma']}  ", f"**Варіанти:** {n['variants']}  ",
                      f"**Анатомія:** {n['anatomy']}\n"]
        parts.append(f"Токенів: **{len(toks)}**. Посилаються тільки на theme / brand-семантику, не на core.\n")
        colors = [(k, v) for k, v in toks.items() if v["type"] == "color"]
        other = [(k, v) for k, v in toks.items() if v["type"] != "color"]
        if colors:
            parts.append("## Кольори\n")
            if MAP_FLAT:
                parts.append("> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.\n")
            rows = [[code(k), figma_name(k), code(v["value"]),
                     swatch(resolve(v["value"], pool("aurum", "light"))),
                     swatch(resolve(v["value"], pool("aurum", "dark")))] for k, v in colors]
            parts.append(table(rows, ["Токен", "Figma variable", "→ Alias", "Aurum light", "Aurum dark"]))
            parts.append("")
        if other:
            parts.append("## Розміри та форма\n")
            rows = [[code(k), figma_name(k), v["type"], code(v["value"]),
                     code(resolve(v["value"], pool("aurum")))] for k, v in other]
            parts.append(table(rows, ["Токен", "Figma variable", "Тип", "→ Alias", "Значення"]))
            parts.append("")
        if n.get("text_styles"):
            parts.append("## Текст (text styles, не токени)\n")
            parts.append(table([(code(s), st) for s, st in n["text_styles"]], ["Розмір", "Стиль"]))
            parts.append("")
        if n.get("notes"):
            parts.append("## Нотатки\n")
            parts += [f"- {x}" for x in n["notes"]]
        write(f"references/components/{c}.md", "\n".join(parts))
    return comps

# ---------------------------------------------------------------- index
def doc_index(comps):
    th_rows = []
    for t in themes:
        sel = ", ".join(f"{s}{'' if st == 'enabled' else ' (source)'}" for s, st in t["selectedTokenSets"].items())
        out = "text styles" if t["group"] == "Typography" else "variables"
        th_rows.append([t["group"], t["name"], sel, out])
    set_rows = [[code(s), len(SETS[s]), desc] for s, desc in [
        ("core", "примітиви: dimension, borderRadius, borderWidth, fontWeight, fontSize, lineHeight, letterSpacing, textCase, color.white/black/transparent"),
        ("brand/aurum", "кольори бренду, шрифти, розмірна семантика"),
        ("brand/nova", "ті самі ключі, інші значення"),
        ("brand/fiesta", "ті самі ключі, інші значення"),
        ("map", "рампи 100…900 від базових кольорів бренду"),
        ("theme/light", "семантика кольорів: bg, fill, text, border, outline"),
        ("theme/dark", "ті самі ключі, інші кроки рампи"),
        ("typography", "text styles"),
        ("components", "усі компонентні токени в одному сеті"),
    ] if s in SETS]
    comp_rows = [[f"[{COMPONENT_NOTES.get(c, {}).get('title', c)}](references/components/{c}.md)", len(v)] for c, v in comps.items()]
    total = sum(len(v) for v in SETS.values())
    text = f"""---
name: multibrand-design-system
description: Реєстр токенів Multibrand Design System (репо multibrand-design-system; бренди Aurum / Nova / Fiesta) — усі сети Token Studio (core, brand/aurum|nova|fiesta, map, theme/light|dark, typography, components), їхні значення, посилання й Figma-змінні. Use ANY TIME the user works with tokens of the Multibrand Design System — adding a component's tokens, binding variables in Figma, checking what a token resolves to, adding a brand, or asking "який токен для…". INDEX — деталі в references/*.md, вантажити тільки потрібний файл. Генерується з JSON скриптом scripts/build-token-docs.py.
---

# Multibrand Design System — токени (індекс)

{HEADER}
Джерело правди — Token Studio JSON у `tokens/`. Figma Variables і text styles — синхронізована копія.
Усього токенів: **{total}**.

## Потік

```
core ──► brand/<x> ──► map ──► theme/<mode> ──► components ──► шар у Figma
  │         │                                      ▲
  │         └── розміри, радіуси, шрифти ──────────┘
  └──► typography (text styles) ──► текстовий шар у Figma
```

- **core** — словник сирих значень. Ніколи не на шарі.
- **brand** — що відрізняє бренд: кольори, шрифти, розмірна семантика.
- **map** — рампи від базових кольорів бренду.
- **theme** — семантика кольорів; light/dark дивляться в різні кроки рампи. Тільки кольори.
- **typography** — text styles; компоненти беруть стиль, а не токени.
- **components** — єдине, що прив'язується до шару. Посилається на theme/brand-семантику.

## Сети (порядок = `$metadata.tokenSetOrder`)

{table(set_rows, ["Сет", "Токенів", "Що всередині"])}

## Теми → Figma

{table(th_rows, ["Група (колекція)", "Mode", "Сети", "Що створює"])}

Експорт: **Variables** — теми Base, Brand, Theme, Components (Typography не вибирати). **Styles** — тільки Typography/Default з «Create styles with variable references».

## Правила

1. Ім'я токена = CSS-властивість: `bg`, `color`, `br`, `iconColor`, `size`, `paddingH/V`, `gap`, `iconSize`, `borderRadius`, `borderWidth`. Формат `компонент.[підчастина].[варіант].властивість.[стан|розмір]`; стан/розмір — завжди останній.
2. Компонент посилається тільки на theme / brand-семантику (`color.*`, `space.*`, `size.control.*`, `iconSize.*`, `borderRadius.*`, `borderWidth.*`). Ніколи на core і ніколи на `map` напряму.
3. Компонент не має typography-токенів — текстовий шар отримує text style (`typography/…`).
4. Ключі трьох брендів ідентичні; ключі light і dark ідентичні.
5. Бренд = тільки значення. Нові ключі в бренді — лише якщо їх додано в усі три.
6. Розміри й радіуси — у бренді, не в темі. Тема міняє лише кольори.
7. Стани: `default / hover / active / disabled` (focus не робимо). Розміри: `xs / sm / md / lg / xl`.

## Карта файлів

| Файл | Коли читати |
|---|---|
| [references/core.md](references/core.md) | примітиви, шкали розмірів і шрифтів |
| [references/brand.md](references/brand.md) | значення трьох брендів поруч |
| [references/map.md](references/map.md) | рампи кольорів |
| [references/theme.md](references/theme.md) | семантика кольорів light / dark |
| [references/typography.md](references/typography.md) | text styles |

### Компоненти

{table(comp_rows, ["Компонент", "Токенів"])}

## Додати компонент

1. Блок `<component>` у `tokens/components.json` (посилання тільки на theme/brand-семантику).
2. Нотатки (анатомія, варіанти, text styles) — у `COMPONENT_NOTES` скрипта.
3. `python3 scripts/build-token-docs.py` — з'явиться `references/components/<component>.md`, індекс оновиться.
"""
    write("SKILL.md", text)

doc_core(); doc_brand(); doc_map(); doc_theme(); doc_typography()
comps = doc_components()
doc_index(comps)
print("docs →", OUT)
