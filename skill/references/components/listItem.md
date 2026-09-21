# List Item

> Згенеровано `tools/build-skill.py` з Token Studio JSON · 2026-09-21. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** List Item (component set) · State  
**Варіанти:** State: Default / Hover / Active / Disabled  
**Анатомія:** Рядок (auto-layout H, ghost-фон) → `Icon box` · `Text` (Title + Subtitle) · `Value` · `Chevron` · `Divider` (absolute).

Токенів: **20**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `listItem.bg.default` | listItem/bg/default | `{color.fill.ghost.default}` | `rgba(0, 0, 0, 0)` | `rgba(0, 0, 0, 0)` |
| `listItem.bg.hover` | listItem/bg/hover | `{color.fill.ghost.hover}` | `#16130F` | `#16130F` |
| `listItem.bg.active` | listItem/bg/active | `{color.fill.ghost.active}` | `#16130F` | `#16130F` |
| `listItem.bg.disabled` | listItem/bg/disabled | `{color.fill.ghost.disabled}` | `rgba(0, 0, 0, 0)` | `rgba(0, 0, 0, 0)` |
| `listItem.title.color.default` | listItem/title/color/default | `{color.text.primary}` | `#16130F` | `#16130F` |
| `listItem.title.color.disabled` | listItem/title/color/disabled | `{color.text.quaternary}` | `#16130F` | `#16130F` |
| `listItem.subtitle.color` | listItem/subtitle/color | `{color.text.tertiary}` | `#16130F` | `#16130F` |
| `listItem.detail.color` | listItem/detail/color | `{color.text.secondary}` | `#16130F` | `#16130F` |
| `listItem.icon.bg` | listItem/icon/bg | `{color.fill.secondary.default}` | `#16130F` | `#16130F` |
| `listItem.icon.color` | listItem/icon/color | `{color.text.secondary}` | `#16130F` | `#16130F` |
| `listItem.chevron.color` | listItem/chevron/color | `{color.text.tertiary}` | `#16130F` | `#16130F` |
| `listItem.divider.br` | listItem/divider/br | `{color.border.tertiary}` | `#16130F` | `#16130F` |

## Розміри та форма

| Токен | Figma variable | Тип | → Alias | Значення |
|---|---|---|---|---|
| `listItem.icon.size` | listItem/icon/size | sizing | `{size.control.md}` | `40` |
| `listItem.icon.iconSize` | listItem/icon/iconSize | sizing | `{iconSize.lg}` | `24` |
| `listItem.chevron.iconSize` | listItem/chevron/iconSize | sizing | `{iconSize.md}` | `20` |
| `listItem.paddingH` | listItem/paddingH | spacing | `{space.padding.md}` | `16` |
| `listItem.paddingV` | listItem/paddingV | spacing | `{space.padding.sm}` | `12` |
| `listItem.gap` | listItem/gap | spacing | `{space.gap.xl}` | `12` |
| `listItem.borderRadius` | listItem/borderRadius | borderRadius | `{borderRadius.surface}` | `12` |
| `listItem.divider.borderWidth` | listItem/divider/borderWidth | borderWidth | `{borderWidth.control}` | `1` |

## Текст (text styles, не токени)

| Розмір | Стиль |
|---|---|
| `title` | label/md |
| `subtitle` | caption/md |
| `value` | body/sm/regular |

## Нотатки

- Меню профілю/налаштувань. Booleans: Icon, Subtitle, Value, Chevron, Divider · 💠 Icon (swap).
