# Multibrand Design System — правила для Claude Code

## Проєкт
Мультибрендова дизайн-система: одна токен-архітектура, бренди Aurum / Nova / Fiesta, теми Light / Dark.
Власник — Андрій Озеров. Мова комунікації й документації — українська.

## Джерело правди
- `tokens/*.json` (Token Studio) — єдине джерело правди. Figma — синхронізована копія.
- `docs/tokens/` генерується. **Ніколи не редагувати вручну.**
- Після будь-якої зміни в `tokens/` або `COMPONENT_NOTES` у скрипті — запусти `python3 scripts/build-token-docs.py` і коміть `tokens/` + `docs/tokens/` разом.

## Структура токенів (не змінювати без прямої вказівки)
- Порядок сетів: core → brand/aurum|nova|fiesta → map → theme/light|dark → typography → components.
- **core** — примітиви. Компоненти на core не посилаються.
- **brand/<x>** — одиничні базові кольори (product1–3, onProduct1/2, success, warning, danger, ink), fontFamily.display/base, розмірна семантика (space.padding/gap, size.control, iconSize, borderRadius.control|surface, borderWidth.none|control). Ключі трьох брендів ідентичні. Рамп у бренді немає.
- **map** — рампи 100…900 від базових кольорів.
- **theme/light|dark** — тільки кольори. Ключі ідентичні.
- **typography** — text styles. Компоненти не мають typography-токенів.
- **components** — один сет, посилання тільки на theme / brand-семантику.
- Змінюючи кольори бренду — міняй тільки значення, структуру не чіпай.

## Нейминг
Ім'я = CSS-властивість: bg, color, br, iconColor, size, paddingH/V, gap, iconSize, borderRadius, borderWidth.
Формат `компонент.[підчастина].[варіант].властивість.[стан|розмір]`. Стани: default / hover / active / disabled (focus не робимо). Розміри: xs–xl.
Заборонено: inset, elevation, paddingX, stack.

## Перевірка перед комітом
1. JSON валідний.
2. Усі `{посилання}` резолвляться для кожної пари бренд × тема.
3. Ключі brand/aurum = nova = fiesta; theme/light = dark.
4. `components` не посилається на `core.*` і `map.*` напряму.
5. `docs/tokens/` перегенеровано.

## Коміти
Коротко, українською, у форматі `<область>: <що>`, напр. `tokens(input): прибрано placeholder.color`, `docs: перегенеровано`.
