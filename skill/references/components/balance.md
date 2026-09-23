# Balance

> Згенеровано `tools/build-skill.py` з Token Studio JSON · 2026-09-23. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Balance (component set) · Size — молекула всередині Header  
**Варіанти:** Size: sm (Deposit = Button Primary sm icon-only `plus`) / md (Button Primary md «Deposit»). Властивості: ✏️ Amount · 💰 Icon · 💠 Icon  
**Анатомія:** Контейнер (auto-layout H, bg `balance.bg`, radius `balance.borderRadius`, paddingL `balance.paddingL.{size}`, paddingR 0, gap `balance.gap.{size}`) → `Icon` (instance `wallet`, `balance.iconSize.{size}`, `balance.iconColor`) · `Amount` (text) · `Deposit` (Button Primary).

Токенів: **10**. Посилаються тільки на theme / brand-семантику, не на core.

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
| `balance.borderRadius` | balance/borderRadius | borderRadius | `{borderRadius.control}` | `8` |
| `balance.paddingL.sm` | balance/paddingL/sm | spacing | `{space.padding.sm}` | `12` |
| `balance.paddingL.md` | balance/paddingL/md | spacing | `{space.padding.md}` | `16` |
| `balance.gap.sm` | balance/gap/sm | spacing | `{space.gap.sm}` | `6` |
| `balance.gap.md` | balance/gap/md | spacing | `{space.gap.md}` | `8` |
| `balance.iconSize.sm` | balance/iconSize/sm | sizing | `{iconSize.sm}` | `16` |
| `balance.iconSize.md` | balance/iconSize/md | sizing | `{iconSize.md}` | `20` |

## Текст (text styles, не токени)

| Розмір | Стиль |
|---|---|
| `Amount` | label/md |

## Нотатки

- Висота = висота кнопки Deposit (sm 32 / md 40): контейнер hug, кнопка впритул праворуч.
- Deposit — exposed instance Button.
