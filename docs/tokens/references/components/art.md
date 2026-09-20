# Game Art

> Згенеровано `scripts/build-token-docs.py` з Token Studio JSON · 2026-09-20. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Game Art (component set) · Pattern  
**Варіанти:** Pattern: a–f  
**Анатомія:** Фрейм 240×320 (clip) → `Shape 1` (велике коло, правий нижній кут) · `Shape 2` (мале коло, лівий верхній) · `Shape 3` (скошена смуга).

Токенів: **18**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `art.a.bg` | art/a/bg | `{color.fill.primary.subtle}` | `#CFA74A` | `#CFA74A` |
| `art.a.shape1` | art/a/shape1 | `{color.fill.primary.default}` | `#CFA74A` | `#CFA74A` |
| `art.a.shape2` | art/a/shape2 | `{color.fill.accent.default}` | `#8E2C43` | `#8E2C43` |
| `art.b.bg` | art/b/bg | `{color.fill.accent.subtle}` | `#8E2C43` | `#8E2C43` |
| `art.b.shape1` | art/b/shape1 | `{color.fill.accent.default}` | `#8E2C43` | `#8E2C43` |
| `art.b.shape2` | art/b/shape2 | `{color.fill.primary.default}` | `#CFA74A` | `#CFA74A` |
| `art.c.bg` | art/c/bg | `{color.fill.info.subtle}` | `#B8704B` | `#B8704B` |
| `art.c.shape1` | art/c/shape1 | `{color.fill.info.default}` | `#B8704B` | `#B8704B` |
| `art.c.shape2` | art/c/shape2 | `{color.fill.primary.default}` | `#CFA74A` | `#CFA74A` |
| `art.d.bg` | art/d/bg | `{color.bg.tertiary}` | `#16130F` | `#16130F` |
| `art.d.shape1` | art/d/shape1 | `{color.fill.success.default}` | `#1F9D5B` | `#1F9D5B` |
| `art.d.shape2` | art/d/shape2 | `{color.fill.accent.default}` | `#8E2C43` | `#8E2C43` |
| `art.e.bg` | art/e/bg | `{color.fill.primary.default}` | `#CFA74A` | `#CFA74A` |
| `art.e.shape1` | art/e/shape1 | `{color.fill.accent.default}` | `#8E2C43` | `#8E2C43` |
| `art.e.shape2` | art/e/shape2 | `{color.fill.primary.subtle}` | `#CFA74A` | `#CFA74A` |
| `art.f.bg` | art/f/bg | `{color.fill.accent.default}` | `#8E2C43` | `#8E2C43` |
| `art.f.shape1` | art/f/shape1 | `{color.fill.info.default}` | `#B8704B` | `#B8704B` |
| `art.f.shape2` | art/f/shape2 | `{color.fill.primary.default}` | `#CFA74A` | `#CFA74A` |

## Нотатки

- Абстрактні плейсхолдери замість зображень: кольори беруться з теми/бренду, тому арт міняє палітру при перемиканні.
- Використовується як 💠 Art у Game Tile, Promo Banner, Tournament Card. Замінюється фото заливкою.
