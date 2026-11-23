#!/usr/bin/env python3
"""Builds the static Karl Agentic site.

Edit CONFIG and the SERIES content below, then run:
    python3 scripts/build.py
It rewrites index.html, academy/*.html and brand/index.html. Commit the result;
Vercel serves the files as they are (no build step needed).
"""
import html, json, pathlib, re, urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------- config
CONFIG = {
    "site_url": "https://karlagentic.vercel.app",       # change when the domain is live
    "email": "karlagenticzw@gmail.com",                   # TODO: real inbox
    "instagram": "https://instagram.com/karlagentic",
    "instagram_handle": "@karlagentic",
}
def gmail(subject, intro):
    """Gmail compose link to our inbox with the subject and an enquiry template filled in."""
    body = (f"Hi Karl Agentic,\n\n{intro}\n\nName:\nCompany:\nWhat I need:\nBudget (USD):\nTimeline:\n"
            "Best way to reach me:\n\nThank you")
    q = lambda t: urllib.parse.quote(t, safe="")
    return f'https://mail.google.com/mail/?view=cm&amp;fs=1&amp;to={q(CONFIG["email"])}&amp;su={q(subject)}&amp;body={q(body)}'
WA = gmail("Enquiry: free demo and quote", "I'd like a free demo and a quote for my business.")

# ---------------------------------------------------------------- academy content
SERIES = [
 {"slug":"agent-tools","cover":"agent-tools","pre":"Weekly","title":"Agent tools","part":"Part 1","tag":"AI",
  "intro":"The tools we use to build AI agents for clients. You can start with most of them for free.",
  "items":[
   ("Claude","The brain","An AI model that reads, writes and reasons. We use it to understand guest messages, draft replies and summarise long documents.","Ask it to rewrite your business's FAQ as short WhatsApp replies.","https://claude.ai"),
   ("Claude Code","The builder","An AI coding agent that works inside your code projects. It writes features, fixes bugs and commits to GitHub.","Ask it to build a one-page website for your business, then deploy it on Vercel.","https://claude.com/claude-code"),
   ("n8n","The wiring","Open-source workflow automation. Connect WhatsApp, Google Sheets, email and an AI model with drag-and-drop nodes. Can be self-hosted.","Build a workflow: new form entry → AI summary → email to you.","https://n8n.io"),
   ("Zapier","The quick connector","Connects thousands of apps without code. The fastest way to test an automation idea.","Create a Zap that saves every new Gmail attachment to Google Drive.","https://zapier.com"),
   ("WhatsApp Business Platform","The channel","Meta's official API for WhatsApp. This is how an agent sends and receives real customer messages at scale.","Set up the free WhatsApp Business app first, with a catalogue and quick replies.","https://business.whatsapp.com"),
   ("Cal.com","The calendar","Open-source scheduling. Agents check availability and book meetings through its API.","Create a 15-minute 'Free demo' event and put the link in your Instagram bio.","https://cal.com"),
   ("Vercel","The launchpad","Hosts websites and small apps straight from GitHub. Every push goes live in about a minute.","Import a GitHub repo and get a free .vercel.app address.","https://vercel.com"),
  ]},
 {"slug":"blender-skills","cover":"blender-skills","pre":"Selected","title":"Blender skills","part":"Part 1","tag":"3D",
  "intro":"Blender is free, open-source 3D software. These are the first skills to learn, in the order we'd learn them.",
  "items":[
   ("Move around the scene","Navigation","Orbit with the middle mouse button, pan with <kbd>Shift</kbd> + middle mouse, zoom with the scroll wheel. Number pad keys give front (<kbd>1</kbd>), side (<kbd>3</kbd>) and top (<kbd>7</kbd>) views.","Spend five minutes orbiting the default cube until it feels natural.","https://docs.blender.org/manual/en/latest/editors/3dview/navigate/index.html"),
   ("Grab, rotate, scale","Transform","Press <kbd>G</kbd> to move, <kbd>R</kbd> to rotate and <kbd>S</kbd> to scale. Type <kbd>X</kbd>, <kbd>Y</kbd> or <kbd>Z</kbd> after to lock to an axis.","Scale the cube to half size on Z only: S, Z, 0.5, Enter.","https://docs.blender.org/manual/en/latest/scene_layout/object/editing/transform/index.html"),
   ("Edit mode modelling","Model","<kbd>Tab</kbd> enters Edit Mode. Extrude with <kbd>E</kbd>, inset faces with <kbd>I</kbd>, add a loop cut with <kbd>Ctrl</kbd>+<kbd>R</kbd> and bevel edges with <kbd>Ctrl</kbd>+<kbd>B</kbd>.","Turn a cube into a simple mug: inset the top face, then extrude it down.","https://docs.blender.org/manual/en/latest/modeling/meshes/editing/index.html"),
   ("Modifiers","Non-destructive","Subdivision Surface smooths a shape, Bevel rounds edges, Solidify adds thickness. You can change them any time without losing work.","Add a Subdivision Surface modifier with <kbd>Ctrl</kbd>+<kbd>2</kbd> and right-click → Shade Smooth.","https://docs.blender.org/manual/en/latest/modeling/modifiers/index.html"),
   ("Materials","Look","The Principled BSDF shader handles most materials. Base Color sets the colour, Roughness sets how glossy it is (low = shiny).","Make glossy brand pink: Base Color #F0287A, Roughness 0.25.","https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/principled.html"),
   ("Three-point lighting","Light","A bright key light at 45°, a softer fill light opposite, and a rim light behind the object to separate it from the background.","Light your mug with three Area lights and compare it to a single light.","https://docs.blender.org/manual/en/latest/render/lights/light_object.html"),
   ("Render","Export","Cycles is slower but realistic; Eevee is fast and great for social posts. Press <kbd>F12</kbd> to render, then Image → Save As to export a PNG.","Render at 1080 × 1350 for an Instagram portrait post.","https://docs.blender.org/manual/en/latest/render/index.html"),
  ]},
 {"slug":"mcp-servers","cover":"mcp-servers","pre":"Best","title":"MCP servers","part":"for business","tag":"AI",
  "intro":"MCP (Model Context Protocol) is an open standard that lets AI apps such as Claude connect to your tools and data. An MCP server is the plug for one tool. These are the ones we reach for most.",
  "items":[
   ("Google Drive","Documents","Lets the AI search and read your files, so it can answer questions from your own price lists, menus and policies.","Ask: 'Using our rates sheet in Drive, what does a 3-night stay for 2 cost?'","https://modelcontextprotocol.io"),
   ("GitHub","Code","Reads repos, opens issues and pull requests. This is how our coding agents ship work you can review.","Ask an agent to open an issue listing broken links on your website.","https://github.com/github/github-mcp-server"),
   ("Slack","Team chat","Lets an agent post daily summaries or answer staff questions in a channel.","Have the agent post 'today's bookings' to #front-desk every morning.","https://modelcontextprotocol.io"),
   ("Notion","Knowledge base","Reads and updates pages and databases, which makes it a natural home for SOPs and client notes.","Turn your call notes into a Notion client page automatically.","https://modelcontextprotocol.io"),
   ("Stripe","Payments","Creates payment links and checks invoices, so the agent can send a guest a deposit link mid-chat.","Ask the agent to create a payment link for a $50 deposit.","https://docs.stripe.com/mcp"),
   ("Playwright","Browser","Lets an agent open real web pages, click and fill forms. Useful for testing your own site or checking competitor prices.","Ask the agent to test that your booking form submits correctly.","https://github.com/microsoft/playwright-mcp"),
  ],
  "note":"Connect only servers you trust, start with read-only access, and review what the AI is allowed to do before giving it write access."},
 {"slug":"adobe-tricks","cover":"adobe-tricks","pre":"Useful","title":"Adobe tricks","part":"for creators","tag":"Design",
  "intro":"Small Adobe features that save hours every week. If you don't have Creative Cloud, the free alternatives are listed at the end.",
  "items":[
   ("Generative Fill","Photoshop","Select an area, type what you want (or leave it blank to remove), and Photoshop fills it to match the photo.","Extend a square product photo to 4:5 for Instagram with Crop + Generative Expand.","https://www.adobe.com/products/photoshop/generative-fill.html"),
   ("Remove Background","Photoshop","In the Properties panel, Quick Actions → Remove Background cuts out a person or product in one click.","Cut out a product and place it on a brand-pink background.","https://helpx.adobe.com/photoshop/using/remove-background.html"),
   ("Image Trace","Illustrator","Turns a PNG or JPG logo into sharp vectors, so you can print it on anything at any size.","Trace an old logo, then use Expand to edit the shapes.","https://helpx.adobe.com/illustrator/using/image-trace.html"),
   ("Recolor Artwork","Illustrator","Swaps every colour in an illustration to your brand palette at once.","Recolour an icon set to Navy, Blue and Pink in one step.","https://helpx.adobe.com/illustrator/using/recolor-artwork.html"),
   ("Auto captions","Premiere Pro","Speech to Text transcribes your video and creates captions you can style. Most Reels are watched on mute, so captions matter.","Caption a 30-second talking-head Reel and style it in your brand font.","https://helpx.adobe.com/premiere-pro/using/speech-to-text.html"),
   ("Easy Ease","After Effects","Select keyframes and press <kbd>F9</kbd>. Motion speeds up and slows down naturally instead of moving like a robot.","Animate your logo sliding in, then apply Easy Ease and compare.","https://helpx.adobe.com/after-effects/using/speed.html"),
  ],
  "note":"Free alternatives: Photopea (Photoshop-like, in the browser), Inkscape (vectors), CapCut (video and auto captions), Blender (motion and 3D)."},
 {"slug":"design-skills","cover":"design-skills","pre":"Selected","title":"Design skills","part":"Part 1","tag":"Design",
  "intro":"Good design follows rules you can learn. Check every post against these before you publish.",
  "items":[
   ("Hierarchy","Rule 1","Decide the one thing people should see first and make it the biggest. Then the second thing. Everything else is small.","Squint at your design. Whatever you still see is your hierarchy.",None),
   ("Two fonts maximum","Rule 2","One display font for headlines and one calm font for body text. Our brand uses Unbounded and Manrope.","Rebuild an old post using only two fonts and compare.",None),
   ("60 · 30 · 10 colour","Rule 3","60% main colour, 30% secondary, 10% accent. Our accent is pink, so pink means 'click here'.","Count the colours in your last five posts. Cut the extras.",None),
   ("White space","Rule 4","Empty space is not wasted. It makes the important thing louder and the design look expensive.","Double the margin around your headline and see how it changes.",None),
   ("Align to a grid","Rule 5","Every edge should line up with something. Use guides in Canva, Figma or Photoshop.","Turn on rulers and snap every element to the same left edge.",None),
   ("Contrast you can read","Rule 6","Text needs a contrast ratio of at least 4.5:1 against its background to be readable (WCAG guidance).","Check your colours with a free contrast checker.","https://webaim.org/resources/contrastchecker/"),
   ("Export at the right size","Rule 7","Instagram feed portrait 1080 × 1350, Stories and Reels 1080 × 1920, square 1080 × 1080.","Set up these three sizes as templates in your design app.",None),
  ]},
 {"slug":"automation-recipes","cover":"automation","pre":"Pro","title":"Automation recipes","part":"Zapier · Make · n8n","tag":"Automation",
  "intro":"Every automation has the same shape: a trigger, a brain, and an action. Here are six recipes you can build this week.",
  "items":[
   ("WhatsApp booking assistant","Trigger → Brain → Action","New WhatsApp message → AI reads the dates, guests and budget → checks the calendar, holds the room and replies with a confirmation.","Start simple: AI drafts the reply, a person taps send.",None),
   ("Instagram keyword DM","Marketing","Someone comments 'AGENT' on a post → they get an automatic DM with your demo link.","Use a DM automation tool connected to your Instagram professional account.",None),
   ("Instant lead follow-up","Sales","New website form → add to CRM → AI writes a personal reply in under a minute → you get a WhatsApp alert.","Measure how fast you reply today, then try to get it under 5 minutes.",None),
   ("Invoice reminders","Operations","Invoice 3 days overdue → friendly reminder → 7 days → firmer reminder with payment link → 14 days → alert to you.","Write the three messages first; the automation is the easy part.",None),
   ("Monday morning report","Reporting","Every Monday 7:00 → pull last week's bookings, sales and posts → AI writes a 5-line summary → email to you.","List the 5 numbers you actually care about each week.",None),
   ("Review replies","Reputation","New Google review → AI drafts a reply in your brand voice → you approve it → it's posted.","Collect 3 of your best past replies as examples for the AI.",None),
  ]},
 {"slug":"github","cover":"github","pre":"Beginner","title":"GitHub in 5 min","part":"Part 1","tag":"Code",
  "intro":"GitHub stores your code online and keeps a history of every change. This whole website lives in a GitHub repo.",
  "items":[
   ("Repository","The project folder","A repo holds all your project's files and their full history. Create one at github.com/new.","Create a repo called my-first-site with a README.","https://github.com/new"),
   ("Commit","A saved snapshot","A commit saves your changes with a short message explaining why. Small, frequent commits are easier to undo.","<pre class=\"code\">git add .\ngit commit -m \"Add pricing section\"\ngit push</pre>","https://docs.github.com/en/get-started/using-git/about-git"),
   ("Branch","A safe copy","Try new ideas on a branch without breaking the live site. main is usually the live version.","<pre class=\"code\">git checkout -b new-homepage</pre>","https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches"),
   ("Pull request","Review before merging","A pull request asks to merge a branch into main. Teammates (or AI reviewers) can comment first.","Open a pull request from new-homepage into main and read the 'Files changed' tab.","https://docs.github.com/en/pull-requests"),
   ("GitHub Desktop","No terminal needed","A free app for commits, branches and pushes with buttons instead of commands.","Clone your repo with GitHub Desktop and make one commit.","https://desktop.github.com"),
   ("Deploy with Vercel","Go live","Connect the repo to Vercel. Every push to main updates your live website automatically.","Import your repo at vercel.com/new and click Deploy.","https://vercel.com/new"),
  ]},
 {"slug":"websites","cover":"websites","pre":"Launch","title":"Websites that book","part":"in one weekend","tag":"Web",
  "intro":"A website's job is to turn a visitor into a booking. This is the checklist we use for every client site.",
  "items":[
   ("Domain","Saturday morning","Buy yourbusiness.com (or a local domain) from a registrar such as Cloudflare or Namecheap. Keep it short and easy to say.","Say the domain out loud to a friend. If they can't type it, change it.",None),
   ("Builder","Saturday","Framer or Webflow for no-code; Next.js or plain HTML for full control. This site is plain HTML on Vercel.","Pick one and build only the home page first.",None),
   ("One clear action","The rule","Every page needs one main button: Book now, WhatsApp us, or Get a quote. Make it pink (your action colour).","Remove every button that isn't the main action from your hero.",None),
   ("WhatsApp button","Conversion","A wa.me link opens a chat with a pre-filled message. Most local customers prefer it to forms.","<pre class=\"code\">https://wa.me/[country code][number]?text=Hi%2C%20I%27d%20like%20to%20book</pre>","https://faq.whatsapp.com/5913398998672934"),
   ("Host and HTTPS","Sunday","Vercel or Netlify host for free on small sites and add HTTPS automatically. Connect your domain in the dashboard.","Deploy, then open the site on your phone over mobile data.",None),
   ("Get found","Sunday afternoon","Create a Google Business Profile, write a clear page title and description, and add real photos.","Search your business name on Google Maps and fix what you see.","https://business.google.com"),
   ("Speed check","Before launch","Compress images (this site uses JPGs under 200 KB) and test with PageSpeed Insights.","Aim for a mobile score in the green.","https://pagespeed.web.dev"),
  ]},
 {"slug":"llm-prompts","cover":"llm-prompts","pre":"Copy these","title":"LLM prompts","part":"Part 1","tag":"AI",
  "intro":"Works in Claude, ChatGPT or Gemini. Every prompt follows the formula Role + Task + Context + Format. Replace the [brackets] and copy.",
  "prompts":[
   ("Booking reply","You are the friendly booking assistant for [business name], a [type of business] in [town].\nReply to this customer message: \"[paste message]\".\nAvailable dates: [dates]. Price: [price].\nWrite a warm WhatsApp reply under 50 words, offer two options and end with a question."),
   ("Instagram caption","You are a social media manager for [business].\nWrite 3 Instagram captions for a post about [topic].\nOur audience: [who]. Our tone: [e.g. confident, warm, no jargon].\nEach caption: a hook in the first line, 2 short lines of value, a call to action, and 5 relevant hashtags."),
   ("A month of content","You are a content strategist.\nCreate a 4-week Instagram plan for [business] that sells [product/service] to [audience].\nUse 3 content pillars: education, proof, behind the scenes.\nReturn a table: week, day, format (Reel/carousel/story), hook, call to action."),
   ("Summarise reviews","Here are our latest customer reviews: [paste reviews].\nList the top 3 things customers love and the top 3 complaints, with one quote for each.\nThen suggest 3 changes we could make this month. Keep it under 200 words."),
   ("Follow-up email","You are a polite, confident salesperson for [business].\nWrite a follow-up email to [name], who asked about [service] [X] days ago and hasn't replied.\nMention one benefit relevant to them: [benefit]. Under 90 words. One clear next step."),
   ("FAQ from your website","Read this text from our website: [paste text].\nWrite the 10 questions customers are most likely to ask, with short, accurate answers using only this text.\nIf the text doesn't answer something important, list it separately as 'Missing info'."),
   ("Price increase message","You are the owner of [business].\nWrite a short, honest message telling regular customers our price for [service] is going from [old] to [new] on [date].\nThank them, give one reason, and offer [small perk] to anyone who books before the change."),
   ("Turn notes into a proposal","Here are my call notes: [paste notes].\nWrite a one-page proposal for [client] with: their goal, our solution in 3 steps, timeline, what we need from them, and price: [price].\nUse plain language and short headings."),
  ]},
]

# ---------------------------------------------------------------- shared layout
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Unbounded:wght@400;600;700;800&family=Manrope:wght@400;500;600;700;800&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;600&display=swap">')

def head(title, desc, path, image="/assets/brand/og-image.jpg"):
    url = CONFIG["site_url"] + path
    return f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{CONFIG["site_url"]}{image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#000000">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" href="/assets/logo/favicon-32.png"><link rel="apple-touch-icon" href="/assets/logo/apple-touch-icon.png">
{FONTS}
<link rel="stylesheet" href="/css/site.css"><link rel="stylesheet" href="/css/theme.css">
</head><body>'''

def header(active=""):
    def a(href, label, key):
        cur = ' aria-current="page"' if key == active else ""
        return f'<a href="{href}"{cur}>{label}</a>'
    return f'''<header class="site-head"><div class="wrap">
  <a class="brand" href="/" aria-label="Karl Agentic home"><img src="/assets/logo/pink-tile-64.png" alt="" width="36" height="36"><span class="wm"><b>KARL</b> <i>AGENTIC</i></span></a>
  <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav class="nav" id="nav">{a("/#solutions","Solutions","solutions")}{a("/hardware","Hardware","hardware")}{a("/studio","Studio","studio")}{a("/academy","Academy","academy")}{a("/#work","Work","work")}
    <a class="btn btn-pink" href="{WA}" target="_blank" rel="noopener">Get a quote</a></nav>
</div></header>'''

def footer():
    s = "".join(f'<a href="/academy/{x["slug"]}">{x["title"]}</a>' for x in SERIES[:5])
    return f'''<footer class="site-foot"><div class="wrap">
  <div><a class="brand" href="/" style="color:#fff"><img src="/assets/logo/pink-tile-64.png" alt="" width="36" height="36"><span class="wm"><b>KARL</b> <i>AGENTIC</i></span></a>
    <p style="margin-top:.9rem;max-width:36ch">Tech consulting, AI agents, automation, GPU infrastructure and creative production.</p></div>
  <div><h4>Solutions</h4><a href="/#agents">AI agents and bots</a><a href="/#social">Social media automation</a><a href="/#servers">Servers and setup</a><a href="/hardware">GPUs and hardware</a><a href="/#creative">Rendering and video</a></div>
  <div><h4>Resources</h4><a href="/studio">Studio</a><a href="/academy">Academy</a>{s}<a href="/brand">Brand kit</a></div>
  <div><h4>Contact</h4><a href="{WA}" target="_blank" rel="noopener">Email us (Gmail)</a><a href="{CONFIG["instagram"]}" target="_blank" rel="noopener">Instagram {CONFIG["instagram_handle"]}</a><span style="user-select:all">{CONFIG["email"]}</span></div>
  <p class="tm">NVIDIA, GeForce, RTX, DGX and Jetson are trademarks of NVIDIA Corporation. Other product names are trademarks of their owners. Karl Agentic is an independent consultancy and is not affiliated with or endorsed by NVIDIA. Hardware images on this site are our own illustrations. Prices, stock and warranty terms are confirmed in writing with each quote.</p>
  <div class="legal"><span>© 2026 Karl Agentic. Part of the KarlCon family.</span><span>Hosted on Vercel.</span></div>
</div></footer>
<div class="toast" id="toast" role="status"></div>
<script src="/js/site.js" defer></script>
</body></html>'''

HARDWARE = [
 ("gpu-geforce","GeForce RTX 50 Series","RTX 5090 · 5080 · 5070 Ti · 5070","Fast rendering, video editing, local AI models and creative workstations."),
 ("gpu-workstation","RTX PRO workstation GPUs","RTX PRO Blackwell family","Large memory and certified drivers for pro rendering, CAD and AI development."),
 ("workstation","Custom AI workstations","1–4 GPUs · built and tested","Towers specced to your workload, assembled, stress-tested and delivered."),
 ("ai-mini","Desktop AI systems","e.g. NVIDIA DGX Spark","Run and fine-tune large models on your desk, with no data leaving the office."),
 ("server-2u","GPU servers","2U / 4U · 4–8 GPUs","Rack servers for private AI, inference, render farms and virtual desktops."),
 ("gpu-datacenter","Data-centre GPUs","H200 · Blackwell-class via OEM servers","Large-scale training and inference for enterprises and research teams."),
 ("edge","Edge AI","Jetson Orin · Jetson Thor","On-site AI for cameras, retail analytics, robotics and smart devices."),
 ("network","Networking and storage","Switches · NAS · UPS · racks","Everything around the GPUs: fast networks, safe storage and backup power."),
]

def hw_card(k, name, ex, desc, quote=True):
    link = f'<a class="more" href="{gmail(f"Quote request: {name}", f"I would like a quote for: {name} ({ex}).")}" target="_blank" rel="noopener">Request a quote</a>' if quote else '<a class="more" href="/hardware">See options</a>'
    return f'<article class="hw"><img src="/assets/hw/{k}.jpg" alt="Illustration: {html.escape(name)}" loading="lazy" width="1200" height="800"><div class="tb"><span class="ex">{ex}</span><h3>{name}</h3><p>{desc}</p>{link}</div></article>'

SOLUTIONS = [
 ("agents","/assets/studio/what-is-an-ai-agent/thumb-1.jpg","AI agents and bots","Agents that answer, book and follow up.","WhatsApp, Instagram, Telegram and web-chat bots connected to your calendar, CRM and payments.",["Booking and front-desk agents","Lead follow-up and sales bots","Human hand-over rules you approve"],"/#agents"),
 ("social","/assets/studio/comment-to-dm/thumb-1.jpg","Social media automation","Content that runs on a system.","Content pipelines, scheduling, comment-to-DM funnels and branded carousels produced from templates.",["Comment-to-DM keyword funnels","Template-driven carousels and Reels","Weekly performance reports"],"/studio"),
 ("servers","/assets/hw/server-2u.jpg","Server installation and configuration","Your own AI and automation servers.","We install, configure and secure Linux servers and GPU machines, on-site or in the cloud.",["Ubuntu Server, Docker, NVIDIA drivers and CUDA","Private LLMs and self-hosted n8n","Backups, monitoring and remote access"],"/#servers"),
 ("hardware","/assets/hw/gpu-geforce.jpg","GPUs and hardware sourcing","NVIDIA GPUs and servers, sourced locally.","We spec the right hardware, compare South African suppliers, deliver and install it.",["GeForce RTX and RTX PRO GPUs","AI workstations and GPU servers","Networking, storage and UPS"],"/hardware"),
 ("rendering","/assets/carousel/02-blender.jpg","3D rendering and visualisation","Product shots without a studio.","Blender product renders, 3D logos, architectural visuals and render setups on GPU machines.",["Product and packaging renders","3D brand assets and icons","GPU render workstations"],"/#creative"),
 ("video","/assets/studio/captions-on-every-reel/thumb-1.jpg","Video production and motion","Reels, ads and motion graphics.","Editing, captions, animated logos and AI-assisted video, cut for each platform.",["Reels, Shorts and TikToks","Animated logos and motion graphics","Auto-captioned, on-brand edits"],"/#creative"),
 ("design","/assets/studio/60-30-10-colour/thumb-1.jpg","Graphic design and branding","Brands that look the same everywhere.","Brand kits, logos, carousels, posters and templates your team can reuse.",["Logos and brand kits","Social templates and carousels","Print and signage files"],"/brand"),
 ("web","/assets/studio/websites-that-book/thumb-1.jpg","Websites and web apps","Sites that turn visitors into bookings.","Fast websites and small web apps, deployed on Vercel and connected to WhatsApp and your tools.",["Landing pages and business sites","Booking and lead forms","Dashboards and internal tools"],"/#solutions"),
 ("consulting","/assets/studio/which-ai-should-i-use/thumb-1.jpg","Tech consulting","A clear plan before you spend.","AI readiness, tool selection, hardware vs cloud costs and a step-by-step roadmap for your team.",["AI and automation audit","Hardware vs cloud cost plan","Team training and handover"],"/#contact"),
]


ICONS = {
 "book":'<rect x="4" y="6" width="24" height="22" rx="5" fill="none" stroke="#1D8BF7" stroke-width="3"/><path d="M4 13h24M11 3v6M21 3v6" stroke="#1D8BF7" stroke-width="3" stroke-linecap="round"/><path d="M11 20l3.5 3.5L21 17" fill="none" stroke="#F0287A" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
 "reach":'<path d="M5 13v6l14 7V6L5 13z" fill="none" stroke="#1D8BF7" stroke-width="3" stroke-linejoin="round"/><path d="M24 11c2 1.5 2 8.5 0 10" fill="none" stroke="#F0287A" stroke-width="3" stroke-linecap="round"/><path d="M8 19l2 7" stroke="#1D8BF7" stroke-width="3" stroke-linecap="round"/>',
 "close":'<circle cx="16" cy="16" r="12" fill="none" stroke="#1D8BF7" stroke-width="3"/><circle cx="16" cy="16" r="5" fill="none" stroke="#1D8BF7" stroke-width="3"/><path d="M16 16l9-9" stroke="#F0287A" stroke-width="3" stroke-linecap="round"/><path d="M22 5h4v4" fill="none" stroke="#F0287A" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
 "ops":'<circle cx="16" cy="16" r="5" fill="none" stroke="#F0287A" stroke-width="3"/><path d="M16 3v5M16 24v5M3 16h5M24 16h5M6.8 6.8l3.5 3.5M21.7 21.7l3.5 3.5M6.8 25.2l3.5-3.5M21.7 10.3l3.5-3.5" stroke="#1D8BF7" stroke-width="3" stroke-linecap="round"/>',
}
def icon(k): return f'<span class="ic"><svg width="30" height="30" viewBox="0 0 32 32" aria-hidden="true">{ICONS[k]}</svg></span>'

# ---------------------------------------------------------------- landing page

# ---------------------------------------------------------------- price guide (data/prices.json)
def load_prices():
    data = json.loads((ROOT / "data" / "prices.json").read_text())
    for pr in data["products"]:
        ls = sorted(pr["listings"], key=lambda l: l["price"])[:4]
        pr["used"] = ls
        pr["avg"] = round(sum(l["price"] for l in ls) / len(ls)) if ls else None
        pr["low"] = ls[0]["price"] if ls else None
        pr["high"] = ls[-1]["price"] if ls else None
    return data

def rand(v): return "R" + f"{v:,.0f}".replace(",", " ")
def usd(v, fx): return "$" + f"{v / fx:,.0f}"

def price_table(data, compact=False):
    rows = ""
    for pr in data["products"]:
        if pr["avg"] is None:
            rows += f'<tr><th scope="row">{pr["name"]}</th><td class="avg">Quote only</td><td>–</td><td>{pr.get("note","")}</td></tr>'
            continue
        n = len(pr["used"])
        stores = ", ".join(dict.fromkeys(l["store"] for l in pr["used"]))
        label = f"Avg of {n} lowest" if n == 4 else f"Avg of {n} found"
        fx = data["fx"]["usd_zar"]
        rows += f'<tr><th scope="row">{pr["name"]}</th><td class="avg">{usd(pr["avg"], fx)}<small>{label}</small></td><td>{usd(pr["low"], fx)} – {usd(pr["high"], fx)}</td><td>{stores}</td></tr>'
    d = data["checked"]
    return f'''<div class="price-wrap"><table class="prices"><thead><tr><th scope="col">Product</th><th scope="col">Average (USD)</th><th scope="col">Range used</th><th scope="col">Sources</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="note-sm">Checked {d}. {data["method"]} Exchange rate: 1 USD = R{data["fx"]["usd_zar"]} ({data["fx"]["source"]}, {data["fx"]["date"]}). Store links, rand prices and listing notes are in the project README.</p>'''

def landing():
    tiles = "".join(f'''<article class="tile2" id="sol-{i}"><div class="img"><img src="{img}" alt="" loading="lazy"></div><div class="tb"><span class="lab">{lab}</span><h3>{h}</h3><p>{p}</p><ul>{"".join(f"<li>{x}</li>" for x in li)}</ul><a class="more" href="{href}">Learn more</a></div></article>''' for i,img,lab,h,p,li,href in SOLUTIONS)
    hw = "".join(hw_card(*x) for x in HARDWARE[:4])
    covers = "".join(f'<img src="/assets/studio/{s}/thumb-1.jpg" alt="" loading="lazy" width="360" height="450">' for s in ["the-prompt-formula","reply-to-leads-fast","carousels-that-get-saved","trigger-brain-action"])
    faqs = [
      ("What does Karl Agentic do?","We're a tech consultancy and creative studio. We build AI agents and bots, automate social media and admin, install and configure servers, source GPUs and hardware, and produce renders, video and design."),
      ("Do you sell NVIDIA hardware?","We source NVIDIA GPUs, workstations and servers from suppliers in South Africa, compare prices for you, then deliver, install and configure them. We are an independent consultancy, not an NVIDIA partner or reseller of record."),
      ("What about warranty and delivery?","Hardware comes with the supplier's or manufacturer's warranty. We confirm warranty, delivery time and price in writing with every quote, because stock changes quickly."),
      ("Can you host AI privately, without sending data to the cloud?","Yes. We can set up local models on your own GPU machine or server, so documents and customer data stay on your network."),
      ("Do I need hardware to use AI agents?","No. Most agents and automations run in the cloud. Hardware makes sense for private AI, heavy rendering or high volumes. We'll tell you honestly which fits."),
      ("How do we start?",f"Tap any Get a quote button. Gmail opens with an enquiry to {CONFIG['email']} ready to send. We book a free call, understand your goals and send a written proposal and quote in US dollars."),
    ]
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faqs)
    body = f'''{header("solutions")}
<main class="nv">
<section class="nv-hero"><div class="wrap">
  <div>
    <span class="eyebrow">Tech consulting · AI agents · GPU infrastructure · Creative</span>
    <h1>Intelligent agents.<br>Powerful hardware.<br><span>Work that ships.</span></h1>
    <p class="lede">Karl Agentic builds AI agents and automated bots, installs and configures servers, sources NVIDIA GPUs locally, and produces the renders, video and design that make brands stand out.</p>
    <div class="ctas"><a class="nv-btn solid" href="{WA}" target="_blank" rel="noopener">Get a quote</a><a class="nv-btn line" href="#solutions">Explore solutions</a></div>
  </div>
  <div class="logo-card"><img src="/assets/brand/karl-agentic-hero.jpg" alt="Karl Agentic logo" width="1200" height="1200" fetchpriority="high"></div>
</div></section>

<nav class="tabs" aria-label="Sections"><div class="wrap">
  <a href="#solutions">All solutions</a><a href="#agents">AI agents</a><a href="#social">Social automation</a><a href="#servers">Servers</a><a href="#hardware">GPUs and hardware</a><a href="#creative">Rendering and video</a><a href="#work">Work</a><a href="#faq">FAQ</a>
</div></nav>

<section class="nv-sec" id="solutions"><div class="wrap">
  <div class="nv-head"><span class="bar"></span><span class="eyebrow">Solutions</span><h2>Nine ways we put technology to work for you.</h2><p class="lede">One team for strategy, build and creative, so your agents, servers and content work together instead of in separate silos.</p></div>
  <div class="tiles">{tiles}</div>
</div></section>

<section class="nv-sec alt" id="servers"><div class="wrap split">
  <div>
    <div class="nv-head" style="margin-bottom:0"><span class="bar"></span><span class="eyebrow">Server installation and configuration</span><h2>From bare metal to running AI in a day.</h2>
    <p class="lede">We install and harden the operating system, set up GPU drivers, containers and your automation stack, then hand over documentation and remote support.</p></div>
    <ul class="checks"><li>Ubuntu Server and security hardening</li><li>NVIDIA drivers, CUDA and container toolkit</li><li>Docker and Docker Compose stacks</li><li>Private LLMs with Ollama or vLLM</li><li>Self-hosted n8n automations</li><li>Backups, monitoring and alerts</li><li>VPN and secure remote access</li><li>Documentation and handover</li></ul>
    <p style="margin-top:1.8rem"><a class="nv-btn solid" href="{gmail("Enquiry: server installation and configuration", "I'd like a quote to install and configure a server.")}" target="_blank" rel="noopener">Book a server setup</a></p>
  </div>
  <div class="term" role="img" aria-label="Example terminal session on a GPU server"><div class="bar"><span><i></i><i></i><i></i></span><span>EXAMPLE SETUP · gpu-01</span></div>
<pre><span class="p">karl@gpu-01</span>:~$ nvidia-smi --query-gpu=name,memory.total --format=csv
<span class="dim">name, memory.total [MiB]</span>
<span class="dim">NVIDIA GeForce RTX (example), 32768 MiB</span>
<span class="p">karl@gpu-01</span>:~$ docker compose up -d
 <span class="ok">✔</span> Container ollama       Started
 <span class="ok">✔</span> Container n8n          Started
 <span class="ok">✔</span> Container open-webui   Started
 <span class="ok">✔</span> Container backups      Started
<span class="p">karl@gpu-01</span>:~$ curl -s localhost:5678/healthz
<span class="ok">{{"status":"ok"}}</span>
<span class="p">karl@gpu-01</span>:~$ <span class="dim"># private AI + automations are live</span></pre></div>
</div></section>

<section class="nv-sec" id="hardware"><div class="wrap">
  <div class="nv-head"><span class="bar"></span><span class="eyebrow">GPUs and hardware</span><h2>NVIDIA GPUs and servers, sourced in South Africa.</h2><p class="lede">Tell us the workload. We spec the hardware, compare local suppliers, quote you in writing, then deliver, install and configure it.</p></div>
  <div class="hw-row">{hw}</div>
  <div class="chips-row">{"".join(f'<span class="pchip"><b>{p["name"].split(" (")[0]}</b>{usd(p["avg"], load_prices()["fx"]["usd_zar"])} avg</span>' for p in load_prices()["products"] if p["avg"])}</div>
  <p style="margin-top:2rem;display:flex;gap:1rem;flex-wrap:wrap"><a class="nv-btn line" href="/hardware#prices">See the price guide</a><a class="nv-btn line" href="/hardware">View all hardware</a><a class="nv-btn solid" href="{WA}" target="_blank" rel="noopener">Request a quote</a></p>
  <p class="note-sm">Illustrations are representative. Model availability changes often; we confirm current models, prices and warranty with each quote.</p>
</div></section>

<section class="nv-sec alt" id="agents"><div class="wrap split">
  <div class="nv-head" style="margin-bottom:0"><span class="bar"></span><span class="eyebrow">AI agents and automated bots</span><h2>Agents that answer, book and follow up, 24/7.</h2>
    <p class="lede">Your agent reads WhatsApp, Instagram and web-chat messages, understands what people want and acts in your tools. You approve the rules; anything sensitive goes to a person.</p>
    <ul class="checks"><li>Booking and front-desk agents</li><li>Lead qualification and follow-up</li><li>Invoice and payment reminders</li><li>Review replies for approval</li></ul></div>
  <div class="chat" aria-label="Example conversation"><span class="eyebrow" style="color:#8EC9FF">Example conversation</span>
      <div class="bub in">Hi, do you have availability for 2 adults next weekend?<span class="t">GUEST · 21:14</span></div>
      <div class="bub out" style="background:#F0287A">Good evening! Yes, Friday and Saturday are open. Would you like the garden suite or the classic room? 🌿<span class="t">KARL AGENT · 21:14</span></div>
      <div class="bub in">Garden suite please, Friday to Sunday.<span class="t">GUEST · 21:15</span></div>
      <div class="bub out" style="background:#F0287A">Lovely. I've noted 2 adults, garden suite, Friday to Sunday. May I have your full name to prepare the booking?<span class="t">KARL AGENT · 21:15</span></div></div>
</div></section>

<section class="nv-sec" id="social"><div class="wrap split">
  <div class="gallery">{covers}</div>
  <div class="nv-head" style="margin-bottom:0"><span class="bar"></span><span class="eyebrow">Social media automation</span><h2>A content engine, not a posting chore.</h2>
    <p class="lede">We build template systems that turn one idea into a 5-slide carousel, a caption and a comment-to-DM funnel. Our own Studio produced 30 posts this way.</p>
    <ul class="checks"><li>Branded carousel templates</li><li>Captions and hashtags generated</li><li>Comment-to-DM keyword funnels</li><li>Scheduling and weekly reports</li></ul>
    <p style="margin-top:1.6rem"><a class="more" href="/studio">See the Studio</a></p></div>
</div></section>

<section class="nv-sec alt" id="creative"><div class="wrap">
  <div class="nv-head"><span class="bar"></span><span class="eyebrow">Rendering, video and design</span><h2>Creative production, powered by GPUs.</h2><p class="lede">3D renders in Blender, Reels and motion graphics, and brand design, all produced on the same GPU workflows we install for clients.</p></div>
  <div class="split">
    <div class="timeline" role="img" aria-label="Video editing timeline example">
      <div class="ruler"><span>00:00</span><span>00:05</span><span>00:10</span><span>00:15</span><span>00:20</span></div>
      <div class="track"><span>TEXT</span><div class="lane"><span class="clip" style="left:4%;width:30%;background:#7B2BFF">Hook: “Your front desk…”</span><span class="clip" style="left:52%;width:40%;background:#7B2BFF">Comment AGENT</span><div class="playhead"></div></div></div>
      <div class="track"><span>V2</span><div class="lane"><span class="clip" style="left:18%;width:44%;background:#F0287A">3D cursor render.mp4</span></div></div>
      <div class="track"><span>V1</span><div class="lane"><span class="clip" style="left:0;width:36%;background:#2b5bff">Studio B-roll</span><span class="clip" style="left:37%;width:33%;background:#1D8BF7">Product shot</span><span class="clip" style="left:71%;width:29%;background:#0A5CE0">Logo sting</span></div></div>
      <div class="track"><span>A1</span><div class="lane"><div class="wave"></div></div></div>
      <div class="track"><span>CC</span><div class="lane"><span class="clip" style="left:4%;width:88%;background:#2c2c31">Auto captions · 2 lines · bold</span></div></div>
    </div>
    <div class="tiles" style="grid-template-columns:1fr 1fr">
      <article class="tile2"><div class="img"><img src="/assets/brand/pink-cursor-arrow.jpg" alt="" loading="lazy"></div><div class="tb"><span class="lab">3D and motion</span><h3>Renders and animated logos</h3></div></article>
      <article class="tile2"><div class="img"><img src="/assets/carousel/04-graphic-design.jpg" alt="" loading="lazy"></div><div class="tb"><span class="lab">Design</span><h3>Brand kits and campaigns</h3></div></article>
    </div>
  </div>
</div></section>

<section class="nv-sec" id="how"><div class="wrap">
  <div class="nv-head"><span class="bar"></span><span class="eyebrow">How we work</span><h2>Consult. Build. Deploy. Support.</h2></div>
  <div class="steps4"><div><b>01</b><h3>Consult</h3><p>A free call to understand your goals, budget and current tools.</p></div><div><b>02</b><h3>Build</h3><p>We spec hardware, build agents and automations, and design the creative.</p></div><div><b>03</b><h3>Deploy</h3><p>Install, configure and test with you. Nothing goes live without your OK.</p></div><div><b>04</b><h3>Support</h3><p>Monitoring, monthly improvements and a team that answers your emails fast.</p></div></div>
</div></section>

<section class="nv-sec alt" id="work"><div class="wrap">
  <div class="case">
    <div><span class="eyebrow">Client work · Royal Crest</span>
      <h2 style="margin:.6rem 0 1rem;font-size:clamp(1.7rem,3.2vw,2.5rem);font-weight:800">A WhatsApp concierge for a luxury brand.</h2>
      <p class="lede">We built Royal Crest a booking assistant that talks to guests on WhatsApp, understands what they're asking for and keeps the conversation moving toward a confirmed booking.</p>
      <ul class="ticks"><li>Replies instantly, day and night</li><li>Answers from the business's own information</li><li>Collects dates, guests and preferences</li><li>Escalates anything sensitive to a person</li></ul></div>
    <div><img src="/assets/studio/ai-front-desk/thumb-1.jpg" alt="" loading="lazy" style="width:100%;max-width:420px;margin-inline:auto"></div>
  </div>
</div></section>

<section class="nv-sec" id="faq"><div class="wrap">
  <div class="nv-head"><span class="bar"></span><span class="eyebrow">FAQ</span><h2>Questions clients ask us.</h2></div>
  <div class="faq">{faq}</div>
</div></section>

<section class="cta-nv" id="contact"><div class="wrap">
  <div><h2>Let's build your agents, servers and content.</h2><p>Free 15-minute call. Tell us what you want to automate, render or run, and we'll send a written plan and quote.</p><p class="contact-line">{CONFIG["email"]}</p></div>
  <a class="nv-btn solid" href="{WA}" target="_blank" rel="noopener">Email us in Gmail</a>
</div></section>
</main>
{footer()}'''
    return head("Karl Agentic | AI agents, GPU servers and creative tech", "Tech consulting from Karl Agentic: AI agents and bots, social media automation, server installation, NVIDIA GPUs sourced in South Africa, 3D rendering, video and design.", "/") + body

def hardware_page():
    cards = "".join(hw_card(*x) for x in HARDWARE)
    body = f'''{header("hardware")}
<main class="nv">
<section class="nv-hero"><div class="wrap">
  <div><span class="eyebrow">GPUs · Workstations · Servers · Edge AI</span>
    <h1>Hardware for AI,<br>rendering and <span>video.</span></h1>
    <p class="lede">We source NVIDIA GPUs, AI workstations and GPU servers from suppliers in South Africa, then deliver, install and configure them for your workload.</p>
    <div class="ctas"><a class="nv-btn solid" href="{gmail("Quote request: hardware", "I'd like a hardware quote.")}" target="_blank" rel="noopener">Request a quote</a><a class="nv-btn line" href="#catalogue">Browse categories</a></div></div>
  <div class="logo-card"><img src="/assets/hw/rack.jpg" alt="Illustration of a GPU server rack" width="1200" height="800"></div>
</div></section>
<section class="nv-sec" id="catalogue"><div class="wrap">
  <div class="nv-head"><span class="bar"></span><span class="eyebrow">Categories</span><h2>Pick a starting point. We'll spec the rest.</h2></div>
  <div class="hw-row">{cards}</div>
  <p class="note-sm">Illustrations are representative, not photos of specific products. NVIDIA, GeForce, RTX, DGX and Jetson are trademarks of NVIDIA Corporation. Karl Agentic is an independent consultancy and is not affiliated with NVIDIA. Current models, prices, stock and warranty are confirmed in writing with each quote.</p>
</div></section>
<section class="nv-sec alt" id="prices"><div class="wrap">
  <div class="nv-head"><span class="bar"></span><span class="eyebrow">South African price guide</span><h2>What these GPUs cost locally.</h2><p class="lede">The average of the four lowest prices we found at South African stores. Your quote uses live supplier pricing on the day.</p></div>
  {price_table(load_prices())}
</div></section>
<section class="nv-sec"><div class="wrap">
  <div class="nv-head"><span class="bar"></span><span class="eyebrow">How sourcing works</span><h2>From workload to working machine.</h2></div>
  <div class="steps4"><div><b>01</b><h3>Workload</h3><p>Tell us what you'll run: rendering, video, local AI, servers or edge devices.</p></div><div><b>02</b><h3>Spec and compare</h3><p>We recommend a configuration and compare prices from South African suppliers.</p></div><div><b>03</b><h3>Quote</h3><p>A written quote with model, price, warranty and delivery time.</p></div><div><b>04</b><h3>Install</h3><p>Delivery, installation, drivers, CUDA, Docker and your software stack.</p></div></div>
</div></section>
<section class="cta-nv"><div class="wrap"><div><h2>Not sure what you need?</h2><p>Send us your workload and budget. We'll recommend the right GPU or server, or tell you if the cloud is the better deal.</p></div><a class="nv-btn solid" href="{WA}" target="_blank" rel="noopener">Email us in Gmail</a></div></section>
</main>
{footer()}'''
    return head("Hardware | Karl Agentic", "NVIDIA GPUs, AI workstations, GPU servers and edge AI hardware sourced in South Africa, delivered, installed and configured by Karl Agentic.", "/hardware", "/assets/hw/rack.jpg") + body

# ---------------------------------------------------------------- academy pages
def item_html(i, it):
    name, kicker, text, tryit, link = it
    try_block = f'<div class="try"><b>TRY THIS</b>{tryit}</div>'
    ext = f'<a class="ext" href="{link}" target="_blank" rel="noopener">Learn more ↗</a>' if link else ""
    return f'<article class="item"><div class="top"><h3>{name}</h3><span class="num">{i:02d} · {kicker.upper()}</span></div><p>{text}</p>{try_block}{ext}</article>'

def prompt_html(i, p):
    name, text = p
    return f'<article class="item"><div class="top"><h3>{name}</h3><span class="num">PROMPT {i:02d}</span></div><div class="prompt"><pre class="code">{html.escape(text)}</pre><button class="copy" type="button">Copy</button></div></article>'

def aside(current):
    cur = ' aria-current="page"'
    links = "".join(f'<a class="series" href="/academy/{s["slug"]}"{cur if s["slug"]==current else ""}><img src="/assets/covers/{s["cover"]}.jpg" alt="" loading="lazy">{s["title"]}</a>' for s in SERIES)
    return f'''<aside class="aside">
  <div class="box navy"><span class="eyebrow" style="color:#8EC9FF">Want this done for you?</span><h3 style="color:#fff">We build agents with these tools.</h3><p>Get a free demo of an AI agent built around your business.</p><a class="btn btn-pink" href="{WA}" target="_blank" rel="noopener">Book a demo</a></div>
  <div class="box"><span class="eyebrow">All series</span>{links}</div>
</aside>'''

def series_page(s):
    if "prompts" in s:
        items = "".join(prompt_html(i+1, p) for i,p in enumerate(s["prompts"]))
        count = f'{len(s["prompts"])} prompts'
    else:
        items = "".join(item_html(i+1, it) for i,it in enumerate(s["items"]))
        count = f'{len(s["items"])} lessons'
    note = f'<div class="item" style="background:#FFF4F8;border-color:#F8C6DA"><p style="color:#0B1530"><b>Note:</b> {s["note"]}</p></div>' if s.get("note") else ""
    title = f'{s["title"]}: {s["part"]}'
    body = f'''{header("academy")}
<main>
<section class="art-hero"><div class="wrap">
  <div>
    <div class="crumbs"><a href="/academy">ACADEMY</a> / {s["tag"].upper()}</div>
    <h1>{s["pre"]} <em class="serif">{s["title"]}</em></h1>
    <p class="lede">{s["intro"]}</p>
    <div class="meta"><span class="pill">{s["part"].upper()}</span><span class="pill">{count.upper()}</span><span class="pill">FROM OUR INSTAGRAM SERIES</span></div>
  </div>
  <img src="/assets/covers/{s["cover"]}.jpg" alt="{s["pre"]} {s["title"]} {s["part"]} cover" width="720" height="900">
</div></section>
<div class="wrap article">
  <div class="items">{items}{note}</div>
  {aside(s["slug"])}
</div>
</main>
{footer()}'''
    return head(f"{title} | Karl Agentic Academy", s["intro"][:155], f'/academy/{s["slug"]}', f'/assets/covers/{s["cover"]}.jpg') + body

def academy_hub():
    covers = "".join(f'<a class="cover" href="/academy/{s["slug"]}"><img src="/assets/covers/{s["cover"]}.jpg" alt="{s["pre"]} {s["title"]} {s["part"]} cover" loading="lazy" width="720" height="900"><span class="lab">{s["title"]}<span>{s["tag"].upper()}</span></span></a>' for s in SERIES)
    slides = "".join(f'<img src="/assets/carousel/{n}.jpg" alt="Academy carousel slide {i+1}" loading="lazy" width="900" height="1125">' for i,n in enumerate(["01-cover","02-blender","03-adobe","04-graphic-design","05-automation","06-github","07-websites","08-llms","09-cta"]))
    body = f'''{header("academy")}
<main>
<section class="hub-hero"><div class="wrap">
  <span class="eyebrow" style="color:#8EC9FF">Karl Agentic Academy</span>
  <h1>Learn the tools <em class="serif">that build brands.</em></h1>
  <p class="lede">Every series on our Instagram has a full guide here: the tools, the shortcuts and something to try today.</p>
</div></section>
<section class="block dark" style="padding-top:1rem"><div class="wrap"><div class="covers">{covers}</div></div></section>
<section class="block"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Start here</span><h2>The 7-tool <em class="serif">crash course.</em></h2><p class="lede">Our first carousel, slide by slide. Swipe sideways.</p></div>
  <div class="slides">{slides}</div>
</div></section>
</main>
{footer()}'''
    return head("Academy | Karl Agentic", "Free guides on Blender, Adobe, graphic design, automation, GitHub, websites and LLMs from the Karl Agentic Instagram series.", "/academy") + body

def brand_page():
    src = (ROOT / "brand" / "kit.src.html").read_text()
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
            '<meta name="description" content="Karl Agentic brand kit: logo, colours, typography, voice and applications.">'
            '<link rel="icon" href="/favicon.ico" sizes="any"><style>body{margin:0}</style>'
            + src.replace("<title>", '<title>', 1) +
            '<p style="text-align:center;padding:2rem;font-family:Manrope,sans-serif"><a href="/" style="color:#0A5CE0;font-weight:700">← Back to karlagentic</a></p></body></html>')

def studio_page():
    posts = json.loads((ROOT / "studio" / "posts.json").read_text())
    cats = ["All"] + sorted({p["cat"] for p in posts})
    chips = "".join(f'<button type="button" aria-pressed="{"true" if c=="All" else "false"}">{c}</button>' for c in cats)
    body = f'''{header("studio")}
<main>
<section class="studio-hero"><div class="wrap">
  <span class="eyebrow" style="color:#8EC9FF">Studio · Instagram posts, ready to publish</span>
  <h1>Five slides. <em class="serif">One tap.</em></h1>
  <p class="lede">Every post is a 5-slide carousel at 1080 × 1350 (Instagram 4:5). The artwork flows from slide to slide as you swipe. Download all five at once, then post them in order with the caption.</p>
  <div class="studio-bar"><div class="filters" id="studio-filters">{chips}</div>
    <div style="display:flex;gap:.8rem;align-items:center;flex-wrap:wrap"><span class="eyebrow" id="studio-count" style="color:#93A1BF">{len(posts)} posts</span><button class="btn btn-pink" id="dl-all" type="button">Download everything (.zip)</button></div></div>
</div></section>
<div class="wrap"><div class="studio-grid" id="studio-grid" aria-live="polite"><p style="color:var(--muted)">Loading posts…</p></div></div>
</main>
<script src="/js/vendor/jszip.min.js"></script>
<script src="/js/studio.js" defer></script>
{footer()}'''
    return head("Studio | Karl Agentic", "Download ready-made 5-slide Instagram carousels with captions: AI agents, automation, design, 3D, web and marketing.", "/studio", "/assets/studio/what-is-an-ai-agent/what-is-an-ai-agent-1.jpg") + body


def write_readme_sources(data):
    lines = [f"Checked {data['checked']}. {data['method']}", "", f"Exchange rate: 1 USD = R{data['fx']['usd_zar']} ([{data['fx']['source']}]({data['fx']['url']}), {data['fx']['date']}).", ""]
    stores = {}
    for pr in data["products"]:
        if not pr["used"]:
            lines += [f"### {pr['name']}", "", pr.get("note", ""), ""]
            continue
        fx = data["fx"]["usd_zar"]
        lines += [f"### {pr['name']}: average {usd(pr['avg'], fx)} ({rand(pr['avg'])})", "", "| Store | Item | Price (USD) | Price (ZAR) | Note |", "|---|---|---|---|---|"]
        for l in pr["used"]:
            lines.append(f"| [{l['store']}]({l['url']}) | {l['item']} | {usd(l['price'], fx)} | {rand(l['price'])} | {l['note']} |")
            stores.setdefault(l["store"], l["url"].split("/")[2])
        lines.append("")
    lines += ["### All stores and where each price was found", ""] + [f"- **{k}**: price found on {v}" for k, v in stores.items()] + [""]
    md = "\n".join(lines)
    rp = ROOT / "README.md"; t = rp.read_text()
    start, end = "<!-- prices:start -->", "<!-- prices:end -->"
    block = f"{start}\n{md}\n{end}"
    if start in t:
        t = t[:t.index(start)] + block + t[t.index(end) + len(end):]
    else:
        t += "\n## South African price guide and store locations\n\nGenerated from `data/prices.json` by `scripts/build.py`. To refresh, ask Claude Code to re-check the prices with web search, update the JSON, and rebuild.\n\n" + block + "\n"
    rp.write_text(t)

def sitemap():
    urls = ["/", "/hardware", "/academy", "/studio", "/brand"] + [f'/academy/{s["slug"]}' for s in SERIES]
    rows = "".join(f"<url><loc>{CONFIG['site_url']}{u}</loc></url>" for u in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{rows}</urlset>\n'

if __name__ == "__main__":
    (ROOT / "index.html").write_text(landing())
    (ROOT / "academy").mkdir(exist_ok=True)
    (ROOT / "academy" / "index.html").write_text(academy_hub())
    for s in SERIES:
        (ROOT / "academy" / f'{s["slug"]}.html').write_text(series_page(s))
    (ROOT / "brand" / "index.html").write_text(brand_page())
    (ROOT / "hardware").mkdir(exist_ok=True)
    (ROOT / "hardware" / "index.html").write_text(hardware_page())
    (ROOT / "studio").mkdir(exist_ok=True)
    (ROOT / "studio" / "index.html").write_text(studio_page())
    (ROOT / "sitemap.xml").write_text(sitemap())
    write_readme_sources(load_prices())
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {CONFIG['site_url']}/sitemap.xml\n")
    print("built", 5 + len(SERIES), "pages")
