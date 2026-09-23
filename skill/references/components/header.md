# Header

> Згенеровано `tools/build-skill.py` з Token Studio JSON · 2026-09-23. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Header (component set) · Size × State  ·  частини: Logo (component set · Brand × Type), Balance (component set · Size)  
**Варіанти:** Size: xs (mobile 360) / md (desktop, від sm 768 і ширше — Fill) · State: Logged in / Search open / Logged out  
**Анатомія:** Контейнер (auto-layout H, space-between, padding `header.paddingH/V.{size}`, нижній бордер `header.br` × `header.borderWidth`) → `Logo` (instance) · `Actions` (auto-layout H, gap `header.gap`) → `Tools` (gap `header.actions.gap`: Search · Support) · `Balance`.

Токенів: **19**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `header.bg` | header/bg | `{color.bg.primary}` | `#16130F` | `#16130F` |
| `header.br` | header/br | `{color.border.tertiary}` | `#16130F` | `#16130F` |
| `header.logo.color` | header/logo/color | `{color.text.primary}` | `#16130F` | `#16130F` |
| `header.logo.iconColor` | header/logo/iconColor | `{color.text.accent}` | `#CFA74A` | `#CFA74A` |
| `header.link.color.default` | header/link/color/default | `{color.text.secondary}` | `#16130F` | `#16130F` |
| `header.link.color.active` | header/link/color/active | `{color.text.accent}` | `#CFA74A` | `#CFA74A` |
| `header.link.bg.hover` | header/link/bg/hover | `{color.fill.ghost.hover}` | `#16130F` | `#16130F` |

## Розміри та форма

| Токен | Figma variable | Тип | → Alias | Значення |
|---|---|---|---|---|
| `header.borderWidth` | header/borderWidth | borderWidth | `{borderWidth.control}` | `1` |
| `header.paddingH.xs` | header/paddingH/xs | spacing | `{space.padding.md}` | `16` |
| `header.paddingH.md` | header/paddingH/md | spacing | `{space.padding.xl}` | `24` |
| `header.paddingV.xs` | header/paddingV/xs | spacing | `{space.padding.xs}` | `12` |
| `header.paddingV.md` | header/paddingV/md | spacing | `{space.padding.md}` | `16` |
| `header.gap` | header/gap | spacing | `{space.gap.xl}` | `12` |
| `header.actions.gap` | header/actions/gap | spacing | `{space.gap.md}` | `8` |
| `header.logo.height` | header/logo/height | sizing | `{size.control.sm}` | `32` |
| `header.link.paddingH` | header/link/paddingH | spacing | `{space.padding.sm}` | `12` |
| `header.link.paddingV` | header/link/paddingV | spacing | `{space.gap.md}` | `8` |
| `header.link.borderRadius` | header/link/borderRadius | borderRadius | `{borderRadius.control}` | `8` |
| `header.nav.gap` | header/nav/gap | spacing | `{space.gap.xs}` | `4` |

## Нотатки

- Організм: збирається з Button, Input, Logo і Balance — власних кольорів у контролах немає, тільки контейнер і лого.
- md · Logged in: Search і Support = Button Secondary md icon-only (`search`, `support`), далі Balance md.
- md · Search open: замість кнопки пошуку — Input md State=Active, Label off, іконки `search` / `close`, ширина 320.
- md · Logged out: Log in (Button Secondary md) і Sign up (Button Primary md).
- xs: Logo Type=Mark, контроли sm (32), Support прихований (іде в меню / TabBar), Balance Size=sm. Search open — Input sm Fill на місці лого.
- Висота не токен: md 72 = `header.paddingV.md` 16 × 2 + control md 40; xs 56 = `header.paddingV.xs` 12 × 2 + control sm 32.
- Logo — asset, не токен: Brand-варіант (Aurum / Nova / Fiesta / Ultra) обирається разом із Brand-mode; Type=Full / Mark. Кольори — `header.logo.iconColor` (марка) і `header.logo.color` (wordmark).
- Logo, Balance, Search, Support, Log in, Sign up — exposed instances.
