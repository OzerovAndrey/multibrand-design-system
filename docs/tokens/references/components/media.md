# Media

> Згенеровано `scripts/build-token-docs.py` з Token Studio JSON · 2026-09-19. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Media (component set) · Ratio × State  
**Варіанти:** Ratio: 1:1 / 4:3 / 16:9 / 3:4 · State: Loaded / Loading / Error  
**Анатомія:** Контейнер (fill `media.bg`, radius `media.borderRadius`, clip) → `image` (rectangle, image fill) · `overlay` (`media.overlay.bg`) · `icon` (fallback, `media.fallback.iconSize`) · `Content` (slot, padding `media.padding`, gap `media.gap`).

Токенів: **8**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `media.bg` | media/bg | `{color.fill.secondary.default}` | `#16130F` | `#16130F` |
| `media.overlay.bg` | media/overlay/bg | `{color.bg.overlay}` | `rgba(0, 0, 0, 0.6)` | `rgba(0, 0, 0, 0.6)` |
| `media.skeleton.bg` | media/skeleton/bg | `{color.fill.secondary.default}` | `#16130F` | `#16130F` |
| `media.fallback.iconColor` | media/fallback/iconColor | `{color.text.tertiary}` | `#16130F` | `#16130F` |

## Розміри та форма

| Токен | Figma variable | Тип | → Alias | Значення |
|---|---|---|---|---|
| `media.borderRadius` | media/borderRadius | borderRadius | `{borderRadius.surface}` | `8` |
| `media.padding` | media/padding | spacing | `{space.padding.xs}` | `12` |
| `media.gap` | media/gap | spacing | `{space.gap.md}` | `8` |
| `media.fallback.iconSize` | media/fallback/iconSize | sizing | `{iconSize.lg}` | `24` |

## Нотатки

- Медіа-примітив: зображення з брендовим радіусом і станами завантаження; основа для Thumb, PromoCard, банерів.
- Loading — фон `media.skeleton.bg`; Error — іконка `placeholder-default` кольору `media.fallback.iconColor`.
- Властивості: boolean Overlay · swap 💠 Fallback icon · slot Content (бейджі, кнопки).
- Ratio — фіксовані пропорції; у макеті Fill по ширині, висота за пропорцією. Картинка міняється заливкою шару image.
