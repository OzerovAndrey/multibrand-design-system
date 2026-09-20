import { useSyncExternalStore } from "react";

export type Provider = "email" | "phone" | "google" | "telegram" | "oneclick";
export type User = { name: string; email: string; provider: Provider };
type State = { user: User | null; balance: number; deposited: boolean; depositOpen: boolean; bonusClaimed: boolean };

const KEY = "mb-session";
const load = (): State => {
  try {
    const s = JSON.parse(localStorage.getItem(KEY) || "null");
    if (s?.user) return { user: s.user, balance: s.balance ?? 0, deposited: !!s.deposited, depositOpen: false, bonusClaimed: !!s.bonusClaimed };
  } catch { /* storage may be blocked */ }
  return { user: null, balance: 0, deposited: false, depositOpen: false, bonusClaimed: false };
};

let state: State = load();
const listeners = new Set<() => void>();
const set = (patch: Partial<State>) => {
  state = { ...state, ...patch };
  try { localStorage.setItem(KEY, JSON.stringify({ user: state.user, balance: state.balance, deposited: state.deposited, bonusClaimed: state.bonusClaimed })); } catch { /* ignore */ }
  listeners.forEach((l) => l());
};

export const useSession = () => useSyncExternalStore((cb) => { listeners.add(cb); return () => { listeners.delete(cb); }; }, () => state);

export const signIn = (user: User) => set({ user });
export const signOut = () => set({ user: null, balance: 0, deposited: false, depositOpen: false, bonusClaimed: false });
export const claimBonus = () => set({ bonusClaimed: true });
export const openDeposit = () => set({ depositOpen: true });
export const closeDeposit = () => set({ depositOpen: false });
export const WELCOME_CAP = 500;
export const welcomeBonus = (amount: number) => Math.min(amount * 2, WELCOME_CAP);
export function credit(amount: number) {
  const bonus = state.deposited ? 0 : welcomeBonus(amount);
  set({ balance: state.balance + amount + bonus, deposited: true });
  return bonus;
}

export const money = (n: number) => "€" + n.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
export const initials = (name: string) => name.split(/[\s.@_-]+/).filter(Boolean).slice(0, 2).map((s) => s[0]).join("").toUpperCase() || "U";
export const nameFromEmail = (e: string) => e.split("@")[0].replace(/[._-]+/g, " ").replace(/\b\w/g, (c) => c.toUpperCase()) || "Player";
