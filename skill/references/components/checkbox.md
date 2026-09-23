# Checkbox

> Згенеровано `tools/build-skill.py` з Token Studio JSON · 2026-09-23. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Checkbox (component set) · Checked × State  
**Варіанти:** Checked: False / True · State: Default / Hover / Active / Disabled  
**Анатомія:** Контейнер (auto-layout H) → `Box` (frame, іконка `check-mark` при Checked) · `Label` (text).

Токенів: **20**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `checkbox.bg.default` | checkbox/bg/default | `{color.fill.secondary.default}` | `#16130F` | `#16130F` |
| `checkbox.bg.hover` | checkbox/bg/hover | `{color.fill.secondary.hover}` | `#16130F` | `#16130F` |
| `checkbox.bg.active` | checkbox/bg/active | `{color.fill.secondary.active}` | `#16130F` | `#16130F` |
| `checkbox.bg.disabled` | checkbox/bg/disabled | `{color.fill.secondary.disabled}` | `#16130F` | `#16130F` |
| `checkbox.checked.bg.default` | checkbox/checked/bg/default | `{color.fill.primary.default}` | `#CFA74A` | `#CFA74A` |
| `checkbox.checked.bg.hover` | checkbox/checked/bg/hover | `{color.fill.primary.hover}` | `#CFA74A` | `#CFA74A` |
| `checkbox.checked.bg.active` | checkbox/checked/bg/active | `{color.fill.primary.active}` | `#CFA74A` | `#CFA74A` |
| `checkbox.checked.bg.disabled` | checkbox/checked/bg/disabled | `{color.fill.primary.disabled}` | `#16130F` | `#16130F` |
| `checkbox.checked.iconColor` | checkbox/checked/iconColor | `{color.text.onPrimary}` | `#000000` | `#000000` |
| `checkbox.br.default` | checkbox/br/default | `{color.border.primary}` | `#16130F` | `#16130F` |
| `checkbox.br.hover` | checkbox/br/hover | `{color.border.accent}` | `#CFA74A` | `#CFA74A` |
| `checkbox.br.active` | checkbox/br/active | `{color.border.accent}` | `#CFA74A` | `#CFA74A` |
| `checkbox.br.disabled` | checkbox/br/disabled | `{color.border.tertiary}` | `#16130F` | `#16130F` |
| `checkbox.label.color.default` | checkbox/label/color/default | `{color.text.primary}` | `#16130F` | `#16130F` |
| `checkbox.label.color.disabled` | checkbox/label/color/disabled | `{color.text.quaternary}` | `#16130F` | `#16130F` |

## Розміри та форма

| Токен | Figma variable | Тип | → Alias | Значення |
|---|---|---|---|---|
| `checkbox.size` | checkbox/size | sizing | `{iconSize.lg}` | `24` |
| `checkbox.iconSize` | checkbox/iconSize | sizing | `{iconSize.sm}` | `16` |
| `checkbox.gap` | checkbox/gap | spacing | `{space.gap.lg}` | `10` |
| `checkbox.borderRadius` | checkbox/borderRadius | borderRadius | `{borderRadius.control}` | `8` |
| `checkbox.borderWidth` | checkbox/borderWidth | borderWidth | `{borderWidth.control}` | `1` |

## Текст (text styles, не токени)

| Розмір | Стиль |
|---|---|
| `label` | body/md/regular |

## Нотатки

- Форма боксу від `borderRadius.control` — у Nova квадрат, у Fiesta коло.
- Властивості: ✏️ Label · Show label (boolean).
