# Modal

> Згенеровано `scripts/build-token-docs.py` з Token Studio JSON · 2026-09-20. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Modal (component set) · Size  
**Варіанти:** Size: xs (bottom sheet 360, лише верхні кути) / md (діалог 480)  
**Анатомія:** Контейнер (V, clip) → `Handle` (тільки xs) · `Header` (Title + Close) · `Content` (slot) · `Actions`.

Токенів: **15**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `modal.bg` | modal/bg | `{color.bg.secondary}` | `#16130F` | `#16130F` |
| `modal.br` | modal/br | `{color.border.tertiary}` | `#16130F` | `#16130F` |
| `modal.overlay.bg` | modal/overlay/bg | `{color.bg.overlay}` | `rgba(0, 0, 0, 0.6)` | `rgba(0, 0, 0, 0.6)` |
| `modal.title.color` | modal/title/color | `{color.text.primary}` | `#16130F` | `#16130F` |
| `modal.text.color` | modal/text/color | `{color.text.secondary}` | `#16130F` | `#16130F` |
| `modal.handle.bg` | modal/handle/bg | `{color.border.primary}` | `#16130F` | `#16130F` |

## Розміри та форма

| Токен | Figma variable | Тип | → Alias | Значення |
|---|---|---|---|---|
| `modal.borderRadius` | modal/borderRadius | borderRadius | `{borderRadius.surface}` | `12` |
| `modal.borderWidth` | modal/borderWidth | borderWidth | `{borderWidth.control}` | `1` |
| `modal.paddingH.xs` | modal/paddingH/xs | spacing | `{space.padding.lg}` | `20` |
| `modal.paddingH.md` | modal/paddingH/md | spacing | `{space.padding.xl}` | `24` |
| `modal.paddingV.xs` | modal/paddingV/xs | spacing | `{space.padding.lg}` | `20` |
| `modal.paddingV.md` | modal/paddingV/md | spacing | `{space.padding.xl}` | `24` |
| `modal.gap` | modal/gap | spacing | `{space.gap.xl}` | `12` |
| `modal.header.gap` | modal/header/gap | spacing | `{space.gap.md}` | `8` |
| `modal.actions.gap` | modal/actions/gap | spacing | `{space.gap.md}` | `8` |

## Текст (text styles, не токени)

| Розмір | Стиль |
|---|---|
| `title` | title/t3 |
| `text` | body/md/regular |

## Нотатки

- Scrim — `modal.overlay.bg` (окремий шар під модалкою). ✏️ Title · Secondary action (boolean) · slot Content.
