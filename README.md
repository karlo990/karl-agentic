# Karl Agentic website

The website for **Karl Agentic**, the AI agent studio. It has:

- `/`: the landing page (agents, how it works, Royal Crest example, Academy, FAQ, demo call to action)
- `/academy`: the Karl Agentic Academy hub, plus one guide per Instagram series in `/academy/*`
  (Agent tools, Blender skills, MCP servers, Adobe tricks, Design skills, Automation recipes, GitHub, Websites, LLM prompts)
- `/brand`: the brand kit (logo, colours, type, voice, applications)

It's a plain static site (HTML, CSS and a little JavaScript), so Vercel needs no build settings.

## Deploy on Vercel

1. Go to <https://vercel.com/new> and import this GitHub repository.
2. Framework preset: **Other**. Leave the build command and output directory empty.
3. Click **Deploy**. Every push to `main` redeploys the site automatically.
4. Add your domain under **Project → Settings → Domains**.

## Before launch: replace the placeholders

Open `scripts/build.py` and edit `CONFIG`:

| Key | What to put |
|---|---|
| `whatsapp` | `https://wa.me/` followed by your WhatsApp Business number in international format, digits only |
| `email` | Your real inbox |
| `site_url` | Your live domain once connected |

Then rebuild:

```bash
python3 scripts/build.py
```

## Editing content

- **Academy guides**: the `SERIES` list in `scripts/build.py`. Add a new series by adding an entry and a cover image in `assets/covers/`.
- **Landing page copy**: the `landing()` function in `scripts/build.py`.
- **Styles**: `css/site.css`.
- **Brand kit page**: `brand/kit.src.html` (wrapped into `brand/index.html` by the build).

Always run `python3 scripts/build.py` after editing, then commit the generated HTML.

## Assets

- `assets/logo/`: mark, horizontal logo, app icon, round profile picture, favicons
- `assets/covers/`: the nine Instagram series covers
- `assets/carousel/`: the 9-slide Academy carousel
- `assets/brand/`: hero image, social sharing image and the pink cursor variants

## Studio: Instagram carousels (`/studio`)

30 ready-to-post carousels. Each post has 5 slides at 1080 × 1350 (Instagram 4:5):
a cover, three slides explaining the idea, and a "Comment AGENT" slide. Each post's
artwork is painted as one 5400 × 1350 panorama and cut into slides, so the art
flows on as people swipe.

On the site, **Download all 5** saves a zip with the five JPGs plus `caption.txt`.
On phones that support it, **Save to phone** opens the share sheet so you can save
all five to your gallery at once. **Download everything** zips all 30 posts.

### Make or edit posts

- Content: `studio-src/posts.js` (titles, slides, gift for the "Comment AGENT" slide, hook for the caption)
- Design: `studio-src/template.html` (12 palettes, 10 art styles, 5 slide layouts: `big`, `list`, `steps`, `compare`, `prompt`)
- Renderer: `studio-src/render.js`

```bash
cd studio-src
npm install && npx playwright install chromium   # first time only
node render.js                    # render all posts
node render.js comment-to-dm      # or just one
cd .. && python3 scripts/build.py # refresh the /studio page
```

Output goes to `assets/studio/<slug>/` and `studio/posts.json` (captions included).

## South African price guide and store locations

Generated from `data/prices.json` by `scripts/build.py`. To refresh, ask Claude Code to re-check the prices with web search, update the JSON, and rebuild.

<!-- prices:start -->
Checked 2026-11-23. Average of the 4 lowest South African listings found by web search on the date checked, converted from rand to US dollars. Store prices include South African VAT. Listings change daily; these are indicative only and every quote is confirmed with the supplier.

Exchange rate: 1 USD = R16.72 ([Wise mid-market rate](https://wise.com/us/currency-converter/usd-to-zar-rate?amount=1), 2026-11-23).

### GeForce RTX 5070 (12GB): average $852 (R14 249)

| Store | Item | Price (USD) | Price (ZAR) | Note |
|---|---|---|---|---|
| [Evetech](https://evezone.evetech.co.za/build-lab/rtx-5070-price-south-africa) | Palit RTX 5070 Infinity 3 | $837 | R13 999 | Evetech price guide, Aug 2026 |
| [Evetech](https://evezone.evetech.co.za/build-lab/rtx-5070-price-south-africa) | Palit RTX 5070 OC White | $837 | R13 999 | Evetech price guide, Aug 2026 |
| [Evetech](https://evezone.evetech.co.za/build-lab/rtx-5070-price-south-africa) | MSI RTX 5070 Shadow 2X | $867 | R14 499 | Evetech price guide, Aug 2026 |
| [Evetech](https://evezone.evetech.co.za/build-lab/rtx-5070-price-south-africa) | MSI RTX 5070 Ventus 2X | $867 | R14 499 | Evetech price guide, Aug 2026 |

### GeForce RTX 5070 Ti (16GB): average $1,196 (R19 989)

| Store | Item | Price (USD) | Price (ZAR) | Note |
|---|---|---|---|---|
| [Dreamware](https://evezone.evetech.co.za/performance-pulse/is-the-rtx-5070-ti-worth-buying-in-south-africa-in-2026) | RTX 5070 Ti (lowest recorded) | $1,098 | R18 359 | Lowest price in a 2026 retailer comparison |
| [Evetech](https://evezone.evetech.co.za/build-lab/rtx-5070-ti-price-south-africa) | RTX 5070 Ti (from) | $1,196 | R19 999 | Evetech price guide, Aug 2026 |
| [Comx Computers](https://www.comx-computers.co.za/RTX-5070-TI-16G-SHA-3X-OC-MSI-RTX-5070-Ti-Shadow-3x-Buy-p-324201.php) | MSI RTX 5070 Ti Shadow 3X OC | $1,232 | R20 600 | Listing date unclear |
| [Evetech](https://evezone.evetech.co.za/build-lab/rtx-5070-ti-price-south-africa) | PNY RTX 5070 Ti | $1,256 | R20 999 | Evetech price guide, Aug 2026 |

### GeForce RTX 5080 (16GB): average $1,809 (R30 246)

| Store | Item | Price (USD) | Price (ZAR) | Note |
|---|---|---|---|---|
| [Evetech](https://evezone.evetech.co.za/build-lab/rtx-5080-price-south-africa) | Palit RTX 5080 GamingPro | $1,615 | R26 999 | Evetech price guide, Aug 2026; product page later showed R33,999 |
| [Evetech](https://evezone.evetech.co.za/build-lab/rtx-5080-price-south-africa) | Palit RTX 5080 GamingPro OC | $1,675 | R27 999 | Evetech price guide, Aug 2026 |
| [tech.co.za](https://tech.co.za/product/gigabyte-nvidia-geforce-rtx-5080-gaming-16gb-graphics-card/) | Gigabyte RTX 5080 Gaming | $1,853 | R30 989 | Listing about 318 days old |
| [Evetech](https://evezone.evetech.co.za/build-lab/rtx-5080-price-south-africa) | ASUS ProArt RTX 5080 | $2,093 | R34 999 | Evetech listing |

### GeForce RTX 5090 (32GB): average $3,691 (R61 706)

| Store | Item | Price (USD) | Price (ZAR) | Note |
|---|---|---|---|---|
| [Comx Computers](https://www.comx-computers.co.za/RTX5090GAMINGTRIOOC32GB-MSI-nVidia-Geforce-RTX-5090-Buy-p-319474.php) | MSI RTX 5090 Gaming Trio OC | $3,376 | R56 455 | Price dated 7 Oct 2025, likely stale |
| [MyGaming retailer comparison](https://mygaming.co.za/news/features/127048-how-much-an-rtx-50-series-graphics-card-costs-in-south-africa) | RTX 5090 (cheapest retailer) | $3,611 | R60 369 | Comparison table, June 2026 |
| [MyGaming retailer comparison](https://mygaming.co.za/news/features/127048-how-much-an-rtx-50-series-graphics-card-costs-in-south-africa) | RTX 5090 (second retailer) | $3,888 | R64 999 | Comparison table, June 2026 |
| [MyGaming retailer comparison](https://mygaming.co.za/news/features/127048-how-much-an-rtx-50-series-graphics-card-costs-in-south-africa) | RTX 5090 (third retailer) | $3,888 | R64 999 | Comparison table, June 2026 |

### NVIDIA DGX Spark (128GB): average $7,889 (R131 901)

| Store | Item | Price (USD) | Price (ZAR) | Note |
|---|---|---|---|---|
| [Evetech (EveZone listing)](https://evezone.evetech.co.za/launch-radar/dgx-spark-64gb-local-ai-memory-guide) | DGX Spark 128GB | $6,280 | R104 999 | Listing quoted in EveZone guide |
| [Bob Shop (Gradagio, Johannesburg)](https://www.bobshop.co.za/nvidia-dgx-spark-founders-edition-gb10-2-cortex-a725-cortex-x925-128gb-ram-4tb-ssd-mini-pc/p/677504603) | DGX Spark Founders Edition 128GB / 4TB | $6,436 | R107 608 | Listed 24 Apr, about 213 days old |
| [IT Procurement](https://itprocurement.co.za/products/nvidia-dgx-spark) | DGX Spark | $8,074 | R135 000 | Marked sold out |
| [Evetech](https://www.evetech.co.za/nvidia-dgx-spark-mini-pc-gb10-grace-blackwell/best-deal/25429) | DGX Spark GB10 Mini PC | $10,765 | R179 999 | In stock; list price R219,999 |

### Jetson Orin Nano Super Developer Kit: average $362 (R6 060)

| Store | Item | Price (USD) | Price (ZAR) | Note |
|---|---|---|---|---|
| [Bob Shop](https://www.bobshop.co.za/nvidia-jetson-orin-nano-super-developer-kit-development-kit/p/672551173) | Jetson Orin Nano Super Developer Kit | $347 | R5 800 | Marketplace listing |
| [RS South Africa](https://za.rs-online.com/web/p/processor-development-tools/2647384) | Jetson Orin Nano Super Developer Kit (945-13766-0005-000) | $378 | R6 321 | Indicative price incl. VAT (R5,496.26 excl.) |

### RTX PRO 6000 Blackwell (96GB)

No South African rand listings found. Quote on request.

### All stores and where each price was found

- **Evetech**: price found on evezone.evetech.co.za
- **Dreamware**: price found on evezone.evetech.co.za
- **Comx Computers**: price found on www.comx-computers.co.za
- **tech.co.za**: price found on tech.co.za
- **MyGaming retailer comparison**: price found on mygaming.co.za
- **Evetech (EveZone listing)**: price found on evezone.evetech.co.za
- **Bob Shop (Gradagio, Johannesburg)**: price found on www.bobshop.co.za
- **IT Procurement**: price found on itprocurement.co.za
- **Bob Shop**: price found on www.bobshop.co.za
- **RS South Africa**: price found on za.rs-online.com

<!-- prices:end -->
