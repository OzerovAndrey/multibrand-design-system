# Balance

> Згенеровано `scripts/build-token-docs.py` з Token Studio JSON · 2026-09-19. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Balance (component) · молекула всередині Header  
**Варіанти:** Без варіантів. Властивості: ✏️ Amount · 💰 Icon (boolean) · 💠 Icon (swap)  
**Анатомія:** Контейнер (auto-layout H, bg `balance.bg`, radius `balance.borderRadius`, paddingL `balance.paddingL`, paddingR 0, gap `balance.gap`) → `Icon` (instance `wallet`, `balance.iconSize`, `balance.iconColor`) · `Amount` (text) · `Deposit` (Button Primary md).

Токенів: **7**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `balance.bg` | balance/bg | `{color.fill.secondary.default}` | `#16130F` | `#16130F` |
| `balance.color` | balance/color | `{color.text.primary}` | `#16130F` | `#16130F` |
| `balance.iconColor` | balance/iconColor | `{color.text.secondary}` | `#16130F` | `#16130F` |

## Розміри та форма

| Токен | Figma variable | Тип | → Alias | Значення |
|---|---|---|---|---|
| `balance.borderRadius` | balance/borderRadius | borderRadius | `{borderRadius.control}` | `999` |
| `balance.paddingL` | balance/paddingL | spacing | `{space.padding.md}` | `16` |
| `balance.gap` | balance/gap | spacing | `{space.gap.md}` | `8` |
| `balance.iconSize` | balance/iconSize | sizing | `{iconSize.md}` | `20` |

## Текст (text styles, не токени)

| Розмір | Стиль |
|---|---|
| `Amount` | label/md |

## Нотатки

- Висота = висота кнопки Deposit (control md 40): контейнер hug, кнопка впритул праворуч.
- Deposit — exposed instance Button: розмір/іконку/текст можна міняти з панелі.
