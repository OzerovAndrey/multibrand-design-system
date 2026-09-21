# Section Heading

> Згенеровано `tools/build-skill.py` з Token Studio JSON · 2026-09-21. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Section Heading (component set) · Size  
**Варіанти:** Size: xs (mobile 328) / md (desktop 720). Booleans: Icon, Subtitle, See all, Arrows  
**Анатомія:** Контейнер (auto-layout H, space-between) → `Title group` (`Icon` · `Text`: Title + Subtitle) · `Actions` (`See all` = Button Text sm · `Arrows` = 2 × Button Secondary sm icon-only).

Токенів: **7**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `sectionHeader.title.color` | sectionHeader/title/color | `{color.text.primary}` | `#16130F` | `#16130F` |
| `sectionHeader.subtitle.color` | sectionHeader/subtitle/color | `{color.text.tertiary}` | `#16130F` | `#16130F` |
| `sectionHeader.icon.color` | sectionHeader/icon/color | `{color.text.accent}` | `#CFA74A` | `#CFA74A` |

## Розміри та форма

| Токен | Figma variable | Тип | → Alias | Значення |
|---|---|---|---|---|
| `sectionHeader.iconSize` | sectionHeader/iconSize | sizing | `{iconSize.lg}` | `24` |
| `sectionHeader.gap.xs` | sectionHeader/gap/xs | spacing | `{space.gap.md}` | `8` |
| `sectionHeader.gap.md` | sectionHeader/gap/md | spacing | `{space.gap.xl}` | `12` |
| `sectionHeader.actions.gap` | sectionHeader/actions/gap | spacing | `{space.gap.md}` | `8` |

## Текст (text styles, не токени)

| Розмір | Стиль |
|---|---|
| `xs` | title/t4 |
| `md` | title/t2 |
| `subtitle` | body/sm/regular |

## Нотатки

- Заголовок — display-шрифт бренду; ✏️ Title · ✏️ Subtitle · 💠 Icon (swap, `flame-filled`).
