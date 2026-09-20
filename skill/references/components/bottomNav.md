# Bottom Nav

> Згенеровано `tools/build-skill.py` з Token Studio JSON · 2026-09-20. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Bottom Nav (component set) · Active  
**Варіанти:** Active: Home / Games / Tournaments / Shop / Profile  
**Анатомія:** Контейнер (auto-layout H, верхній бордер) → 5 × Nav Item: Home · Games · Tournaments · Shop · Profile.

Токенів: **5**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `bottomNav.bg` | bottomNav/bg | `{color.bg.secondary}` | `#16130F` | `#16130F` |
| `bottomNav.br` | bottomNav/br | `{color.border.tertiary}` | `#16130F` | `#16130F` |

## Розміри та форма

| Токен | Figma variable | Тип | → Alias | Значення |
|---|---|---|---|---|
| `bottomNav.borderWidth` | bottomNav/borderWidth | borderWidth | `{borderWidth.control}` | `1` |
| `bottomNav.paddingH` | bottomNav/paddingH | spacing | `{space.padding.sm}` | `12` |
| `bottomNav.paddingV` | bottomNav/paddingV | spacing | `{space.gap.md}` | `8` |

## Нотатки

- Мобільна навігація лобі (xs 360).
