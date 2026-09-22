# Badge

> Згенеровано `tools/build-skill.py` з Token Studio JSON · 2026-09-22. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Badge (component set) · Tone  
**Варіанти:** Tone: Neutral / Primary / Accent / Success / Warning / Danger / Info. Стани відсутні — статична мітка  
**Анатомія:** Контейнер (auto-layout H, height `badge.size`) → `Icon` (instance, вимкнена за замовчуванням) · `Label` (text).

Токенів: **19**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `badge.neutral.bg` | badge/neutral/bg | `{color.fill.secondary.hover}` | `#16130F` | `#16130F` |
| `badge.neutral.color` | badge/neutral/color | `{color.text.secondary}` | `#16130F` | `#16130F` |
| `badge.primary.bg` | badge/primary/bg | `{color.fill.primary.default}` | `#CFA74A` | `#CFA74A` |
| `badge.primary.color` | badge/primary/color | `{color.text.onPrimary}` | `#000000` | `#000000` |
| `badge.accent.bg` | badge/accent/bg | `{color.fill.accent.default}` | `#8E2C43` | `#8E2C43` |
| `badge.accent.color` | badge/accent/color | `{color.text.onAccent}` | `#FFFFFF` | `#FFFFFF` |
| `badge.success.bg` | badge/success/bg | `{color.fill.success.subtle}` | `#1F9D5B` | `#1F9D5B` |
| `badge.success.color` | badge/success/color | `{color.text.success}` | `#1F9D5B` | `#1F9D5B` |
| `badge.warning.bg` | badge/warning/bg | `{color.fill.warning.subtle}` | `#E69A12` | `#E69A12` |
| `badge.warning.color` | badge/warning/color | `{color.text.warning}` | `#E69A12` | `#E69A12` |
| `badge.danger.bg` | badge/danger/bg | `{color.fill.danger.default}` | `#D23B34` | `#D23B34` |
| `badge.danger.color` | badge/danger/color | `{color.text.onDanger}` | `#FFFFFF` | `#FFFFFF` |
| `badge.info.bg` | badge/info/bg | `{color.fill.info.subtle}` | `#B8704B` | `#B8704B` |
| `badge.info.color` | badge/info/color | `{color.text.info}` | `#B8704B` | `#B8704B` |

## Розміри та форма

| Токен | Figma variable | Тип | → Alias | Значення |
|---|---|---|---|---|
| `badge.size` | badge/size | sizing | `{size.control.xs}` | `24` |
| `badge.paddingH` | badge/paddingH | spacing | `{space.gap.lg}` | `10` |
| `badge.gap` | badge/gap | spacing | `{space.gap.xs}` | `4` |
| `badge.iconSize` | badge/iconSize | sizing | `{iconSize.sm}` | `16` |
| `badge.borderRadius` | badge/borderRadius | borderRadius | `{borderRadius.control}` | `8` |

## Текст (text styles, не токени)

| Розмір | Стиль |
|---|---|
| `label` | label/xs |

## Нотатки

- Тони мапляться на теми: Primary = product1, Accent = product2, Info = product3 — змінюються разом із брендом.
- Рідкість лутбоксів: Common = Neutral, Rare = Info, Epic = Accent, Legendary = Primary.
- Властивості: ✏️ Label · Icon (boolean) · 💠 Icon (swap, за замовчуванням `star-filled`).
