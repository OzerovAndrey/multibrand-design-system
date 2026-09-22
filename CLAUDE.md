# Multibrand Design System — правила для Claude Code

## Проєкт
Мультибрендова дизайн-система: одна токен-архітектура, бренди Aurum / Nova / Fiesta / Ultra, теми Light / Dark.
Власник — Андрій Озеров. Мова комунікації й документації — українська.

## Мета й ідеологія
Кінцевий результат — живий сайт-демо на власному домені, де клієнти перемикають бренд (Aurum / Nova / Fiesta / Ultra) і тему (Light / Dark) і бачать, як увесь iGaming-інтерфейс перебудовується миттєво, без змін у компонентах і розмітці.
- Перемикання — головний продукт: кожен компонент і сторінка перевіряються в усіх 8 комбінаціях. Не змінюється або ламається — помилка архітектури.
- Бренди різняться характером, не тільки кольором: колір + шрифт + радіуси + товщина бордера (Aurum — м'які кути, Nova — гострі, Fiesta — pill і товстіші контури, Ultra — neon navy/pink/cyan, широкий display-гротеск, кути 12 і контур 2).
- Компоненти — будівельні блоки для геймблових структур: лобі, каталог ігор, турніри, профіль, реєстрація, магазин з лутбоксами.
- Компонент не знає про бренд і тему; лише токени.

## Джерело правди
- `tokens/*.json` (Token Studio) — єдине джерело правди. Figma — синхронізована копія.
- `skill/` генерується. **Ніколи не редагувати вручну.**
- Після будь-якої зміни в `tokens/` або `COMPONENT_NOTES` у скрипті — запусти `python3 tools/build-skill.py` і коміть `tokens/` + `skill/` разом.

## Структура токенів (не змінювати без прямої вказівки)
- Порядок сетів: core → brand/aurum|nova|fiesta|ultra → map → theme/light|dark → typography → components.
- **core** — примітиви. Компоненти на core не посилаються.
- **brand/<x>** — одиничні базові кольори (product1–3, onProduct1/2, success, warning, danger, ink), fontFamily.display/base, розмірна семантика (space.padding/gap, size.control, iconSize, borderRadius.control|surface, borderWidth.none|control), сітка сторінки (layout.columns/columnGap/paddingH/rowGap по xs–xl). Ключі трьох брендів ідентичні. Рамп у бренді немає.
- **map** — рампи 100…900 від базових кольорів.
- **theme/light|dark** — тільки кольори. Ключі ідентичні.
- **typography** — text styles. Компоненти не мають typography-токенів.
- **components** — один сет, посилання тільки на theme / brand-семантику (включно з layout.*).
- Змінюючи кольори бренду — міняй тільки значення, структуру не чіпай.

## Нейминг
Ім'я = CSS-властивість: bg, color, br, iconColor, size, paddingH/V, gap, iconSize, borderRadius, borderWidth.
Формат `компонент.[підчастина].[варіант].властивість.[стан|розмір]`. Стани: default / hover / active / disabled (focus не робимо). Розміри: xs–xl.
Заборонено: inset, elevation, paddingX, stack.
Ім'я групи не може бути `value`, `type`, `description` (зарезервовані Token Studio) — використовуй `amount` / `percent` / `detail`.

## Перевірка перед комітом
1. JSON валідний.
2. Усі `{посилання}` резолвляться для кожної пари бренд × тема.
3. Ключі brand/aurum = nova = fiesta = ultra; theme/light = dark.
4. `components` не посилається на `core.*` і `map.*` напряму.
5. `skill/` перегенеровано.

## Коміти
Коротко, українською, у форматі `<область>: <що>`, напр. `tokens(input): прибрано placeholder.color`, `docs: перегенеровано`.

## Структура репо
`tokens/` (джерело) · `skill/` (генерується) · `site/` (демо) · `tools/` (генератори). Нових тек не створювати без потреби — по одній теці на роль, без дублів.

## Сайт (`site/`)
Живе демо (Vite + React + TS): перемикач брендів/тем, сторінки Home · Slots · Tournaments · Profile · Sign up · Shop.
- `npm --prefix site run tokens` генерує `site/src/styles/tokens.generated.css` і `site/public/tokens-manifest.json` з `tokens/*.json` (через `tools/build-css.mjs`). Ці файли **не редагувати вручну**.
- Стилі компонентів у CSS беруть тільки змінні компонентних токенів (`var(--button-primary-bg-default)`); оболонка сторінок і панель — theme/brand-семантику (`--color-*`, `--space-*`). Ніколи core/map, hex, px чи шрифт напряму.
- Нова зміна в `tokens/` → перегенерувати `skill/` (`python3 tools/build-skill.py`) і токени сайту разом.
- Перевірка перед комітом сайту: `npm --prefix site run build` без помилок.
- Казино-ілюстрації (слоти, рулетка, карти, фішки, кубики, кристал, скриня, кубок + сцени jackpot/arena) генерує `python3 tools/build-art.py` у `site/src/art/illustrations.ts` (не редагувати вручну). Усі заливки — токени `illustration.*`; тому ілюстрації перефарбовуються разом із брендом і темою. Фони — `art.*.bg`.
