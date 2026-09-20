import { useEffect, useState } from "react";
import { Alert, Button, Chip, Input, Progress } from "./atoms";
import { ListItem } from "./molecules";
import { Modal } from "./organisms";
import { IconName } from "./atoms";
import { closeDeposit, credit, money, signIn, useSession, welcomeBonus, WELCOME_CAP, type User } from "../session";

const PRESETS = [25, 50, 100, 250, 500];
const METHODS: { id: string; label: string; icon: IconName }[] = [
  { id: "card", label: "Card", icon: "game-casino" },
  { id: "wallet", label: "E-wallet", icon: "wallet" },
  { id: "crypto", label: "Crypto", icon: "coins-filled" },
  { id: "bank", label: "Bank", icon: "diamond-filled" },
];

export function DepositModal() {
  const { depositOpen, deposited, balance } = useSession();
  const [amount, setAmount] = useState("100");
  const [method, setMethod] = useState("card");
  const [step, setStep] = useState<"form" | "processing" | "done">("form");
  const [result, setResult] = useState({ amount: 0, bonus: 0 });

  useEffect(() => { if (depositOpen) { setStep("form"); setAmount("100"); setMethod("card"); } }, [depositOpen]);

  const n = Number(amount.replace(",", "."));
  const valid = Number.isFinite(n) && n >= 10 && n <= 5000;
  const bonus = valid && !deposited ? welcomeBonus(n) : 0;

  const pay = () => {
    if (!valid) return;
    setStep("processing");
    window.setTimeout(() => { const b = credit(n); setResult({ amount: n, bonus: b }); setStep("done"); }, 1500);
  };
  const close = () => { if (step !== "processing") closeDeposit(); };

  const actions = step === "form"
    ? <><Button variant="primary" size="lg" full disabled={!valid} onClick={pay}>Deposit {valid ? money(n) : ""}</Button><Button variant="secondary" size="lg" full onClick={close}>Cancel</Button></>
    : step === "processing"
      ? <Button variant="primary" size="lg" full disabled>Processing…</Button>
      : <><Button variant="primary" size="lg" full onClick={() => { closeDeposit(); location.hash = "#/slots"; }}>Start playing</Button><Button variant="secondary" size="lg" full onClick={closeDeposit}>Close</Button></>;

  return (
    <Modal open={depositOpen} title={step === "done" ? "Deposit successful" : "Deposit"} onClose={close} actions={actions}>
      {step === "form" && (
        <div className="stack gap-lg deposit">
          <Alert tone="info" title="Demo payment">No real money is charged — this is a portfolio demo.</Alert>
          <div className="stack">
            <span className="ts-label-md">Amount</span>
            <div className="chips-row deposit__presets">{PRESETS.map((p) => <Chip key={p} selected={n === p} onClick={() => setAmount(String(p))}>€{p}</Chip>)}</div>
            <Input placeholder="Other amount" value={amount} onChange={(v) => setAmount(v.replace(/[^0-9.,]/g, ""))} helper={valid || !amount ? "Min €10 · max €5,000" : "Enter an amount between €10 and €5,000"} />
          </div>
          <div className="stack">
            <span className="ts-label-md">Payment method</span>
            <div className="chips-row deposit__methods">{METHODS.map((m) => <Chip key={m.id} icon={m.icon} selected={method === m.id} onClick={() => setMethod(m.id)}>{m.label}</Chip>)}</div>
          </div>
          {!deposited && <Alert tone="success" title="Welcome bonus 200%">Your first deposit gets +200%, up to €{WELCOME_CAP}{valid ? `: +${money(bonus)} on this deposit` : ""}.</Alert>}
          <div className="deposit__summary">
            <ListItem title="You pay" value={valid ? money(n) : "—"} chevron={false} divider />
            <ListItem title="Bonus" value={bonus ? "+" + money(bonus) : "—"} chevron={false} divider />
            <ListItem title="You get" value={valid ? money(n + bonus) : "—"} chevron={false} />
          </div>
        </div>
      )}
      {step === "processing" && <div className="stack gap-lg deposit"><p className="ts-body-md-regular">Contacting your bank…</p><Progress value={72} label="Processing payment" showValue={false} /></div>}
      {step === "done" && (
        <div className="stack gap-lg deposit">
          <Alert tone="success" title={`${money(result.amount)} added`}>{result.bonus ? `Plus ${money(result.bonus)} welcome bonus.` : "Funds are available instantly."}</Alert>
          <ListItem icon="wallet" title="New balance" value={money(balance)} chevron={false} />
        </div>
      )}
    </Modal>
  );
}

const ACCOUNTS = {
  google: [{ name: "Andrii Ozerov", email: "andrii.ozerov@gmail.com" }, { name: "Demo Player", email: "demo.player@gmail.com" }],
  telegram: [{ name: "Andrii O.", email: "@andrii_ozerov" }, { name: "Demo Player", email: "@demo_player" }],
};

export function GoogleChooser({ open, onClose, onDone, provider = "google" }: { open: boolean; onClose: () => void; onDone: (u: User) => void; provider?: "google" | "telegram" }) {
  const list = ACCOUNTS[provider];
  const label = provider === "google" ? "Google" : "Telegram";
  return (
    <Modal open={open} title={`Continue with ${label}`} onClose={onClose} actions={<Button variant="secondary" size="md" full onClick={onClose}>Cancel</Button>}>
      <div className="stack gap-lg">
        <Alert tone="info" title="Demo sign-in">Choose any account below — no real {label} login happens.</Alert>
        <div className="stack">
          {list.map((a, i) => <ListItem key={a.email} icon="user" title={a.name} subtitle={a.email} divider={i < list.length - 1} onClick={() => { const u = { ...a, provider }; signIn(u); onDone(u); }} />)}
        </div>
      </div>
    </Modal>
  );
}
