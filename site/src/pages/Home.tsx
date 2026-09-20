import { useMemo, useState } from "react";
import { Chip, Button } from "../ui/atoms";
import { SectionHeading } from "../ui/molecules";
import { GameTile, PromoBanner, TournamentCard } from "../ui/organisms";
import { GAMES, LIVE, TOURNAMENTS } from "../data";
import type { IconName } from "../ui/atoms";

const CATS: { id: string; label: string; icon?: IconName }[] = [
  { id: "all", label: "All" }, { id: "slots", label: "Slots", icon: "game-casino" }, { id: "live", label: "Live casino", icon: "game-casino" }, { id: "table", label: "Table games" },
  { id: "jackpots", label: "Jackpots", icon: "jackpot" }, { id: "new", label: "New" }, { id: "megaways", label: "Megaways" }, { id: "bonus buy", label: "Bonus buy" },
];

export default function Home() {
  const [cat, setCat] = useState("all");
  const games = useMemo(() => GAMES.filter((g) => cat === "all" || g.category === cat).slice(0, 12), [cat]);
  return (
    <div className="main container">
      <PromoBanner eyebrow="Welcome bonus" title="Get 200% on your first deposit" text="Up to €500 + 200 free spins. Claim it in one tap and join the Weekend Race." primary={{ label: "Claim bonus", href: "#/register" }} secondary={{ label: "Details", href: "#/shop" }} />
      <div className="chips-row">{CATS.map((c) => <Chip key={c.id} selected={cat === c.id} icon={c.icon} onClick={() => setCat(c.id)}>{c.label}</Chip>)}</div>
      <section className="stack section">
        <SectionHeading title="Popular games" icon="flame-filled" seeAll arrows />
        <div className="grid grid--games">{games.map((g) => <GameTile key={g.id} id={g.id} title={g.title} provider={g.provider} art={g.art} badge={g.badge} />)}</div>
        {games.length === 0 && <p className="ts-body-md-regular muted">No games in this category yet.</p>}
      </section>
      <section className="stack section">
        <SectionHeading title="Live casino" subtitle="Real dealers, real time" icon="users" seeAll arrows />
        <div className="grid grid--live">{LIVE.map((g) => <GameTile key={g.id} id={g.id} type="live" title={g.title} provider={g.provider} art={g.art} players={g.players} badge={{ tone: "danger", label: "Live" }} />)}</div>
      </section>
      <section className="stack section">
        <SectionHeading title="Tournaments" icon="goblet-filled" seeAll seeAllHref="#/tournaments" />
        <div className="grid grid--cards">{TOURNAMENTS.slice(0, 3).map((t) => <TournamentCard key={t.id} state={t.state} title={t.title} prize={t.prize} time={t.time} players={t.players} progress={t.progress} />)}</div>
        <div className="row row--center"><Button variant="secondary" size="lg" href="#/tournaments">All tournaments</Button></div>
      </section>
    </div>
  );
}
