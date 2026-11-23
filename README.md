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
