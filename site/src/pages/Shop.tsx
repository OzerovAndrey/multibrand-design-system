import { useState } from "react";
import { Alert, Button, Chip } from "../ui/atoms";
import { SectionHeading, StatTile } from "../ui/molecules";
import { LootboxCard, Modal, Rarity } from "../ui/organisms";
import { BOXES, Box, fmt } from "../data";

const FILTERS: (Rarity | "all")[] = ["all", "common", "rare", "epic", "legendary"];
export default function Shop() {
  const [f, setF] = useState<Rarity | "all">("all");
  const [coins, setCoins] = useState(2450);
  const [pick, setPick] = useState<Box | null>(null);
  const [won, setWon] = useState<string | null>(null);
  const list = BOXES.filter((b) => f === "all" || b.rarity === f);
  const buy = () => { if (!pick) return; setCoins(coins - pick.price); setWon(`${pick.title} opened — you won ${pick.rarity === "legendary" ? "a Jackpot ticket" : pick.rarity === "epic" ? "€25 bonus cash" : "20 free spins"}!`); setPick(null); };
  return (
    <div className="main container">
      <SectionHeading title="Shop" subtitle="Open lootboxes to win bonuses, free spins and rewards" icon="gift" />
      {won && <Alert tone="success" title="Lootbox opened" onClose={() => setWon(null)}>{won}</Alert>}
      <div className="grid grid--3">
        <StatTile label="Your coins" value={fmt(coins)} delta="+300 this week" trend="up" icon="coins-filled" />
        <StatTile label="Gems" value="120" icon="diamond-filled" />
        <StatTile label="Free spins" value="35" icon="gift" />
      </div>
      <div className="chips-row">{FILTERS.map((r) => <Chip key={r} selected={f === r} onClick={() => setF(r)}>{r === "all" ? "All" : r[0].toUpperCase() + r.slice(1)}</Chip>)}</div>
      <section className="stack section">
        <SectionHeading title="Lootboxes" icon="gift" />
        <div className="grid grid--boxes">{list.map((b) => <LootboxCard key={b.id} rarity={b.rarity} title={b.title} description={b.description} price={fmt(b.price)} onOpen={() => setPick(b)} />)}</div>
      </section>
      <Modal open={!!pick} title={`Open ${pick?.title}?`} onClose={() => setPick(null)} actions={<><Button variant="primary" size="md" onClick={buy} disabled={!!pick && coins < pick.price}>Confirm</Button><Button variant="secondary" size="md" onClick={() => setPick(null)}>Cancel</Button></>}>
        {pick && (coins >= pick.price ? `You are about to open a ${pick.title} for ${fmt(pick.price)} coins. This action cannot be undone.` : "Not enough coins — top up your balance first.")}
      </Modal>
    </div>
  );
}
