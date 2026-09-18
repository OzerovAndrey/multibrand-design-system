# Brand — Aurum / Nova / Fiesta

> Згенеровано `scripts/build-token-docs.py` з Token Studio JSON · 2026-09-18. Не редагувати вручну — правити JSON і перегенерувати.

Бренд = набір значень. Ключі в усіх трьох файлах **ідентичні**, різняться лише значення.
Figma: колекція **Brand** (modes Aurum / Nova / Fiesta). Разом із брендом у цю колекцію потрапляє `map` (enabled у темах Brand).
Токенів у бренді: **35**.

Що живе в бренді:
- **Кольори** — одиничні базові (`product1–3`, `onProduct1/2`, `success`, `warning`, `danger`, `ink`). Без рамп: відтінки — у `map`.
- **Шрифти** — `fontFamily.display` (display/title), `fontFamily.base` (решта тексту).
- **Розмірна семантика** — `space.padding.*`, `space.gap.*`, `size.control.*`, `iconSize.*`, `borderRadius.control|surface`, `borderWidth.none|control`. Живе в бренді, а не в темі: бренд може мати інші радіуси/щільність, тема (light/dark) міняє тільки кольори.

## color

| Токен | Тип | Aurum | Nova | Fiesta |
|---|---|---|---|---|
| `color.product1` | color | `#CFA74A` | `#22D3EE` | `#FFC93C` |
| `color.product2` | color | `#8E2C43` | `#7C3AED` | `#FF4FA3` |
| `color.product3` | color | `#B8704B` | `#38BDF8` | `#38BDF8` |
| `color.onProduct1` | color | `{color.black}` → `#000000` | `{color.black}` → `#000000` | `{color.black}` → `#000000` |
| `color.onProduct2` | color | `{color.white}` → `#FFFFFF` | `{color.white}` → `#FFFFFF` | `{color.white}` → `#FFFFFF` |
| `color.success` | color | `#1F9D5B` | `#0EA45B` | `#0EA45B` |
| `color.warning` | color | `#E69A12` | `#F59E0B` | `#F59E0B` |
| `color.danger` | color | `#D23B34` | `#D83232` | `#D83232` |
| `color.ink` | color | `#16130F` | `#0B1020` | `#2A1657` |

## fontFamily

| Токен | Тип | Aurum | Nova | Fiesta |
|---|---|---|---|---|
| `fontFamily.display` | fontFamilies | `Cormorant Garamond` | `Space Grotesk` | `Nunito` |
| `fontFamily.base` | fontFamilies | `Cormorant Garamond` | `Space Grotesk` | `Nunito` |

## space.padding

| Токен | Тип | Aurum | Nova | Fiesta |
|---|---|---|---|---|
| `space.padding.xs` | spacing | `{dimension.12}` → `12` | `{dimension.12}` → `12` | `{dimension.12}` → `12` |
| `space.padding.sm` | spacing | `{dimension.12}` → `12` | `{dimension.12}` → `12` | `{dimension.12}` → `12` |
| `space.padding.md` | spacing | `{dimension.16}` → `16` | `{dimension.16}` → `16` | `{dimension.16}` → `16` |
| `space.padding.lg` | spacing | `{dimension.20}` → `20` | `{dimension.20}` → `20` | `{dimension.20}` → `20` |
| `space.padding.xl` | spacing | `{dimension.24}` → `24` | `{dimension.24}` → `24` | `{dimension.24}` → `24` |

## space.gap

| Токен | Тип | Aurum | Nova | Fiesta |
|---|---|---|---|---|
| `space.gap.xs` | spacing | `{dimension.4}` → `4` | `{dimension.4}` → `4` | `{dimension.4}` → `4` |
| `space.gap.sm` | spacing | `{dimension.6}` → `6` | `{dimension.6}` → `6` | `{dimension.6}` → `6` |
| `space.gap.md` | spacing | `{dimension.8}` → `8` | `{dimension.8}` → `8` | `{dimension.8}` → `8` |
| `space.gap.lg` | spacing | `{dimension.10}` → `10` | `{dimension.10}` → `10` | `{dimension.10}` → `10` |
| `space.gap.xl` | spacing | `{dimension.12}` → `12` | `{dimension.12}` → `12` | `{dimension.12}` → `12` |

## borderRadius

| Токен | Тип | Aurum | Nova | Fiesta |
|---|---|---|---|---|
| `borderRadius.control` | borderRadius | `{borderRadius.999}` → `999` | `{borderRadius.999}` → `999` | `{borderRadius.999}` → `999` |
| `borderRadius.surface` | borderRadius | `{borderRadius.8}` → `8` | `{borderRadius.8}` → `8` | `{borderRadius.8}` → `8` |

## borderWidth

| Токен | Тип | Aurum | Nova | Fiesta |
|---|---|---|---|---|
| `borderWidth.none` | borderWidth | `{borderWidth.0}` → `0` | `{borderWidth.0}` → `0` | `{borderWidth.0}` → `0` |
| `borderWidth.control` | borderWidth | `{borderWidth.1}` → `1` | `{borderWidth.1}` → `1` | `{borderWidth.1}` → `1` |

## size

| Токен | Тип | Aurum | Nova | Fiesta |
|---|---|---|---|---|
| `size.control.xs` | sizing | `{dimension.24}` → `24` | `{dimension.24}` → `24` | `{dimension.24}` → `24` |
| `size.control.sm` | sizing | `{dimension.32}` → `32` | `{dimension.32}` → `32` | `{dimension.32}` → `32` |
| `size.control.md` | sizing | `{dimension.40}` → `40` | `{dimension.40}` → `40` | `{dimension.40}` → `40` |
| `size.control.lg` | sizing | `{dimension.48}` → `48` | `{dimension.48}` → `48` | `{dimension.48}` → `48` |
| `size.control.xl` | sizing | `{dimension.56}` → `56` | `{dimension.56}` → `56` | `{dimension.56}` → `56` |

## iconSize

| Токен | Тип | Aurum | Nova | Fiesta |
|---|---|---|---|---|
| `iconSize.xs` | sizing | `{dimension.12}` → `12` | `{dimension.12}` → `12` | `{dimension.12}` → `12` |
| `iconSize.sm` | sizing | `{dimension.16}` → `16` | `{dimension.16}` → `16` | `{dimension.16}` → `16` |
| `iconSize.md` | sizing | `{dimension.20}` → `20` | `{dimension.20}` → `20` | `{dimension.20}` → `20` |
| `iconSize.lg` | sizing | `{dimension.24}` → `24` | `{dimension.24}` → `24` | `{dimension.24}` → `24` |
| `iconSize.xl` | sizing | `{dimension.32}` → `32` | `{dimension.32}` → `32` | `{dimension.32}` → `32` |
