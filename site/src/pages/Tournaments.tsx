import { useState } from "react";
import { Alert, Button, Tabs } from "../ui/atoms";
import { SectionHeading } from "../ui/molecules";
import { TournamentCard } from "../ui/organisms";
import { TOURNAMENTS } from "../data";
import { useSession } from "../session";

type Tab = "live" | "upcoming" | "finished" | "mine";
export default function Tournaments() {
  const [tab, setTab] = useState<Tab>("live");
  const { joined } = useSession();
  const list = TOURNAMENTS.filter((t) => (tab === "mine" ? joined.includes(t.id) : t.state === tab));
  return (
    <div className="main container">
      <SectionHeading title="Tournaments" subtitle="Compete for prize pools, climb the leaderboard" icon="goblet-filled" />
      <Tabs value={tab} onChange={setTab} items={[{ id: "live", label: "Active" }, { id: "upcoming", label: "Upcoming" }, { id: "finished", label: "Finished" }, { id: "mine", label: "My tournaments" }]} />
      {tab === "mine" && list.length === 0 && <Alert tone="info" title="No tournaments yet">Join an active tournament and it will show up here.<br /><Button variant="text" size="sm" onClick={() => setTab("live")}>Browse active tournaments</Button></Alert>}
      <div className="grid grid--cards">{list.map((t) => <TournamentCard key={t.id} id={t.id} state={t.state} title={t.title} prize={t.prize} time={t.time} players={t.players} progress={t.progress} />)}</div>
    </div>
  );
}
