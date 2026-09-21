# Progress

> Згенеровано `tools/build-skill.py` з Token Studio JSON · 2026-09-21. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Progress (component set) · Size × Tone × Value  
**Варіанти:** Size: sm (6) / md (8) · Tone: Primary / Success / Accent · Value: 0 / 25 / 50 / 75 / 100  
**Анатомія:** Вертикальний auto-layout → `Header` (Label + Value, boolean) · `Track` (frame) → `Fill` (масштабується разом із треком).

Токенів: **10**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `progress.track.bg` | progress/track/bg | `{color.fill.secondary.default}` | `#16130F` | `#16130F` |
| `progress.fill.primary.bg` | progress/fill/primary/bg | `{color.fill.primary.default}` | `#CFA74A` | `#CFA74A` |
| `progress.fill.success.bg` | progress/fill/success/bg | `{color.fill.success.default}` | `#1F9D5B` | `#1F9D5B` |
| `progress.fill.accent.bg` | progress/fill/accent/bg | `{color.fill.accent.default}` | `#8E2C43` | `#8E2C43` |
| `progress.label.color` | progress/label/color | `{color.text.secondary}` | `#16130F` | `#16130F` |
| `progress.percent.color` | progress/percent/color | `{color.text.primary}` | `#16130F` | `#16130F` |

## Розміри та форма

| Токен | Figma variable | Тип | → Alias | Значення |
|---|---|---|---|---|
| `progress.height.sm` | progress/height/sm | spacing | `{space.gap.sm}` | `6` |
| `progress.height.md` | progress/height/md | spacing | `{space.gap.md}` | `8` |
| `progress.borderRadius` | progress/borderRadius | borderRadius | `{borderRadius.control}` | `8` |
| `progress.gap` | progress/gap | spacing | `{space.gap.md}` | `8` |

## Текст (text styles, не токени)

| Розмір | Стиль |
|---|---|
| `label` | caption/md |
| `value` | label/sm |

## Нотатки

- XP-рівень (Primary), wagering (Success), призовий фонд турніру (Accent).
- Проміжні значення — змінити ширину `Fill` в інстансі.
