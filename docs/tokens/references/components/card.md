# Card Default

> Згенеровано `scripts/build-token-docs.py` з Token Studio JSON · 2026-09-18. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Card Default (component set) · Size  
**Варіанти:** Size: xs (mobile) / sm (tablet) / md (desktop). Станів немає — статичний контейнер  
**Анатомія:** Контейнер (auto-layout V, padding `card.default.paddingH/V.{size}`, gap `card.default.gap.{size}`) → `Slot 1` · `Slot 2` · `Slot 3` (інстанси `_Card slot`).

Токенів: **13**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `card.default.bg` | card/default/bg | `{color.bg.secondary}` | `#16130F` | `#16130F` |
| `card.default.br` | card/default/br | `{color.border.tertiary}` | `#16130F` | `#16130F` |

## Розміри та форма

| Токен | Figma variable | Тип | → Alias | Значення |
|---|---|---|---|---|
| `card.default.borderWidth` | card/default/borderWidth | borderWidth | `{borderWidth.control}` | `1` |
| `card.default.borderRadius` | card/default/borderRadius | borderRadius | `{borderRadius.surface}` | `8` |
| `card.default.paddingH.xs` | card/default/paddingH/xs | spacing | `{space.padding.sm}` | `12` |
| `card.default.paddingH.sm` | card/default/paddingH/sm | spacing | `{space.padding.md}` | `16` |
| `card.default.paddingH.md` | card/default/paddingH/md | spacing | `{space.padding.xl}` | `24` |
| `card.default.paddingV.xs` | card/default/paddingV/xs | spacing | `{space.padding.sm}` | `12` |
| `card.default.paddingV.sm` | card/default/paddingV/sm | spacing | `{space.padding.md}` | `16` |
| `card.default.paddingV.md` | card/default/paddingV/md | spacing | `{space.padding.xl}` | `24` |
| `card.default.gap.xs` | card/default/gap/xs | spacing | `{space.gap.md}` | `8` |
| `card.default.gap.sm` | card/default/gap/sm | spacing | `{space.gap.lg}` | `10` |
| `card.default.gap.md` | card/default/gap/md | spacing | `{space.gap.xl}` | `12` |

## Нотатки

- Власного контенту немає — вміст підставляється через instance swap 💠 Slot 1–3; Slot 2 і Slot 3 вмикаються булеанами.
- Ширина в сеті — референс (320 / 400 / 480); у макеті картка тягнеться (Fill) по колонці сітки.
- Padding: xs 12 · sm 16 · md 24; gap: xs 8 · sm 10 · md 12 — з існуючої брендової шкали `space.*`.
