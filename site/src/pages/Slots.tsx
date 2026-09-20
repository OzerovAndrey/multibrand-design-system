import { useMemo, useState } from "react";
import { Button, Chip, Input, Select } from "../ui/atoms";
import { SectionHeading } from "../ui/molecules";
import { GameTile } from "../ui/organisms";
import { GAMES, PROVIDERS } from "../data";

export default function Slots() {
  const [q, setQ] = useState("");
  const [prov, setProv] = useState(PROVIDERS[0]);
  const [count, setCount] = useState(18);
  const [sort, setSort] = useState<"popular" | "az">("popular");
  const list = useMemo(() => {
    let l = GAMES.filter((g) => (prov === PROVIDERS[0] || g.provider === prov) && g.title.toLowerCase().includes(q.toLowerCase()));
    if (sort === "az") l = [...l].sort((a, b) => a.title.localeCompare(b.title));
    return l;
  }, [q, prov, sort]);
  return (
    <div className="main container">
      <SectionHeading title="Slots" subtitle={`${GAMES.length * 94} games · sorted by ${sort === "popular" ? "popularity" : "name"}`} icon="game-casino" />
      <div className="filters">
        <Input placeholder={`Search ${GAMES.length * 94} games`} iconLeft="search" value={q} onChange={setQ} />
        <div className="filters__sort"><Select value={sort} onChange={setSort} options={[{ id: "popular", label: "Sort: Popular" }, { id: "az", label: "Sort: A–Z" }]} /></div>
      </div>
      <div className="chips-row">{PROVIDERS.map((p) => <Chip key={p} selected={prov === p} onClick={() => setProv(p)}>{p}</Chip>)}</div>
      <div className="grid grid--games">{list.slice(0, count).map((g) => <GameTile key={g.id} title={g.title} provider={g.provider} art={g.art} badge={g.badge} favorite={g.id.endsWith("5")} />)}</div>
      {list.length === 0 && <p className="ts-body-md-regular muted center">Nothing found — try another search.</p>}
      <div className="stack center-col">
        <span className="ts-caption-md muted">Showing {Math.min(count, list.length)} of {list.length}</span>
        {count < list.length && <Button variant="secondary" size="lg" onClick={() => setCount(count + 12)}>Load more games</Button>}
      </div>
    </div>
  );
}
