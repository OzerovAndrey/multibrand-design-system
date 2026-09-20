import { useEffect } from "react";
import { useRoute } from "./router";
import { useLook } from "./theme";
import { BottomNav } from "./ui/molecules";
import { Footer, Header } from "./ui/organisms";
import { IllustrationSprite } from "./art/Illustration";
import { DepositModal } from "./ui/auth";
import { GameLauncher, Toaster } from "./ui/game";
import ControlPanel from "./panel/ControlPanel";
import Home from "./pages/Home";
import Slots from "./pages/Slots";
import Tournaments from "./pages/Tournaments";
import Profile from "./pages/Profile";
import Register from "./pages/Register";
import Shop from "./pages/Shop";

export default function App() {
  const route = useRoute();
  useLook();
  useEffect(() => { window.scrollTo({ top: 0 }); }, [route]);
  const Page = { home: Home, slots: Slots, tournaments: Tournaments, profile: Profile, register: Register, login: () => <Register mode="login" />, shop: Shop }[route];
  return (
    <div className="app">
      <IllustrationSprite />
      <Header route={route} />
      <main><Page /></main>
      <Footer />
      <BottomNav active={route} />
      <DepositModal />
      <GameLauncher />
      <Toaster />
      <ControlPanel />
    </div>
  );
}
