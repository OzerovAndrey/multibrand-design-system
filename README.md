# Multibrand Design System

Одна токен-архітектура, три бренди (Aurum / Nova / Fiesta), дві теми (Light / Dark).
Token Studio → Figma Variables + text styles.

```
tokens/                     Token Studio JSON — джерело правди
docs/tokens/                реєстр токенів у форматі скіла (генерується)
  SKILL.md                  індекс: шари, сети, теми → Figma, правила
  references/*.md           core · brand · map · theme · typography
  references/components/    по файлу на компонент
scripts/build-token-docs.py генератор docs/tokens з tokens/
CLAUDE.md                   правила роботи для Claude Code
```

## Оновити документацію

```
python3 scripts/build-token-docs.py
```

Запускати після будь-якої зміни в `tokens/`. `docs/tokens/` вручну не редагувати.

## Як скіл

`docs/tokens/` — готовий скіл `multibrand-design-system` (папка з `SKILL.md` + `references/`).

## Сайт-демо

`site/` — Vite + React застосунок, що збирається прямо з токенів: `tokens/*.json` → CSS-змінні (`data-brand` × `data-theme`) → компоненти → 6 сторінок.

```
cd site && npm install
npm run dev      # локально, http://localhost:5173
npm run build    # production у site/dist
```

Перемикач брендів і тем (правий нижній кут), «Play tour» і панель **Under the hood** (diff токенів, ланцюжок alias'ів, метрики).

