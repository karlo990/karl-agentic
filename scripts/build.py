#!/usr/bin/env python3
"""Builds the static Karl Agentic site.

Edit CONFIG and the SERIES content below, then run:
    python3 scripts/build.py
It rewrites index.html, academy/*.html and brand/index.html. Commit the result;
Vercel serves the files as they are (no build step needed).
"""
import html, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------- config
CONFIG = {
    "site_url": "https://karlagentic.vercel.app",       # change when the domain is live
    "whatsapp": "https://wa.me/000000000000",           # TODO: your WhatsApp Business number, digits only
    "whatsapp_text": "Hi Karl Agentic, I'd like a free demo of an AI agent for my business.",
    "email": "hello@karlagentic.com",                   # TODO: real inbox
    "instagram": "https://instagram.com/karlagentic",
    "instagram_handle": "@karlagentic",
}
WA = f'{CONFIG["whatsapp"]}?text={html.escape(CONFIG["whatsapp_text"]).replace(" ", "%20")}'

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
<meta name="theme-color" content="#0B1530">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" href="/assets/logo/favicon-32.png"><link rel="apple-touch-icon" href="/assets/logo/apple-touch-icon.png">
{FONTS}
<link rel="stylesheet" href="/css/site.css">
</head><body>'''

def header(active=""):
    def a(href, label, key):
        cur = ' aria-current="page"' if key == active else ""
        return f'<a href="{href}"{cur}>{label}</a>'
    return f'''<header class="site-head"><div class="wrap">
  <a class="brand" href="/" aria-label="Karl Agentic home"><img src="/assets/logo/logo-mark-transparent.png" alt="" width="34" height="34"><b>Karl</b><span>Agentic</span></a>
  <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav class="nav" id="nav">{a("/#agents","Agents","agents")}{a("/#how","How it works","how")}{a("/#work","Work","work")}{a("/academy","Academy","academy")}{a("/studio","Studio","studio")}{a("/brand","Brand","brand")}
    <a class="btn btn-pink" href="{WA}" target="_blank" rel="noopener">Book a demo</a></nav>
</div></header>'''

def footer():
    s = "".join(f'<a href="/academy/{x["slug"]}">{x["title"]}</a>' for x in SERIES[:5])
    return f'''<footer class="site-foot"><div class="wrap">
  <div><a class="brand" href="/" style="color:#fff"><img src="/assets/logo/logo-mark-transparent.png" alt="" width="34" height="34"><b>Karl</b><span>Agentic</span></a>
    <p style="margin-top:.9rem;max-width:34ch">Verified AI agents for real businesses. Booking, marketing, sales and operations.</p></div>
  <div><h4>Company</h4><a href="/#agents">Agents</a><a href="/#how">How it works</a><a href="/#work">Work</a><a href="/#faq">FAQ</a><a href="/studio">Studio</a><a href="/brand">Brand kit</a></div>
  <div><h4>Academy</h4>{s}<a href="/academy">All series →</a></div>
  <div><h4>Contact</h4><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a><a href="{CONFIG["instagram"]}" target="_blank" rel="noopener">Instagram {CONFIG["instagram_handle"]}</a><span style="user-select:all">{CONFIG["email"]}</span></div>
  <div class="legal"><span>© 2026 Karl Agentic. Part of the KarlCon family.</span><span>Built with HTML, hosted on Vercel.</span></div>
</div></footer>
<div class="toast" id="toast" role="status"></div>
<script src="/js/site.js" defer></script>
</body></html>'''

ICONS = {
 "book":'<rect x="4" y="6" width="24" height="22" rx="5" fill="none" stroke="#1D8BF7" stroke-width="3"/><path d="M4 13h24M11 3v6M21 3v6" stroke="#1D8BF7" stroke-width="3" stroke-linecap="round"/><path d="M11 20l3.5 3.5L21 17" fill="none" stroke="#F0287A" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
 "reach":'<path d="M5 13v6l14 7V6L5 13z" fill="none" stroke="#1D8BF7" stroke-width="3" stroke-linejoin="round"/><path d="M24 11c2 1.5 2 8.5 0 10" fill="none" stroke="#F0287A" stroke-width="3" stroke-linecap="round"/><path d="M8 19l2 7" stroke="#1D8BF7" stroke-width="3" stroke-linecap="round"/>',
 "close":'<circle cx="16" cy="16" r="12" fill="none" stroke="#1D8BF7" stroke-width="3"/><circle cx="16" cy="16" r="5" fill="none" stroke="#1D8BF7" stroke-width="3"/><path d="M16 16l9-9" stroke="#F0287A" stroke-width="3" stroke-linecap="round"/><path d="M22 5h4v4" fill="none" stroke="#F0287A" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
 "ops":'<circle cx="16" cy="16" r="5" fill="none" stroke="#F0287A" stroke-width="3"/><path d="M16 3v5M16 24v5M3 16h5M24 16h5M6.8 6.8l3.5 3.5M21.7 21.7l3.5 3.5M6.8 25.2l3.5-3.5M21.7 10.3l3.5-3.5" stroke="#1D8BF7" stroke-width="3" stroke-linecap="round"/>',
}
def icon(k): return f'<span class="ic"><svg width="30" height="30" viewBox="0 0 32 32" aria-hidden="true">{ICONS[k]}</svg></span>'

# ---------------------------------------------------------------- landing page
def landing():
    covers = "".join(f'<a class="cover" href="/academy/{s["slug"]}"><img src="/assets/covers/{s["cover"]}.jpg" alt="{s["pre"]} {s["title"]} {s["part"]} cover" loading="lazy" width="720" height="900"><span class="lab">{s["title"]}<span>{s["tag"].upper()}</span></span></a>' for s in SERIES)
    faqs = [
      ("What is an AI agent?","Software that understands messages, makes decisions and takes actions, such as replying to a customer, checking your calendar and confirming a booking. A chatbot only talks. An agent does the work."),
      ("Will it replace my staff?","No. It handles the repetitive first steps, like answering the same questions and collecting details, so your team spends time on guests and sales instead of typing."),
      ("Do I stay in control?","Yes. You approve the agent's tone, rules and answers before it goes live, and you can require a person to approve sensitive replies such as discounts or refunds."),
      ("Which channels do you support?","WhatsApp is our main channel, plus website chat, email, Instagram DMs and Google Calendar. We connect to the tools you already use where they have an API."),
      ("How long does it take?","A focused first agent, such as a booking assistant, is usually live in about two weeks after the discovery call."),
      ("How much does it cost?","Every business is different, so we quote after a free demo. You get a fixed setup price and a monthly running fee, with no surprises."),
    ]
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faqs)
    body = f'''{header()}
<main>
<section class="hero"><div class="wrap">
  <div>
    <span class="eyebrow">AI agents for real businesses</span>
    <h1>Hire agents that <em class="serif">actually do the work.</em></h1>
    <p class="lede">We design, install and run AI agents that answer customers, book appointments, run your marketing and chase every lead. Tested, approved by you, and working 24/7.</p>
    <div class="ctas"><a class="btn btn-pink" href="{WA}" target="_blank" rel="noopener">Book a free demo →</a><a class="btn btn-ghost" href="#work">See a live example</a></div>
    <div class="proof"><span>✔ VERIFIED BEFORE LAUNCH</span><span>✔ YOU APPROVE EVERY RULE</span><span>✔ WHATSAPP-FIRST</span></div>
  </div>
  <div class="hero-art">
    <img src="/assets/brand/karl-agentic-hero.jpg" alt="Karl Agentic logo: a verified seal with a cursor clicking the word Agentic" width="1200" height="1200" fetchpriority="high">
    <div class="float f1"><span class="dot"></span><span>Booked: table for 4<small>Fri 19:30 · example</small></span></div>
    <div class="float f2"><span class="dot" style="background:#1D8BF7;box-shadow:0 0 0 4px rgba(29,139,247,.18)"></span><span>12 leads replied<small>in under a minute · example</small></span></div>
  </div>
</div></section>

<section class="block" id="agents"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Four agent lines</span><h2>One team of agents, <em class="serif">four jobs.</em></h2><p class="lede">Start with one agent, then add more as you grow. Every agent shares the same memory of your business.</p></div>
  <div class="grid-4">
    <article class="card">{icon("book")}<span class="code">KA-BOOK</span><h3>Booking agents</h3><p>Answer WhatsApp, web chat and calls. Check availability, take details and confirm bookings.</p></article>
    <article class="card">{icon("reach")}<span class="code">KA-REACH</span><h3>Marketing agents</h3><p>Plan posts, write captions, run email campaigns and send you a weekly report on what worked.</p></article>
    <article class="card">{icon("close")}<span class="code">KA-CLOSE</span><h3>Sales agents</h3><p>Reply to every lead in under a minute, qualify them, follow up and put warm deals in your calendar.</p></article>
    <article class="card">{icon("ops")}<span class="code">KA-OPS</span><h3>Operations agents</h3><p>Invoices, reminders, reports and admin: the repetitive work that eats your team's week.</p></article>
  </div>
</div></section>

<section class="block" id="how" style="padding-top:0"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">How it works</span><h2>From first call to <em class="serif">live agent.</em></h2></div>
  <div class="steps">
    <div class="step"><span class="n">01 · DISCOVER</span><h3>Free demo call</h3><p>We map the questions you answer every day and where time is lost.</p></div>
    <div class="step"><span class="n">02 · BUILD</span><h3>We build it</h3><p>Your agent is trained on your prices, policies and tone, and connected to your tools.</p></div>
    <div class="step"><span class="n">03 · VERIFY</span><h3>You approve it</h3><p>You test it, change the rules and sign off. Nothing goes live without your OK.</p></div>
    <div class="step"><span class="n">04 · RUN</span><h3>It works 24/7</h3><p>We monitor it, improve it every month and report what it handled.</p></div>
  </div>
</div></section>

<section class="block" id="work" style="padding-top:0"><div class="wrap">
  <div class="case">
    <div>
      <span class="eyebrow">Client work · Royal Crest</span>
      <h2 style="margin:.6rem 0 1rem;font-size:clamp(1.7rem,3.2vw,2.5rem)">A WhatsApp concierge for a <em class="serif">luxury brand.</em></h2>
      <p class="lede">We built Royal Crest a booking assistant that talks to guests on WhatsApp, understands what they're asking for and keeps the conversation moving toward a confirmed booking.</p>
      <ul class="ticks"><li>Replies instantly, day and night</li><li>Answers questions from the business's own information</li><li>Collects dates, guests and preferences before handing over</li><li>Escalates anything sensitive to a real person</li></ul>
    </div>
    <div class="chat" aria-label="Example conversation"><span class="eyebrow" style="color:#8EC9FF">Example conversation</span>
      <div class="bub in">Hi, do you have availability for 2 adults next weekend?<span class="t">GUEST · 21:14</span></div>
      <div class="bub out">Good evening! Yes, we have availability on Friday and Saturday. Would you like the garden suite or the classic room? I can share prices for both. 🌿<span class="t">KARL AGENT · 21:14</span></div>
      <div class="bub in">Garden suite please, Friday to Sunday.<span class="t">GUEST · 21:15</span></div>
      <div class="bub out">Lovely choice. I've noted 2 adults, garden suite, Friday to Sunday. May I have your full name to prepare the booking?<span class="t">KARL AGENT · 21:15</span></div>
    </div>
  </div>
</div></section>

<section class="block dark" id="academy"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Karl Agentic Academy</span><h2>Learn the tools <em class="serif">behind the agents.</em></h2><p class="lede">The full guides behind our Instagram series: 3D, design, automation, code and AI. Free, practical, and updated as we post.</p></div>
  <div class="covers">{covers}</div>
  <p style="margin-top:2rem"><a class="btn btn-ghost" href="/academy">Open the Academy →</a></p>
</div></section>

<section class="block" id="faq"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">FAQ</span><h2>Questions owners <em class="serif">ask us.</em></h2></div>
  <div class="faq">{faq}</div>
</div></section>

<section class="block" style="padding-top:0"><div class="wrap">
  <div class="cta-band">
    <div><h2>Your front desk never sleeps. Neither does your agent.</h2><p>Book a free 15-minute demo. We'll show you an agent built around your business before you spend anything.</p><p class="contact-line">{CONFIG["email"]}</p></div>
    <a class="btn btn-light" href="{WA}" target="_blank" rel="noopener">Chat on WhatsApp →</a>
  </div>
</div></section>
</main>
{footer()}'''
    return head("Karl Agentic | AI agents that do the work", "Karl Agentic designs, installs and runs verified AI agents for businesses: booking, marketing, sales and operations, on WhatsApp and the web.", "/") + body

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

def sitemap():
    urls = ["/", "/academy", "/studio", "/brand"] + [f'/academy/{s["slug"]}' for s in SERIES]
    rows = "".join(f"<url><loc>{CONFIG['site_url']}{u}</loc></url>" for u in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{rows}</urlset>\n'

if __name__ == "__main__":
    (ROOT / "index.html").write_text(landing())
    (ROOT / "academy").mkdir(exist_ok=True)
    (ROOT / "academy" / "index.html").write_text(academy_hub())
    for s in SERIES:
        (ROOT / "academy" / f'{s["slug"]}.html').write_text(series_page(s))
    (ROOT / "brand" / "index.html").write_text(brand_page())
    (ROOT / "studio").mkdir(exist_ok=True)
    (ROOT / "studio" / "index.html").write_text(studio_page())
    (ROOT / "sitemap.xml").write_text(sitemap())
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {CONFIG['site_url']}/sitemap.xml\n")
    print("built", 4 + len(SERIES), "pages")
