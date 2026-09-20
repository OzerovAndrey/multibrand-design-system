import { CSSProperties, ReactNode, useEffect } from "react";
import { Badge, BadgeTone, Button, Icon, IconName, Progress } from "./atoms";
import { Balance, Logo } from "./molecules";
import { cx } from "./util";
import { ROUTES, Route, href } from "../router";
import { Illustration, type IllusKey } from "../art/Illustration";

// ---------- Header ----------
export function Header({ route, loggedIn = true }: { route: Route; loggedIn?: boolean }) {
  const links = ROUTES.filter((r) => ["home", "slots", "tournaments", "shop"].includes(r.id));
  return (
    <header className="header">
      <div className="header__inner container">
        <a href="#/" className="header__logo" aria-label="Home"><Logo /></a>
        <nav className="header__nav hide-mobile" aria-label="Primary">
          {links.map((l) => <a key={l.id} href={href(l.id)} className={cx("header__link ts-label-md", route === l.id && "is-active")}>{l.label}</a>)}
        </nav>
        <div className="header__actions">
          <div className="header__tools">
            <Button variant="secondary" size="md" iconOnly="search" label="Search" />
            <span className="hide-mobile"><Button variant="secondary" size="md" iconOnly="gift" label="Bonuses" href="#/shop" /></span>
          </div>
          {loggedIn ? (
            <>
              <span className="hide-mobile"><Balance amount="€1,250.00" /></span>
              <span className="hide-desktop"><Balance amount="€1,250" compact /></span>
            </>
          ) : (
            <div className="header__auth"><Button variant="secondary" size="md" href="#/register">Log in</Button><Button variant="primary" size="md" href="#/register">Sign up</Button></div>
          )}
        </div>
      </div>
    </header>
  );
}

// ---------- Footer ----------
const FOOT = [
  { title: "Casino", links: ["Slots", "Live casino", "Table games", "Jackpots", "New games"] },
  { title: "Promotions", links: ["Bonuses", "Tournaments", "VIP club", "Promo codes"] },
  { title: "Help", links: ["Support 24/7", "FAQ", "Payments", "Responsible gaming"] },
  { title: "Company", links: ["About us", "Terms & Conditions", "Privacy policy", "AML policy"] },
];
export function Footer() {
  return (
    <footer className="footer">
      <div className="container footer__inner">
        <div className="footer__top">
          <div className="footer__about">
            <Logo />
            <p className="footer__tagline ts-body-sm-regular">Premium casino lobby with 3,000+ games, instant payouts and 24/7 support.</p>
            <div className="footer__social">{(["mail", "users", "gift", "jackpot"] as IconName[]).map((n) => <Button key={n} variant="secondary" size="sm" iconOnly={n} label={n} />)}</div>
          </div>
          <div className="footer__links">
            {FOOT.map((c) => (
              <div key={c.title} className="footer__col">
                <span className="footer__title ts-label-md">{c.title}</span>
                {c.links.map((l) => <a key={l} href="#/" className="footer__link ts-body-sm-regular">{l}</a>)}
              </div>
            ))}
          </div>
        </div>
        <div className="footer__pay">
          <span className="footer__title ts-label-md">Payment methods</span>
          <div className="footer__badges">{([["wallet", "E-wallets"], ["coins-filled", "Crypto"], ["game-casino", "Cards"], ["diamond-filled", "Bank transfer"]] as [IconName, string][]).map(([i, l]) => <span key={l} className="footer__badge ts-label-sm"><Icon name={i} />{l}</span>)}</div>
        </div>
        <div className="footer__bottom">
          <span className="footer__age ts-label-sm">18+</span>
          <p className="footer__caption ts-caption-md">Gambling can be addictive — play responsibly. 18+ only. Demo product for a design-system portfolio, no real-money gaming.<br />© 2026 Demo Casino. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
}

// ---------- Game art (brand-reactive casino illustrations) ----------
export type ArtKey = "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h";
const ART_ILLUSTRATION: Record<ArtKey, IllusKey> = { a: "slots", b: "roulette", c: "cards", d: "chips", e: "dice", f: "gem", g: "chest", h: "trophy" };
export function GameArt({ pattern = "a", className }: { pattern?: ArtKey; className?: string }) {
  const name = ART_ILLUSTRATION[pattern];
  return (
    <div className={cx("art", className)} style={{ "--bg": `var(--art-${pattern}-bg)` } as CSSProperties}>
      <i className="art__glow" />
      <Illustration name={name} className={cx("art__ill", name === "chest" && "art__ill--wide")} />
    </div>
  );
}

// Wide scenes for banners and tournament covers
export function SceneArt({ scene, className }: { scene: "jackpot" | "arena"; className?: string }) {
  return (
    <div className={cx("scene", `scene--${scene}`, className)} style={{ "--bg": `var(--art-${scene}-bg)` } as CSSProperties}>
      <Illustration name={scene} className="scene__ill" />
    </div>
  );
}

// ---------- Game tile ----------
export function GameTile({ title, provider, art, type = "slot", badge, favorite, players, onPlay }: { title: string; provider: string; art: ArtKey; type?: "slot" | "live"; badge?: { tone: BadgeTone; label: string }; favorite?: boolean; players?: string; onPlay?: () => void }) {
  return (
    <article className={cx("game-tile", `game-tile--${type}`)}>
      <div className="game-tile__cover">
        <GameArt pattern={art} className="game-tile__art" />
        <div className="game-tile__hover"><button type="button" className="game-tile__play" aria-label={`Play ${title}`} onClick={onPlay}><Icon name="play-filled" /></button></div>
        <div className="game-tile__top">
          {badge ? <Badge tone={badge.tone}>{badge.label}</Badge> : <span />}
          <button type="button" className="game-tile__fav" aria-label="Favorite">{favorite ? <Icon name="heart-filled" /> : <Icon name="heart" />}</button>
        </div>
        {players && <div className="game-tile__bottom"><span className="game-tile__players ts-label-sm"><Icon name="users" />{players}</span></div>}
      </div>
      <div className="game-tile__info"><span className="game-tile__title ts-label-md">{title}</span><span className="game-tile__provider ts-caption-md">{provider}</span></div>
    </article>
  );
}

// ---------- Promo banner ----------
export function PromoBanner({ eyebrow, title, text, primary, secondary }: { eyebrow?: string; title: string; text: string; primary: { label: string; href?: string }; secondary?: { label: string; href?: string } }) {
  return (
    <section className="promo">
      <SceneArt scene="jackpot" className="promo__art" />
      <div className="promo__content">
        {eyebrow && <Badge tone="accent">{eyebrow}</Badge>}
        <h1 className="promo__title ts-title-t2 ts-display-d3-md">{title}</h1>
        <p className="promo__text ts-body-md-regular">{text}</p>
        <div className="promo__actions">
          <Button variant="primary" size="lg" href={primary.href}>{primary.label}</Button>
          {secondary && <Button variant="secondary" size="lg" href={secondary.href}>{secondary.label}</Button>}
        </div>
      </div>
    </section>
  );
}

// ---------- Tournament card ----------
const T_BADGE: Record<string, { tone: BadgeTone; label: string }> = { live: { tone: "danger", label: "Live" }, upcoming: { tone: "info", label: "Starts in 2d" }, finished: { tone: "neutral", label: "Finished" } };
export function TournamentCard({ state, title, prize, players = "1,204 players", time, progress = 75, onJoin }: { state: "live" | "upcoming" | "finished"; title: string; prize: string; players?: string; time: string; progress?: number; onJoin?: () => void }) {
  const b = T_BADGE[state];
  return (
    <article className="tournament">
      <div className="tournament__cover"><SceneArt scene="arena" className="tournament__art" /><div className="tournament__top"><Badge tone={b.tone}>{b.label}</Badge></div></div>
      <div className="tournament__body">
        <h3 className="tournament__title ts-title-t4">{title}</h3>
        <div className="tournament__prize"><span className="tournament__prize-label ts-caption-md">Prize pool</span><span className="tournament__prize-row"><Icon name="goblet-filled" className="tournament__trophy" /><span className="tournament__prize-amount ts-title-t2">{prize}</span></span></div>
        <div className="tournament__meta">
          <span className="tournament__meta-row ts-body-sm-regular"><Icon name="users" />{players}</span>
          <span className="tournament__meta-row ts-body-sm-regular"><Icon name="clock" />{time}</span>
        </div>
        {state !== "finished" && <Progress value={progress} tone="accent" size="sm" label="Seats taken" />}
        {state === "live" ? <Button variant="primary" size="md" full onClick={onJoin}>Join now</Button> : state === "upcoming" ? <Button variant="secondary" size="md" full>Remind me</Button> : <Button variant="text" size="md" full>View results</Button>}
      </div>
    </article>
  );
}

// ---------- Lootbox card ----------
export type Rarity = "common" | "rare" | "epic" | "legendary";
const R_BADGE: Record<Rarity, BadgeTone> = { common: "neutral", rare: "info", epic: "accent", legendary: "primary" };
export function LootboxCard({ rarity, title, description, price, onOpen }: { rarity: Rarity; title: string; description: string; price: string; onOpen?: () => void }) {
  return (
    <article className={cx("lootbox", `lootbox--${rarity}`)}>
      <div className="lootbox__art">
        <i className="lootbox__halo" /><Icon name="gift" className="lootbox__icon" /><i className="lootbox__strip" />
        <div className="lootbox__top"><Badge tone={R_BADGE[rarity]}>{rarity}</Badge></div>
      </div>
      <div className="lootbox__info"><h3 className="lootbox__title ts-title-t4">{title}</h3><p className="lootbox__desc ts-body-sm-regular">{description}</p></div>
      <div className="lootbox__buy">
        <span className="lootbox__price ts-label-lg"><Icon name="coins-filled" />{price}</span>
        <Button variant="primary" size="sm" onClick={onOpen}>Open</Button>
      </div>
    </article>
  );
}

// ---------- Card (card.default tokens) ----------
export function Card({ children, className, title }: { children: ReactNode; className?: string; title?: string }) {
  return <section className={cx("card", className)}>{title && <h3 className="card__title ts-title-t4">{title}</h3>}{children}</section>;
}

// ---------- Modal ----------
export function Modal({ open, title, onClose, children, actions }: { open: boolean; title: string; onClose: () => void; children: ReactNode; actions: ReactNode }) {
  useEffect(() => {
    if (!open) return;
    const k = (e: KeyboardEvent) => e.key === "Escape" && onClose();
    window.addEventListener("keydown", k); document.body.style.overflow = "hidden";
    return () => { window.removeEventListener("keydown", k); document.body.style.overflow = ""; };
  }, [open, onClose]);
  if (!open) return null;
  return (
    <div className="modal-scrim" onMouseDown={(e) => e.target === e.currentTarget && onClose()}>
      <div className="modal" role="dialog" aria-modal="true" aria-label={title}>
        <span className="modal__handle" />
        <div className="modal__head"><h2 className="modal__title ts-title-t3">{title}</h2><Button variant="secondary" size="sm" iconOnly="close" label="Close" onClick={onClose} /></div>
        <div className="modal__content ts-body-md-regular">{children}</div>
        <div className="modal__actions">{actions}</div>
      </div>
    </div>
  );
}
