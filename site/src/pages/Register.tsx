import { useState } from "react";
import { Alert, Button, Checkbox, Input, Select, Tabs } from "../ui/atoms";
import { Card, Modal, PromoBanner } from "../ui/organisms";

type Method = "email" | "phone" | "oneclick";
export default function Register() {
  const [method, setMethod] = useState<Method>("email");
  const [show, setShow] = useState(false);
  const [f, setF] = useState({ email: "", phone: "", password: "", country: "ua", promo: "WELCOME200" });
  const [c, setC] = useState({ age: true, terms: true, offers: false });
  const [done, setDone] = useState(false);
  const valid = c.age && c.terms && (method === "oneclick" || (method === "email" ? /.+@.+\..+/.test(f.email) : f.phone.length > 6) && f.password.length >= 8);
  return (
    <div className="main container">
      <div className="auth">
        <Card className="auth__form">
          <div className="stack gap-md">
            <h1 className="ts-title-t1">Create your account</h1>
            <p className="ts-body-md-regular muted">Join in 30 seconds and get a 200% welcome bonus on your first deposit.</p>
          </div>
          <Tabs value={method} onChange={setMethod} items={[{ id: "email", label: "Email" }, { id: "phone", label: "Phone" }, { id: "oneclick", label: "One-click" }]} />
          <form className="stack gap-lg" onSubmit={(e) => { e.preventDefault(); if (valid) setDone(true); }}>
            {method === "email" && <Input label="Email" placeholder="you@example.com" iconLeft="mail" value={f.email} onChange={(v) => setF({ ...f, email: v })} type="email" />}
            {method === "phone" && <Input label="Phone" placeholder="+380 00 000 0000" value={f.phone} onChange={(v) => setF({ ...f, phone: v })} type="tel" />}
            {method !== "oneclick" && <Input label="Password" placeholder="At least 8 characters" helper="Use letters, numbers and a symbol" type={show ? "text" : "password"} iconRight="eye-off" onIconRight={() => setShow(!show)} value={f.password} onChange={(v) => setF({ ...f, password: v })} />}
            <Select label="Country" value={f.country} onChange={(v) => setF({ ...f, country: v })} options={[{ id: "ua", label: "Ukraine" }, { id: "pl", label: "Poland" }, { id: "de", label: "Germany" }, { id: "es", label: "Spain" }]} />
            <Input label="Promo code (optional)" placeholder="WELCOME200" value={f.promo} onChange={(v) => setF({ ...f, promo: v })} />
            <Alert tone={f.promo.toUpperCase() === "WELCOME200" ? "success" : "info"} title={f.promo.toUpperCase() === "WELCOME200" ? "Welcome bonus selected" : "No bonus selected"}>{f.promo.toUpperCase() === "WELCOME200" ? "200% up to €500 + 200 free spins." : "Enter WELCOME200 to get the welcome pack."}</Alert>
            <div className="stack gap-md">
              <Checkbox checked={c.age} onChange={(v) => setC({ ...c, age: v })} label="I am 18 or older" />
              <Checkbox checked={c.terms} onChange={(v) => setC({ ...c, terms: v })} label="I accept the Terms & Conditions and Privacy Policy" />
              <Checkbox checked={c.offers} onChange={(v) => setC({ ...c, offers: v })} label="Send me bonus offers and news" />
            </div>
            <Button variant="primary" size="lg" full type="submit" disabled={!valid}>Create account</Button>
          </form>
          <div className="divider"><span /><em className="ts-caption-md muted">or continue with</em><span /></div>
          <div className="grid grid--2"><Button variant="secondary" size="md" full>Google</Button><Button variant="secondary" size="md" full>Telegram</Button></div>
          <p className="ts-body-sm-regular muted">Already have an account? <a className="link" href="#/">Log in</a></p>
        </Card>
        <div className="auth__promo hide-mobile">
          <PromoBanner eyebrow="Welcome bonus" title="Your welcome pack is waiting" text="200% bonus, 200 free spins and a seat in the Weekend Race." primary={{ label: "See how it works", href: "#/shop" }} />
        </div>
      </div>
      <Modal open={done} title="Welcome aboard!" onClose={() => setDone(false)} actions={<><Button variant="primary" size="md" href="#/">Start playing</Button><Button variant="secondary" size="md" onClick={() => setDone(false)}>Close</Button></>}>Your account is ready and the welcome bonus is on its way to your balance.</Modal>
    </div>
  );
}
