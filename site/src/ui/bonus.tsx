import { useEffect, useState } from "react";
import { Alert, Badge, Button, Checkbox } from "./atoms";
import { ListItem } from "./molecules";
import { Modal } from "./organisms";
import { claimBonus, openDeposit, useSession } from "../session";
import { closeBonus, openBonus, toast, useBonusView } from "../store";

const STEPS = [
  { icon: "user", title: "1. Create an account", sub: "Sign up with email, phone or Google in 30 seconds" },
  { icon: "wallet", title: "2. Make your first deposit", sub: "From €10 — we add +200% up to €500" },
  { icon: "game-casino", title: "3. Spin and enjoy", sub: "200 free spins on Golden Pharaoh, 20 a day" },
] as const;
const TERMS = [
  { title: "Bonus", value: "200% up to €500" },
  { title: "Free spins", value: "200" },
  { title: "Wagering", value: "35×" },
  { title: "Valid for", value: "30 days" },
];

export function BonusModal() {
  const view = useBonusView();
  const { user, bonusClaimed } = useSession();
  const [agree, setAgree] = useState(false);
  useEffect(() => { if (view) setAgree(false); }, [view]);

  if (view === "details") {
    return (
      <Modal open title="Welcome bonus" onClose={closeBonus}
        actions={<><Button variant="primary" size="md" onClick={() => openBonus("claim")}>Claim bonus</Button><Button variant="secondary" size="md" onClick={closeBonus}>Close</Button></>}>
        <div className="stack gap-lg">
          <p>Double your first deposit and get free spins on top. Here is how it works:</p>
          <div className="stack">{STEPS.map((s, i) => <ListItem key={s.title} icon={s.icon} title={s.title} subtitle={s.sub} chevron={false} divider={i < STEPS.length - 1} />)}</div>
          <div className="stack">{TERMS.map((t, i) => <ListItem key={t.title} title={t.title} value={t.value} chevron={false} divider={i < TERMS.length - 1} />)}</div>
          <p className="ts-caption-md muted">18+ only. Bonus funds and winnings are subject to the wagering requirement. Demo product — no real money.</p>
        </div>
      </Modal>
    );
  }

  if (view === "claim") {
    if (!user) {
      return (
        <Modal open title="Sign up to claim" onClose={closeBonus}
          actions={<><Button variant="primary" size="md" onClick={() => { closeBonus(); location.hash = "#/register"; }}>Create account</Button><Button variant="secondary" size="md" onClick={() => { closeBonus(); location.hash = "#/login"; }}>Log in</Button></>}>
          <div className="stack gap-lg">
            <Badge tone="accent">Welcome bonus</Badge>
            <p>The welcome bonus is for new players: <b>+200% up to €500</b> and <b>200 free spins</b>. Create a free account to claim it.</p>
          </div>
        </Modal>
      );
    }
    if (bonusClaimed) {
      return (
        <Modal open title="Bonus is active" onClose={closeBonus}
          actions={<><Button variant="primary" size="md" onClick={() => { closeBonus(); openDeposit(); }}>Deposit now</Button><Button variant="secondary" size="md" onClick={closeBonus}>Close</Button></>}>
          <Alert tone="success" title="Welcome bonus is on">Make your first deposit and we will add +200% (up to €500) automatically.</Alert>
        </Modal>
      );
    }
    return (
      <Modal open title="Claim your welcome bonus" onClose={closeBonus}
        actions={<><Button variant="primary" size="md" disabled={!agree} onClick={() => { claimBonus(); closeBonus(); toast("success", "Welcome bonus activated", "Make your first deposit to receive +200% and 200 free spins."); }}>Claim bonus</Button><Button variant="secondary" size="md" onClick={closeBonus}>Not now</Button></>}>
        <div className="stack gap-lg">
          <div className="stack">{TERMS.map((t, i) => <ListItem key={t.title} title={t.title} value={t.value} chevron={false} divider={i < TERMS.length - 1} />)}</div>
          <Checkbox checked={agree} onChange={setAgree} label="I accept the bonus terms and conditions" />
        </div>
      </Modal>
    );
  }
  return null;
}
