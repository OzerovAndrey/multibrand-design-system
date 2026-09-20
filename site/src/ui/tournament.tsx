import { useEffect, useState } from "react";
import { Alert, Badge, Button } from "./atoms";
import { ListItem } from "./molecules";
import { Modal } from "./organisms";
import { TOURNAMENTS } from "../data";
import { joinTournament, money, openDeposit, useSession } from "../session";
import { closeJoin, toast, useJoinTarget } from "../store";
import { tournamentHref } from "../router";

export function JoinModal() {
  const id = useJoinTarget();
  const { user, balance, joined } = useSession();
  const [done, setDone] = useState(false);
  useEffect(() => { setDone(false); }, [id]);
  const t = TOURNAMENTS.find((x) => x.id === id);
  if (!t) return null;
  const fee = t.entry;
  const already = joined.includes(t.id);

  if (!user) {
    return (
      <Modal open title={`Join ${t.title}`} onClose={closeJoin}
        actions={<><Button variant="primary" size="md" onClick={() => { closeJoin(); location.hash = "#/login"; }}>Log in</Button><Button variant="secondary" size="md" onClick={() => { closeJoin(); location.hash = "#/register"; }}>Sign up</Button></>}>
        <div className="stack gap-lg"><Badge tone="accent">{t.prize} prize pool</Badge><p>Log in or create an account to join this tournament.</p></div>
      </Modal>
    );
  }

  if (done || already) {
    return (
      <Modal open title="You're in!" onClose={closeJoin}
        actions={<><Button variant="primary" size="md" onClick={() => { closeJoin(); location.hash = tournamentHref(t.id); }}>View tournament</Button><Button variant="secondary" size="md" onClick={closeJoin}>Close</Button></>}>
        <Alert tone="success" title={`You joined ${t.title}`}>Every real-money spin on eligible slots now earns points. Good luck!</Alert>
      </Modal>
    );
  }

  const short = fee > balance;
  return (
    <Modal open title={`Join ${t.title}`} onClose={closeJoin}
      actions={short
        ? <><Button variant="primary" size="md" onClick={() => { closeJoin(); openDeposit(); }}>Deposit</Button><Button variant="secondary" size="md" onClick={closeJoin}>Cancel</Button></>
        : <><Button variant="primary" size="md" onClick={() => { joinTournament(t.id, fee); setDone(true); toast("success", "Tournament joined", `${t.title} — you're on the leaderboard.`); }}>{fee ? `Join for ${money(fee)}` : "Join for free"}</Button><Button variant="secondary" size="md" onClick={closeJoin}>Cancel</Button></>}>
      <div className="stack gap-lg">
        <div className="stack">
          <ListItem icon="goblet-filled" title="Prize pool" value={t.prize} chevron={false} divider />
          <ListItem icon="users" title="Players" value={t.players.replace(" players", "")} chevron={false} divider />
          <ListItem icon="clock" title={t.state === "upcoming" ? "Starts" : "Ends"} value={t.time.replace(/^(Ends in|Starts) /, "")} chevron={false} divider />
          <ListItem icon="wallet" title="Entry fee" value={fee ? money(fee) : "Free"} chevron={false} />
        </div>
        {short ? <Alert tone="danger" title="Not enough balance">You need {money(fee)} to enter. Top up your balance and come back.</Alert>
          : <Alert tone="warning" title="Min. bet €0.20">Only real-money spins on eligible slots count towards the leaderboard.</Alert>}
      </div>
    </Modal>
  );
}
