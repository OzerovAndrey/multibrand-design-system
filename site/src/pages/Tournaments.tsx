import { useState } from "react";
import { Alert, Button, Progress, Tabs } from "../ui/atoms";
import { LeaderRow, SectionHeading, StatTile } from "../ui/molecules";
import { Card, TournamentCard } from "../ui/organisms";
import { LEADERS, TOURNAMENTS } from "../data";

type Tab = "live" | "upcoming" | "finished" | "mine";
export default function Tournaments() {
  const [tab, setTab] = useState<Tab>("live");
  const [joined, setJoined] = useState(false);
  const list = TOURNAMENTS.filter((t) => (tab === "mine" ? t.id === "t1" : t.state === tab));
  return (
    <div className="main container">
      <SectionHeading title="Tournaments" subtitle="Compete for prize pools, climb the leaderboard" icon="goblet-filled" />
      <Tabs value={tab} onChange={setTab} items={[{ id: "live", label: "Active" }, { id: "upcoming", label: "Upcoming" }, { id: "finished", label: "Finished" }, { id: "mine", label: "My tournaments" }]} />
      <div className="grid grid--cards">{list.map((t) => <TournamentCard key={t.id} state={t.state} title={t.title} prize={t.prize} time={t.time} art={t.art} players={t.players} progress={t.progress} />)}</div>
      <section className="stack section">
        <SectionHeading title="Weekend Race — leaderboard" icon="goblet-filled" />
        <div className="split">
          <div className="stack gap-md">
            {LEADERS.map((l, i) => <LeaderRow key={l.name} rank={i + 1} {...l} />)}
            <LeaderRow rank={42} name="You" sub="Level 7 · VIP" score="98,410" prize="€10" you />
          </div>
          <Card title="Prize pool" className="split__side">
            <span className="prize-big ts-display-d3">€50,000</span>
            <Progress value={75} tone="accent" label="Seats taken" />
            <div className="grid grid--2"><StatTile label="Players" value="1,204" icon="users" /><StatTile label="Ends in" value="02:14:36" icon="clock" /></div>
            <Button variant="primary" size="lg" full onClick={() => setJoined(true)} disabled={joined}>{joined ? "You're in!" : "Join now"}</Button>
            {joined ? <Alert tone="success" title="You joined Weekend Race">Every real-money spin on eligible slots now earns points.</Alert> : <Alert tone="warning" title="Min. bet €0.20">Only real-money spins on eligible slots count.</Alert>}
          </Card>
        </div>
      </section>
    </div>
  );
}
