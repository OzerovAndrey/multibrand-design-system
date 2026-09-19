# Footer

> Згенеровано `scripts/build-token-docs.py` з Token Studio JSON · 2026-09-19. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Footer (component set) · Size  ·  частини: _Footer badge, _Footer age  
**Варіанти:** Size: xs (mobile 360) / sm (tablet 768) / md (desktop, Fill для md 1024 · lg 1200 · xl 1440)  
**Анатомія:** Контейнер (auto-layout V, padding `footer.paddingH/V.{size}`, gap `footer.gap.{size}`, верхній бордер) → `Top` (md — H, xs/sm — V) → `About` (Logo · Tagline · Social) · `Links` (4 колонки, gap `footer.links.gap.{size}`) → `Divider` → `Payments` (Title · Methods з _Footer badge) → `Divider` → `Bottom` (Legal: _Footer age · Disclaimer · © | Language).

Токенів: **33**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `footer.bg` | footer/bg | `{color.bg.primary}` | `#16130F` | `#16130F` |
| `footer.br` | footer/br | `{color.border.tertiary}` | `#16130F` | `#16130F` |
| `footer.title.color` | footer/title/color | `{color.text.primary}` | `#16130F` | `#16130F` |
| `footer.link.color` | footer/link/color | `{color.text.secondary}` | `#16130F` | `#16130F` |
| `footer.caption.color` | footer/caption/color | `{color.text.tertiary}` | `#16130F` | `#16130F` |
| `footer.badge.bg` | footer/badge/bg | `{color.fill.secondary.default}` | `#16130F` | `#16130F` |
| `footer.badge.color` | footer/badge/color | `{color.text.secondary}` | `#16130F` | `#16130F` |
| `footer.badge.iconColor` | footer/badge/iconColor | `{color.text.secondary}` | `#16130F` | `#16130F` |
| `footer.age.br` | footer/age/br | `{color.border.primary}` | `#16130F` | `#16130F` |
| `footer.age.color` | footer/age/color | `{color.text.secondary}` | `#16130F` | `#16130F` |

## Розміри та форма

| Токен | Figma variable | Тип | → Alias | Значення |
|---|---|---|---|---|
| `footer.borderWidth` | footer/borderWidth | borderWidth | `{borderWidth.control}` | `1` |
| `footer.paddingH.xs` | footer/paddingH/xs | spacing | `{layout.paddingH.xs}` | `16` |
| `footer.paddingH.sm` | footer/paddingH/sm | spacing | `{layout.paddingH.sm}` | `24` |
| `footer.paddingH.md` | footer/paddingH/md | spacing | `{layout.paddingH.md}` | `24` |
| `footer.paddingV.xs` | footer/paddingV/xs | spacing | `{layout.rowGap.xs}` | `24` |
| `footer.paddingV.sm` | footer/paddingV/sm | spacing | `{layout.rowGap.sm}` | `32` |
| `footer.paddingV.md` | footer/paddingV/md | spacing | `{layout.rowGap.lg}` | `40` |
| `footer.gap.xs` | footer/gap/xs | spacing | `{layout.rowGap.xs}` | `24` |
| `footer.gap.sm` | footer/gap/sm | spacing | `{layout.rowGap.xs}` | `24` |
| `footer.gap.md` | footer/gap/md | spacing | `{layout.rowGap.sm}` | `32` |
| `footer.links.gap.xs` | footer/links/gap/xs | spacing | `{layout.columnGap.xs}` | `16` |
| `footer.links.gap.sm` | footer/links/gap/sm | spacing | `{layout.columnGap.sm}` | `16` |
| `footer.links.gap.md` | footer/links/gap/md | spacing | `{layout.columnGap.lg}` | `24` |
| `footer.column.gap` | footer/column/gap | spacing | `{space.gap.xl}` | `12` |
| `footer.social.gap` | footer/social/gap | spacing | `{space.gap.md}` | `8` |
| `footer.badge.borderRadius` | footer/badge/borderRadius | borderRadius | `{borderRadius.control}` | `999` |
| `footer.badge.size` | footer/badge/size | sizing | `{size.control.sm}` | `32` |
| `footer.badge.paddingH` | footer/badge/paddingH | spacing | `{space.padding.sm}` | `12` |
| `footer.badge.gap` | footer/badge/gap | spacing | `{space.gap.sm}` | `6` |
| `footer.badge.iconSize` | footer/badge/iconSize | sizing | `{iconSize.sm}` | `16` |
| `footer.age.borderWidth` | footer/age/borderWidth | borderWidth | `{borderWidth.control}` | `1` |
| `footer.age.borderRadius` | footer/age/borderRadius | borderRadius | `{borderRadius.control}` | `999` |
| `footer.age.size` | footer/age/size | sizing | `{size.control.sm}` | `32` |

## Текст (text styles, не токени)

| Розмір | Стиль |
|---|---|
| `Title колонки / Payments` | label/md |
| `Посилання, Tagline` | body/sm/regular |
| `Disclaimer, ©` | caption/md |
| `_Footer badge` | label/sm |
| `_Footer age` | label/xs |

## Нотатки

- Колонки: Casino · Promotions · Help · Company. md — About фіксовано 320 + колонки Fill; sm — About над колонками; xs — колонки 2×2 (wrap, ширина 156).
- Social = Button Secondary sm icon-only: telegram · instagram · facebook · youtube · tiktok (Static — Icons).
- Payment methods — бейджі `_Footer badge` (💠 Icon + ✏️ Label): Cards `card-send` · Bank transfer `money-send` · E-wallets `wallet` · Crypto `coin`. Ряд з wrap.
- Language = Button Secondary sm з іконками `translate` / `chevron-down`.
- Поля й відступи прив'язані до сітки сторінки (`layout.paddingH.*`, `layout.rowGap.*`, `layout.columnGap.*`) — футер вирівняний з контентом.
- Фон `color.bg.primary` (як Header), щоб Secondary-кнопки і бейджі (`fill.secondary`) були видимі в обох темах.
- Logo і Language — exposed instances.
