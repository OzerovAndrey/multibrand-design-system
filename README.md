# Multibrand Design System

Одна токен-архітектура, чотири бренди (Aurum / Nova / Fiesta / Ultra), дві теми (Light / Dark).
**Демо:** https://ozerovandrey.github.io/multibrand-design-system/

```
tokens/    джерело правди — Token Studio JSON (core → brand → map → theme → components)
skill/     скіл для Claude: SKILL.md + references/ (генерується з tokens/)
site/      живий сайт-демо (Vite + React), збирається з tokens/
tools/     генератори: build-skill.py (tokens → skill/) · build-css.mjs (tokens → CSS сайту)
CLAUDE.md  правила роботи для Claude Code
```

## Команди

```bash
python3 tools/build-skill.py      # оновити skill/ після зміни в tokens/
cd site && npm install
npm run dev                       # сайт локально: http://localhost:5173
npm run build                     # production у site/dist
```

`skill/` і згенеровані файли сайту вручну не редагувати — правити `tokens/` і перегенерувати.
Пуш у `main` з правками в `site/`, `tokens/` або `tools/` сам оновлює демо на GitHub Pages.
