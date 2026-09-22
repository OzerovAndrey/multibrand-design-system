# Input

> Згенеровано `tools/build-skill.py` з Token Studio JSON · 2026-09-22. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Input (component set) · Size × State  
**Варіанти:** Size: sm / md / lg · State: Default / Hover / Active / Disabled (focus не робимо)  
**Анатомія:** Wrapper (auto-layout V, gap `input.wrapper.gap`) → `Label` (text) · `Field` (auto-layout H) · `Helper` (text). Field → `Icon left` · `Placeholder` · `Value` · `Icon right`.

Токенів: **39**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `input.bg.default` | input/bg/default | `{color.bg.secondary}` | `#16130F` | `#16130F` |
| `input.bg.hover` | input/bg/hover | `{color.bg.secondary}` | `#16130F` | `#16130F` |
| `input.bg.active` | input/bg/active | `{color.bg.secondary}` | `#16130F` | `#16130F` |
| `input.bg.disabled` | input/bg/disabled | `{color.fill.secondary.disabled}` | `#16130F` | `#16130F` |
| `input.br.default` | input/br/default | `{color.border.secondary}` | `#16130F` | `#16130F` |
| `input.br.hover` | input/br/hover | `{color.border.primary}` | `#16130F` | `#16130F` |
| `input.br.active` | input/br/active | `{color.border.accent}` | `#CFA74A` | `#CFA74A` |
| `input.br.disabled` | input/br/disabled | `{color.border.tertiary}` | `#16130F` | `#16130F` |
| `input.color.default` | input/color/default | `{color.text.primary}` | `#16130F` | `#16130F` |
| `input.color.hover` | input/color/hover | `{color.text.primary}` | `#16130F` | `#16130F` |
| `input.color.active` | input/color/active | `{color.text.primary}` | `#16130F` | `#16130F` |
| `input.color.disabled` | input/color/disabled | `{color.text.tertiary}` | `#16130F` | `#16130F` |
| `input.iconColor.default` | input/iconColor/default | `{color.text.secondary}` | `#16130F` | `#16130F` |
| `input.iconColor.hover` | input/iconColor/hover | `{color.text.secondary}` | `#16130F` | `#16130F` |
| `input.iconColor.active` | input/iconColor/active | `{color.text.primary}` | `#16130F` | `#16130F` |
| `input.iconColor.disabled` | input/iconColor/disabled | `{color.text.quaternary}` | `#16130F` | `#16130F` |
| `input.label.color.default` | input/label/color/default | `{color.text.secondary}` | `#16130F` | `#16130F` |
| `input.label.color.hover` | input/label/color/hover | `{color.text.secondary}` | `#16130F` | `#16130F` |
| `input.label.color.active` | input/label/color/active | `{color.text.secondary}` | `#16130F` | `#16130F` |
| `input.label.color.disabled` | input/label/color/disabled | `{color.text.tertiary}` | `#16130F` | `#16130F` |
| `input.helper.color.default` | input/helper/color/default | `{color.text.tertiary}` | `#16130F` | `#16130F` |
| `input.helper.color.hover` | input/helper/color/hover | `{color.text.tertiary}` | `#16130F` | `#16130F` |
| `input.helper.color.active` | input/helper/color/active | `{color.text.tertiary}` | `#16130F` | `#16130F` |
| `input.helper.color.disabled` | input/helper/color/disabled | `{color.text.quaternary}` | `#16130F` | `#16130F` |

## Розміри та форма

| Токен | Figma variable | Тип | → Alias | Значення |
|---|---|---|---|---|
| `input.size.sm` | input/size/sm | sizing | `{size.control.sm}` | `32` |
| `input.size.md` | input/size/md | sizing | `{size.control.md}` | `40` |
| `input.size.lg` | input/size/lg | sizing | `{size.control.lg}` | `48` |
| `input.paddingH.sm` | input/paddingH/sm | spacing | `{space.padding.sm}` | `12` |
| `input.paddingH.md` | input/paddingH/md | spacing | `{space.padding.md}` | `16` |
| `input.paddingH.lg` | input/paddingH/lg | spacing | `{space.padding.lg}` | `20` |
| `input.gap.sm` | input/gap/sm | spacing | `{space.gap.sm}` | `6` |
| `input.gap.md` | input/gap/md | spacing | `{space.gap.md}` | `8` |
| `input.gap.lg` | input/gap/lg | spacing | `{space.gap.lg}` | `10` |
| `input.iconSize.sm` | input/iconSize/sm | sizing | `{iconSize.sm}` | `16` |
| `input.iconSize.md` | input/iconSize/md | sizing | `{iconSize.md}` | `20` |
| `input.iconSize.lg` | input/iconSize/lg | sizing | `{iconSize.lg}` | `24` |
| `input.borderRadius` | input/borderRadius | borderRadius | `{borderRadius.surface}` | `12` |
| `input.borderWidth` | input/borderWidth | borderWidth | `{borderWidth.control}` | `1` |
| `input.wrapper.gap` | input/wrapper/gap | spacing | `{space.gap.xs}` | `4` |

## Текст (text styles, не токени)

| Розмір | Стиль |
|---|---|
| `sm` | value/placeholder body/sm/regular · label label/sm · helper caption/md |
| `md` | value/placeholder body/md/regular · label label/md · helper caption/md |
| `lg` | value/placeholder body/lg/regular · label label/md · helper caption/md |

## Нотатки

- Placeholder і Value фарбуються одним токеном `input.color.*` — окремого `placeholder.color` немає.
- Властивості: ✏️ Label / Placeholder / Value / Helper · booleans Label, Helper, Placeholder, Value, ⬅️ Icon, Icon ➡️ · swap 💠 Icon left / right.
- Іконки за замовчуванням: left `search`, right `close` (Static — Icons).
- Висоти sm/md/lg = Button sm/md/lg (32/40/48) — стають в один ряд.
