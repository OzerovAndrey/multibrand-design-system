import { useSyncExternalStore } from "react";
export type Route = "home" | "slots" | "tournaments" | "tournament" | "profile" | "register" | "login" | "shop";
export const ROUTES: { id: Route; path: string; label: string }[] = [
  { id: "home", path: "/", label: "Home" },
  { id: "slots", path: "/slots", label: "Slots" },
  { id: "tournaments", path: "/tournaments", label: "Tournaments" },
  { id: "tournament", path: "/tournament", label: "Tournament" },
  { id: "shop", path: "/shop", label: "Shop" },
  { id: "profile", path: "/profile", label: "Profile" },
  { id: "register", path: "/register", label: "Sign up" },
  { id: "login", path: "/login", label: "Log in" },
];
const subscribe = (cb: () => void) => { window.addEventListener("hashchange", cb); return () => window.removeEventListener("hashchange", cb); };
const hashPath = () => location.hash.replace(/^#/, "").split("?")[0] || "/";
const current = (): Route => {
  const p = hashPath();
  if (p.startsWith("/tournament/")) return "tournament";
  return ROUTES.find((r) => r.path === p)?.id ?? "home";
};
export const tournamentId = () => hashPath().replace(/^\/tournament\//, "");
export const tournamentHref = (id: string) => `#/tournament/${id}`;
export const useTournamentId = () => useSyncExternalStore(subscribe, tournamentId);
export const useRoute = () => useSyncExternalStore(subscribe, current);
export const href = (id: Route) => "#" + (ROUTES.find((r) => r.id === id)?.path ?? "/");
