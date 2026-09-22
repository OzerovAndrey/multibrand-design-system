# Avatar

> Згенеровано `tools/build-skill.py` з Token Studio JSON · 2026-09-22. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Avatar (component set) · Size × Type  
**Варіанти:** Size: xs–xl (24–56) · Type: Initials / Icon. Booleans: VIP, Status  
**Анатомія:** Контейнер (фіксований квадрат `avatar.size.{size}`) → `Initials` (text) або `Icon` · `VIP ring` (absolute) · `Status` (absolute, нижній правий кут).

Токенів: **22**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `avatar.bg` | avatar/bg | `{color.fill.secondary.default}` | `#16130F` | `#16130F` |
| `avatar.color` | avatar/color | `{color.text.secondary}` | `#16130F` | `#16130F` |
| `avatar.br` | avatar/br | `{color.border.secondary}` | `#16130F` | `#16130F` |
| `avatar.vip.br` | avatar/vip/br | `{color.border.accent}` | `#CFA74A` | `#CFA74A` |
| `avatar.status.bg` | avatar/status/bg | `{color.fill.success.default}` | `#1F9D5B` | `#1F9D5B` |
| `avatar.status.br` | avatar/status/br | `{color.bg.primary}` | `#16130F` | `#16130F` |
| `avatar.brand.bg.default` | avatar/brand/bg/default | `{color.fill.primary.default}` | `#CFA74A` | `#CFA74A` |
| `avatar.brand.bg.hover` | avatar/brand/bg/hover | `{color.fill.primary.hover}` | `#CFA74A` | `#CFA74A` |
| `avatar.brand.color` | avatar/brand/color | `{color.text.onPrimary}` | `#000000` | `#000000` |

## Розміри та форма

| Токен | Figma variable | Тип | → Alias | Значення |
|---|---|---|---|---|
| `avatar.size.xs` | avatar/size/xs | sizing | `{size.control.xs}` | `24` |
| `avatar.size.sm` | avatar/size/sm | sizing | `{size.control.sm}` | `32` |
| `avatar.size.md` | avatar/size/md | sizing | `{size.control.md}` | `40` |
| `avatar.size.lg` | avatar/size/lg | sizing | `{size.control.lg}` | `48` |
| `avatar.size.xl` | avatar/size/xl | sizing | `{size.control.xl}` | `56` |
| `avatar.borderRadius` | avatar/borderRadius | borderRadius | `{borderRadius.control}` | `8` |
| `avatar.borderWidth` | avatar/borderWidth | borderWidth | `{borderWidth.control}` | `1` |
| `avatar.status.size` | avatar/status/size | sizing | `{iconSize.xs}` | `12` |
| `avatar.iconSize.xs` | avatar/iconSize/xs | sizing | `{iconSize.xs}` | `12` |
| `avatar.iconSize.sm` | avatar/iconSize/sm | sizing | `{iconSize.sm}` | `16` |
| `avatar.iconSize.md` | avatar/iconSize/md | sizing | `{iconSize.md}` | `20` |
| `avatar.iconSize.lg` | avatar/iconSize/lg | sizing | `{iconSize.lg}` | `24` |
| `avatar.iconSize.xl` | avatar/iconSize/xl | sizing | `{iconSize.xl}` | `32` |

## Текст (text styles, не токени)

| Розмір | Стиль |
|---|---|
| `xs` | label/xs |
| `sm` | label/sm |
| `md` | label/md |
| `lg` | label/lg |
| `xl` | label/xl |

## Нотатки

- Форма від `borderRadius.control`: Aurum — м'який квадрат, Nova — гострий, Fiesta — коло.
- Фото — заливка Image поверх контейнера; ✏️ Initials і 💠 Icon — властивості інстансу.
