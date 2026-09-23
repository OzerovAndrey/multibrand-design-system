# Alert

> Згенеровано `tools/build-skill.py` з Token Studio JSON · 2026-09-23. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Alert (component set) · Tone  
**Варіанти:** Tone: Info / Success / Warning / Danger  
**Анатомія:** Контейнер (auto-layout H) → `Icon` · `Text` (Title + Message) · `Close`.

Токенів: **20**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `alert.text.color` | alert/text/color | `{color.text.primary}` | `#16130F` | `#16130F` |
| `alert.close.color` | alert/close/color | `{color.text.tertiary}` | `#16130F` | `#16130F` |
| `alert.info.bg` | alert/info/bg | `{color.fill.info.subtle}` | `#B8704B` | `#B8704B` |
| `alert.info.color` | alert/info/color | `{color.text.info}` | `#B8704B` | `#B8704B` |
| `alert.info.br` | alert/info/br | `{color.border.secondary}` | `#16130F` | `#16130F` |
| `alert.success.bg` | alert/success/bg | `{color.fill.success.subtle}` | `#1F9D5B` | `#1F9D5B` |
| `alert.success.color` | alert/success/color | `{color.text.success}` | `#1F9D5B` | `#1F9D5B` |
| `alert.success.br` | alert/success/br | `{color.border.secondary}` | `#16130F` | `#16130F` |
| `alert.warning.bg` | alert/warning/bg | `{color.fill.warning.subtle}` | `#E69A12` | `#E69A12` |
| `alert.warning.color` | alert/warning/color | `{color.text.warning}` | `#E69A12` | `#E69A12` |
| `alert.warning.br` | alert/warning/br | `{color.border.secondary}` | `#16130F` | `#16130F` |
| `alert.danger.bg` | alert/danger/bg | `{color.fill.danger.subtle}` | `#D23B34` | `#D23B34` |
| `alert.danger.color` | alert/danger/color | `{color.text.danger}` | `#D23B34` | `#D23B34` |
| `alert.danger.br` | alert/danger/br | `{color.border.danger}` | `#D23B34` | `#D23B34` |

## Розміри та форма

| Токен | Figma variable | Тип | → Alias | Значення |
|---|---|---|---|---|
| `alert.borderRadius` | alert/borderRadius | borderRadius | `{borderRadius.surface}` | `12` |
| `alert.paddingH` | alert/paddingH | spacing | `{space.padding.md}` | `16` |
| `alert.paddingV` | alert/paddingV | spacing | `{space.padding.md}` | `16` |
| `alert.gap` | alert/gap | spacing | `{space.gap.lg}` | `10` |
| `alert.iconSize` | alert/iconSize | sizing | `{iconSize.lg}` | `24` |
| `alert.borderWidth` | alert/borderWidth | borderWidth | `{borderWidth.control}` | `1` |

## Текст (text styles, не токени)

| Розмір | Стиль |
|---|---|
| `title` | label/md |
| `message` | body/sm/regular |

## Нотатки

- Booleans: Show title, Dismissible. Іконка тону — статична (info / check-mark-circle-filled / warning-filled / close-circle-filled).
