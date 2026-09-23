# Nav Item

> Згенеровано `tools/build-skill.py` з Token Studio JSON · 2026-09-23. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Nav Item (component set) · Selected  
**Варіанти:** Selected: False / True  
**Анатомія:** Вертикальний auto-layout → `Pill` (фон при Selected) з `Icon` · `Dot` (absolute) · `Label`.

Токенів: **10**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `navItem.color.default` | navItem/color/default | `{color.text.tertiary}` | `#16130F` | `#16130F` |
| `navItem.color.selected` | navItem/color/selected | `{color.text.accent}` | `#CFA74A` | `#CFA74A` |
| `navItem.bg.selected` | navItem/bg/selected | `{color.fill.primary.subtle}` | `#CFA74A` | `#CFA74A` |
| `navItem.dot.bg` | navItem/dot/bg | `{color.fill.danger.default}` | `#D23B34` | `#D23B34` |

## Розміри та форма

| Токен | Figma variable | Тип | → Alias | Значення |
|---|---|---|---|---|
| `navItem.iconSize` | navItem/iconSize | sizing | `{iconSize.lg}` | `24` |
| `navItem.gap` | navItem/gap | spacing | `{space.gap.xs}` | `4` |
| `navItem.paddingV` | navItem/paddingV | spacing | `{space.gap.md}` | `8` |
| `navItem.paddingH` | navItem/paddingH | spacing | `{space.padding.md}` | `16` |
| `navItem.indicator.borderRadius` | navItem/indicator/borderRadius | borderRadius | `{borderRadius.control}` | `8` |
| `navItem.dot.size` | navItem/dot/size | sizing | `{iconSize.xs}` | `12` |

## Текст (text styles, не токени)

| Розмір | Стиль |
|---|---|
| `label` | caption/sm |

## Нотатки

- Складова Bottom Nav. ✏️ Label · 💠 Icon (swap) · Dot (boolean).
