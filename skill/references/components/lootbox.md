# Lootbox Card

> Згенеровано `tools/build-skill.py` з Token Studio JSON · 2026-09-20. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Lootbox Card (component set) · Rarity × State  
**Варіанти:** Rarity: Common / Rare / Epic / Legendary · State: Default / Hover (контур accent)  
**Анатомія:** Картка (V, clip) → `Art` (фон рідкості, `Halo`, `Icon`, `Rarity strip`, Badge) · `Info` (Title + Description) · `Purchase` (Price + Buy).

Токенів: **24**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `lootbox.bg` | lootbox/bg | `{color.bg.secondary}` | `#16130F` | `#16130F` |
| `lootbox.br.default` | lootbox/br/default | `{color.border.tertiary}` | `#16130F` | `#16130F` |
| `lootbox.br.hover` | lootbox/br/hover | `{color.border.accent}` | `#CFA74A` | `#CFA74A` |
| `lootbox.title.color` | lootbox/title/color | `{color.text.primary}` | `#16130F` | `#16130F` |
| `lootbox.desc.color` | lootbox/desc/color | `{color.text.secondary}` | `#16130F` | `#16130F` |
| `lootbox.price.color` | lootbox/price/color | `{color.text.primary}` | `#16130F` | `#16130F` |
| `lootbox.price.iconColor` | lootbox/price/iconColor | `{color.text.accent}` | `#CFA74A` | `#CFA74A` |
| `lootbox.common.art.bg` | lootbox/common/art/bg | `{color.fill.secondary.default}` | `#16130F` | `#16130F` |
| `lootbox.common.strip.bg` | lootbox/common/strip/bg | `{color.fill.secondary.active}` | `#16130F` | `#16130F` |
| `lootbox.rare.art.bg` | lootbox/rare/art/bg | `{color.fill.info.subtle}` | `#B8704B` | `#B8704B` |
| `lootbox.rare.strip.bg` | lootbox/rare/strip/bg | `{color.fill.info.default}` | `#B8704B` | `#B8704B` |
| `lootbox.epic.art.bg` | lootbox/epic/art/bg | `{color.fill.accent.subtle}` | `#8E2C43` | `#8E2C43` |
| `lootbox.epic.strip.bg` | lootbox/epic/strip/bg | `{color.fill.accent.default}` | `#8E2C43` | `#8E2C43` |
| `lootbox.legendary.art.bg` | lootbox/legendary/art/bg | `{color.fill.primary.subtle}` | `#CFA74A` | `#CFA74A` |
| `lootbox.legendary.strip.bg` | lootbox/legendary/strip/bg | `{color.fill.primary.default}` | `#CFA74A` | `#CFA74A` |

## Розміри та форма

| Токен | Figma variable | Тип | → Alias | Значення |
|---|---|---|---|---|
| `lootbox.borderRadius` | lootbox/borderRadius | borderRadius | `{borderRadius.surface}` | `12` |
| `lootbox.borderWidth` | lootbox/borderWidth | borderWidth | `{borderWidth.control}` | `1` |
| `lootbox.padding` | lootbox/padding | spacing | `{space.padding.md}` | `16` |
| `lootbox.gap` | lootbox/gap | spacing | `{space.gap.xl}` | `12` |
| `lootbox.info.gap` | lootbox/info/gap | spacing | `{space.gap.sm}` | `6` |
| `lootbox.price.gap` | lootbox/price/gap | spacing | `{space.gap.sm}` | `6` |
| `lootbox.iconSize` | lootbox/iconSize | sizing | `{iconSize.md}` | `20` |
| `lootbox.art.iconSize` | lootbox/art/iconSize | sizing | `{size.control.xl}` | `56` |
| `lootbox.inset` | lootbox/inset | spacing | `{space.gap.lg}` | `10` |

## Текст (text styles, не токени)

| Розмір | Стиль |
|---|---|
| `title` | title/t4 |
| `description` | body/sm/regular |
| `price` | label/lg |

## Нотатки

- Рідкість мапиться на neutral / info(product3) / accent(product2) / primary(product1) — кольори міняються з брендом. ✏️ Title · Description · Price · Rarity badge (boolean).
