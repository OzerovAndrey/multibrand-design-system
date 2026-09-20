import { useEffect, useState } from "react";
import { Alert, Button, Checkbox, Input, Select, Tabs } from "../ui/atoms";
import { Card, Modal, PromoBanner } from "../ui/organisms";
import { GoogleChooser } from "../ui/auth";
import { nameFromEmail, signIn, useSession, type Provider, type User } from "../session";

type Method = "email" | "phone" | "oneclick";
const home = () => { location.hash = "#/"; };

export default function Register({ mode = "signup" }: { mode?: "signup" | "login" }) {
  const login = mode === "login";
  const { user } = useSession();
  const [method, setMethod] = useState<Method>("email");
  const [show, setShow] = useState(false);
  const [f, setF] = useState({ email: "", phone: "", password: "", country: "ua", promo: "WELCOME200" });
  const [c, setC] = useState({ age: true, terms: true, offers: false });
  const [pending, setPending] = useState<User | null>(null);
  const [google, setGoogle] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => { if (user && !pending) home(); }, [user, pending]);
  useEffect(() => { setError(""); if (login && method === "oneclick") setMethod("email"); }, [login, method]);

  const idOk = method === "email" ? /.+@.+\..+/.test(f.email) : method === "phone" ? f.phone.replace(/\D/g, "").length > 6 : true;
  const valid = login ? idOk && f.password.length >= 1 : c.age && c.terms && idOk && (method === "oneclick" || f.password.length >= 8);

  const submit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!valid) return;
    const provider: Provider = method;
    const email = method === "phone" ? f.phone : method === "oneclick" ? "player@demo.casino" : f.email;
    const u: User = { name: method === "email" ? nameFromEmail(f.email) : "Player", email, provider };
    if (login) { signIn(u); home(); } else setPending(u);
  };
  const finish = () => { if (pending) { signIn(pending); setPending(null); home(); } };
  const social = (p: "google" | "telegram") => {
    if (p === "google") { setGoogle(true); return; }
    signIn({ name: "Telegram User", email: "@telegram_user", provider: "telegram" });
  };

  return (
    <div className="main container">
      <div className="auth">
        <Card className="auth__form">
          <div className="stack gap-md">
            <h1 className="ts-title-t1">{login ? "Welcome back" : "Create your account"}</h1>
            <p className="ts-body-md-regular muted">{login ? "Log in to continue playing and see your balance." : "Join in 30 seconds and get a 200% welcome bonus on your first deposit."}</p>
          </div>
          <Tabs value={method} onChange={setMethod} items={login ? [{ id: "email", label: "Email" }, { id: "phone", label: "Phone" }] : [{ id: "email", label: "Email" }, { id: "phone", label: "Phone" }, { id: "oneclick", label: "One-click" }]} />
          <form className="stack gap-lg" onSubmit={submit}>
            {method === "email" && <Input label="Email" placeholder="you@example.com" iconLeft="mail" value={f.email} onChange={(v) => setF({ ...f, email: v })} type="email" />}
            {method === "phone" && <Input label="Phone" placeholder="+380 00 000 0000" value={f.phone} onChange={(v) => setF({ ...f, phone: v })} type="tel" />}
            {method !== "oneclick" && <Input label="Password" placeholder={login ? "Your password" : "At least 8 characters"} helper={login ? undefined : "Use letters, numbers and a symbol"} type={show ? "text" : "password"} iconRight="eye-off" onIconRight={() => setShow(!show)} value={f.password} onChange={(v) => setF({ ...f, password: v })} />}
            {!login && (
              <>
                <Select label="Country" value={f.country} onChange={(v) => setF({ ...f, country: v })} options={[{ id: "ua", label: "Ukraine" }, { id: "pl", label: "Poland" }, { id: "de", label: "Germany" }, { id: "es", label: "Spain" }]} />
                <Input label="Promo code (optional)" placeholder="WELCOME200" value={f.promo} onChange={(v) => setF({ ...f, promo: v })} />
                <Alert tone={f.promo.toUpperCase() === "WELCOME200" ? "success" : "info"} title={f.promo.toUpperCase() === "WELCOME200" ? "Welcome bonus selected" : "No bonus selected"}>{f.promo.toUpperCase() === "WELCOME200" ? "200% up to €500 + 200 free spins." : "Enter WELCOME200 to get the welcome pack."}</Alert>
                <div className="stack gap-md">
                  <Checkbox checked={c.age} onChange={(v) => setC({ ...c, age: v })} label="I am 18 or older" />
                  <Checkbox checked={c.terms} onChange={(v) => setC({ ...c, terms: v })} label="I accept the Terms & Conditions and Privacy Policy" />
                  <Checkbox checked={c.offers} onChange={(v) => setC({ ...c, offers: v })} label="Send me bonus offers and news" />
                </div>
              </>
            )}
            {error && <Alert tone="danger">{error}</Alert>}
            <Button variant="primary" size="lg" full type="submit" disabled={!valid}>{login ? "Log in" : "Create account"}</Button>
          </form>
          <div className="divider"><span /><em className="ts-caption-md muted">or continue with</em><span /></div>
          <div className="grid grid--2"><Button variant="secondary" size="md" full onClick={() => social("google")}>Google</Button><Button variant="secondary" size="md" full onClick={() => social("telegram")}>Telegram</Button></div>
          <p className="ts-body-sm-regular muted">{login ? <>New here? <a className="link" href="#/register">Create an account</a></> : <>Already have an account? <a className="link" href="#/login">Log in</a></>}</p>
        </Card>
        <div className="auth__promo hide-mobile">
          <PromoBanner eyebrow="Welcome bonus" title="Your welcome pack is waiting" text="200% bonus, 200 free spins and a seat in the Weekend Race." primary={{ label: "See how it works", href: "#/shop" }} />
        </div>
      </div>
      <GoogleChooser open={google} onClose={() => setGoogle(false)} onDone={() => { setGoogle(false); home(); }} />
      <Modal open={!!pending} title="Welcome aboard!" onClose={finish} actions={<><Button variant="primary" size="md" onClick={finish}>Start playing</Button></>}>Your account is ready. Make your first deposit to claim the 200% welcome bonus.</Modal>
    </div>
  );
}
