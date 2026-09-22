# Tab

> Згенеровано `tools/build-skill.py` з Token Studio JSON · 2026-09-22. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Tab (component set) · Selected × State × Size  
**Варіанти:** Selected: False / True · State: Default / Hover / Active / Disabled · Size: sm (40) / md (48)  
**Анатомія:** Контейнер (auto-layout H) → `Icon` · `Label` · `Indicator` (absolute, знизу, вмикається при Selected).

Токенів: **16**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `tab.color.default` | tab/color/default | `{color.text.secondary}` | `#16130F` | `#16130F` |
| `tab.color.hover` | tab/color/hover | `{color.text.primary}` | `#16130F` | `#16130F` |
| `tab.color.active` | tab/color/active | `{color.text.primary}` | `#16130F` | `#16130F` |
| `tab.color.disabled` | tab/color/disabled | `{color.text.quaternary}` | `#16130F` | `#16130F` |
| `tab.selected.color` | tab/selected/color | `{color.text.primary}` | `#16130F` | `#16130F` |
| `tab.indicator.bg` | tab/indicator/bg | `{color.fill.primary.default}` | `#CFA74A` | `#CFA74A` |
| `tab.track.br` | tab/track/br | `{color.border.tertiary}` | `#16130F` | `#16130F` |

## Розміри та форма

| Токен | Figma variable | Тип | → Alias | Значення |
|---|---|---|---|---|
| `tab.indicator.size` | tab/indicator/size | spacing | `{space.gap.xs}` | `4` |
| `tab.indicator.borderRadius` | tab/indicator/borderRadius | borderRadius | `{borderRadius.control}` | `8` |
| `tab.track.borderWidth` | tab/track/borderWidth | borderWidth | `{borderWidth.control}` | `1` |
| `tab.size.sm` | tab/size/sm | sizing | `{size.control.md}` | `40` |
| `tab.size.md` | tab/size/md | sizing | `{size.control.lg}` | `48` |
| `tab.paddingH.sm` | tab/paddingH/sm | spacing | `{space.padding.md}` | `16` |
| `tab.paddingH.md` | tab/paddingH/md | spacing | `{space.padding.lg}` | `20` |
| `tab.gap` | tab/gap | spacing | `{space.gap.md}` | `8` |
| `tab.iconSize` | tab/iconSize | sizing | `{iconSize.md}` | `20` |

## Текст (text styles, не токени)

| Розмір | Стиль |
|---|---|
| `sm` | label/sm |
| `md` | label/md |

## Нотатки

- Ряд вкладок збирається вручну в auto-layout; нижня лінія-трек — `tab.track.br` / `tab.track.borderWidth`.
- Форма індикатора від бренду: pill (Fiesta), м'який (Aurum), гострий (Nova).
