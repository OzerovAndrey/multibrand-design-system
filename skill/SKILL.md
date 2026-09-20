---
name: multibrand-design-system
description: Реєстр токенів Multibrand Design System (репо multibrand-design-system; бренди Aurum / Nova / Fiesta) — усі сети Token Studio (core, brand/aurum|nova|fiesta, map, theme/light|dark, typography, components), їхні значення, посилання й Figma-змінні. Use ANY TIME the user works with tokens of the Multibrand Design System — adding a component's tokens, binding variables in Figma, checking what a token resolves to, adding a brand, or asking "який токен для…". INDEX — деталі в references/*.md, вантажити тільки потрібний файл. Генерується з JSON скриптом tools/build-skill.py.
---

# Multibrand Design System — токени (індекс)

> Згенеровано `tools/build-skill.py` з Token Studio JSON · 2026-09-20. Не редагувати вручну — правити JSON і перегенерувати.

Джерело правди — Token Studio JSON у `tokens/`. Figma Variables і text styles — синхронізована копія.
Усього токенів: **952**.

## Мета й ідеологія

**Кінцевий результат** — живий сайт-демо на власному домені: клієнт перемикає бренд (Aurum / Nova / Fiesta) і тему (Light / Dark), і весь iGaming-інтерфейс перебудовується миттєво, а компоненти й розмітка не змінюються. Ця система — доказ, що один набір токенів керує цілим продуктом.

1. **Перемикання — головний продукт.** Кожен компонент і сторінка мають виглядати добре й змінюватись у всіх 6 комбінаціях (3 бренди × Light/Dark). Не змінилось або зламалось — це помилка архітектури, а не токенів.
2. **Компонент не знає про бренд і тему.** Лише токени; жодного hex, px чи шрифту напряму.
3. **Бренди відрізняються характером, а не тільки кольором:** колір + шрифт + радіуси + товщина бордера. Aurum — тепла преміум-класика, м'які кути. Nova — холодний tech, гострі кути. Fiesta — яскравий mass-market, pill-форми, товстіші контури.
4. **Бренд = значення, тема = кольори.** Ключі брендів ідентичні; світла й темна теми різняться лише кольорами.
5. **Будівельні блоки для геймблових структур:** компоненти проєктуються під лобі, каталог ігор, турніри, профіль, реєстрацію, магазин з лутбоксами — від атомів до секцій.
6. **Кожна демо-функція вимірювана:** скільки токенів змінилось при перемиканні і скільки компонентів не торкнулись.
7. **Репо — джерело правди;** Figma і сайт — його похідні.

## Потік

```
core ──► brand/<x> ──► map ──► theme/<mode> ──► components ──► шар у Figma
  │         │                                      ▲
  │         └── розміри, радіуси, шрифти ──────────┘
  └──► typography (text styles) ──► текстовий шар у Figma
```

- **core** — словник сирих значень. Ніколи не на шарі.
- **brand** — що відрізняє бренд: кольори, шрифти, розмірна семантика, сітка сторінки.
- **map** — рампи від базових кольорів бренду.
- **theme** — семантика кольорів; light/dark дивляться в різні кроки рампи. Тільки кольори.
- **typography** — text styles; компоненти беруть стиль, а не токени.
- **components** — єдине, що прив'язується до шару. Посилається на theme/brand-семантику.

## Сети (порядок = `$metadata.tokenSetOrder`)

| Сет | Токенів | Що всередині |
|---|---|---|
| `core` | 59 | примітиви: dimension, borderRadius, borderWidth, fontWeight, fontSize, lineHeight, letterSpacing, textCase, color.white/black/transparent |
| `brand/aurum` | 55 | кольори бренду, шрифти, розмірна семантика, сітка сторінки (layout) |
| `brand/nova` | 55 | ті самі ключі, інші значення |
| `brand/fiesta` | 55 | ті самі ключі, інші значення |
| `map` | 41 | рампи 100…900 від базових кольорів бренду |
| `theme/light` | 73 | семантика кольорів: bg, fill, text, border, outline |
| `theme/dark` | 73 | ті самі ключі, інші кроки рампи |
| `typography` | 25 | text styles |
| `components` | 516 | усі компонентні токени в одному сеті |

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
2. Компонент посилається тільки на theme / brand-семантику (`color.*`, `space.*`, `layout.*`, `size.control.*`, `iconSize.*`, `borderRadius.*`, `borderWidth.*`). Ніколи на core і ніколи на `map` напряму.
3. Компонент не має typography-токенів — текстовий шар отримує text style (`typography/…`).
4. Ключі трьох брендів ідентичні; ключі light і dark ідентичні.
5. Бренд = тільки значення. Нові ключі в бренді — лише якщо їх додано в усі три.
6. Розміри й радіуси — у бренді, не в темі. Тема міняє лише кольори.
7. Стани: `default / hover / active / disabled` (focus не робимо). Розміри: `xs / sm / md / lg / xl`.
8. Ім'я групи не може бути `value`, `type` або `description` — Token Studio читає їх як поля токена. Замість `value` — `amount` / `percent` / `detail`.

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
| [Card Default](references/components/card.md) | 13 |
| [Media](references/components/media.md) | 8 |
| [Header](references/components/header.md) | 19 |
| [Balance](references/components/balance.md) | 10 |
| [Footer](references/components/footer.md) | 33 |
| [Badge](references/components/badge.md) | 19 |
| [Chip](references/components/chip.md) | 32 |
| [Tab](references/components/tab.md) | 16 |
| [Avatar](references/components/avatar.md) | 22 |
| [Progress](references/components/progress.md) | 10 |
| [Checkbox](references/components/checkbox.md) | 20 |
| [Switch](references/components/switch.md) | 15 |
| [Section Heading](references/components/sectionHeader.md) | 7 |
| [Stat Tile](references/components/stat.md) | 19 |
| [List Item](references/components/listItem.md) | 20 |
| [Alert](references/components/alert.md) | 20 |
| [Leaderboard Row](references/components/leaderRow.md) | 23 |
| [Nav Item](references/components/navItem.md) | 10 |
| [Bottom Nav](references/components/bottomNav.md) | 5 |
| [Game Tile](references/components/gameTile.md) | 14 |
| [Promo Banner](references/components/promo.md) | 11 |
| [Tournament Card](references/components/tournament.md) | 15 |
| [Lootbox Card](references/components/lootbox.md) | 24 |
| [Modal](references/components/modal.md) | 15 |
| [Game Art](references/components/art.md) | 10 |
| [illustration](references/components/illustration.md) | 19 |

## Додати компонент

1. Блок `<component>` у `tokens/components.json` (посилання тільки на theme/brand-семантику).
2. Нотатки (анатомія, варіанти, text styles) — у `COMPONENT_NOTES` скрипта.
3. `python3 tools/build-skill.py` — з'явиться `references/components/<component>.md`, індекс оновиться.
