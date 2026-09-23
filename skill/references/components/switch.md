# Switch

> Згенеровано `tools/build-skill.py` з Token Studio JSON · 2026-09-23. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Switch (component set) · On × State  
**Варіанти:** On: False / True · State: Default / Hover / Disabled  
**Анатомія:** Контейнер (auto-layout H) → `Track` (auto-layout, knob вирівнюється вліво/вправо) → `Knob` · `Label` (text).

Токенів: **15**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `switch.knob.bg` | switch/knob/bg | `{color.bg.primary}` | `#16130F` | `#16130F` |
| `switch.off.bg.default` | switch/off/bg/default | `{color.border.primary}` | `#16130F` | `#16130F` |
| `switch.off.bg.hover` | switch/off/bg/hover | `{color.text.tertiary}` | `#16130F` | `#16130F` |
| `switch.off.bg.disabled` | switch/off/bg/disabled | `{color.fill.secondary.disabled}` | `#16130F` | `#16130F` |
| `switch.on.bg.default` | switch/on/bg/default | `{color.fill.primary.default}` | `#CFA74A` | `#CFA74A` |
| `switch.on.bg.hover` | switch/on/bg/hover | `{color.fill.primary.hover}` | `#CFA74A` | `#CFA74A` |
| `switch.on.bg.disabled` | switch/on/bg/disabled | `{color.fill.primary.disabled}` | `#16130F` | `#16130F` |
| `switch.label.color.default` | switch/label/color/default | `{color.text.primary}` | `#16130F` | `#16130F` |
| `switch.label.color.disabled` | switch/label/color/disabled | `{color.text.quaternary}` | `#16130F` | `#16130F` |

## Розміри та форма

| Токен | Figma variable | Тип | → Alias | Значення |
|---|---|---|---|---|
| `switch.width` | switch/width | sizing | `{size.control.lg}` | `48` |
| `switch.height` | switch/height | sizing | `{size.control.xs}` | `24` |
| `switch.knob.size` | switch/knob/size | sizing | `{iconSize.sm}` | `16` |
| `switch.padding` | switch/padding | spacing | `{space.gap.xs}` | `4` |
| `switch.borderRadius` | switch/borderRadius | borderRadius | `{borderRadius.control}` | `8` |
| `switch.gap` | switch/gap | spacing | `{space.gap.lg}` | `10` |

## Текст (text styles, не токени)

| Розмір | Стиль |
|---|---|
| `label` | body/md/regular |

## Нотатки

- Track і knob беруть `borderRadius.control` — у Nova перемикач прямокутний, у Fiesta капсула.
- Властивості: ✏️ Label · Show label (boolean).
