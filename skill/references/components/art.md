# Game Art

> Згенеровано `tools/build-skill.py` з Token Studio JSON · 2026-09-22. Не редагувати вручну — правити JSON і перегенерувати.

**Figma:** Game Art (component set) · Pattern  
**Варіанти:** Pattern: a–f  
**Анатомія:** Фрейм 240×320 (clip) → `Shape 1` (велике коло, правий нижній кут) · `Shape 2` (мале коло, лівий верхній) · `Shape 3` (скошена смуга).

Токенів: **10**. Посилаються тільки на theme / brand-семантику, не на core.

## Кольори

> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.

| Токен | Figma variable | → Alias | Aurum light | Aurum dark |
|---|---|---|---|---|
| `art.a.bg` | art/a/bg | `{color.fill.primary.subtle}` | `#CFA74A` | `#CFA74A` |
| `art.b.bg` | art/b/bg | `{color.fill.accent.subtle}` | `#8E2C43` | `#8E2C43` |
| `art.c.bg` | art/c/bg | `{color.fill.info.subtle}` | `#B8704B` | `#B8704B` |
| `art.d.bg` | art/d/bg | `{color.bg.tertiary}` | `#16130F` | `#16130F` |
| `art.e.bg` | art/e/bg | `{color.fill.danger.subtle}` | `#D23B34` | `#D23B34` |
| `art.f.bg` | art/f/bg | `{color.fill.warning.subtle}` | `#E69A12` | `#E69A12` |
| `art.g.bg` | art/g/bg | `{color.fill.secondary.default}` | `#16130F` | `#16130F` |
| `art.h.bg` | art/h/bg | `{color.fill.success.subtle}` | `#1F9D5B` | `#1F9D5B` |
| `art.jackpot.bg` | art/jackpot/bg | `{color.illustration.stage.primary}` | `#CFA74A` | `#CFA74A` |
| `art.arena.bg` | art/arena/bg | `{color.illustration.stage.accent}` | `#8E2C43` | `#8E2C43` |

## Нотатки

- Абстрактні плейсхолдери замість зображень: кольори беруться з теми/бренду, тому арт міняє палітру при перемиканні.
- Використовується як 💠 Art у Game Tile, Promo Banner, Tournament Card. Замінюється фото заливкою.
