import { Alert, Badge, Button, Progress } from "../ui/atoms";
import { LeaderRow, ListItem, SectionHeading, StatTile } from "../ui/molecules";
import { Card, PromoBanner } from "../ui/organisms";
import { PRIZE_SPLIT, TOURNAMENTS, leadersFor, prizeNum } from "../data";
import { useTournamentId } from "../router";
import { money, useSession } from "../session";
import { openJoin, toast } from "../store";

const STATE_BADGE = { live: { tone: "danger", label: "Live" }, upcoming: { tone: "info", label: "Starts soon" }, finished: { tone: "neutral", label: "Finished" } } as const;
const ORD = ["1st", "2nd", "3rd", "4th", "5th"];

export default function TournamentPage() {
  const id = useTournamentId();
  const t = TOURNAMENTS.find((x) => x.id === id);
  const { user, joined } = useSession();
  if (!t) {
    return <div className="main container"><Card className="auth__form"><div className="stack gap-lg"><h1 className="ts-title-t2">Tournament not found</h1><Button variant="primary" size="md" href="#/tournaments">All tournaments</Button></div></Card></div>;
  }
  const isJoined = joined.includes(t.id);
  const leaders = leadersFor(t);
  const pool = prizeNum(t);
  const b = STATE_BADGE[t.state];
  const timeLabel = t.state === "upcoming" ? "Starts in" : t.state === "finished" ? "Ended" : "Ends in";
  const timeValue = t.time.replace(/^(Ends in|Starts|Ended) /, "");

  const primary = t.state === "live"
    ? (isJoined ? { label: "You're in", icon: "check-mark" as const, disabled: true } : { label: "Join tournament", onClick: () => openJoin(t.id) })
    : t.state === "upcoming"
      ? { label: "Remind me", onClick: () => toast("info", "We'll remind you", `${t.title} — you'll get a reminder before it starts.`) }
      : { label: "View winners", href: "#/tournaments" };

  return (
    <div className="main container">
      <a className="link ts-label-md back-link" href="#/tournaments">← All tournaments</a>
      <PromoBanner scene="arena" h1 eyebrow={b.label} eyebrowTone={b.tone} title={t.title} text={t.about} primary={primary} secondary={{ label: "How it works", onClick: () => document.getElementById("how")?.scrollIntoView({ behavior: "smooth" }) }} />

      <div className="grid grid--stats">
        <StatTile label="Prize pool" value={t.prize} icon="goblet-filled" />
        <StatTile label="Players" value={t.players.replace(" players", "")} icon="users" />
        <StatTile label={timeLabel} value={timeValue} icon="clock" />
        <StatTile label="Entry" value={t.entry ? money(t.entry) : "Free"} icon="wallet" />
      </div>

      <div className="split">
        <section className="stack section">
          <SectionHeading title="Leaderboard" subtitle={t.state === "upcoming" ? "Opens when the tournament starts" : isJoined ? "You are #42 — keep spinning" : undefined} icon="goblet-filled" />
          {t.state === "upcoming" ? (
            <Alert tone="info" title="Leaderboard opens at the start">{isJoined ? "You're registered — your points start counting on kick-off." : "Register to be ready when the race begins."}</Alert>
          ) : (
            <div className="stack gap-md">
              {leaders.map((l, i) => <LeaderRow key={l.name} rank={i + 1} {...l} prize={i < PRIZE_SPLIT.length ? money(pool * PRIZE_SPLIT[i]).replace(".00", "") : l.prize} />)}
              {isJoined && t.state === "live" && <><div className="leader-gap ts-caption-md muted">· · ·</div><LeaderRow rank={42} name={user?.name ?? "You"} sub="Level 7 · You" score="98,410" prize="€10" you /></>}
              {!isJoined && t.state === "live" && <Alert tone="info" title="You're not on the board yet">Join the tournament to appear on the leaderboard.</Alert>}
            </div>
          )}
        </section>
        <div className="stack split__side gap-lg">
          <Card title="Seats">
            <Progress value={t.progress} tone="accent" label="Seats taken" />
            {t.state === "live" && !isJoined && <Button variant="primary" size="lg" full onClick={() => openJoin(t.id)}>Join tournament</Button>}
            {isJoined && <Alert tone="success" title="You are in">Every eligible real-money spin earns points.</Alert>}
          </Card>
          <Card title="Prize distribution">
            <div className="stack">{PRIZE_SPLIT.map((p, i) => <ListItem key={i} icon="goblet-filled" title={`${ORD[i]} place`} value={money(pool * p).replace(".00", "")} chevron={false} divider={i < PRIZE_SPLIT.length - 1} />)}</div>
          </Card>
          <Card title="How it works" className="how-card"><span id="how" />
            <div className="stack">
              <ListItem icon="user" title="Join the tournament" subtitle={t.entry ? `Entry fee ${money(t.entry)}` : "Entry is free"} chevron={false} divider />
              <ListItem icon="game-casino" title="Play eligible games" subtitle={`${t.game} · min. bet €0.20`} chevron={false} divider />
              <ListItem icon="jackpot" title="Earn points" subtitle="1 point for every €1 wagered" chevron={false} divider />
              <ListItem icon="wallet" title="Prizes are paid automatically" subtitle="Right after the tournament ends" chevron={false} />
            </div>
            <span><Badge tone="neutral">Demo — no real money</Badge></span>
          </Card>
        </div>
      </div>
    </div>
  );
}
