# Chip

> Згенеровано `tools/build-skill.py` з Token Studio JSON · 2026-09-20. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Chip (component set) · Selected × State × Size  
**Варіанти:** Selected: False / True · State: Default / Hover / Active / Disabled · Size: sm (32) / md (40)  
**Анатомія:** Контейнер (auto-layout H, pill/м'який/гострий від бренду) → `Icon` (instance) · `Label` (text).

Токенів: **32**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `chip.bg.default` | chip/bg/default | `{color.fill.secondary.default}` | `#16130F` | `#16130F` |
| `chip.bg.hover` | chip/bg/hover | `{color.fill.secondary.hover}` | `#16130F` | `#16130F` |
| `chip.bg.active` | chip/bg/active | `{color.fill.secondary.active}` | `#16130F` | `#16130F` |
| `chip.bg.disabled` | chip/bg/disabled | `{color.fill.secondary.disabled}` | `#16130F` | `#16130F` |
| `chip.color.default` | chip/color/default | `{color.text.secondary}` | `#16130F` | `#16130F` |
| `chip.color.hover` | chip/color/hover | `{color.text.primary}` | `#16130F` | `#16130F` |
| `chip.color.active` | chip/color/active | `{color.text.primary}` | `#16130F` | `#16130F` |
| `chip.color.disabled` | chip/color/disabled | `{color.text.quaternary}` | `#16130F` | `#16130F` |
| `chip.br.default` | chip/br/default | `{color.border.secondary}` | `#16130F` | `#16130F` |
| `chip.br.hover` | chip/br/hover | `{color.border.primary}` | `#16130F` | `#16130F` |
| `chip.br.active` | chip/br/active | `{color.border.primary}` | `#16130F` | `#16130F` |
| `chip.br.disabled` | chip/br/disabled | `{color.border.tertiary}` | `#16130F` | `#16130F` |
| `chip.selected.bg.default` | chip/selected/bg/default | `{color.fill.primary.subtle}` | `#CFA74A` | `#CFA74A` |
| `chip.selected.bg.hover` | chip/selected/bg/hover | `{color.fill.primary.default}` | `#CFA74A` | `#CFA74A` |
| `chip.selected.bg.active` | chip/selected/bg/active | `{color.fill.primary.active}` | `#CFA74A` | `#CFA74A` |
| `chip.selected.bg.disabled` | chip/selected/bg/disabled | `{color.fill.secondary.disabled}` | `#16130F` | `#16130F` |
| `chip.selected.color.default` | chip/selected/color/default | `{color.text.accent}` | `#CFA74A` | `#CFA74A` |
| `chip.selected.color.hover` | chip/selected/color/hover | `{color.text.onPrimary}` | `#000000` | `#000000` |
| `chip.selected.color.active` | chip/selected/color/active | `{color.text.onPrimary}` | `#000000` | `#000000` |
| `chip.selected.color.disabled` | chip/selected/color/disabled | `{color.text.quaternary}` | `#16130F` | `#16130F` |
| `chip.selected.br.default` | chip/selected/br/default | `{color.border.accent}` | `#CFA74A` | `#CFA74A` |
| `chip.selected.br.hover` | chip/selected/br/hover | `{color.border.accent}` | `#CFA74A` | `#CFA74A` |
| `chip.selected.br.active` | chip/selected/br/active | `{color.border.accent}` | `#CFA74A` | `#CFA74A` |
| `chip.selected.br.disabled` | chip/selected/br/disabled | `{color.border.tertiary}` | `#16130F` | `#16130F` |

## Розміри та форма

| Токен | Figma variable | Тип | → Alias | Значення |
|---|---|---|---|---|
| `chip.size.sm` | chip/size/sm | sizing | `{size.control.sm}` | `32` |
| `chip.size.md` | chip/size/md | sizing | `{size.control.md}` | `40` |
| `chip.paddingH.sm` | chip/paddingH/sm | spacing | `{space.padding.sm}` | `12` |
| `chip.paddingH.md` | chip/paddingH/md | spacing | `{space.padding.md}` | `16` |
| `chip.gap` | chip/gap | spacing | `{space.gap.md}` | `8` |
| `chip.iconSize` | chip/iconSize | sizing | `{iconSize.sm}` | `16` |
| `chip.borderRadius` | chip/borderRadius | borderRadius | `{borderRadius.control}` | `8` |
| `chip.borderWidth` | chip/borderWidth | borderWidth | `{borderWidth.control}` | `1` |

## Текст (text styles, не токени)

| Розмір | Стиль |
|---|---|
| `sm` | label/sm |
| `md` | label/md |

## Нотатки

- Фільтр категорій (Slots / Live / Jackpots). Selected Hover/Active — суцільний primary з `text.onPrimary`.
- Товщина контуру береться з `borderWidth.control` — у Fiesta 2, в інших 1.
- Властивості: ✏️ Label · Icon (boolean) · 💠 Icon (swap, за замовчуванням `game-casino`).
