import { ReactNode } from "react";
import { Avatar, Button, Icon, IconName, Progress } from "./atoms";
import { cx } from "./util";
import { MARKS } from "../icons/paths";
import { BRANDS } from "../theme";

// ---------- Logo (mark = SVG from Figma, wordmark = live text in the brand display font) ----------
export function Logo({ mark }: { mark?: boolean }) {
  return (
    <span className="logo">
      {BRANDS.map(({ id: b }) => (
        <svg key={b} className="logo__mark" data-b={b} viewBox={MARKS[b].vb} fill="currentColor" aria-hidden="true">
          {MARKS[b].paths.map(([d, eo], i) => <path key={i} d={d} fillRule={eo ? "evenodd" : undefined} />)}
        </svg>
      ))}
      {!mark && <span className="logo__word">
        <span data-b="aurum">Aurum</span><span data-b="nova">Nova</span><span data-b="fiesta">fiesta</span><span data-b="ultra">Ultra</span>
      </span>}
    </span>
  );
}

// ---------- Balance ----------
export function Balance({ amount, compact, onDeposit }: { amount: string; compact?: boolean; onDeposit?: () => void }) {
  return (
    <div className={cx("balance", compact && "balance--sm")}>
      <Icon name="wallet" className="balance__icon" />
      <span className="balance__amount ts-label-md">{amount}</span>
      {compact ? <Button size="sm" iconOnly="plus" label="Deposit" onClick={onDeposit} /> : <Button size="md" iconLeft="plus" onClick={onDeposit}>Deposit</Button>}
    </div>
  );
}

// ---------- Section heading ----------
export function SectionHeading({ title, subtitle, icon, seeAll, arrows, onPrev, onNext, seeAllHref }: { title: string; subtitle?: string; icon?: IconName; seeAll?: boolean; arrows?: boolean; onPrev?: () => void; onNext?: () => void; seeAllHref?: string }) {
  return (
    <div className="section-heading">
      <div className="section-heading__title">
        {icon && <Icon name={icon} className="section-heading__icon" />}
        <div className="stack">
          <h2 className="section-heading__h ts-title-t4 ts-title-t2-md">{title}</h2>
          {subtitle && <span className="section-heading__sub ts-body-sm-regular">{subtitle}</span>}
        </div>
      </div>
      <div className="section-heading__actions">
        {seeAll && <Button variant="text" size="sm" iconRight="chevron-right" href={seeAllHref ?? "#/slots"}>See all</Button>}
        {arrows && <div className="section-heading__arrows"><Button variant="secondary" size="sm" iconOnly="chevron-left" label="Previous" onClick={onPrev} /><Button variant="secondary" size="sm" iconOnly="chevron-right" label="Next" onClick={onNext} /></div>}
      </div>
    </div>
  );
}

// ---------- Stat tile ----------
export function StatTile({ label, value, delta, trend = "neutral", icon }: { label: string; value: string; delta?: string; trend?: "neutral" | "up" | "down"; icon?: IconName }) {
  return (
    <div className="stat">
      <div className="stat__head">
        {icon && <span className="stat__icon"><Icon name={icon} /></span>}
        <span className="stat__label ts-label-sm">{label}</span>
      </div>
      <span className="stat__value ts-title-t4 ts-title-t3-md">{value}</span>
      {delta && <span className={cx("stat__delta ts-label-sm", `is-${trend}`)}>{delta}</span>}
    </div>
  );
}

// ---------- List item ----------
export function ListItem({ icon, title, subtitle, value, chevron = true, divider, active, disabled, onClick, right }: { icon?: IconName; title: string; subtitle?: string; value?: string; chevron?: boolean; divider?: boolean; active?: boolean; disabled?: boolean; onClick?: () => void; right?: ReactNode }) {
  return (
    <button type="button" className={cx("list-item", divider && "has-divider", active && "is-active")} disabled={disabled} onClick={onClick}>
      {icon && <span className="list-item__icon"><Icon name={icon} /></span>}
      <span className="list-item__text"><span className="list-item__title ts-label-md">{title}</span>{subtitle && <span className="list-item__sub ts-caption-md">{subtitle}</span>}</span>
      {value && <span className="list-item__value ts-body-sm-regular">{value}</span>}
      {right}
      {chevron && <Icon name="chevron-right" className="list-item__chevron" />}
    </button>
  );
}

// ---------- Leaderboard row ----------
export function LeaderRow({ rank, name, sub, score, prize, you }: { rank: number; name: string; sub: string; score: string; prize?: string; you?: boolean }) {
  const tier = rank === 1 ? "first" : rank === 2 ? "second" : rank === 3 ? "third" : "default";
  const initials = name === "You" ? "YOU" : name.split(/[ .]/).filter(Boolean).slice(0, 2).map((s) => s[0]).join("").toUpperCase();
  return (
    <div className={cx("leader", you && "is-you")}>
      <span className={cx("leader__rank ts-label-sm", `is-${tier}`)}>{rank}</span>
      <Avatar size="md" initials={initials} />
      <div className="leader__player"><span className="leader__name ts-label-md">{name}</span><span className="leader__sub ts-caption-md">{sub}</span></div>
      <div className="leader__result"><span className="leader__score ts-label-md">{score}</span>{prize && <span className="leader__prize ts-label-sm">{prize}</span>}</div>
    </div>
  );
}

// ---------- Bottom navigation ----------
export type NavKey = "home" | "slots" | "tournaments" | "shop" | "profile";
const NAV: { id: NavKey; label: string; icon: IconName; href: string }[] = [
  { id: "home", label: "Home", icon: "home", href: "#/" },
  { id: "slots", label: "Games", icon: "gamepad", href: "#/slots" },
  { id: "tournaments", label: "Tournaments", icon: "goblet-filled", href: "#/tournaments" },
  { id: "shop", label: "Shop", icon: "gift", href: "#/shop" },
  { id: "profile", label: "Profile", icon: "user", href: "#/profile" },
];
export function BottomNav({ active }: { active?: string }) {
  return (
    <nav className="bottom-nav" aria-label="Main">
      {NAV.map((n) => (
        <a key={n.id} href={n.href} className={cx("nav-item", active === n.id && "is-selected")}>
          <span className="nav-item__pill"><Icon name={n.icon} /></span>
          <span className="nav-item__label ts-caption-sm">{n.label}</span>
        </a>
      ))}
    </nav>
  );
}

// ---------- Progress row helper ----------
export { Progress };
