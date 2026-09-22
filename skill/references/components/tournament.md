# Tournament Card

> Згенеровано `tools/build-skill.py` з Token Studio JSON · 2026-09-22. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Tournament Card (component set) · State  
**Варіанти:** State: Live (CTA Join now) / Upcoming (Remind me) / Finished (View results)  
**Анатомія:** Картка (V, clip) → `Cover` (`Art` + статус-`Badge`) · `Body` (Title · Prize pool · Meta: Players/Time · Progress · CTA).

Токенів: **15**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `tournament.bg` | tournament/bg | `{color.bg.secondary}` | `#16130F` | `#16130F` |
| `tournament.br` | tournament/br | `{color.border.tertiary}` | `#16130F` | `#16130F` |
| `tournament.title.color` | tournament/title/color | `{color.text.primary}` | `#16130F` | `#16130F` |
| `tournament.prize.label.color` | tournament/prize/label/color | `{color.text.tertiary}` | `#16130F` | `#16130F` |
| `tournament.prize.color` | tournament/prize/color | `{color.text.accent}` | `#CFA74A` | `#CFA74A` |
| `tournament.meta.color` | tournament/meta/color | `{color.text.secondary}` | `#16130F` | `#16130F` |
| `tournament.meta.iconColor` | tournament/meta/iconColor | `{color.text.tertiary}` | `#16130F` | `#16130F` |

## Розміри та форма

| Токен | Figma variable | Тип | → Alias | Значення |
|---|---|---|---|---|
| `tournament.borderRadius` | tournament/borderRadius | borderRadius | `{borderRadius.surface}` | `12` |
| `tournament.borderWidth` | tournament/borderWidth | borderWidth | `{borderWidth.control}` | `1` |
| `tournament.padding` | tournament/padding | spacing | `{space.padding.md}` | `16` |
| `tournament.gap` | tournament/gap | spacing | `{space.gap.xl}` | `12` |
| `tournament.info.gap` | tournament/info/gap | spacing | `{space.gap.md}` | `8` |
| `tournament.meta.gap` | tournament/meta/gap | spacing | `{space.gap.sm}` | `6` |
| `tournament.iconSize` | tournament/iconSize | sizing | `{iconSize.md}` | `20` |
| `tournament.cover.padding` | tournament/cover/padding | spacing | `{space.gap.lg}` | `10` |

## Текст (text styles, не токени)

| Розмір | Стиль |
|---|---|
| `title` | title/t4 |
| `prize` | title/t2 |
| `meta` | body/sm/regular |

## Нотатки

- Призовий фонд — `tournament.prize.color` (accent). ✏️ Title · ✏️ Prize · Progress (boolean) · 💠 Art.
