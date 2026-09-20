import { useEffect, useState } from "react";
import { BRANDS, setLook, toggleTour, useLook, useTouring } from "../theme";
import { Button, Icon, Switch } from "../ui/atoms";
import { cx } from "../ui/util";
import UnderTheHood from "./UnderTheHood";

export default function ControlPanel() {
  const look = useLook();
  const touring = useTouring();
  const [hood, setHood] = useState(false);
  const [open, setOpen] = useState(() => window.innerWidth >= 768);
  const [hint, setHint] = useState(false);
  useEffect(() => {
    let seen = false; try { seen = !!localStorage.getItem("mb-hint"); } catch { /* ignore */ }
    if (seen) return;
    const a = window.setTimeout(() => setHint(true), 1800), b = window.setTimeout(() => setHint(false), 12000);
    return () => { window.clearTimeout(a); window.clearTimeout(b); };
  }, []);
  const dismiss = () => { setHint(false); try { localStorage.setItem("mb-hint", "1"); } catch { /* ignore */ } };
  useEffect(() => { if (look.tick > 0) dismiss(); }, [look.tick]);
  return (
    <aside className={cx("panel", hood && "is-open", open && "is-expanded")} aria-label="Brand and theme controls">
      {hint && !hood && <button type="button" className="panel__hint ts-label-md" onClick={() => { dismiss(); setOpen(true); }}><Icon name="settings" /><span>Try it: switch brand & theme — the whole UI re-skins instantly</span></button>}
      {hood && <UnderTheHood onClose={() => setHood(false)} />}
      <button type="button" className="panel__fab hide-desktop" onClick={() => setOpen(!open)} aria-expanded={open} aria-label="Brand and theme">
        <i className="panel__swatch" style={{ background: `linear-gradient(135deg, var(--swatch-${look.brand}-1) 50%, var(--swatch-${look.brand}-2) 50%)` }} />
        <span className="ts-label-md">{open ? "Hide" : "Look"}</span>
      </button>
      <div className="panel__bar">
        <div className="panel__brands" role="radiogroup" aria-label="Brand">
          {BRANDS.map((b) => (
            <button key={b.id} type="button" role="radio" aria-checked={look.brand === b.id} title={b.tagline} className={cx("panel__brand ts-label-md", look.brand === b.id && "is-active")}
              onClick={(e) => setLook({ brand: b.id }, { x: e.clientX, y: e.clientY })}>
              <i className="panel__swatch" style={{ background: `linear-gradient(135deg, var(--swatch-${b.id}-1) 50%, var(--swatch-${b.id}-2) 50%)` }} />{b.name}
            </button>
          ))}
        </div>
        <div className="panel__theme"><Switch checked={look.theme === "dark"} label="Dark" onChange={(v) => { const el = document.activeElement as HTMLElement | null; const r = el?.getBoundingClientRect(); setLook({ theme: v ? "dark" : "light" }, r ? { x: r.left + r.width / 2, y: r.top + r.height / 2 } : undefined); }} /></div>
        <div className="panel__actions">
          <Button variant={touring ? "primary" : "secondary"} size="sm" onClick={toggleTour}>{touring ? "Stop tour" : "Play tour"}</Button>
          <Button variant={hood ? "primary" : "secondary"} size="sm" iconLeft="settings" onClick={() => setHood(!hood)}>Under the hood</Button>
        </div>
      </div>
    </aside>
  );
}
