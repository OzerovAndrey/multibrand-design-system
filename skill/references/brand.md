# Brand — Aurum / Nova / Fiesta / Ultra

> Згенеровано `tools/build-skill.py` з Token Studio JSON · 2026-09-23. Не редагувати вручну — правити JSON і перегенерувати.

Бренд = набір значень. Ключі в усіх файлах брендів **ідентичні**, різняться лише значення.
Figma: колекція **Brand** (modes Aurum / Nova / Fiesta / Ultra). Разом із брендом у цю колекцію потрапляє `map` (enabled у темах Brand).
Токенів у бренді: **55**.

Що живе в бренді:
- **Кольори** — одиничні базові (`product1–3`, `onProduct1/2`, `success`, `warning`, `danger`, `ink`). Без рамп: відтінки — у `map`.
- **Шрифти** — `fontFamily.display` (display/title), `fontFamily.base` (решта тексту).
- **Розмірна семантика** — `space.padding.*`, `space.gap.*`, `size.control.*`, `iconSize.*`, `borderRadius.control|surface`, `borderWidth.none|control`. Живе в бренді, а не в темі: бренд може мати інші радіуси/щільність, тема (light/dark) міняє тільки кольори.
- **Сітка сторінки** — `layout.columns.*` (кількість колонок), `layout.columnGap.*` (gutter), `layout.paddingH.*` (поля), `layout.rowGap.*` (відстань між секціями) по брейкпоінтах xs 360 · sm 768 · md 1024 · lg 1200 · xl 1440. У Figma прив'язані до Layout grid фреймів сторінок; організми (Footer) беруть поля й відступи звідси.

## color

| Токен | Тип | Aurum | Nova | Fiesta | Ultra |
|---|---|---|---|---|---|
| `color.product1` | color | `#CFA74A` | `#22D3EE` | `#FFC93C` | `#FF3D9E` |
| `color.product2` | color | `#8E2C43` | `#7C3AED` | `#FF4FA3` | `#17E1FF` |
| `color.product3` | color | `#B8704B` | `#38BDF8` | `#38BDF8` | `#7B4DFF` |
| `color.onProduct1` | color | `{color.black}` → `#000000` | `{color.black}` → `#000000` | `{color.black}` → `#000000` | `{color.black}` → `#000000` |
| `color.onProduct2` | color | `{color.white}` → `#FFFFFF` | `{color.white}` → `#FFFFFF` | `{color.white}` → `#FFFFFF` | `{color.black}` → `#000000` |
| `color.success` | color | `#1F9D5B` | `#0EA45B` | `#0EA45B` | `#087A42` |
| `color.warning` | color | `#E69A12` | `#F59E0B` | `#F59E0B` | `#FF9A1F` |
| `color.danger` | color | `#D23B34` | `#D83232` | `#D83232` | `#D42A38` |
| `color.ink` | color | `#16130F` | `#0B1020` | `#2A1657` | `#0B1329` |

## fontFamily

| Токен | Тип | Aurum | Nova | Fiesta | Ultra |
|---|---|---|---|---|---|
| `fontFamily.display` | fontFamilies | `Montserrat` | `Space Grotesk` | `Nunito` | `Unbounded` |
| `fontFamily.base` | fontFamilies | `Manrope` | `Space Grotesk` | `Nunito` | `Inter` |

## space.padding

| Токен | Тип | Aurum | Nova | Fiesta | Ultra |
|---|---|---|---|---|---|
| `space.padding.xs` | spacing | `{dimension.12}` → `12` | `{dimension.12}` → `12` | `{dimension.12}` → `12` | `{dimension.12}` → `12` |
| `space.padding.sm` | spacing | `{dimension.12}` → `12` | `{dimension.12}` → `12` | `{dimension.12}` → `12` | `{dimension.12}` → `12` |
| `space.padding.md` | spacing | `{dimension.16}` → `16` | `{dimension.16}` → `16` | `{dimension.16}` → `16` | `{dimension.16}` → `16` |
| `space.padding.lg` | spacing | `{dimension.20}` → `20` | `{dimension.20}` → `20` | `{dimension.20}` → `20` | `{dimension.20}` → `20` |
| `space.padding.xl` | spacing | `{dimension.24}` → `24` | `{dimension.24}` → `24` | `{dimension.24}` → `24` | `{dimension.24}` → `24` |

## space.gap

| Токен | Тип | Aurum | Nova | Fiesta | Ultra |
|---|---|---|---|---|---|
| `space.gap.xs` | spacing | `{dimension.4}` → `4` | `{dimension.4}` → `4` | `{dimension.4}` → `4` | `{dimension.4}` → `4` |
| `space.gap.sm` | spacing | `{dimension.6}` → `6` | `{dimension.6}` → `6` | `{dimension.6}` → `6` | `{dimension.6}` → `6` |
| `space.gap.md` | spacing | `{dimension.8}` → `8` | `{dimension.8}` → `8` | `{dimension.8}` → `8` | `{dimension.8}` → `8` |
| `space.gap.lg` | spacing | `{dimension.10}` → `10` | `{dimension.10}` → `10` | `{dimension.10}` → `10` | `{dimension.10}` → `10` |
| `space.gap.xl` | spacing | `{dimension.12}` → `12` | `{dimension.12}` → `12` | `{dimension.12}` → `12` | `{dimension.12}` → `12` |

## borderRadius

| Токен | Тип | Aurum | Nova | Fiesta | Ultra |
|---|---|---|---|---|---|
| `borderRadius.control` | borderRadius | `{borderRadius.8}` → `8` | `{borderRadius.0}` → `0` | `{borderRadius.999}` → `999` | `{borderRadius.12}` → `12` |
| `borderRadius.surface` | borderRadius | `{borderRadius.12}` → `12` | `{borderRadius.4}` → `4` | `{borderRadius.24}` → `24` | `{borderRadius.12}` → `12` |

## borderWidth

| Токен | Тип | Aurum | Nova | Fiesta | Ultra |
|---|---|---|---|---|---|
| `borderWidth.none` | borderWidth | `{borderWidth.0}` → `0` | `{borderWidth.0}` → `0` | `{borderWidth.0}` → `0` | `{borderWidth.0}` → `0` |
| `borderWidth.control` | borderWidth | `{borderWidth.1}` → `1` | `{borderWidth.1}` → `1` | `{borderWidth.2}` → `2` | `{borderWidth.2}` → `2` |

## size

| Токен | Тип | Aurum | Nova | Fiesta | Ultra |
|---|---|---|---|---|---|
| `size.control.xs` | sizing | `{dimension.24}` → `24` | `{dimension.24}` → `24` | `{dimension.24}` → `24` | `{dimension.24}` → `24` |
| `size.control.sm` | sizing | `{dimension.32}` → `32` | `{dimension.32}` → `32` | `{dimension.32}` → `32` | `{dimension.32}` → `32` |
| `size.control.md` | sizing | `{dimension.40}` → `40` | `{dimension.40}` → `40` | `{dimension.40}` → `40` | `{dimension.40}` → `40` |
| `size.control.lg` | sizing | `{dimension.48}` → `48` | `{dimension.48}` → `48` | `{dimension.48}` → `48` | `{dimension.48}` → `48` |
| `size.control.xl` | sizing | `{dimension.56}` → `56` | `{dimension.56}` → `56` | `{dimension.56}` → `56` | `{dimension.56}` → `56` |

## iconSize

| Токен | Тип | Aurum | Nova | Fiesta | Ultra |
|---|---|---|---|---|---|
| `iconSize.xs` | sizing | `{dimension.12}` → `12` | `{dimension.12}` → `12` | `{dimension.12}` → `12` | `{dimension.12}` → `12` |
| `iconSize.sm` | sizing | `{dimension.16}` → `16` | `{dimension.16}` → `16` | `{dimension.16}` → `16` | `{dimension.16}` → `16` |
| `iconSize.md` | sizing | `{dimension.20}` → `20` | `{dimension.20}` → `20` | `{dimension.20}` → `20` | `{dimension.20}` → `20` |
| `iconSize.lg` | sizing | `{dimension.24}` → `24` | `{dimension.24}` → `24` | `{dimension.24}` → `24` | `{dimension.24}` → `24` |
| `iconSize.xl` | sizing | `{dimension.32}` → `32` | `{dimension.32}` → `32` | `{dimension.32}` → `32` | `{dimension.32}` → `32` |

## layout.columns

| Токен | Тип | Aurum | Nova | Fiesta | Ultra |
|---|---|---|---|---|---|
| `layout.columns.xs` | number | `4` | `4` | `4` | `4` |
| `layout.columns.sm` | number | `8` | `8` | `8` | `8` |
| `layout.columns.md` | number | `12` | `12` | `12` | `12` |
| `layout.columns.lg` | number | `12` | `12` | `12` | `12` |
| `layout.columns.xl` | number | `12` | `12` | `12` | `12` |

## layout.columnGap

| Токен | Тип | Aurum | Nova | Fiesta | Ultra |
|---|---|---|---|---|---|
| `layout.columnGap.xs` | spacing | `{dimension.16}` → `16` | `{dimension.16}` → `16` | `{dimension.16}` → `16` | `{dimension.16}` → `16` |
| `layout.columnGap.sm` | spacing | `{dimension.16}` → `16` | `{dimension.16}` → `16` | `{dimension.16}` → `16` | `{dimension.16}` → `16` |
| `layout.columnGap.md` | spacing | `{dimension.16}` → `16` | `{dimension.16}` → `16` | `{dimension.16}` → `16` | `{dimension.16}` → `16` |
| `layout.columnGap.lg` | spacing | `{dimension.24}` → `24` | `{dimension.24}` → `24` | `{dimension.24}` → `24` | `{dimension.24}` → `24` |
| `layout.columnGap.xl` | spacing | `{dimension.24}` → `24` | `{dimension.24}` → `24` | `{dimension.24}` → `24` | `{dimension.24}` → `24` |

## layout.paddingH

| Токен | Тип | Aurum | Nova | Fiesta | Ultra |
|---|---|---|---|---|---|
| `layout.paddingH.xs` | spacing | `{dimension.16}` → `16` | `{dimension.16}` → `16` | `{dimension.16}` → `16` | `{dimension.16}` → `16` |
| `layout.paddingH.sm` | spacing | `{dimension.24}` → `24` | `{dimension.24}` → `24` | `{dimension.24}` → `24` | `{dimension.24}` → `24` |
| `layout.paddingH.md` | spacing | `{dimension.24}` → `24` | `{dimension.24}` → `24` | `{dimension.24}` → `24` | `{dimension.24}` → `24` |
| `layout.paddingH.lg` | spacing | `{dimension.24}` → `24` | `{dimension.24}` → `24` | `{dimension.24}` → `24` | `{dimension.24}` → `24` |
| `layout.paddingH.xl` | spacing | `{dimension.24}` → `24` | `{dimension.24}` → `24` | `{dimension.24}` → `24` | `{dimension.24}` → `24` |

## layout.rowGap

| Токен | Тип | Aurum | Nova | Fiesta | Ultra |
|---|---|---|---|---|---|
| `layout.rowGap.xs` | spacing | `{dimension.24}` → `24` | `{dimension.24}` → `24` | `{dimension.24}` → `24` | `{dimension.24}` → `24` |
| `layout.rowGap.sm` | spacing | `{dimension.32}` → `32` | `{dimension.32}` → `32` | `{dimension.32}` → `32` | `{dimension.32}` → `32` |
| `layout.rowGap.md` | spacing | `{dimension.32}` → `32` | `{dimension.32}` → `32` | `{dimension.32}` → `32` | `{dimension.32}` → `32` |
| `layout.rowGap.lg` | spacing | `{dimension.40}` → `40` | `{dimension.40}` → `40` | `{dimension.40}` → `40` | `{dimension.40}` → `40` |
| `layout.rowGap.xl` | spacing | `{dimension.48}` → `48` | `{dimension.48}` → `48` | `{dimension.48}` → `48` | `{dimension.48}` → `48` |
