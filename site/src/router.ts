import { useSyncExternalStore } from "react";
export type Route = "home" | "slots" | "tournaments" | "profile" | "register" | "login" | "shop";
export const ROUTES: { id: Route; path: string; label: string }[] = [
  { id: "home", path: "/", label: "Home" },
  { id: "slots", path: "/slots", label: "Slots" },
  { id: "tournaments", path: "/tournaments", label: "Tournaments" },
  { id: "shop", path: "/shop", label: "Shop" },
  { id: "profile", path: "/profile", label: "Profile" },
  { id: "register", path: "/register", label: "Sign up" },
  { id: "login", path: "/login", label: "Log in" },
];
const current = (): Route => {
  const p = location.hash.replace(/^#/, "") || "/";
  return ROUTES.find((r) => r.path === p)?.id ?? "home";
};
const subscribe = (cb: () => void) => { window.addEventListener("hashchange", cb); return () => window.removeEventListener("hashchange", cb); };
export const useRoute = () => useSyncExternalStore(subscribe, current);
export const href = (id: Route) => "#" + (ROUTES.find((r) => r.id === id)?.path ?? "/");
