# Header

> Згенеровано `scripts/build-token-docs.py` з Token Studio JSON · 2026-09-19. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Header (component set) · State  ·  частини: Logo (component set · Brand), Balance (component)  
**Варіанти:** State: Logged in / Search open / Logged out  
**Анатомія:** Контейнер (auto-layout H, space-between, padding `header.paddingH/V`, нижній бордер `header.br` × `header.borderWidth`) → `Logo` (instance) · `Actions` (auto-layout H, gap `header.gap`) → `Tools` (gap `header.actions.gap`: Search · Support) · `Balance`.

Токенів: **10**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `header.bg` | header/bg | `{color.bg.primary}` | `#16130F` | `#16130F` |
| `header.br` | header/br | `{color.border.tertiary}` | `#16130F` | `#16130F` |
| `header.logo.color` | header/logo/color | `{color.text.primary}` | `#16130F` | `#16130F` |
| `header.logo.iconColor` | header/logo/iconColor | `{color.text.accent}` | `#CFA74A` | `#CFA74A` |

## Розміри та форма

| Токен | Figma variable | Тип | → Alias | Значення |
|---|---|---|---|---|
| `header.borderWidth` | header/borderWidth | borderWidth | `{borderWidth.control}` | `1` |
| `header.paddingH` | header/paddingH | spacing | `{space.padding.xl}` | `24` |
| `header.paddingV` | header/paddingV | spacing | `{space.padding.md}` | `16` |
| `header.gap` | header/gap | spacing | `{space.gap.xl}` | `12` |
| `header.actions.gap` | header/actions/gap | spacing | `{space.gap.md}` | `8` |
| `header.logo.height` | header/logo/height | sizing | `{size.control.sm}` | `32` |

## Нотатки

- Організм: збирається з Button, Input, Logo і Balance — власних кольорів у контролах немає, тільки контейнер і лого.
- Logged in: Search і Support = Button Secondary md icon-only (іконки `search`, `support`), далі Balance.
- Search open: замість кнопки пошуку — Input md State=Active, Label off, іконки `search` / `close`, ширина 320 (референс, у макеті — Fill).
- Logged out: тільки Log in (Button Secondary md) і Sign up (Button Primary md).
- Висота 72 не токен: `header.paddingV` 16 × 2 + control md 40.
- Logo — asset, не токен: Brand-варіант (Aurum / Nova / Fiesta) обирається разом із Brand-mode; кольори — `header.logo.iconColor` (марка) і `header.logo.color` (wordmark), тому лого саме перемикається light/dark.
- Logo, Balance, Search, Support, Log in, Sign up — exposed instances: властивості вкладених компонентів доступні з панелі хедера.
