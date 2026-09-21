# Leaderboard Row

> Згенеровано `tools/build-skill.py` з Token Studio JSON · 2026-09-21. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Leaderboard Row (component set) · Rank × You  
**Варіанти:** Rank: 1 / 2 / 3 / Other · You: False / True (підсвітка поточного гравця)  
**Анатомія:** Рядок (auto-layout H) → `Rank` (число) · `Avatar` (instance) · `Player` (Name + Sub) · `Result` (Score + Prize).

Токенів: **23**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `leaderRow.bg.default` | leaderRow/bg/default | `{color.bg.secondary}` | `#16130F` | `#16130F` |
| `leaderRow.bg.highlight` | leaderRow/bg/highlight | `{color.fill.primary.subtle}` | `#CFA74A` | `#CFA74A` |
| `leaderRow.br.default` | leaderRow/br/default | `{color.border.tertiary}` | `#16130F` | `#16130F` |
| `leaderRow.br.highlight` | leaderRow/br/highlight | `{color.border.accent}` | `#CFA74A` | `#CFA74A` |
| `leaderRow.rank.bg.first` | leaderRow/rank/bg/first | `{color.fill.primary.default}` | `#CFA74A` | `#CFA74A` |
| `leaderRow.rank.bg.second` | leaderRow/rank/bg/second | `{color.fill.secondary.active}` | `#16130F` | `#16130F` |
| `leaderRow.rank.bg.third` | leaderRow/rank/bg/third | `{color.fill.accent.default}` | `#8E2C43` | `#8E2C43` |
| `leaderRow.rank.bg.default` | leaderRow/rank/bg/default | `{color.fill.secondary.default}` | `#16130F` | `#16130F` |
| `leaderRow.rank.color.first` | leaderRow/rank/color/first | `{color.text.onPrimary}` | `#000000` | `#000000` |
| `leaderRow.rank.color.second` | leaderRow/rank/color/second | `{color.text.primary}` | `#16130F` | `#16130F` |
| `leaderRow.rank.color.third` | leaderRow/rank/color/third | `{color.text.onAccent}` | `#FFFFFF` | `#FFFFFF` |
| `leaderRow.rank.color.default` | leaderRow/rank/color/default | `{color.text.secondary}` | `#16130F` | `#16130F` |
| `leaderRow.name.color` | leaderRow/name/color | `{color.text.primary}` | `#16130F` | `#16130F` |
| `leaderRow.sub.color` | leaderRow/sub/color | `{color.text.tertiary}` | `#16130F` | `#16130F` |
| `leaderRow.score.color` | leaderRow/score/color | `{color.text.primary}` | `#16130F` | `#16130F` |
| `leaderRow.prize.color` | leaderRow/prize/color | `{color.text.accent}` | `#CFA74A` | `#CFA74A` |

## Розміри та форма

| Токен | Figma variable | Тип | → Alias | Значення |
|---|---|---|---|---|
| `leaderRow.borderRadius` | leaderRow/borderRadius | borderRadius | `{borderRadius.surface}` | `12` |
| `leaderRow.borderWidth` | leaderRow/borderWidth | borderWidth | `{borderWidth.control}` | `1` |
| `leaderRow.paddingH` | leaderRow/paddingH | spacing | `{space.padding.md}` | `16` |
| `leaderRow.paddingV` | leaderRow/paddingV | spacing | `{space.padding.sm}` | `12` |
| `leaderRow.gap` | leaderRow/gap | spacing | `{space.gap.xl}` | `12` |
| `leaderRow.rank.size` | leaderRow/rank/size | sizing | `{size.control.sm}` | `32` |
| `leaderRow.rank.borderRadius` | leaderRow/rank/borderRadius | borderRadius | `{borderRadius.control}` | `8` |

## Текст (text styles, не токени)

| Розмір | Стиль |
|---|---|
| `rank` | label/sm |
| `name` | label/md |
| `sub` | caption/md |
| `score` | label/md |
| `prize` | label/sm |

## Нотатки

- Ранг 1–3 — акцентні кольори (product1 / neutral / product2), далі нейтральний. ✏️ Name · Sub · Score · Prize; Prize (boolean).
