# Promo Banner

> Згенеровано `tools/build-skill.py` з Token Studio JSON · 2026-09-20. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Promo Banner (component set) · Size  
**Варіанти:** Size: xs (mobile 328×420, контент знизу) / md (desktop 1000×360, панель зліва)  
**Анатомія:** Контейнер (clip) → `Art` (absolute, фон) · `Content` (панель `promo.overlay.bg`: Eyebrow Badge · Title · Text · Actions: Primary + Secondary).

Токенів: **11**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `promo.overlay.bg` | promo/overlay/bg | `{color.bg.overlay}` | `rgba(0, 0, 0, 0.6)` | `rgba(0, 0, 0, 0.6)` |
| `promo.title.color` | promo/title/color | `{color.text.onOverlay}` | `#FFFFFF` | `#FFFFFF` |
| `promo.text.color` | promo/text/color | `{color.text.onOverlay}` | `#FFFFFF` | `#FFFFFF` |

## Розміри та форма

| Токен | Figma variable | Тип | → Alias | Значення |
|---|---|---|---|---|
| `promo.borderRadius` | promo/borderRadius | borderRadius | `{borderRadius.surface}` | `12` |
| `promo.paddingH.xs` | promo/paddingH/xs | spacing | `{space.padding.lg}` | `20` |
| `promo.paddingH.md` | promo/paddingH/md | spacing | `{space.padding.xl}` | `24` |
| `promo.paddingV.xs` | promo/paddingV/xs | spacing | `{space.padding.lg}` | `20` |
| `promo.paddingV.md` | promo/paddingV/md | spacing | `{space.padding.xl}` | `24` |
| `promo.gap.xs` | promo/gap/xs | spacing | `{space.gap.lg}` | `10` |
| `promo.gap.md` | promo/gap/md | spacing | `{space.gap.xl}` | `12` |
| `promo.actions.gap` | promo/actions/gap | spacing | `{space.gap.md}` | `8` |

## Текст (text styles, не токени)

| Розмір | Стиль |
|---|---|
| `title xs` | title/t2 |
| `title md` | display/d3 |
| `text xs` | body/md/regular |
| `text md` | body/lg/regular |

## Нотатки

- Hero лобі. ✏️ Title · ✏️ Text · Eyebrow, Secondary action (boolean) · 💠 Art.
