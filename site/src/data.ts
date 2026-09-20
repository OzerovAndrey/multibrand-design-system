import type { ArtKey, Rarity } from "./ui/organisms";
import type { BadgeTone } from "./ui/atoms";

export type Game = { id: string; title: string; provider: string; art: ArtKey; badge?: { tone: BadgeTone; label: string }; category: string };
const P = ["Aurum Studio", "Nova Games", "Fiesta Play"];
const NAMES = ["Golden Pharaoh", "Sweet Bonanza", "Book of Stars", "Neon Sevens", "Wild Safari", "Cosmic Cash", "Dragon Vault", "Fruit Party", "Ocean King", "Lucky Lantern", "Thunder Reels", "Royal Flush",
  "Pirate Gold", "Mystic Moon", "Diamond Rush", "Samurai Spin", "Viking Fortune", "Aztec Treasure", "Jungle Jackpot", "Retro Reels", "Crystal Cave", "Fire Phoenix", "Lucky Clover", "Space Miners",
  "Egyptian Nights", "Candy Land", "Wolf Legend", "Magic Lamp", "Tiger Temple", "Robin Hood", "Big Bass Party", "Zeus Thunder"];
const ARTS: ArtKey[] = ["a", "b", "c", "d", "e", "f"];
const CATS = ["slots", "jackpots", "megaways", "bonus buy", "new"];
export const GAMES: Game[] = NAMES.map((title, i) => ({
  id: "g" + i, title, provider: P[(i * 7) % 3], art: ARTS[(i * 5 + Math.floor(i / 6)) % 6], category: CATS[i % 5],
  badge: i % 11 === 0 ? { tone: "primary", label: "New" } : i % 7 === 3 ? { tone: "danger", label: "Hot" } : i % 13 === 5 ? { tone: "accent", label: "Jackpot" } : undefined,
}));
export const PROVIDERS = ["All providers", ...P];

export const LIVE = [
  { id: "l1", title: "Lightning Roulette", provider: "Aurum Live", art: "e" as ArtKey, players: "1,204" },
  { id: "l2", title: "Crazy Time", provider: "Nova Live", art: "b" as ArtKey, players: "3,871" },
  { id: "l3", title: "Blackjack VIP", provider: "Fiesta Live", art: "c" as ArtKey, players: "412" },
  { id: "l4", title: "Baccarat Gold", provider: "Aurum Live", art: "a" as ArtKey, players: "986" },
];

export type Tournament = { id: string; state: "live" | "upcoming" | "finished"; title: string; prize: string; time: string; art: ArtKey; players: string; progress: number };
export const TOURNAMENTS: Tournament[] = [
  { id: "t1", state: "live", title: "Weekend Race", prize: "€50,000", time: "Ends in 02:14:36", art: "f", players: "1,204 players", progress: 75 },
  { id: "t2", state: "live", title: "Spin & Win Marathon", prize: "€30,000", time: "Ends in 1d 04:10", art: "b", players: "2,318 players", progress: 62 },
  { id: "t3", state: "upcoming", title: "Golden Spin League", prize: "€25,000", time: "Starts Sat, 20:00", art: "c", players: "640 players", progress: 34 },
  { id: "t4", state: "upcoming", title: "Nova Night Cup", prize: "€10,000", time: "Starts Sun, 21:00", art: "e", players: "412 players", progress: 18 },
  { id: "t5", state: "live", title: "Live Casino Rush", prize: "€15,000", time: "Ends in 05:32:10", art: "a", players: "871 players", progress: 81 },
  { id: "t6", state: "finished", title: "Summer Jackpot", prize: "€100,000", time: "Ended 2 days ago", art: "d", players: "5,102 players", progress: 100 },
];

export const LEADERS = [
  { name: "Alexander M.", sub: "Level 12 · VIP", score: "214,900", prize: "€1,000" },
  { name: "Maria K.", sub: "Level 11 · VIP", score: "198,220", prize: "€500" },
  { name: "Ivan P.", sub: "Level 9", score: "176,015", prize: "€250" },
  { name: "Olena S.", sub: "Level 8", score: "151,300", prize: "€100" },
  { name: "Dmytro L.", sub: "Level 8", score: "139,880", prize: "€75" },
  { name: "Andrii T.", sub: "Level 7", score: "118,040", prize: "€25" },
  { name: "Katya V.", sub: "Level 7", score: "109,760", prize: "€25" },
];

export type Box = { id: string; rarity: Rarity; title: string; description: string; price: number };
export const BOXES: Box[] = [
  { id: "b1", rarity: "common", title: "Wooden Crate", description: "2–3 items · cash or free spins", price: 300 },
  { id: "b2", rarity: "rare", title: "Silver Chest", description: "3–4 items · 1 guaranteed Rare", price: 600 },
  { id: "b3", rarity: "epic", title: "Royal Coffer", description: "3–5 items · 1 guaranteed Epic", price: 1200 },
  { id: "b4", rarity: "legendary", title: "Golden Vault", description: "4–6 items · guaranteed Legendary", price: 2500 },
  { id: "b5", rarity: "rare", title: "Mystic Barrel", description: "3–4 items · bonus multipliers", price: 650 },
  { id: "b6", rarity: "common", title: "Iron Chest", description: "2–3 items · free spins", price: 350 },
  { id: "b7", rarity: "epic", title: "Crown Casket", description: "3–5 items · VIP points", price: 1400 },
  { id: "b8", rarity: "legendary", title: "Diamond Vault", description: "4–6 items · jackpot ticket", price: 3000 },
];
export const fmt = (n: number) => n.toLocaleString("en-US");
