import { useSyncExternalStore } from "react";

// ---------- Favorites ----------
const FKEY = "mb-favorites";
let favs: string[] = (() => { try { return JSON.parse(localStorage.getItem(FKEY) || "[]"); } catch { return []; } })();
const fl = new Set<() => void>();
export const useFavorites = () => useSyncExternalStore((cb) => { fl.add(cb); return () => { fl.delete(cb); }; }, () => favs);
export function toggleFavorite(id: string, title: string) {
  const on = !favs.includes(id);
  favs = on ? [...favs, id] : favs.filter((x) => x !== id);
  try { localStorage.setItem(FKEY, JSON.stringify(favs)); } catch { /* ignore */ }
  fl.forEach((l) => l());
  toast(on ? "success" : "info", on ? "Added to favorites" : "Removed from favorites", on ? `${title} is now in your favorites.` : `${title} was removed from your favorites.`);
}

// ---------- Toasts ----------
export type Toast = { id: number; tone: "success" | "info" | "warning" | "danger"; title: string; text?: string };
let toasts: Toast[] = [];
let tid = 0;
const tl = new Set<() => void>();
export const useToasts = () => useSyncExternalStore((cb) => { tl.add(cb); return () => { tl.delete(cb); }; }, () => toasts);
export function dismissToast(id: number) { toasts = toasts.filter((t) => t.id !== id); tl.forEach((l) => l()); }
export function toast(tone: Toast["tone"], title: string, text?: string) {
  const id = ++tid;
  toasts = [...toasts.slice(-2), { id, tone, title, text }];
  tl.forEach((l) => l());
  window.setTimeout(() => dismissToast(id), 3200);
}

// ---------- Game launcher ----------
export type Launch = { id: string; title: string; provider: string; art: string; mode: "play" | "demo" } | null;
let launch: Launch = null;
const ll = new Set<() => void>();
export const useLaunch = () => useSyncExternalStore((cb) => { ll.add(cb); return () => { ll.delete(cb); }; }, () => launch);
export function launchGame(g: NonNullable<Launch>) { launch = g; ll.forEach((l) => l()); }
export function closeGame() { launch = null; ll.forEach((l) => l()); }

// ---------- Bonus modal ----------
export type BonusView = "claim" | "details" | null;
let bonus: BonusView = null;
const bl = new Set<() => void>();
export const useBonusView = () => useSyncExternalStore((cb) => { bl.add(cb); return () => { bl.delete(cb); }; }, () => bonus);
export function openBonus(v: NonNullable<BonusView>) { bonus = v; bl.forEach((l) => l()); }
export function closeBonus() { bonus = null; bl.forEach((l) => l()); }
