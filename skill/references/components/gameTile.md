# Game Tile

> Згенеровано `tools/build-skill.py` з Token Studio JSON · 2026-09-23. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Game Tile (component set) · Type × State  
**Варіанти:** Type: Slot (3:4, 176×235) / Live (16:9, 320×180) · State: Default / Hover (overlay + Play)  
**Анатомія:** Вертикальний auto-layout → `Cover` (clip; `Art` · `Hover overlay` · `Play` · `Top row`: Badge + Favorite · для Live `Bottom row`: Players) · `Info` (Title + Provider).

Токенів: **14**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `gameTile.title.color` | gameTile/title/color | `{color.text.primary}` | `#16130F` | `#16130F` |
| `gameTile.provider.color` | gameTile/provider/color | `{color.text.tertiary}` | `#16130F` | `#16130F` |
| `gameTile.meta.color` | gameTile/meta/color | `{color.text.secondary}` | `#16130F` | `#16130F` |
| `gameTile.overlay.bg` | gameTile/overlay/bg | `{color.bg.overlay}` | `rgba(0, 0, 0, 0.6)` | `rgba(0, 0, 0, 0.6)` |
| `gameTile.action.bg` | gameTile/action/bg | `{color.bg.overlay}` | `rgba(0, 0, 0, 0.6)` | `rgba(0, 0, 0, 0.6)` |
| `gameTile.action.color` | gameTile/action/color | `{color.text.onOverlay}` | `#FFFFFF` | `#FFFFFF` |
| `gameTile.action.selected.color` | gameTile/action/selected/color | `{color.fill.danger.default}` | `#D23B34` | `#D23B34` |

## Розміри та форма

| Токен | Figma variable | Тип | → Alias | Значення |
|---|---|---|---|---|
| `gameTile.borderRadius` | gameTile/borderRadius | borderRadius | `{borderRadius.surface}` | `12` |
| `gameTile.gap` | gameTile/gap | spacing | `{space.gap.md}` | `8` |
| `gameTile.info.gap` | gameTile/info/gap | spacing | `{space.gap.xs}` | `4` |
| `gameTile.overlay.padding` | gameTile/overlay/padding | spacing | `{space.gap.lg}` | `10` |
| `gameTile.action.size` | gameTile/action/size | sizing | `{size.control.sm}` | `32` |
| `gameTile.action.iconSize` | gameTile/action/iconSize | sizing | `{iconSize.md}` | `20` |
| `gameTile.actions.gap` | gameTile/actions/gap | spacing | `{space.gap.md}` | `8` |

## Текст (text styles, не токени)

| Розмір | Стиль |
|---|---|
| `title` | label/md |
| `provider` | caption/md |
| `players` | label/sm |

## Нотатки

- ✏️ Title · ✏️ Provider · Favorite · Badge (boolean, swap тону: NEW / HOT / LIVE) · 💠 Art (swap патерна або фото). Форма Play — від `borderRadius.surface` бренду.
