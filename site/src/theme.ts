import { useSyncExternalStore } from "react";

export type Brand = "aurum" | "nova" | "fiesta";
export type Theme = "light" | "dark";
export const BRANDS: { id: Brand; name: string; tagline: string }[] = [
  { id: "aurum", name: "Aurum", tagline: "Warm premium · soft corners · serif" },
  { id: "nova", name: "Nova", tagline: "Cold tech · sharp corners · grotesk" },
  { id: "fiesta", name: "Fiesta", tagline: "Bold mass-market · pill shapes · rounded" },
];
export const THEMES: Theme[] = ["light", "dark"];

type State = { brand: Brand; theme: Theme; prev: { brand: Brand; theme: Theme } | null; tick: number };
const root = document.documentElement;
let state: State = { brand: (root.dataset.brand as Brand) || "aurum", theme: (root.dataset.theme as Theme) || "light", prev: null, tick: 0 };
const listeners = new Set<() => void>();
const emit = () => listeners.forEach((l) => l());

function persist() {
  try {
    localStorage.setItem("mb-state", JSON.stringify({ brand: state.brand, theme: state.theme }));
    const q = new URLSearchParams(location.search);
    q.set("brand", state.brand); q.set("theme", state.theme);
    history.replaceState(null, "", `${location.pathname}?${q.toString()}${location.hash}`);
  } catch { /* storage may be blocked */ }
}

const reduceMotion = () => window.matchMedia("(prefers-reduced-motion: reduce)").matches;

let target = { brand: state.brand, theme: state.theme };
function commit(snap: { brand: Brand; theme: Theme }) {
  if (state.brand === snap.brand && state.theme === snap.theme && root.dataset.brand === snap.brand && root.dataset.theme === snap.theme) return;
  const prev = { brand: state.brand, theme: state.theme };
  root.dataset.brand = snap.brand; root.dataset.theme = snap.theme;
  state = { ...snap, prev, tick: state.tick + 1 };
  persist(); emit();
}

export function setLook(next: Partial<Pick<State, "brand" | "theme">>, origin?: { x: number; y: number }) {
  target = { ...target, ...next };
  const snap = { ...target };
  if (snap.brand === state.brand && snap.theme === state.theme) return;
  const doc = document as Document & { startViewTransition?: (cb: () => void) => { ready: Promise<void>; finished: Promise<void> } };
  if (doc.startViewTransition && !reduceMotion()) {
    const x = origin?.x ?? window.innerWidth - 60, y = origin?.y ?? window.innerHeight - 60;
    const r = Math.hypot(Math.max(x, window.innerWidth - x), Math.max(y, window.innerHeight - y));
    const t = doc.startViewTransition(() => commit(snap));
    t.ready.then(() => {
      root.animate({ clipPath: [`circle(0px at ${x}px ${y}px)`, `circle(${r}px at ${x}px ${y}px)`] }, { duration: 750, easing: "cubic-bezier(.22,.7,.18,1)", pseudoElement: "::view-transition-new(root)" });
    }).catch(() => {});
    // safety net: whatever happened to the transition, the DOM must end up in the latest requested look
    t.finished.catch(() => {}).finally(() => commit(target));
  } else {
    root.classList.add("switching"); commit(snap);
    window.setTimeout(() => root.classList.remove("switching"), 500);
  }
}

const subscribe = (cb: () => void) => { listeners.add(cb); return () => listeners.delete(cb); };
export const getLook = () => state;
export function useLook() { return useSyncExternalStore(subscribe, () => state); }

// guided tour: cycles through all 6 combinations
let tourTimer: number | null = null;
const tourListeners = new Set<() => void>();
export const isTouring = () => tourTimer !== null;
export function useTouring() { return useSyncExternalStore((cb) => { tourListeners.add(cb); return () => tourListeners.delete(cb); }, () => tourTimer !== null); }
export function toggleTour() {
  if (tourTimer !== null) { clearInterval(tourTimer); tourTimer = null; tourListeners.forEach((l) => l()); return; }
  const seq: { brand: Brand; theme: Theme }[] = [];
  for (const b of BRANDS) for (const t of THEMES) seq.push({ brand: b.id, theme: t });
  let i = seq.findIndex((s) => s.brand === state.brand && s.theme === state.theme);
  const step = () => { i = (i + 1) % seq.length; setLook(seq[i], { x: window.innerWidth / 2, y: window.innerHeight / 2 }); };
  tourTimer = window.setInterval(step, 3200); tourListeners.forEach((l) => l()); step();
}
