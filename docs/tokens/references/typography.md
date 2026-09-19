# Typography — text styles

> Згенеровано `scripts/build-token-docs.py` з Token Studio JSON · 2026-09-19. Не редагувати вручну — правити JSON і перегенерувати.

Окремий шар. Сет `typography` → тема **Typography / Default** → Figma **text styles** `typography/…`.
Компоненти **не мають** власних typography-токенів: текстовий шар бере стиль зі шкали. Той самий набір — для вільного тексту.
Стилів: **25**.

Експорт: Styles & Variables → Export styles → тільки тема Typography/Default, галочка Typography, **Create styles with variable references** (fontFamily/fontSize/lineHeight/fontWeight прив'язані до змінних → шрифт перемикається з брендом).

| Стиль | Figma | Family | Size/LH | Weight | LS | Case | Для чого |
|---|---|---|---|---|---|---|---|
| `display.d1` | typography/display/d1 | display | 56/64 | 700 | -1% | none | hero, промо-заголовок |
| `display.d2` | typography/display/d2 | display | 48/56 | 700 | -1% | none |  |
| `display.d3` | typography/display/d3 | display | 40/48 | 700 | -1% | none |  |
| `title.t1` | typography/title/t1 | display | 32/40 | 700 | 0% | none | заголовок сторінки |
| `title.t2` | typography/title/t2 | display | 28/36 | 700 | 0% | none |  |
| `title.t3` | typography/title/t3 | display | 24/32 | 700 | 0% | none | заголовок секції |
| `title.t4` | typography/title/t4 | display | 20/28 | 600 | 0% | none |  |
| `title.t5` | typography/title/t5 | display | 18/26 | 600 | 0% | none | заголовок картки |
| `body.lg.regular` | typography/body/lg/regular | base | 18/28 | 400 | 0% | none |  |
| `body.lg.strong` | typography/body/lg/strong | base | 18/28 | 600 | 0% | none |  |
| `body.md.regular` | typography/body/md/regular | base | 16/24 | 400 | 0% | none | дефолтний текст |
| `body.md.strong` | typography/body/md/strong | base | 16/24 | 600 | 0% | none |  |
| `body.sm.regular` | typography/body/sm/regular | base | 14/20 | 400 | 0% | none |  |
| `body.sm.strong` | typography/body/sm/strong | base | 14/20 | 600 | 0% | none |  |
| `body.xs.regular` | typography/body/xs/regular | base | 12/16 | 400 | 0% | none |  |
| `body.xs.strong` | typography/body/xs/strong | base | 12/16 | 600 | 0% | none |  |
| `label.xl` | typography/label/xl | base | 18/26 | 600 | 0% | none | текст контролів: кнопки, чіпи, таби, інпути |
| `label.lg` | typography/label/lg | base | 16/24 | 600 | 0% | none | текст контролів: кнопки, чіпи, таби, інпути |
| `label.md` | typography/label/md | base | 14/20 | 600 | 0% | none | текст контролів: кнопки, чіпи, таби, інпути |
| `label.sm` | typography/label/sm | base | 12/16 | 600 | 0% | none | текст контролів: кнопки, чіпи, таби, інпути |
| `label.xs` | typography/label/xs | base | 10/14 | 600 | 0% | none | текст контролів: кнопки, чіпи, таби, інпути |
| `caption.md` | typography/caption/md | base | 12/16 | 400 | 0% | none |  |
| `caption.sm` | typography/caption/sm | base | 10/14 | 400 | 0% | none |  |
| `overline.md` | typography/overline/md | base | 12/16 | 600 | 8% | uppercase |  |
| `overline.sm` | typography/overline/sm | base | 10/14 | 600 | 8% | uppercase |  |

Family: `display` → `fontFamily.display`, `base` → `fontFamily.base` (значення — у brand.md).
