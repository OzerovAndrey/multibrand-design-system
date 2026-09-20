import { CSSProperties, ReactNode, useId } from "react";
import { ICON_PATHS } from "../icons/paths";
import { cx } from "./util";

export type IconName = keyof typeof ICON_PATHS;
export function Icon({ name, size, className, style }: { name: IconName; size?: string | number; className?: string; style?: CSSProperties }) {
  const paths = ICON_PATHS[name];
  const s = size !== undefined ? { width: size, height: size } : undefined;
  return (
    <svg className={cx("icon", className)} data-icon={name} viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" style={{ ...s, ...style }}>
      {paths.map(([d, eo], i) => <path key={i} d={d} fillRule={eo ? "evenodd" : undefined} clipRule={eo ? "evenodd" : undefined} />)}
    </svg>
  );
}

// ---------- Button ----------
type Size5 = "xs" | "sm" | "md" | "lg" | "xl";
const BTN_TS: Record<Size5, string> = { xs: "ts-label-sm", sm: "ts-label-md", md: "ts-label-md", lg: "ts-label-lg", xl: "ts-label-xl" };
export function Button({ variant = "primary", size = "md", iconLeft, iconRight, iconOnly, full, disabled, children, onClick, href, type = "button", label }: {
  variant?: "primary" | "secondary" | "text"; size?: Size5; iconLeft?: IconName; iconRight?: IconName; iconOnly?: IconName;
  full?: boolean; disabled?: boolean; children?: ReactNode; onClick?: (e: React.MouseEvent) => void; href?: string; type?: "button" | "submit"; label?: string;
}) {
  const cls = cx("btn", `btn--${variant}`, `btn--${size}`, BTN_TS[size], iconOnly && "btn--icon", full && "btn--full");
  const content = iconOnly ? <Icon name={iconOnly} /> : <>{iconLeft && <Icon name={iconLeft} />}{children}{iconRight && <Icon name={iconRight} />}</>;
  if (href) return <a className={cls} href={href} aria-label={label} aria-disabled={disabled}>{content}</a>;
  return <button className={cls} type={type} disabled={disabled} onClick={onClick} aria-label={label}>{content}</button>;
}

// ---------- Input ----------
export function Input({ label, helper, placeholder, value, onChange, type = "text", iconLeft, iconRight, onIconRight, size = "md", disabled, name }: {
  label?: string; helper?: string; placeholder?: string; value?: string; onChange?: (v: string) => void; type?: string; iconLeft?: IconName; iconRight?: IconName;
  onIconRight?: () => void; size?: "sm" | "md" | "lg"; disabled?: boolean; name?: string;
}) {
  const id = useId();
  return (
    <div className={cx("input", `input--${size}`, disabled && "is-disabled")}>
      {label && <label className="input__label ts-label-md" htmlFor={id}>{label}</label>}
      <div className="input__field">
        {iconLeft && <Icon name={iconLeft} className="input__icon" />}
        <input id={id} name={name} className="input__control ts-body-md-regular" type={type} placeholder={placeholder} value={value} disabled={disabled} onChange={(e) => onChange?.(e.target.value)} />
        {iconRight && (onIconRight ? <button type="button" className="input__icon-btn" onClick={onIconRight} aria-label="toggle"><Icon name={iconRight} className="input__icon" /></button> : <Icon name={iconRight} className="input__icon" />)}
      </div>
      {helper && <span className="input__helper ts-caption-md">{helper}</span>}
    </div>
  );
}

// ---------- Select (native select styled as the Input field) ----------
export function Select<T extends string>({ label, value, options, onChange, size = "md" }: { label?: string; value: T; options: { id: T; label: string }[]; onChange: (v: T) => void; size?: "sm" | "md" | "lg" }) {
  const id = useId();
  return (
    <div className={cx("input", `input--${size}`)}>
      {label && <label className="input__label ts-label-md" htmlFor={id}>{label}</label>}
      <div className="input__field input__field--select">
        <select id={id} className="input__control input__select ts-body-md-regular" value={value} onChange={(e) => onChange(e.target.value as T)}>
          {options.map((o) => <option key={o.id} value={o.id}>{o.label}</option>)}
        </select>
        <Icon name="chevron-down" className="input__icon" />
      </div>
    </div>
  );
}

// ---------- Badge ----------
export type BadgeTone = "neutral" | "primary" | "accent" | "success" | "warning" | "danger" | "info";
export function Badge({ tone = "neutral", icon, children }: { tone?: BadgeTone; icon?: IconName; children: ReactNode }) {
  return <span className={cx("badge", `badge--${tone}`, "ts-label-xs")}>{icon && <Icon name={icon} />}{children}</span>;
}

// ---------- Chip ----------
export function Chip({ selected, icon, size = "md", disabled, onClick, children }: { selected?: boolean; icon?: IconName; size?: "sm" | "md"; disabled?: boolean; onClick?: () => void; children: ReactNode }) {
  return (
    <button type="button" className={cx("chip", `chip--${size}`, selected && "is-selected", size === "sm" ? "ts-label-sm" : "ts-label-md")} disabled={disabled} onClick={onClick} aria-pressed={selected}>
      {icon && <Icon name={icon} />}{children}
    </button>
  );
}

// ---------- Tabs ----------
export function Tabs<T extends string>({ items, value, onChange, size = "md" }: { items: { id: T; label: string; icon?: IconName; disabled?: boolean }[]; value: T; onChange?: (id: T) => void; size?: "sm" | "md" }) {
  return (
    <div className="tabs" role="tablist">
      {items.map((it) => (
        <button key={it.id} role="tab" aria-selected={it.id === value} disabled={it.disabled} type="button" onClick={() => onChange?.(it.id)} className={cx("tab", `tab--${size}`, it.id === value && "is-selected", size === "sm" ? "ts-label-sm" : "ts-label-md")}>
          {it.icon && <Icon name={it.icon} />}{it.label}<span className="tab__indicator" />
        </button>
      ))}
    </div>
  );
}

// ---------- Avatar ----------
export function Avatar({ initials, size = "md", icon, vip, status, brand }: { initials?: string; size?: "xs" | "sm" | "md" | "lg" | "xl"; icon?: IconName; vip?: boolean; status?: boolean; brand?: boolean }) {
  return (
    <span className={cx("avatar", `avatar--${size}`, vip && "is-vip", brand && "avatar--brand", `ts-label-${size === "xs" ? "xs" : size}`)}>
      {icon ? <Icon name={icon} /> : initials}
      {vip && <span className="avatar__ring" />}
      {status && <span className="avatar__status" />}
    </span>
  );
}

// ---------- Progress ----------
export function Progress({ value, tone = "primary", size = "md", label, showValue = true }: { value: number; tone?: "primary" | "success" | "accent"; size?: "sm" | "md"; label?: string; showValue?: boolean }) {
  return (
    <div className={cx("progress", `progress--${size}`, `progress--${tone}`)}>
      {(label || showValue) && <div className="progress__head"><span className="progress__label ts-caption-md">{label}</span>{showValue && <span className="progress__value ts-label-sm">{Math.round(value)}%</span>}</div>}
      <div className="progress__track" role="progressbar" aria-valuenow={value} aria-valuemin={0} aria-valuemax={100}><div className="progress__fill" style={{ width: `${Math.max(0, Math.min(100, value))}%` }} /></div>
    </div>
  );
}

// ---------- Checkbox / Switch ----------
export function Checkbox({ checked, onChange, label, disabled }: { checked: boolean; onChange?: (v: boolean) => void; label?: ReactNode; disabled?: boolean }) {
  return (
    <label className={cx("checkbox", disabled && "is-disabled")}>
      <input type="checkbox" checked={checked} disabled={disabled} onChange={(e) => onChange?.(e.target.checked)} />
      <span className="checkbox__box"><Icon name="check-mark" /></span>
      {label && <span className="checkbox__label ts-body-md-regular">{label}</span>}
    </label>
  );
}
export function Switch({ checked, onChange, label, disabled }: { checked: boolean; onChange?: (v: boolean) => void; label?: ReactNode; disabled?: boolean }) {
  return (
    <label className={cx("switch", disabled && "is-disabled")}>
      <input type="checkbox" role="switch" checked={checked} disabled={disabled} onChange={(e) => onChange?.(e.target.checked)} />
      <span className="switch__track"><span className="switch__knob" /></span>
      {label && <span className="switch__label ts-body-md-regular">{label}</span>}
    </label>
  );
}

// ---------- Alert ----------
const ALERT_ICON: Record<string, IconName> = { info: "info", success: "check-mark-circle-filled", warning: "warning-filled", danger: "close-circle-filled" };
export function Alert({ tone = "info", title, children, onClose }: { tone?: "info" | "success" | "warning" | "danger"; title?: string; children?: ReactNode; onClose?: () => void }) {
  return (
    <div className={cx("alert", `alert--${tone}`)} role="alert">
      <Icon name={ALERT_ICON[tone]} className="alert__icon" />
      <div className="alert__text">{title && <span className="alert__title ts-label-md">{title}</span>}{children && <span className="alert__msg ts-body-sm-regular">{children}</span>}</div>
      {onClose && <button className="alert__close" onClick={onClose} aria-label="Dismiss"><Icon name="close" /></button>}
    </div>
  );
}
