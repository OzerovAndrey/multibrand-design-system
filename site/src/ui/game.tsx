import { useEffect, useState } from "react";
import { Alert, Badge, Button, Progress } from "./atoms";
import { GameArt, Modal, type ArtKey } from "./organisms";
import { closeGame, dismissToast, useLaunch, useToasts } from "../store";
import { useSession } from "../session";

const STEPS = ["Connecting to game server…", "Loading assets…", "Starting the game…"];

export function Toaster() {
  const toasts = useToasts();
  return (
    <div className="toaster" aria-live="polite">
      {toasts.map((t) => <Alert key={t.id} tone={t.tone} title={t.title} onClose={() => dismissToast(t.id)}>{t.text}</Alert>)}
    </div>
  );
}

export function GameLauncher() {
  const game = useLaunch();
  const { user } = useSession();
  const [pct, setPct] = useState(0);
  const needLogin = !!game && game.mode === "play" && !user;

  useEffect(() => {
    setPct(0);
    if (!game || needLogin) return;
    const t = window.setInterval(() => setPct((p) => Math.min(100, p + 4 + Math.random() * 6)), 140);
    return () => window.clearInterval(t);
  }, [game, needLogin]);

  const done = pct >= 100;
  const title = game ? game.title : "";
  const actions = needLogin
    ? <><Button variant="primary" size="md" onClick={() => { closeGame(); location.hash = "#/login"; }}>Log in</Button><Button variant="secondary" size="md" onClick={() => { closeGame(); location.hash = "#/register"; }}>Sign up</Button></>
    : done
      ? <Button variant="primary" size="md" onClick={closeGame}>Close</Button>
      : <Button variant="secondary" size="md" onClick={closeGame}>Cancel</Button>;

  return (
    <Modal open={!!game} title={title} onClose={closeGame} actions={actions}>
      {game && (
        <div className="launch">
          <div className="launch__art"><GameArt pattern={game.art as ArtKey} /></div>
          <div className="launch__body">
            <span><Badge tone={game.mode === "demo" ? "info" : "primary"}>{game.mode === "demo" ? "Demo mode" : "Real play"}</Badge></span>
            {needLogin ? <p className="ts-body-md-regular">Log in or create an account to play {game.title} for real.</p>
              : done ? <Alert tone="success" title="Game is ready">This is a portfolio demo — the game itself is not available.</Alert>
              : <Progress value={Math.round(pct)} label={STEPS[Math.min(2, Math.floor(pct / 34))]} />}
          </div>
        </div>
      )}
    </Modal>
  );
}
