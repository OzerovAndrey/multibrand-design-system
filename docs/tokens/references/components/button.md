# Button

> Згенеровано `scripts/build-token-docs.py` з Token Studio JSON · 2026-09-19. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Button (component set) · Variant × Size × State × Label  
**Варіанти:** Variant: Primary / Secondary / Text · Size: xs–xl · State: Default / Hover / Active / Disabled  
**Анатомія:** Контейнер (auto-layout H) → `Icon left` (instance) · `Label` (text) · `Icon right` (instance). Icon-only варіант = `Label=False`.

Токенів: **48**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `button.primary.bg.default` | button/primary/bg/default | `{color.fill.primary.default}` | `#CFA74A` | `#CFA74A` |
| `button.primary.bg.hover` | button/primary/bg/hover | `{color.fill.primary.hover}` | `#CFA74A` | `#CFA74A` |
| `button.primary.bg.active` | button/primary/bg/active | `{color.fill.primary.active}` | `#CFA74A` | `#CFA74A` |
| `button.primary.bg.disabled` | button/primary/bg/disabled | `{color.fill.primary.disabled}` | `#16130F` | `#16130F` |
| `button.primary.color.default` | button/primary/color/default | `{color.text.onPrimary}` | `#000000` | `#000000` |
| `button.primary.color.hover` | button/primary/color/hover | `{color.text.onPrimary}` | `#000000` | `#000000` |
| `button.primary.color.active` | button/primary/color/active | `{color.text.onPrimary}` | `#000000` | `#000000` |
| `button.primary.color.disabled` | button/primary/color/disabled | `{color.text.tertiary}` | `#16130F` | `#16130F` |
| `button.secondary.bg.default` | button/secondary/bg/default | `{color.fill.secondary.default}` | `#16130F` | `#16130F` |
| `button.secondary.bg.hover` | button/secondary/bg/hover | `{color.fill.secondary.hover}` | `#16130F` | `#16130F` |
| `button.secondary.bg.active` | button/secondary/bg/active | `{color.fill.secondary.active}` | `#16130F` | `#16130F` |
| `button.secondary.bg.disabled` | button/secondary/bg/disabled | `{color.fill.secondary.disabled}` | `#16130F` | `#16130F` |
| `button.secondary.color.default` | button/secondary/color/default | `{color.text.primary}` | `#16130F` | `#16130F` |
| `button.secondary.color.hover` | button/secondary/color/hover | `{color.text.primary}` | `#16130F` | `#16130F` |
| `button.secondary.color.active` | button/secondary/color/active | `{color.text.primary}` | `#16130F` | `#16130F` |
| `button.secondary.color.disabled` | button/secondary/color/disabled | `{color.text.tertiary}` | `#16130F` | `#16130F` |
| `button.text.bg.default` | button/text/bg/default | `{color.fill.ghost.default}` | `rgba(0, 0, 0, 0)` | `rgba(0, 0, 0, 0)` |
| `button.text.bg.hover` | button/text/bg/hover | `{color.fill.ghost.hover}` | `#16130F` | `#16130F` |
| `button.text.bg.active` | button/text/bg/active | `{color.fill.ghost.active}` | `#16130F` | `#16130F` |
| `button.text.bg.disabled` | button/text/bg/disabled | `{color.fill.ghost.disabled}` | `rgba(0, 0, 0, 0)` | `rgba(0, 0, 0, 0)` |
| `button.text.color.default` | button/text/color/default | `{color.text.primary}` | `#16130F` | `#16130F` |
| `button.text.color.hover` | button/text/color/hover | `{color.text.primary}` | `#16130F` | `#16130F` |
| `button.text.color.active` | button/text/color/active | `{color.text.primary}` | `#16130F` | `#16130F` |
| `button.text.color.disabled` | button/text/color/disabled | `{color.text.tertiary}` | `#16130F` | `#16130F` |

## Розміри та форма

| Токен | Figma variable | Тип | → Alias | Значення |
|---|---|---|---|---|
| `button.size.xs` | button/size/xs | sizing | `{size.control.xs}` | `24` |
| `button.size.sm` | button/size/sm | sizing | `{size.control.sm}` | `32` |
| `button.size.md` | button/size/md | sizing | `{size.control.md}` | `40` |
| `button.size.lg` | button/size/lg | sizing | `{size.control.lg}` | `48` |
| `button.size.xl` | button/size/xl | sizing | `{size.control.xl}` | `56` |
| `button.paddingH.xs` | button/paddingH/xs | spacing | `{space.padding.xs}` | `12` |
| `button.paddingH.sm` | button/paddingH/sm | spacing | `{space.padding.sm}` | `12` |
| `button.paddingH.md` | button/paddingH/md | spacing | `{space.padding.md}` | `16` |
| `button.paddingH.lg` | button/paddingH/lg | spacing | `{space.padding.lg}` | `20` |
| `button.paddingH.xl` | button/paddingH/xl | spacing | `{space.padding.xl}` | `24` |
| `button.gap.xs` | button/gap/xs | spacing | `{space.gap.xs}` | `4` |
| `button.gap.sm` | button/gap/sm | spacing | `{space.gap.sm}` | `6` |
| `button.gap.md` | button/gap/md | spacing | `{space.gap.md}` | `8` |
| `button.gap.lg` | button/gap/lg | spacing | `{space.gap.lg}` | `10` |
| `button.gap.xl` | button/gap/xl | spacing | `{space.gap.xl}` | `12` |
| `button.iconSize.xs` | button/iconSize/xs | sizing | `{iconSize.xs}` | `12` |
| `button.iconSize.sm` | button/iconSize/sm | sizing | `{iconSize.sm}` | `16` |
| `button.iconSize.md` | button/iconSize/md | sizing | `{iconSize.md}` | `20` |
| `button.iconSize.lg` | button/iconSize/lg | sizing | `{iconSize.lg}` | `24` |
| `button.iconSize.xl` | button/iconSize/xl | sizing | `{iconSize.xl}` | `32` |
| `button.borderRadius` | button/borderRadius | borderRadius | `{borderRadius.control}` | `999` |
| `button.borderWidth.primary` | button/borderWidth/primary | borderWidth | `{borderWidth.none}` | `0` |
| `button.borderWidth.secondary` | button/borderWidth/secondary | borderWidth | `{borderWidth.none}` | `0` |
| `button.borderWidth.text` | button/borderWidth/text | borderWidth | `{borderWidth.control}` | `1` |

## Текст (text styles, не токени)

| Розмір | Стиль |
|---|---|
| `xs` | label/sm |
| `sm` | label/md |
| `md` | label/md |
| `lg` | label/lg |
| `xl` | label/xl |

## Нотатки

- Власних typography-токенів немає — текст бере text style зі шкали.
- Іконки за замовчуванням: left `plus`, right `chevron-right` (Static — Icons).
