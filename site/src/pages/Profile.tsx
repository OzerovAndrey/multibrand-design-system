import { useState } from "react";
import { Alert, Avatar, Button, Progress, Switch, Tabs } from "../ui/atoms";
import { ListItem, StatTile } from "../ui/molecules";
import { Card } from "../ui/organisms";
import { initials, money, openDeposit, useSession } from "../session";

type Tab = "overview" | "history" | "bonuses" | "settings";
export default function Profile() {
  const [tab, setTab] = useState<Tab>("overview");
  const [prefs, setPrefs] = useState({ sound: true, push: false, twofa: true });
  const { user, balance } = useSession();
  if (!user) return (
    <div className="main container">
      <Card className="auth__form"><div className="stack gap-lg"><h1 className="ts-title-t2">Your profile</h1><p className="ts-body-md-regular muted">Log in to see your balance, bonuses and history.</p><div className="row"><Button variant="primary" size="md" href="#/login">Log in</Button><Button variant="secondary" size="md" href="#/register">Sign up</Button></div></div></Card>
    </div>
  );
  return (
    <div className="main container">
      <Card className="profile-head">
        <div className="profile-head__top">
          <Avatar size="xl" initials={initials(user.name)} vip status />
          <div className="profile-head__info">
            <h1 className="ts-title-t2">{user.name}</h1>
            <span className="ts-body-sm-regular muted">VIP Gold · Member since 2024 · ID 48213</span>
            <Progress value={75} label="VIP level 7 → 8" />
          </div>
          <div className="profile-head__actions"><Button variant="primary" size="md" onClick={openDeposit}>Deposit</Button><Button variant="secondary" size="md">Edit profile</Button></div>
        </div>
      </Card>
      <div className="grid grid--stats">
        <StatTile label="Total wagered" value="€12,480" delta="+12.4% vs last week" trend="up" icon="wallet" />
        <StatTile label="Balance" value={money(balance)} icon="wallet" />
        <StatTile label="Net result" value="−€40.20" delta="−3.1% vs last week" trend="down" icon="jackpot" />
        <StatTile label="Tournaments won" value="3" delta="+1 this month" trend="up" icon="goblet-filled" />
      </div>
      <Tabs value={tab} onChange={setTab} items={[{ id: "overview", label: "Overview" }, { id: "history", label: "History" }, { id: "bonuses", label: "Bonuses" }, { id: "settings", label: "Settings" }]} />
      <div className="split split--profile">
        <Card title={tab === "overview" ? "Account" : tab === "history" ? "Recent activity" : tab === "bonuses" ? "Your bonuses" : "Account settings"}>
          {tab === "overview" || tab === "settings" ? (
            <div className="stack">
              <ListItem icon="user" title="Personal details" subtitle="Name, email, phone" divider />
              <ListItem icon="wallet" title="Payments & withdrawals" value="Verified" divider />
              <ListItem icon="gift" title="Bonuses & promotions" subtitle="3 active offers" divider />
              <ListItem icon="lock" title="Security" subtitle="2FA enabled" divider />
              <ListItem icon="settings" title="Responsible gaming" subtitle="Limits & self-exclusion" />
            </div>
          ) : tab === "history" ? (
            <div className="stack">
              <ListItem icon="game-casino" title="Golden Pharaoh" subtitle="Today, 21:14" value="+€120.00" chevron={false} divider />
              <ListItem icon="game-casino" title="Sweet Bonanza" subtitle="Today, 20:52" value="−€30.00" chevron={false} divider />
              <ListItem icon="goblet-filled" title="Weekend Race" subtitle="Yesterday" value="Rank 42" chevron={false} divider />
              <ListItem icon="wallet" title="Deposit" subtitle="Yesterday" value="+€100.00" chevron={false} />
            </div>
          ) : (
            <div className="stack">
              <ListItem icon="gift" title="Welcome bonus 200%" subtitle="Wager 35× · 12 days left" value="Active" chevron={false} divider />
              <ListItem icon="jackpot" title="200 free spins" subtitle="Golden Pharaoh" value="120 left" chevron={false} divider />
              <ListItem icon="goblet-filled" title="VIP cashback" subtitle="Every Monday" value="10%" chevron={false} />
            </div>
          )}
        </Card>
        <Card title="Preferences" className="split__side">
          <Alert tone="info" title="Verify your email">Confirm your address to unlock withdrawals.</Alert>
          <Switch checked={prefs.sound} onChange={(v) => setPrefs({ ...prefs, sound: v })} label="Sound effects" />
          <Switch checked={prefs.push} onChange={(v) => setPrefs({ ...prefs, push: v })} label="Push notifications" />
          <Switch checked={prefs.twofa} onChange={(v) => setPrefs({ ...prefs, twofa: v })} label="Two-factor authentication" />
          <Switch checked={false} disabled label="Live chat (offline)" />
        </Card>
      </div>
    </div>
  );
}
