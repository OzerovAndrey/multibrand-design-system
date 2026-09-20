# Stat Tile

> Згенеровано `scripts/build-token-docs.py` з Token Studio JSON · 2026-09-20. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Stat Tile (component set) · Size × Trend  
**Варіанти:** Size: xs (160) / md (260) · Trend: Neutral / Up / Down (колір delta)  
**Анатомія:** Картка (auto-layout V) → `Header` (`Icon box` + Label) · `Value` · `Delta`.

Токенів: **19**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `stat.bg` | stat/bg | `{color.bg.secondary}` | `#16130F` | `#16130F` |
| `stat.br` | stat/br | `{color.border.tertiary}` | `#16130F` | `#16130F` |
| `stat.label.color` | stat/label/color | `{color.text.secondary}` | `#16130F` | `#16130F` |
| `stat.value.color` | stat/value/color | `{color.text.primary}` | `#16130F` | `#16130F` |
| `stat.icon.bg` | stat/icon/bg | `{color.fill.primary.subtle}` | `#CFA74A` | `#CFA74A` |
| `stat.icon.color` | stat/icon/color | `{color.text.accent}` | `#CFA74A` | `#CFA74A` |
| `stat.delta.color` | stat/delta/color | `{color.text.tertiary}` | `#16130F` | `#16130F` |
| `stat.delta.up.color` | stat/delta/up/color | `{color.text.success}` | `#1F9D5B` | `#1F9D5B` |
| `stat.delta.down.color` | stat/delta/down/color | `{color.text.danger}` | `#D23B34` | `#D23B34` |

## Розміри та форма

| Токен | Figma variable | Тип | → Alias | Значення |
|---|---|---|---|---|
| `stat.borderRadius` | stat/borderRadius | borderRadius | `{borderRadius.surface}` | `12` |
| `stat.borderWidth` | stat/borderWidth | borderWidth | `{borderWidth.control}` | `1` |
| `stat.paddingH.xs` | stat/paddingH/xs | spacing | `{space.padding.md}` | `16` |
| `stat.paddingH.md` | stat/paddingH/md | spacing | `{space.padding.xl}` | `24` |
| `stat.paddingV.xs` | stat/paddingV/xs | spacing | `{space.padding.md}` | `16` |
| `stat.paddingV.md` | stat/paddingV/md | spacing | `{space.padding.xl}` | `24` |
| `stat.gap.xs` | stat/gap/xs | spacing | `{space.gap.md}` | `8` |
| `stat.gap.md` | stat/gap/md | spacing | `{space.gap.lg}` | `10` |
| `stat.icon.size` | stat/icon/size | sizing | `{size.control.md}` | `40` |
| `stat.icon.iconSize` | stat/icon/iconSize | sizing | `{iconSize.lg}` | `24` |

## Текст (text styles, не токени)

| Розмір | Стиль |
|---|---|
| `label` | label/sm |
| `value xs` | title/t4 |
| `value md` | title/t3 |
| `delta` | label/sm |

## Нотатки

- Властивості: ✏️ Label · ✏️ Value · Delta (boolean) · Icon (boolean) · 💠 Icon (swap, `wallet`). Текст delta — у кожного Trend свій.
