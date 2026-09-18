---
name: multibrand-design-system
description: Реєстр токенів Multibrand Design System (репо multibrand-design-system; бренди Aurum / Nova / Fiesta) — усі сети Token Studio (core, brand/aurum|nova|fiesta, map, theme/light|dark, typography, components), їхні значення, посилання й Figma-змінні. Use ANY TIME the user works with tokens of the Multibrand Design System — adding a component's tokens, binding variables in Figma, checking what a token resolves to, adding a brand, or asking "який токен для…". INDEX — деталі в references/*.md, вантажити тільки потрібний файл. Генерується з JSON скриптом scripts/build-token-docs.py.
---

# Multibrand Design System — токени (індекс)

> Згенеровано `scripts/build-token-docs.py` з Token Studio JSON · 2026-09-18. Не редагувати вручну — правити JSON і перегенерувати.

Джерело правди — Token Studio JSON у `tokens/`. Figma Variables і text styles — синхронізована копія.
Усього токенів: **408**.

## Потік

```
core ──► brand/<x> ──► map ──► theme/<mode> ──► components ──► шар у Figma
  │         │                                      ▲
  │         └── розміри, радіуси, шрифти ──────────┘
  └──► typography (text styles) ──► текстовий шар у Figma
```

- **core** — словник сирих значень. Ніколи не на шарі.
- **brand** — що відрізняє бренд: кольори, шрифти, розмірна семантика.
- **map** — рампи від базових кольорів бренду.
- **theme** — семантика кольорів; light/dark дивляться в різні кроки рампи. Тільки кольори.
- **typography** — text styles; компоненти беруть стиль, а не токени.
- **components** — єдине, що прив'язується до шару. Посилається на theme/brand-семантику.

## Сети (порядок = `$metadata.tokenSetOrder`)

| Сет | Токенів | Що всередині |
|---|---|---|
| `core` | 58 | примітиви: dimension, borderRadius, borderWidth, fontWeight, fontSize, lineHeight, letterSpacing, textCase, color.white/black/transparent |
| `brand/aurum` | 35 | кольори бренду, шрифти, розмірна семантика |
| `brand/nova` | 35 | ті самі ключі, інші значення |
| `brand/fiesta` | 35 | ті самі ключі, інші значення |
| `map` | 41 | рампи 100…900 від базових кольорів бренду |
| `theme/light` | 46 | семантика кольорів: bg, fill, text, border, outline |
| `theme/dark` | 46 | ті самі ключі, інші кроки рампи |
| `typography` | 25 | text styles |
| `components` | 87 | усі компонентні токени в одному сеті |

## Теми → Figma

| Група (колекція) | Mode | Сети | Що створює |
|---|---|---|---|
| Base | Default | core | variables |
| Brand | Aurum | core (source), brand/aurum, map | variables |
| Brand | Nova | core (source), brand/nova, map | variables |
| Brand | Fiesta | core (source), brand/fiesta, map | variables |
| Theme | Light | core (source), brand/aurum (source), map (source), theme/light | variables |
| Theme | Dark | core (source), brand/aurum (source), map (source), theme/dark | variables |
| Typography | Default | core (source), brand/aurum (source), typography | text styles |
| Components | Default | core (source), brand/aurum (source), map (source), theme/light (source), components | variables |

Експорт: **Variables** — теми Base, Brand, Theme, Components (Typography не вибирати). **Styles** — тільки Typography/Default з «Create styles with variable references».

## Правила

1. Ім'я токена = CSS-властивість: `bg`, `color`, `br`, `iconColor`, `size`, `paddingH/V`, `gap`, `iconSize`, `borderRadius`, `borderWidth`. Формат `компонент.[підчастина].[варіант].властивість.[стан|розмір]`; стан/розмір — завжди останній.
2. Компонент посилається тільки на theme / brand-семантику (`color.*`, `space.*`, `size.control.*`, `iconSize.*`, `borderRadius.*`, `borderWidth.*`). Ніколи на core і ніколи на `map` напряму.
3. Компонент не має typography-токенів — текстовий шар отримує text style (`typography/…`).
4. Ключі трьох брендів ідентичні; ключі light і dark ідентичні.
5. Бренд = тільки значення. Нові ключі в бренді — лише якщо їх додано в усі три.
6. Розміри й радіуси — у бренді, не в темі. Тема міняє лише кольори.
7. Стани: `default / hover / active / disabled` (focus не робимо). Розміри: `xs / sm / md / lg / xl`.

## Карта файлів

| Файл | Коли читати |
|---|---|
| [references/core.md](references/core.md) | примітиви, шкали розмірів і шрифтів |
| [references/brand.md](references/brand.md) | значення трьох брендів поруч |
| [references/map.md](references/map.md) | рампи кольорів |
| [references/theme.md](references/theme.md) | семантика кольорів light / dark |
| [references/typography.md](references/typography.md) | text styles |

### Компоненти

| Компонент | Токенів |
|---|---|
| [Button](references/components/button.md) | 48 |
| [Input](references/components/input.md) | 39 |

## Додати компонент

1. Блок `<component>` у `tokens/components.json` (посилання тільки на theme/brand-семантику).
2. Нотатки (анатомія, варіанти, text styles) — у `COMPONENT_NOTES` скрипта.
3. `python3 scripts/build-token-docs.py` — з'явиться `references/components/<component>.md`, індекс оновиться.
