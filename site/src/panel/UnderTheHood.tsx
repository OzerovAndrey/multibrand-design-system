import { useEffect, useMemo, useState } from "react";
import { useLook } from "../theme";
import { Badge, Icon, Tabs } from "../ui/atoms";
import { cx } from "../ui/util";
import meta from "../generated/meta.json";

type Manifest = {
  layers: Record<"brand" | "map" | "theme" | "components", string[]>;
  values: Record<string, Record<string, string>>;
  chains: Record<string, Record<string, { steps: { name: string; layer: string; ref?: string; value?: string; note?: string }[]; value: string }>>;
};
let cache: Promise<Manifest> | null = null;
const load = () => (cache ??= fetch(import.meta.env.BASE_URL + "tokens-manifest.json").then((r) => r.json()));
const isColor = (v: string) => /^(#|rgba?\()/.test(v);
const Swatch = ({ v }: { v: string }) => (isColor(v) ? <i className="hood__sw" style={{ background: v }} /> : null);
const LAYER_TONE: Record<string, "neutral" | "primary" | "accent" | "info" | "success"> = { core: "neutral", brand: "primary", map: "info", theme: "accent", component: "success" };

export default function UnderTheHood({ onClose }: { onClose: () => void }) {
  const look = useLook();
  const [m, setM] = useState<Manifest | null>(null);
  const [tab, setTab] = useState<"diff" | "chain" | "metrics">("diff");
  const [token, setToken] = useState("button.primary.bg.default");
  useEffect(() => { load().then(setM); }, []);
  const key = `${look.brand}|${look.theme}`;
  const prevKey = look.prev ? `${look.prev.brand}|${look.prev.theme}` : null;

  const diff = useMemo(() => {
    if (!m || !prevKey) return null;
    const a = m.values[prevKey], b = m.values[key];
    const res = (["brand", "map", "theme", "components"] as const).map((layer) => {
      const changed = m.layers[layer].filter((n) => a[n] !== b[n]);
      return { layer, total: m.layers[layer].length, changed };
    });
    return res;
  }, [m, key, prevKey]);

  return (
    <div className="hood" role="region" aria-label="Under the hood">
      <div className="hood__head">
        <h3 className="ts-title-t4">Under the hood</h3>
        <button type="button" className="hood__close" onClick={onClose} aria-label="Close"><Icon name="close" /></button>
      </div>
      <Tabs size="sm" value={tab} onChange={setTab} items={[{ id: "diff", label: "Diff" }, { id: "chain", label: "Token chain" }, { id: "metrics", label: "Metrics" }]} />
      <div className="hood__body">
        {!m && <p className="ts-body-sm-regular muted">Loading tokens…</p>}
        {m && tab === "diff" && (
          !diff ? <p className="ts-body-md-regular muted">Switch brand or theme — this panel shows exactly which tokens changed and which components were touched.</p> : (
            <>
              <p className="hood__line ts-label-md">{look.prev!.brand} · {look.prev!.theme} <Icon name="chevron-right" /> {look.brand} · {look.theme}</p>
              <div className="hood__counts">
                <div className="hood__count"><b className="ts-title-t3">0</b><span className="ts-caption-md">core changed</span></div>
                {diff.map((d) => <div key={d.layer} className="hood__count"><b className="ts-title-t3">{d.changed.length}</b><span className="ts-caption-md">{d.layer === "components" ? "component values resolved" : `${d.layer} changed`}</span></div>)}
                <div className="hood__count is-zero"><b className="ts-title-t3">0</b><span className="ts-caption-md">component definitions edited</span></div>
              </div>
              <p className="ts-body-sm-regular muted">Components only hold aliases. The values below re-resolve on their own — no component code or markup was touched.</p>
              <ul className="hood__list">
                {diff.flatMap((d) => d.layer === "components" ? [] : d.changed.slice(0, 8).map((n) => ({ n, layer: d.layer }))).slice(0, 16).map(({ n, layer }) => (
                  <li key={n}><Badge tone={layer === "brand" ? "primary" : layer === "map" ? "info" : "accent"}>{layer}</Badge><code>{n}</code><span className="hood__vals"><Swatch v={m.values[prevKey!][n]} /><em>{m.values[prevKey!][n]}</em><Icon name="chevron-right" /><Swatch v={m.values[key][n]} /><em>{m.values[key][n]}</em></span></li>
                ))}
              </ul>
            </>
          )
        )}
        {m && tab === "chain" && (
          <>
            <select className="hood__select ts-body-sm-regular" value={token} onChange={(e) => setToken(e.target.value)}>{Object.keys(m.chains[key]).map((t) => <option key={t}>{t}</option>)}</select>
            <ol className="hood__chain">
              {m.chains[key][token].steps.map((s, i) => (
                <li key={i}><Badge tone={LAYER_TONE[s.layer] ?? "neutral"}>{s.layer}</Badge><code>{s.name}</code>{s.note && <em className="muted">{s.note}</em>}{s.value && <span className="hood__vals"><Swatch v={s.value} /><em>{s.value}</em></span>}</li>
              ))}
            </ol>
            <p className="hood__final ts-label-md"><Swatch v={m.chains[key][token].value} /> resolves to <b>{m.chains[key][token].value}</b> in {look.brand} · {look.theme}</p>
          </>
        )}
        {tab === "metrics" && (
          <ul className="hood__metrics">
            <li><b>{meta.counts.total}</b><span>tokens in total</span></li>
            <li><b>{meta.counts.components}</b><span>component tokens · {meta.componentCount} components</span></li>
            <li><b>{meta.counts.theme}</b><span>theme tokens (Light + Dark)</span></li>
            <li><b>{meta.counts.brand}</b><span>brand tokens (3 brands)</span></li>
            <li><b>6</b><span>brand × theme combinations</span></li>
            <li><b>{(meta.cssBytes / 1024).toFixed(0)} kB</b><span>generated CSS, all brands and themes</span></li>
          </ul>
        )}
      </div>
    </div>
  );
}
