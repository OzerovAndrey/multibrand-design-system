#!/usr/bin/env python3
"""
Multibrand Design System — генератор документації токенів.

Читає Token Studio JSON (tokens/*.json, $themes.json, $metadata.json)
і пише skill-подібні записи в skill/:
  SKILL.md                      індекс: шари, сети, теми, правила, карта файлів
  references/core.md            примітиви
  references/brand.md           3 бренди поруч
  references/map.md             рампи
  references/theme.md           light / dark поруч
  references/typography.md      text styles
  references/components/<c>.md  по файлу на компонент

Запуск:  python3 tools/build-skill.py [tokens_dir] [out_dir]
За замовчуванням: tokens/  →  skill/
Ручні частини (мапінг text styles, анатомія) — у COMPONENT_NOTES нижче.
"""
import json, re, sys, os, datetime
from collections import OrderedDict

TOK = sys.argv[1] if len(sys.argv) > 1 else "tokens"
OUT = sys.argv[2] if len(sys.argv) > 2 else "skill"
BRANDS = ["aurum", "nova", "fiesta", "ultra"]
MODES = ["light", "dark"]

# ---------------------------------------------------------------- ручні нотатки
COMPONENT_NOTES = {
    "button": {
        "title": "Button",
        "figma": "Button (component set) · Variant × Size × State × Label",
        "anatomy": "Контейнер (auto-layout H) → `Icon left` (instance) · `Label` (text) · `Icon right` (instance). "
                   "Icon-only варіант = `Label=False`.",
        "variants": "Variant: Primary / Secondary / Text · Size: xs–xl · State: Default / Hover / Active / Disabled",
        "text_styles": [("xs", "label/sm"), ("sm", "label/md"), ("md", "label/md"), ("lg", "label/lg"), ("xl", "label/xl")],
        "notes": [
            "Власних typography-токенів немає — текст бере text style зі шкали.",
            "Іконки за замовчуванням: left `plus`, right `chevron-right` (Static — Icons).",
        ],
    },
    "input": {
        "title": "Input",
        "figma": "Input (component set) · Size × State",
        "anatomy": "Wrapper (auto-layout V, gap `input.wrapper.gap`) → `Label` (text) · `Field` (auto-layout H) · `Helper` (text). "
                   "Field → `Icon left` · `Placeholder` · `Value` · `Icon right`.",
        "variants": "Size: sm / md / lg · State: Default / Hover / Active / Disabled (focus не робимо)",
        "text_styles": [("sm", "value/placeholder body/sm/regular · label label/sm · helper caption/md"),
                        ("md", "value/placeholder body/md/regular · label label/md · helper caption/md"),
                        ("lg", "value/placeholder body/lg/regular · label label/md · helper caption/md")],
        "notes": [
            "Placeholder і Value фарбуються одним токеном `input.color.*` — окремого `placeholder.color` немає.",
            "Властивості: ✏️ Label / Placeholder / Value / Helper · booleans Label, Helper, Placeholder, Value, ⬅️ Icon, Icon ➡️ · swap 💠 Icon left / right.",
            "Іконки за замовчуванням: left `search`, right `close` (Static — Icons).",
            "Висоти sm/md/lg = Button sm/md/lg (32/40/48) — стають в один ряд.",
        ],
    },
    "card": {
        "title": "Card Default",
        "figma": "Card Default (component set) · Size",
        "anatomy": "Контейнер (auto-layout V, padding `card.default.paddingH/V.{size}`, gap `card.default.gap.{size}`) → "
                   "`Slot 1` · `Slot 2` · `Slot 3` (інстанси `_Card slot`).",
        "variants": "Size: xs (mobile) / sm (tablet) / md (desktop). Станів немає — статичний контейнер",
        "notes": [
            "Власного контенту немає — вміст підставляється через instance swap 💠 Slot 1–3; Slot 2 і Slot 3 вмикаються булеанами.",
            "Ширина в сеті — референс (320 / 400 / 480); у макеті картка тягнеться (Fill) по колонці сітки.",
            "Padding: xs 12 · sm 16 · md 24; gap: xs 8 · sm 10 · md 12 — з існуючої брендової шкали `space.*`.",
        ],
    },
    "media": {
        "title": "Media",
        "figma": "Media (component set) · Ratio × State",
        "anatomy": "Контейнер (fill `media.bg`, radius `media.borderRadius`, clip) → `image` (rectangle, image fill) · `overlay` (`media.overlay.bg`) · "
                   "`icon` (fallback, `media.fallback.iconSize`) · `Content` (slot, padding `media.padding`, gap `media.gap`).",
        "variants": "Ratio: 1:1 / 4:3 / 16:9 / 3:4 · State: Loaded / Loading / Error",
        "notes": [
            "Медіа-примітив: зображення з брендовим радіусом і станами завантаження; основа для Thumb, PromoCard, банерів.",
            "Loading — фон `media.skeleton.bg`; Error — іконка `placeholder-default` кольору `media.fallback.iconColor`.",
            "Властивості: boolean Overlay · swap 💠 Fallback icon · slot Content (бейджі, кнопки).",
            "Ratio — фіксовані пропорції; у макеті Fill по ширині, висота за пропорцією. Картинка міняється заливкою шару image.",
        ],
    },
    "header": {
        "title": "Header",
        "figma": "Header (component set) · Size × State  ·  частини: Logo (component set · Brand × Type), Balance (component set · Size)",
        "anatomy": "Контейнер (auto-layout H, space-between, padding `header.paddingH/V.{size}`, нижній бордер `header.br` × `header.borderWidth`) → "
                   "`Logo` (instance) · `Actions` (auto-layout H, gap `header.gap`) → `Tools` (gap `header.actions.gap`: Search · Support) · `Balance`.",
        "variants": "Size: xs (mobile 360) / md (desktop, від sm 768 і ширше — Fill) · State: Logged in / Search open / Logged out",
        "notes": [
            "Організм: збирається з Button, Input, Logo і Balance — власних кольорів у контролах немає, тільки контейнер і лого.",
            "md · Logged in: Search і Support = Button Secondary md icon-only (`search`, `support`), далі Balance md.",
            "md · Search open: замість кнопки пошуку — Input md State=Active, Label off, іконки `search` / `close`, ширина 320.",
            "md · Logged out: Log in (Button Secondary md) і Sign up (Button Primary md).",
            "xs: Logo Type=Mark, контроли sm (32), Support прихований (іде в меню / TabBar), Balance Size=sm. Search open — Input sm Fill на місці лого.",
            "Висота не токен: md 72 = `header.paddingV.md` 16 × 2 + control md 40; xs 56 = `header.paddingV.xs` 12 × 2 + control sm 32.",
            "Logo — asset, не токен: Brand-варіант (Aurum / Nova / Fiesta / Ultra) обирається разом із Brand-mode; Type=Full / Mark. Кольори — `header.logo.iconColor` (марка) і `header.logo.color` (wordmark).",
            "Logo, Balance, Search, Support, Log in, Sign up — exposed instances.",
        ],
    },
    "balance": {
        "title": "Balance",
        "figma": "Balance (component set) · Size — молекула всередині Header",
        "anatomy": "Контейнер (auto-layout H, bg `balance.bg`, radius `balance.borderRadius`, paddingL `balance.paddingL.{size}`, paddingR 0, gap `balance.gap.{size}`) → "
                   "`Icon` (instance `wallet`, `balance.iconSize.{size}`, `balance.iconColor`) · `Amount` (text) · `Deposit` (Button Primary).",
        "variants": "Size: sm (Deposit = Button Primary sm icon-only `plus`) / md (Button Primary md «Deposit»). Властивості: ✏️ Amount · 💰 Icon · 💠 Icon",
        "text_styles": [("Amount", "label/md")],
        "notes": [
            "Висота = висота кнопки Deposit (sm 32 / md 40): контейнер hug, кнопка впритул праворуч.",
            "Deposit — exposed instance Button.",
        ],
    },
    "footer": {
        "title": "Footer",
        "figma": "Footer (component set) · Size  ·  частини: _Footer badge, _Footer age",
        "anatomy": "Контейнер (auto-layout V, padding `footer.paddingH/V.{size}`, gap `footer.gap.{size}`, верхній бордер) → "
                   "`Top` (md — H, xs/sm — V) → `About` (Logo · Tagline · Social) · `Links` (4 колонки, gap `footer.links.gap.{size}`) → "
                   "`Divider` → `Payments` (Title · Methods з _Footer badge) → `Divider` → `Bottom` (Legal: _Footer age · Disclaimer · © | Language).",
        "variants": "Size: xs (mobile 360) / sm (tablet 768) / md (desktop, Fill для md 1024 · lg 1200 · xl 1440)",
        "text_styles": [("Title колонки / Payments", "label/md"), ("Посилання, Tagline", "body/sm/regular"), ("Disclaimer, ©", "caption/md"),
                        ("_Footer badge", "label/sm"), ("_Footer age", "label/xs")],
        "notes": [
            "Колонки: Casino · Promotions · Help · Company. md — About фіксовано 320 + колонки Fill; sm — About над колонками; xs — колонки 2×2 (wrap, ширина 156).",
            "Social = Button Secondary sm icon-only: telegram · instagram · facebook · youtube · tiktok (Static — Icons).",
            "Payment methods — бейджі `_Footer badge` (💠 Icon + ✏️ Label): Cards `card-send` · Bank transfer `money-send` · E-wallets `wallet` · Crypto `coin`. Ряд з wrap.",
            "Language = Button Secondary sm з іконками `translate` / `chevron-down`.",
            "Поля й відступи прив'язані до сітки сторінки (`layout.paddingH.*`, `layout.rowGap.*`, `layout.columnGap.*`) — футер вирівняний з контентом.",
            "Фон `color.bg.primary` (як Header), щоб Secondary-кнопки і бейджі (`fill.secondary`) були видимі в обох темах.",
            "Logo і Language — exposed instances.",
        ],
    },
}

COMPONENT_NOTES.update({
    "badge": {
        "title": "Badge",
        "figma": "Badge (component set) · Tone",
        "anatomy": "Контейнер (auto-layout H, height `badge.size`) → `Icon` (instance, вимкнена за замовчуванням) · `Label` (text).",
        "variants": "Tone: Neutral / Primary / Accent / Success / Warning / Danger / Info. Стани відсутні — статична мітка",
        "text_styles": [("label", "label/xs")],
        "notes": [
            "Тони мапляться на теми: Primary = product1, Accent = product2, Info = product3 — змінюються разом із брендом.",
            "Рідкість лутбоксів: Common = Neutral, Rare = Info, Epic = Accent, Legendary = Primary.",
            "Властивості: ✏️ Label · Icon (boolean) · 💠 Icon (swap, за замовчуванням `star-filled`).",
        ],
    },
    "chip": {
        "title": "Chip",
        "figma": "Chip (component set) · Selected × State × Size",
        "anatomy": "Контейнер (auto-layout H, pill/м'який/гострий від бренду) → `Icon` (instance) · `Label` (text).",
        "variants": "Selected: False / True · State: Default / Hover / Active / Disabled · Size: sm (32) / md (40)",
        "text_styles": [("sm", "label/sm"), ("md", "label/md")],
        "notes": [
            "Фільтр категорій (Slots / Live / Jackpots). Selected Hover/Active — суцільний primary з `text.onPrimary`.",
            "Товщина контуру береться з `borderWidth.control` — у Fiesta 2, в інших 1.",
            "Властивості: ✏️ Label · Icon (boolean) · 💠 Icon (swap, за замовчуванням `game-casino`).",
        ],
    },
    "tab": {
        "title": "Tab",
        "figma": "Tab (component set) · Selected × State × Size",
        "anatomy": "Контейнер (auto-layout H) → `Icon` · `Label` · `Indicator` (absolute, знизу, вмикається при Selected).",
        "variants": "Selected: False / True · State: Default / Hover / Active / Disabled · Size: sm (40) / md (48)",
        "text_styles": [("sm", "label/sm"), ("md", "label/md")],
        "notes": [
            "Ряд вкладок збирається вручну в auto-layout; нижня лінія-трек — `tab.track.br` / `tab.track.borderWidth`.",
            "Форма індикатора від бренду: pill (Fiesta), м'який (Aurum), гострий (Nova).",
        ],
    },
    "avatar": {
        "title": "Avatar",
        "figma": "Avatar (component set) · Size × Type",
        "anatomy": "Контейнер (фіксований квадрат `avatar.size.{size}`) → `Initials` (text) або `Icon` · `VIP ring` (absolute) · `Status` (absolute, нижній правий кут).",
        "variants": "Size: xs–xl (24–56) · Type: Initials / Icon. Booleans: VIP, Status",
        "text_styles": [("xs", "label/xs"), ("sm", "label/sm"), ("md", "label/md"), ("lg", "label/lg"), ("xl", "label/xl")],
        "notes": [
            "Форма від `borderRadius.control`: Aurum — м'який квадрат, Nova — гострий, Fiesta — коло.",
            "Фото — заливка Image поверх контейнера; ✏️ Initials і 💠 Icon — властивості інстансу.",
        ],
    },
    "progress": {
        "title": "Progress",
        "figma": "Progress (component set) · Size × Tone × Value",
        "anatomy": "Вертикальний auto-layout → `Header` (Label + Value, boolean) · `Track` (frame) → `Fill` (масштабується разом із треком).",
        "variants": "Size: sm (6) / md (8) · Tone: Primary / Success / Accent · Value: 0 / 25 / 50 / 75 / 100",
        "text_styles": [("label", "caption/md"), ("value", "label/sm")],
        "notes": [
            "XP-рівень (Primary), wagering (Success), призовий фонд турніру (Accent).",
            "Проміжні значення — змінити ширину `Fill` в інстансі.",
        ],
    },
    "checkbox": {
        "title": "Checkbox",
        "figma": "Checkbox (component set) · Checked × State",
        "anatomy": "Контейнер (auto-layout H) → `Box` (frame, іконка `check-mark` при Checked) · `Label` (text).",
        "variants": "Checked: False / True · State: Default / Hover / Active / Disabled",
        "text_styles": [("label", "body/md/regular")],
        "notes": [
            "Форма боксу від `borderRadius.control` — у Nova квадрат, у Fiesta коло.",
            "Властивості: ✏️ Label · Show label (boolean).",
        ],
    },
    "switch": {
        "title": "Switch",
        "figma": "Switch (component set) · On × State",
        "anatomy": "Контейнер (auto-layout H) → `Track` (auto-layout, knob вирівнюється вліво/вправо) → `Knob` · `Label` (text).",
        "variants": "On: False / True · State: Default / Hover / Disabled",
        "text_styles": [("label", "body/md/regular")],
        "notes": [
            "Track і knob беруть `borderRadius.control` — у Nova перемикач прямокутний, у Fiesta капсула.",
            "Властивості: ✏️ Label · Show label (boolean).",
        ],
    },
})

COMPONENT_NOTES.update({
    "sectionHeader": {
        "title": "Section Heading",
        "figma": "Section Heading (component set) · Size",
        "anatomy": "Контейнер (auto-layout H, space-between) → `Title group` (`Icon` · `Text`: Title + Subtitle) · `Actions` (`See all` = Button Text sm · `Arrows` = 2 × Button Secondary sm icon-only).",
        "variants": "Size: xs (mobile 328) / md (desktop 720). Booleans: Icon, Subtitle, See all, Arrows",
        "text_styles": [("xs", "title/t4"), ("md", "title/t2"), ("subtitle", "body/sm/regular")],
        "notes": ["Заголовок — display-шрифт бренду; ✏️ Title · ✏️ Subtitle · 💠 Icon (swap, `flame-filled`)."],
    },
    "stat": {
        "title": "Stat Tile",
        "figma": "Stat Tile (component set) · Size × Trend",
        "anatomy": "Картка (auto-layout V) → `Header` (`Icon box` + Label) · `Value` · `Delta`.",
        "variants": "Size: xs (160) / md (260) · Trend: Neutral / Up / Down (колір delta)",
        "text_styles": [("label", "label/sm"), ("value xs", "title/t4"), ("value md", "title/t3"), ("delta", "label/sm")],
        "notes": ["Властивості: ✏️ Label · ✏️ Value · Delta (boolean) · Icon (boolean) · 💠 Icon (swap, `wallet`). Текст delta — у кожного Trend свій."],
    },
    "listItem": {
        "title": "List Item",
        "figma": "List Item (component set) · State",
        "anatomy": "Рядок (auto-layout H, ghost-фон) → `Icon box` · `Text` (Title + Subtitle) · `Value` · `Chevron` · `Divider` (absolute).",
        "variants": "State: Default / Hover / Active / Disabled",
        "text_styles": [("title", "label/md"), ("subtitle", "caption/md"), ("value", "body/sm/regular")],
        "notes": ["Меню профілю/налаштувань. Booleans: Icon, Subtitle, Value, Chevron, Divider · 💠 Icon (swap)."],
    },
    "alert": {
        "title": "Alert",
        "figma": "Alert (component set) · Tone",
        "anatomy": "Контейнер (auto-layout H) → `Icon` · `Text` (Title + Message) · `Close`.",
        "variants": "Tone: Info / Success / Warning / Danger",
        "text_styles": [("title", "label/md"), ("message", "body/sm/regular")],
        "notes": ["Booleans: Show title, Dismissible. Іконка тону — статична (info / check-mark-circle-filled / warning-filled / close-circle-filled)."],
    },
    "leaderRow": {
        "title": "Leaderboard Row",
        "figma": "Leaderboard Row (component set) · Rank × You",
        "anatomy": "Рядок (auto-layout H) → `Rank` (число) · `Avatar` (instance) · `Player` (Name + Sub) · `Result` (Score + Prize).",
        "variants": "Rank: 1 / 2 / 3 / Other · You: False / True (підсвітка поточного гравця)",
        "text_styles": [("rank", "label/sm"), ("name", "label/md"), ("sub", "caption/md"), ("score", "label/md"), ("prize", "label/sm")],
        "notes": ["Ранг 1–3 — акцентні кольори (product1 / neutral / product2), далі нейтральний. ✏️ Name · Sub · Score · Prize; Prize (boolean)."],
    },
    "navItem": {
        "title": "Nav Item",
        "figma": "Nav Item (component set) · Selected",
        "anatomy": "Вертикальний auto-layout → `Pill` (фон при Selected) з `Icon` · `Dot` (absolute) · `Label`.",
        "variants": "Selected: False / True",
        "text_styles": [("label", "caption/sm")],
        "notes": ["Складова Bottom Nav. ✏️ Label · 💠 Icon (swap) · Dot (boolean)."],
    },
    "bottomNav": {
        "title": "Bottom Nav",
        "figma": "Bottom Nav (component set) · Active",
        "anatomy": "Контейнер (auto-layout H, верхній бордер) → 5 × Nav Item: Home · Games · Tournaments · Shop · Profile.",
        "variants": "Active: Home / Games / Tournaments / Shop / Profile",
        "notes": ["Мобільна навігація лобі (xs 360)."],
    },
    "art": {
        "title": "Game Art",
        "figma": "Game Art (component set) · Pattern",
        "anatomy": "Фрейм 240×320 (clip) → `Shape 1` (велике коло, правий нижній кут) · `Shape 2` (мале коло, лівий верхній) · `Shape 3` (скошена смуга).",
        "variants": "Pattern: a–f",
        "notes": [
            "Абстрактні плейсхолдери замість зображень: кольори беруться з теми/бренду, тому арт міняє палітру при перемиканні.",
            "Використовується як 💠 Art у Game Tile, Promo Banner, Tournament Card. Замінюється фото заливкою.",
        ],
    },
    "gameTile": {
        "title": "Game Tile",
        "figma": "Game Tile (component set) · Type × State",
        "anatomy": "Вертикальний auto-layout → `Cover` (clip; `Art` · `Hover overlay` · `Play` · `Top row`: Badge + Favorite · для Live `Bottom row`: Players) · `Info` (Title + Provider).",
        "variants": "Type: Slot (3:4, 176×235) / Live (16:9, 320×180) · State: Default / Hover (overlay + Play)",
        "text_styles": [("title", "label/md"), ("provider", "caption/md"), ("players", "label/sm")],
        "notes": ["✏️ Title · ✏️ Provider · Favorite · Badge (boolean, swap тону: NEW / HOT / LIVE) · 💠 Art (swap патерна або фото). Форма Play — від `borderRadius.surface` бренду."],
    },
    "promo": {
        "title": "Promo Banner",
        "figma": "Promo Banner (component set) · Size",
        "anatomy": "Контейнер (clip) → `Art` (absolute, фон) · `Content` (панель `promo.overlay.bg`: Eyebrow Badge · Title · Text · Actions: Primary + Secondary).",
        "variants": "Size: xs (mobile 328×420, контент знизу) / md (desktop 1000×360, панель зліва)",
        "text_styles": [("title xs", "title/t2"), ("title md", "display/d3"), ("text xs", "body/md/regular"), ("text md", "body/lg/regular")],
        "notes": ["Hero лобі. ✏️ Title · ✏️ Text · Eyebrow, Secondary action (boolean) · 💠 Art."],
    },
    "tournament": {
        "title": "Tournament Card",
        "figma": "Tournament Card (component set) · State",
        "anatomy": "Картка (V, clip) → `Cover` (`Art` + статус-`Badge`) · `Body` (Title · Prize pool · Meta: Players/Time · Progress · CTA).",
        "variants": "State: Live (CTA Join now) / Upcoming (Remind me) / Finished (View results)",
        "text_styles": [("title", "title/t4"), ("prize", "title/t2"), ("meta", "body/sm/regular")],
        "notes": ["Призовий фонд — `tournament.prize.color` (accent). ✏️ Title · ✏️ Prize · Progress (boolean) · 💠 Art."],
    },
    "lootbox": {
        "title": "Lootbox Card",
        "figma": "Lootbox Card (component set) · Rarity × State",
        "anatomy": "Картка (V, clip) → `Art` (фон рідкості, `Halo`, `Icon`, `Rarity strip`, Badge) · `Info` (Title + Description) · `Purchase` (Price + Buy).",
        "variants": "Rarity: Common / Rare / Epic / Legendary · State: Default / Hover (контур accent)",
        "text_styles": [("title", "title/t4"), ("description", "body/sm/regular"), ("price", "label/lg")],
        "notes": ["Рідкість мапиться на neutral / info(product3) / accent(product2) / primary(product1) — кольори міняються з брендом. ✏️ Title · Description · Price · Rarity badge (boolean)."],
    },
    "modal": {
        "title": "Modal",
        "figma": "Modal (component set) · Size",
        "anatomy": "Контейнер (V, clip) → `Handle` (тільки xs) · `Header` (Title + Close) · `Content` (slot) · `Actions`.",
        "variants": "Size: xs (bottom sheet 360, лише верхні кути) / md (діалог 480)",
        "text_styles": [("title", "title/t3"), ("text", "body/md/regular")],
        "notes": ["Scrim — `modal.overlay.bg` (окремий шар під модалкою). ✏️ Title · Secondary action (boolean) · slot Content."],
    },
})

# ---------------------------------------------------------------- завантаження
def load(p):
    with open(os.path.join(TOK, p), encoding="utf-8") as f:
        return json.load(f, object_pairs_hook=OrderedDict)

def flat(d, p=""):
    out = OrderedDict()
    for k, v in d.items():
        if isinstance(v, dict) and "value" in v and "type" in v:
            out[p + k] = v
        elif isinstance(v, dict):
            out.update(flat(v, p + k + "."))
    return out

meta = load("$metadata.json")
themes = load("$themes.json")
SETS = OrderedDict((s, flat(load(s + ".json"))) for s in meta["tokenSetOrder"])

REF = re.compile(r"\{([^}]+)\}")
MAP_FLAT = len({v["value"] for k, v in SETS.get("map", {}).items() if k.startswith("color.product1.")}) <= 1

def pool(brand="aurum", mode="light"):
    p = OrderedDict()
    for s in ["core", f"brand/{brand}", "map", f"theme/{mode}", "typography", "components"]:
        p.update(SETS.get(s, {}))
    return p

def resolve(val, pl, depth=0):
    if depth > 20:
        return "⟳"
    if isinstance(val, dict):
        return {k: resolve(v, pl, depth + 1) for k, v in val.items()}
    s = str(val)
    m = REF.fullmatch(s)
    if m:
        t = pl.get(m.group(1))
        return resolve(t["value"], pl, depth + 1) if t else f"⚠ {m.group(1)}"
    return REF.sub(lambda m: str(resolve("{" + m.group(1) + "}", pl, depth + 1)), s)

def fmt(v):
    if isinstance(v, dict):
        return " · ".join(f"{k}: {v[k]}" for k in v)
    return str(v)

def code(v):
    return f"`{v}`"

def figma_name(path):
    return path.replace(".", "/")

def swatch(v):
    s = str(v)
    return f"`{s}`"

def count_refs(set_name):
    """скільки токенів сету посилаються на інші (а не мають сирих значень)"""
    t = SETS[set_name]
    return sum(1 for v in t.values() if REF.search(json.dumps(v["value"])))

def group_of(path):
    return path.split(".")[0]

def table(rows, head):
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    for r in rows:
        out.append("| " + " | ".join(str(c).replace("|", "\\|") for c in r) + " |")
    return "\n".join(out)

def write(rel, text):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.rstrip() + "\n")

TODAY = datetime.date.today().isoformat()
HEADER = f"> Згенеровано `tools/build-skill.py` з Token Studio JSON · {TODAY}. Не редагувати вручну — правити JSON і перегенерувати.\n"

# ---------------------------------------------------------------- core
def doc_core():
    t = SETS["core"]
    parts = [f"# Core — примітиви\n", HEADER,
             "Словник сирих значень. **Ніколи не прив'язується до шару в Figma** — на core посилаються brand/map/theme/typography.",
             f"Figma: колекція **Base** (mode Default). Токенів: **{len(t)}**.\n"]
    groups = OrderedDict()
    for k, v in t.items():
        groups.setdefault(group_of(k), []).append((k, v))
    for g, items in groups.items():
        parts.append(f"## {g}\n")
        parts.append(table([(code(k), v["type"], code(fmt(v["value"])), figma_name(k)) for k, v in items],
                           ["Токен", "Тип", "Значення", "Figma variable"]))
        parts.append("")
    write("references/core.md", "\n".join(parts))

# ---------------------------------------------------------------- brand
def doc_brand():
    b = {x: SETS[f"brand/{x}"] for x in BRANDS}
    keys = list(b["aurum"].keys())
    parts = ["# Brand — Aurum / Nova / Fiesta / Ultra\n", HEADER,
             "Бренд = набір значень. Ключі в усіх файлах брендів **ідентичні**, різняться лише значення.",
             "Figma: колекція **Brand** (modes Aurum / Nova / Fiesta / Ultra). Разом із брендом у цю колекцію потрапляє `map` (enabled у темах Brand).",
             f"Токенів у бренді: **{len(keys)}**.\n",
             "Що живе в бренді:",
             "- **Кольори** — одиничні базові (`product1–3`, `onProduct1/2`, `success`, `warning`, `danger`, `ink`). Без рамп: відтінки — у `map`.",
             "- **Шрифти** — `fontFamily.display` (display/title), `fontFamily.base` (решта тексту).",
             "- **Розмірна семантика** — `space.padding.*`, `space.gap.*`, `size.control.*`, `iconSize.*`, `borderRadius.control|surface`, `borderWidth.none|control`. "
             "Живе в бренді, а не в темі: бренд може мати інші радіуси/щільність, тема (light/dark) міняє тільки кольори.",
             "- **Сітка сторінки** — `layout.columns.*` (кількість колонок), `layout.columnGap.*` (gutter), `layout.paddingH.*` (поля), `layout.rowGap.*` (відстань між секціями) по брейкпоінтах "
             "xs 360 · sm 768 · md 1024 · lg 1200 · xl 1440. У Figma прив'язані до Layout grid фреймів сторінок; організми (Footer) беруть поля й відступи звідси.\n"]
    groups = OrderedDict()
    for k in keys:
        g = k.split(".")[0] if not k.startswith(("space.", "layout.")) else ".".join(k.split(".")[:2])
        groups.setdefault(g, []).append(k)
    for g, ks in groups.items():
        parts.append(f"## {g}\n")
        rows = []
        for k in ks:
            vals = []
            for x in BRANDS:
                raw = b[x][k]["value"]
                res = resolve(raw, pool(x))
                vals.append(code(raw) + ("" if str(res) == str(raw) else f" → `{res}`"))
            rows.append([code(k), b["aurum"][k]["type"]] + vals)
        parts.append(table(rows, ["Токен", "Тип"] + [x.capitalize() for x in BRANDS]))
        parts.append("")
    write("references/brand.md", "\n".join(parts))

# ---------------------------------------------------------------- map
def doc_map():
    t = SETS["map"]
    parts = ["# Map — рампи\n", HEADER,
             "Міст між брендом і темою: кроки `100…900` (і `neutral.0…900`) для кожного базового кольору бренду.",
             "Figma: колекція **Brand** (map enabled у темах Brand).",
             f"Токенів: **{len(t)}**.\n",
             "> ⚠ Зараз кожен крок рампи посилається на **той самий** базовий колір бренду (`color.product1.100…900 → {color.product1}`). "
             "Hover / Active / фони / бордери візуально не розрізняються, доки кроки не отримають власних значень.\n"]
    groups = OrderedDict()
    for k, v in t.items():
        groups.setdefault(".".join(k.split(".")[:2]), []).append((k, v))
    rows = []
    for g, items in groups.items():
        steps = ", ".join(k.split(".")[-1] for k, _ in items)
        refs = sorted(set(v["value"] for _, v in items))
        rows.append([code(g), steps, ", ".join(code(r) for r in refs)])
    parts.append(table(rows, ["Група", "Кроки", "Посилається на"]))
    write("references/map.md", "\n".join(parts))

# ---------------------------------------------------------------- theme
def doc_theme():
    L, D = SETS["theme/light"], SETS["theme/dark"]
    parts = ["# Theme — Light / Dark\n", HEADER,
             "Семантика кольорів. Тут калькулюється логіка тем: той самий ключ у light і dark дивиться в різні кроки `map`.",
             "Figma: колекція **Theme** (modes Light / Dark). **Тільки кольори** — розміри живуть у бренді.",
             f"Токенів: **{len(L)}** (ключі light і dark ідентичні).\n",
             "Колонки «Aurum» — значення, до якого резолвиться токен у бренді Aurum.\n"]
    groups = OrderedDict()
    for k in L:
        groups.setdefault(".".join(k.split(".")[:2]), []).append(k)
    for g, ks in groups.items():
        parts.append(f"## {g}\n")
        rows = []
        for k in ks:
            lv, dv = L[k]["value"], D[k]["value"]
            rows.append([code(k), code(lv), swatch(resolve(lv, pool("aurum", "light"))),
                         code(dv), swatch(resolve(dv, pool("aurum", "dark")))])
        parts.append(table(rows, ["Токен", "Light", "Aurum light", "Dark", "Aurum dark"]))
        parts.append("")
    write("references/theme.md", "\n".join(parts))

# ---------------------------------------------------------------- typography
def doc_typography():
    t = SETS["typography"]
    tr = lambda r: str(r).strip("{}").split(".")[-1]
    parts = ["# Typography — text styles\n", HEADER,
             "Окремий шар. Сет `typography` → тема **Typography / Default** → Figma **text styles** `typography/…`.",
             "Компоненти **не мають** власних typography-токенів: текстовий шар бере стиль зі шкали. Той самий набір — для вільного тексту.",
             f"Стилів: **{len(t)}**.\n",
             "Експорт: Styles & Variables → Export styles → тільки тема Typography/Default, галочка Typography, "
             "**Create styles with variable references** (fontFamily/fontSize/lineHeight/fontWeight прив'язані до змінних → шрифт перемикається з брендом).\n"]
    rows = []
    for k, v in t.items():
        val = v["value"]
        pl = pool("aurum")
        r = lambda f: resolve(val.get(f, ""), pl)
        rows.append([code(k.replace("typography.", "")), figma_name(k), tr(val.get("fontFamily")),
                     f'{r("fontSize")}/{r("lineHeight")}', r("fontWeight"), r("letterSpacing"),
                     r("textCase"), v.get("description", "")])
    parts.append(table(rows, ["Стиль", "Figma", "Family", "Size/LH", "Weight", "LS", "Case", "Для чого"]))
    parts.append("\nFamily: `display` → `fontFamily.display`, `base` → `fontFamily.base` (значення — у brand.md).")
    write("references/typography.md", "\n".join(parts))

# ---------------------------------------------------------------- components
def doc_components():
    t = SETS["components"]
    comps = OrderedDict()
    for k, v in t.items():
        comps.setdefault(group_of(k), OrderedDict())[k] = v
    for c, toks in comps.items():
        n = COMPONENT_NOTES.get(c, {})
        parts = [f"# {n.get('title', c.capitalize())}\n", HEADER]
        if n:
            parts += [f"**Figma:** {n['figma']}  ", f"**Варіанти:** {n['variants']}  ",
                      f"**Анатомія:** {n['anatomy']}\n"]
        parts.append(f"Токенів: **{len(toks)}**. Посилаються тільки на theme / brand-семантику, не на core.\n")
        colors = [(k, v) for k, v in toks.items() if v["type"] == "color"]
        other = [(k, v) for k, v in toks.items() if v["type"] != "color"]
        if colors:
            parts.append("## Кольори\n")
            if MAP_FLAT:
                parts.append("> Рампи в `map` зараз — заглушки (усі кроки = базовий колір), тому колонки Aurum показують базові кольори бренду. Посилання (→ Alias) — остаточні.\n")
            rows = [[code(k), figma_name(k), code(v["value"]),
                     swatch(resolve(v["value"], pool("aurum", "light"))),
                     swatch(resolve(v["value"], pool("aurum", "dark")))] for k, v in colors]
            parts.append(table(rows, ["Токен", "Figma variable", "→ Alias", "Aurum light", "Aurum dark"]))
            parts.append("")
        if other:
            parts.append("## Розміри та форма\n")
            rows = [[code(k), figma_name(k), v["type"], code(v["value"]),
                     code(resolve(v["value"], pool("aurum")))] for k, v in other]
            parts.append(table(rows, ["Токен", "Figma variable", "Тип", "→ Alias", "Значення"]))
            parts.append("")
        if n.get("text_styles"):
            parts.append("## Текст (text styles, не токени)\n")
            parts.append(table([(code(s), st) for s, st in n["text_styles"]], ["Розмір", "Стиль"]))
            parts.append("")
        if n.get("notes"):
            parts.append("## Нотатки\n")
            parts += [f"- {x}" for x in n["notes"]]
        write(f"references/components/{c}.md", "\n".join(parts))
    return comps

# ---------------------------------------------------------------- index
def doc_index(comps):
    th_rows = []
    for t in themes:
        sel = ", ".join(f"{s}{'' if st == 'enabled' else ' (source)'}" for s, st in t["selectedTokenSets"].items())
        out = "text styles" if t["group"] == "Typography" else "variables"
        th_rows.append([t["group"], t["name"], sel, out])
    set_rows = [[code(s), len(SETS[s]), desc] for s, desc in [
        ("core", "примітиви: dimension, borderRadius, borderWidth, fontWeight, fontSize, lineHeight, letterSpacing, textCase, color.white/black/transparent"),
        ("brand/aurum", "кольори бренду, шрифти, розмірна семантика, сітка сторінки (layout)"),
        ("brand/nova", "ті самі ключі, інші значення"),
        ("brand/fiesta", "ті самі ключі, інші значення"),
        ("brand/ultra", "ті самі ключі, інші значення"),
        ("map", "рампи 100…900 від базових кольорів бренду"),
        ("theme/light", "семантика кольорів: bg, fill, text, border, outline"),
        ("theme/dark", "ті самі ключі, інші кроки рампи"),
        ("typography", "text styles"),
        ("components", "усі компонентні токени в одному сеті"),
    ] if s in SETS]
    comp_rows = [[f"[{COMPONENT_NOTES.get(c, {}).get('title', c)}](references/components/{c}.md)", len(v)] for c, v in comps.items()]
    total = sum(len(v) for v in SETS.values())
    text = f"""---
name: multibrand-design-system
description: Реєстр токенів Multibrand Design System (репо multibrand-design-system; бренди Aurum / Nova / Fiesta / Ultra) — усі сети Token Studio (core, brand/aurum|nova|fiesta|ultra, map, theme/light|dark, typography, components), їхні значення, посилання й Figma-змінні. Use ANY TIME the user works with tokens of the Multibrand Design System — adding a component's tokens, binding variables in Figma, checking what a token resolves to, adding a brand, or asking "який токен для…". INDEX — деталі в references/*.md, вантажити тільки потрібний файл. Генерується з JSON скриптом tools/build-skill.py.
---

# Multibrand Design System — токени (індекс)

{HEADER}
Джерело правди — Token Studio JSON у `tokens/`. Figma Variables і text styles — синхронізована копія.
Усього токенів: **{total}**.

## Мета й ідеологія

**Кінцевий результат** — живий сайт-демо на власному домені: клієнт перемикає бренд (Aurum / Nova / Fiesta / Ultra) і тему (Light / Dark), і весь iGaming-інтерфейс перебудовується миттєво, а компоненти й розмітка не змінюються. Ця система — доказ, що один набір токенів керує цілим продуктом.

1. **Перемикання — головний продукт.** Кожен компонент і сторінка мають виглядати добре й змінюватись у всіх 8 комбінаціях (4 бренди × Light/Dark). Не змінилось або зламалось — це помилка архітектури, а не токенів.
2. **Компонент не знає про бренд і тему.** Лише токени; жодного hex, px чи шрифту напряму.
3. **Бренди відрізняються характером, а не тільки кольором:** колір + шрифт + радіуси + товщина бордера. Aurum — тепла преміум-класика, м'які кути. Nova — холодний tech, гострі кути. Fiesta — яскравий mass-market, pill-форми, товстіші контури. Ultra — нічний neon-казино: navy + hot pink + cyan, широкий display-гротеск, кути 12, контур 2.
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

{table(set_rows, ["Сет", "Токенів", "Що всередині"])}

## Теми → Figma

{table(th_rows, ["Група (колекція)", "Mode", "Сети", "Що створює"])}

Експорт: **Variables** — теми Base, Brand, Theme, Components (Typography не вибирати). **Styles** — тільки Typography/Default з «Create styles with variable references».

## Правила

1. Ім'я токена = CSS-властивість: `bg`, `color`, `br`, `iconColor`, `size`, `paddingH/V`, `gap`, `iconSize`, `borderRadius`, `borderWidth`. Формат `компонент.[підчастина].[варіант].властивість.[стан|розмір]`; стан/розмір — завжди останній.
2. Компонент посилається тільки на theme / brand-семантику (`color.*`, `space.*`, `layout.*`, `size.control.*`, `iconSize.*`, `borderRadius.*`, `borderWidth.*`). Ніколи на core і ніколи на `map` напряму.
3. Компонент не має typography-токенів — текстовий шар отримує text style (`typography/…`).
4. Ключі всіх брендів ідентичні; ключі light і dark ідентичні.
5. Бренд = тільки значення. Нові ключі в бренді — лише якщо їх додано в усі три.
6. Розміри й радіуси — у бренді, не в темі. Тема міняє лише кольори.
7. Стани: `default / hover / active / disabled` (focus не робимо). Розміри: `xs / sm / md / lg / xl`.
8. Ім'я групи не може бути `value`, `type` або `description` — Token Studio читає їх як поля токена. Замість `value` — `amount` / `percent` / `detail`.

## Карта файлів

| Файл | Коли читати |
|---|---|
| [references/core.md](references/core.md) | примітиви, шкали розмірів і шрифтів |
| [references/brand.md](references/brand.md) | значення всіх брендів поруч |
| [references/map.md](references/map.md) | рампи кольорів |
| [references/theme.md](references/theme.md) | семантика кольорів light / dark |
| [references/typography.md](references/typography.md) | text styles |

### Компоненти

{table(comp_rows, ["Компонент", "Токенів"])}

## Додати компонент

1. Блок `<component>` у `tokens/components.json` (посилання тільки на theme/brand-семантику).
2. Нотатки (анатомія, варіанти, text styles) — у `COMPONENT_NOTES` скрипта.
3. `python3 tools/build-skill.py` — з'явиться `references/components/<component>.md`, індекс оновиться.
"""
    write("SKILL.md", text)

doc_core(); doc_brand(); doc_map(); doc_theme(); doc_typography()
comps = doc_components()
doc_index(comps)
print("skill →", OUT)
