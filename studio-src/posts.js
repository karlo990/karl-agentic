// Content for the Studio carousels. Each post = cover + 3 explainer slides + "Comment AGENT" slide.
// Slide types: big, list, steps, compare, prompt. Title lines are split with "|".
window.POSTS = [
{slug:"what-is-an-ai-agent",cat:"Agents",pre:"Simply",title:"What is an|AI agent?",sub:"Explained in 5 slides",pal:"brand",art:"orbs",
 hook:"Everyone says \"AI agent\". Here's what it actually means for your business 👇",gift:"a list of agent ideas for your business",
 slides:[
  {t:"compare",k:"The difference",h:"A chatbot talks.|An agent does the work.",a:{l:"Chatbot",x:["Answers questions","Waits for you to act","Stays inside the chat"]},b:{l:"Agent",x:["Takes real actions","Works 24/7 on its own","Uses your calendar, CRM and payments"]}},
  {t:"steps",k:"How it works",h:"Listen. Think. Act. Report.",items:[["Listens","Reads a message on WhatsApp, email or web chat"],["Thinks","An LLM works out what the customer wants"],["Acts","Books, updates or replies using your tools"],["Reports","Logs it and tells you what happened"]]},
  {t:"list",k:"Start here",h:"Where agents pay off first",items:[["Bookings and enquiries","The same questions, answered instantly"],["Lead follow-up","Every lead gets a reply in minutes"],["Invoices and reminders","Consistent, polite, never forgotten"]]}
 ]},
{slug:"whatsapp-booking-agent",cat:"Agents",pre:"Build it",title:"WhatsApp|booking agent",sub:"Step by step",pal:"ocean",art:"waves",
 hook:"Your customers already live on WhatsApp. Let an agent book them while you sleep 💬",gift:"our WhatsApp agent setup checklist",
 slides:[
  {t:"big",k:"The problem",h:"Most customers ask the same ten questions.",p:"Prices, availability, location, opening hours. An agent answers them instantly, at 2pm or 2am, in your tone."},
  {t:"steps",k:"The build",h:"Four steps to go live",items:[["Connect WhatsApp","Use the WhatsApp Business Platform"],["Teach it your business","Prices, rooms, policies, FAQs"],["Connect your calendar","So it can check and hold real slots"],["Set the rules","Decide what always goes to a human"]]},
  {t:"list",k:"Non-negotiable",h:"Rules we always add",items:[["Escalate complaints and refunds","A person handles anything sensitive"],["Never invent prices","Only quote from your price list"],["Confirm before booking","Repeat the details back to the guest"]]}
 ]},
{slug:"reply-to-leads-fast",cat:"Sales",pre:"Sales",title:"Reply to|leads in 60s",sub:"Speed wins deals",pal:"ember",art:"rays",
 hook:"The business that replies first usually wins. Here's how to never be second again ⚡",gift:"3 follow-up message templates",
 slides:[
  {t:"big",k:"Why speed matters",h:"The first reply usually wins the customer.",p:"People enquire with several businesses at once. A fast, helpful answer builds trust before anyone else responds."},
  {t:"steps",k:"The system",h:"Instant follow-up, automated",items:[["New enquiry","Form, Instagram DM or WhatsApp"],["AI drafts a reply","Personal, using what they asked"],["Sent and saved","Reply goes out, lead lands in your CRM"],["Follow up","A gentle nudge after two days of silence"]]},
  {t:"list",k:"Write it well",h:"Follow-ups that get answers",items:[["Use their name and question","Show you actually read it"],["One clear next step","A call, a link or a date"],["Keep it under 80 words","Easy to read on a phone"]]}
 ]},
{slug:"the-prompt-formula",cat:"AI",pre:"Copy this",title:"The prompt|formula",sub:"Role · Task · Context · Format",pal:"violet",art:"silk",
 hook:"Bad AI answers usually come from vague prompts. Use this 4-part formula instead 🧠",gift:"our 25-prompt pack for business",
 slides:[
  {t:"compare",k:"See the difference",h:"Same AI. Better prompt.",a:{l:"Weak",x:["Write a caption for my hotel."]},b:{l:"Strong",x:["You are a social media manager for a mountain lodge. Write 3 captions about our sunrise breakfast for couples. Warm tone, under 40 words each."]}},
  {t:"list",k:"The formula",h:"Four parts, every time",items:[["Role","Who the AI should be"],["Task","Exactly what you want done"],["Context","Facts, audience, examples"],["Format","Length, tone and layout"]]},
  {t:"prompt",k:"Template",h:"Copy, fill, paste",code:"You are [role] for [business].\n[Task: what to write or do].\nContext: [audience, facts, examples].\nFormat: [length], [tone], [layout]."}
 ]},
{slug:"content-pillars",cat:"Marketing",pre:"Marketing",title:"Content|pillars",sub:"Never run out of ideas",pal:"sunset",art:"ribbon",
 hook:"Stop asking \"what should I post today?\" Pick three pillars and rotate them 🗂",gift:"a 30-day content calendar template",
 slides:[
  {t:"big",k:"The idea",h:"Post with a plan, not a mood.",p:"Choose three pillars and rotate them. Your audience learns what to expect, and you always know what comes next."},
  {t:"list",k:"The three pillars",h:"Educate. Prove. Sell.",items:[["Educate","Teach something useful in your field"],["Prove","Results, reviews, behind the scenes"],["Sell","Offers with one clear call to action"]]},
  {t:"steps",k:"A simple week",h:"Four posts, zero stress",items:[["Monday","Educational carousel"],["Wednesday","Proof: a review or result"],["Friday","Your offer"],["Sunday","Story Q&A"]]}
 ]},
{slug:"hooks-that-work",cat:"Marketing",pre:"Stop the scroll",title:"Hooks|that work",sub:"The first line wins",pal:"red",art:"streaks",
 hook:"Your content isn't bad. Your first line is. Steal these hook formats 🎣",gift:"50 hooks written for your niche",
 slides:[
  {t:"big",k:"The truth",h:"You have about one second.",p:"On a fast scroll, the first line or first frame decides if someone stops. Lead with the benefit or the problem."},
  {t:"list",k:"Formats",h:"Hook formats to steal",items:[["\"Stop doing X if you want Y\"","Calls out a mistake"],["\"I tested X so you don't have to\"","Promises saved time"],["\"The 3 tools behind ___\"","Curiosity plus a list"],["\"Nobody tells you this about ___\"","Insider knowledge"]]},
  {t:"compare",k:"Rewrite it",h:"Weak vs strong",a:{l:"Weak",x:["Here are some tips for your business."]},b:{l:"Strong",x:["Your website is losing bookings at night. Here's why."]}}
 ]},
{slug:"60-30-10-colour",cat:"Design",pre:"Design rule",title:"60 · 30 · 10|colour",sub:"Look expensive",pal:"candy",art:"orbs",
 hook:"The colour rule designers use to make anything look expensive 🎨",gift:"5 ready-made brand palettes",
 slides:[
  {t:"big",k:"The rule",h:"60 · 30 · 10",p:"60% main colour, 30% secondary, 10% accent. It works for posts, websites, packaging and even interiors."},
  {t:"list",k:"Where each goes",h:"Split it like this",items:[["60%","Backgrounds and large areas"],["30%","Cards, text and secondary shapes"],["10%","Buttons and highlights only"]]},
  {t:"list",k:"Pro tip",h:"Make the accent mean something",items:[["Use it for actions","Book, Buy, Comment"],["Never for long text","It gets tiring to read"],["Keep it consistent","Same accent everywhere you post"]]}
 ]},
{slug:"two-fonts-max",cat:"Design",pre:"Design rule",title:"Two fonts.|That's it.",sub:"Typography basics",pal:"mono",art:"silk",
 hook:"Too many fonts is the fastest way to look amateur. Here's the fix ✍️",gift:"our favourite free font pairs",
 slides:[
  {t:"compare",k:"The mistake",h:"More fonts ≠ more style",a:{l:"Messy",x:["4+ fonts","Every heading a different style","Nothing stands out"]},b:{l:"Clean",x:["One display font","One body font","Clear hierarchy"]}},
  {t:"list",k:"The system",h:"How to pair fonts",items:[["Headline font","Bold, with character"],["Body font","Calm and easy to read"],["Big size jump","Headlines at least 2× body size"]]},
  {t:"list",k:"Free on Google Fonts",h:"Pairs we like",items:[["Inter Tight + Inter","Modern and neutral"],["Unbounded + Manrope","Wide, techy, friendly"],["Instrument Serif + Inter","Editorial and premium"]]}
 ]},
{slug:"white-space",cat:"Design",pre:"Design rule",title:"Space makes|it premium",sub:"Less, but louder",pal:"pearl",art:"waves",
 hook:"Luxury brands all have one thing in common: room to breathe 🤍",gift:"a clean carousel template",
 slides:[
  {t:"big",k:"The principle",h:"Empty space is not wasted space.",p:"White space directs attention. The less you put on a slide, the louder the important part becomes."},
  {t:"list",k:"Do this",h:"Three quick fixes",items:[["Double your margins","Pull everything away from the edges"],["One idea per slide","Split long posts into a carousel"],["Group related things","Close together = belongs together"]]},
  {t:"compare",k:"Before and after",h:"Crowded vs clean",a:{l:"Crowded",x:["Five messages fighting","Logos in every corner","Text to the edges"]},b:{l:"Clean",x:["One message","One image","One button"]}}
 ]},
{slug:"carousels-that-get-saved",cat:"Marketing",pre:"Marketing",title:"Carousels|that get saved",sub:"The 5-slide structure",pal:"teal",art:"ribbon",
 hook:"This exact 5-slide structure is what you're swiping right now 👀",gift:"this exact 5-slide template",
 slides:[
  {t:"steps",k:"The structure",h:"Five slides, one story",items:[["Cover","A big, clear promise"],["Slide 2","The problem or the why"],["Slides 3–4","The solution in steps"],["Slide 5","One call to action"]]},
  {t:"list",k:"Why it works",h:"Carousels win attention",items:[["People swipe","More time spent on your post"],["People save","Saves show the post is useful"],["Small steps","Easier to learn and remember"]]},
  {t:"list",k:"Design for the swipe",h:"Make them want slide 2",items:[["Let the art flow","Shapes continue across slides"],["Same layout each slide","Text stays where eyes expect"],["Number your slides","People like to know how far to go"]]}
 ]},
{slug:"blender-in-3-steps",cat:"3D",pre:"Selected",title:"Blender|in 3 steps",sub:"Free 3D software",pal:"ember",art:"orbs",
 hook:"Blender is free and it can make your brand look like a million dollars 🧊",gift:"a Blender shortcut cheat sheet",
 slides:[
  {t:"steps",k:"The workflow",h:"Model. Light. Render.",items:[["Model","Start from a cube. Tab to edit, E to extrude"],["Light","Key, fill and rim lights"],["Render","F12, then save as PNG"]]},
  {t:"list",k:"Learn these first",h:"Shortcuts that matter",items:[["G · R · S","Move, rotate, scale"],["Ctrl + B","Bevel edges for realism"],["Ctrl + R","Loop cut to add detail"]]},
  {t:"list",k:"For business",h:"What to make with it",items:[["Product shots","No photographer or studio"],["3D logos and icons","Stand out in the feed"],["Looping animations","Short motion for ads and Reels"]]}
 ]},
{slug:"product-shots-in-3d",cat:"3D",pre:"3D",title:"Product shots|without a studio",sub:"Blender workflow",pal:"gold",art:"rays",
 hook:"No studio, no photographer, no problem. Product shots in Blender 📦",gift:"our product-render lighting setup",
 slides:[
  {t:"big",k:"The look",h:"Clean background. Soft light. One hero.",p:"Premium product images follow the same recipe. Once you build the scene, every new product takes minutes."},
  {t:"steps",k:"The scene",h:"Build it once",items:[["Product","Model it or import the 3D file"],["Backdrop","A curved infinity background"],["Lighting","Area light plus an HDRI for reflections"],["Render","1080 × 1350 for Instagram"]]},
  {t:"list",k:"Look premium",h:"Small details, big difference",items:[["Low roughness","Glossy surfaces catch light"],["Soft contact shadows","Grounds the product"],["Brand colour backdrop","Instantly recognisable"]]}
 ]},
{slug:"generative-fill",cat:"Design",pre:"Useful",title:"Generative|Fill",sub:"Photoshop AI",pal:"violet",art:"aurora",
 hook:"Remove anything. Add anything. Extend any photo. Photoshop's AI in 3 slides ✨",gift:"a Generative Fill prompt list",
 slides:[
  {t:"big",k:"How it works",h:"Select. Type. Done.",p:"Select an area, describe what you want, and Photoshop fills it to match the photo. Leave the prompt empty to remove things."},
  {t:"list",k:"Use it for",h:"Everyday wins",items:[["Remove clutter or people","Clean shots in seconds"],["Extend to 4:5","Generative Expand with the Crop tool"],["Swap backgrounds","Products on brand colours"]]},
  {t:"list",k:"Tips",h:"Better results",items:[["Select a bit wider","Give the AI room to blend"],["Try 3 variations","Pick the best one"],["Check details","Hands, text and logos need a close look"]]}
 ]},
{slug:"logo-to-vector",cat:"Design",pre:"Useful",title:"Turn a logo|into vectors",sub:"Illustrator Image Trace",pal:"lime",art:"pixel",
 hook:"Blurry logo? Fix it properly in about 2 minutes 🖋",gift:"a logo file checklist for printers",
 slides:[
  {t:"big",k:"The problem",h:"A blurry logo costs you trust.",p:"Pixel logos break on signs, shirts and big screens. Vectors stay sharp at any size."},
  {t:"steps",k:"The fix",h:"Image Trace in Illustrator",items:[["Place the image","PNG or JPG of your logo"],["Image Trace","Window → Image Trace, pick a preset"],["Adjust","Colours and threshold"],["Expand","Then clean up the shapes"]]},
  {t:"list",k:"Why vectors",h:"Every brand needs them",items:[["Sharp at any size","Billboard to favicon"],["Easy to recolour","Light, dark, one-colour versions"],["Printers ask for them","SVG, PDF or AI files"]]}
 ]},
{slug:"captions-on-every-reel",cat:"Marketing",pre:"Video",title:"Captions on|every Reel",sub:"Most scroll on mute",pal:"candy",art:"streaks",
 hook:"If your Reel has no captions, a lot of people never hear your message 🔇",gift:"our caption style presets",
 slides:[
  {t:"big",k:"Why",h:"Many people watch with the sound off.",p:"Captions keep them watching, make your message clear and help people who can't play audio."},
  {t:"list",k:"Tools",h:"Auto captions, fast",items:[["Premiere Pro","Speech to Text"],["CapCut","Free auto captions"],["Descript","Edit video by editing text"]]},
  {t:"list",k:"Style",h:"Captions people can read",items:[["Two lines max","Short chunks are easier"],["High contrast, bold","Readable on any frame"],["Avoid the bottom edge","Instagram's buttons cover it"]]}
 ]},
{slug:"trigger-brain-action",cat:"Automation",pre:"Automation",title:"Trigger.|Brain. Action.",sub:"Every automation",pal:"gold",art:"silk",
 hook:"Every automation you'll ever build has the same three parts ⚙️",gift:"5 automation recipes you can copy",
 slides:[
  {t:"steps",k:"The shape",h:"Three parts, always",items:[["Trigger","Something happens: a message, form or payment"],["Brain","AI decides what it means"],["Action","Reply, update a tool or notify you"]]},
  {t:"list",k:"Tools",h:"Pick your platform",items:[["Zapier","Easiest, thousands of apps"],["Make","Visual and great value"],["n8n","Open source, can self-host"]]},
  {t:"list",k:"Start here",h:"Automate these first",items:[["Daily repeats","Anything you do every day"],["Copy and paste","Moving data between apps"],["Reminders","The ones you keep forgetting"]]}
 ]},
{slug:"get-paid-on-time",cat:"Automation",pre:"Operations",title:"Get paid|on time",sub:"Automated reminders",pal:"teal",art:"rings",
 hook:"Chasing invoices is awkward. So let a polite automation do it 💸",gift:"3 reminder message templates",
 slides:[
  {t:"steps",k:"The sequence",h:"Reminders that run themselves",items:[["3 days late","A friendly reminder"],["7 days late","Reminder plus a payment link"],["14 days late","Alert to you to call"]]},
  {t:"list",k:"Message rules",h:"Keep it professional",items:[["Short and polite","Clear amount and due date"],["Always add the link","Make paying one tap"],["Stop when paid","Nothing annoys clients more"]]},
  {t:"compare",k:"The difference",h:"Manual vs automated",a:{l:"Manual",x:["You remember (sometimes)","Awkward conversations","Inconsistent timing"]},b:{l:"Automated",x:["Every invoice, every time","Polite and consistent","You handle exceptions only"]}}
 ]},
{slug:"the-monday-report",cat:"Automation",pre:"Operations",title:"The Monday|report",sub:"Automated with AI",pal:"ocean",art:"dots",
 hook:"Start every week knowing your numbers, without opening a spreadsheet 📊",gift:"the report template and prompt",
 slides:[
  {t:"big",k:"The goal",h:"Know your week in five lines.",p:"An automation collects your numbers and AI turns them into a short summary, delivered before you start work."},
  {t:"steps",k:"How it runs",h:"Set it once",items:[["Monday 7:00","The automation starts"],["Collect","Bookings, sales, enquiries, posts"],["Summarise","AI writes five clear lines"],["Deliver","Email or WhatsApp to you"]]},
  {t:"list",k:"Track only this",h:"Three numbers that matter",items:[["Enquiries","How many came in"],["Bookings or sales","How many converted"],["Reply time","How fast you answered"]]}
 ]},
{slug:"reply-to-every-review",cat:"Marketing",pre:"Reputation",title:"Reply to|every review",sub:"With AI, approved by you",pal:"sunset",art:"waves",
 hook:"Future customers read your replies, not just your reviews ⭐",gift:"review reply templates",
 slides:[
  {t:"big",k:"Why",h:"Replies show future customers you care.",p:"A thoughtful reply to a good review builds loyalty. A calm reply to a bad one builds trust."},
  {t:"steps",k:"The workflow",h:"One tap to reply",items:[["New review","Google sends the alert"],["AI drafts","A reply in your voice"],["You approve","Edit or send with one tap"],["Posted","Done in under a minute"]]},
  {t:"list",k:"Good replies",h:"What to include",items:[["Thank them by name","Personal beats generic"],["Mention one detail","Proves you read it"],["Complaints: take it offline","Apologise, then offer to call"]]}
 ]},
{slug:"github-in-5-words",cat:"Code",pre:"Beginner",title:"GitHub|in 5 words",sub:"Repo · commit · branch",pal:"mono",art:"pixel",
 hook:"GitHub sounds scary. It's really just five words 💾",gift:"a GitHub cheat sheet",
 slides:[
  {t:"list",k:"Words 1–3",h:"The basics",items:[["Repo","Your project folder, online"],["Commit","A saved snapshot with a note"],["Branch","A safe copy to test ideas"]]},
  {t:"list",k:"Words 4–5",h:"Working as a team",items:[["Pull request","Ask to merge your changes"],["Merge","Combine them into main"]]},
  {t:"steps",k:"For websites",h:"The everyday flow",items:[["Edit","Change your files"],["Commit","Save with a message"],["Push","Send it to GitHub"],["Live","Vercel deploys it automatically"]]}
 ]},
{slug:"website-live-in-10-minutes",cat:"Web",pre:"Launch",title:"Website live|in 10 minutes",sub:"GitHub + Vercel",pal:"brand",art:"rings",
 hook:"You don't need to pay for hosting to launch a simple website 🚀",gift:"our website launch checklist",
 slides:[
  {t:"steps",k:"The steps",h:"From repo to live site",items:[["GitHub","Put your site in a repository"],["Import","Open vercel.com/new and pick the repo"],["Deploy","One click"],["Domain","Settings → Domains"]]},
  {t:"list",k:"Why Vercel",h:"Made for small teams",items:[["Free to start","Great for simple sites"],["HTTPS included","Secure by default"],["Auto updates","Every push goes live"]]},
  {t:"list",k:"Before you share",h:"Quick checks",items:[["Test on your phone","Most visitors are mobile"],["Click every button","No dead links"],["Add a WhatsApp link","The easiest way to contact you"]]}
 ]},
{slug:"websites-that-book",cat:"Web",pre:"Web",title:"Websites|that book",sub:"Conversion basics",pal:"red",art:"ribbon",
 hook:"A pretty website that doesn't get bookings is just a brochure 🖥",gift:"a free review of your homepage",
 slides:[
  {t:"big",k:"The rule",h:"One page. One job. One button.",p:"Every page should lead to one main action: Book, WhatsApp us, or Get a quote."},
  {t:"list",k:"Above the fold",h:"What visitors need first",items:[["A clear headline","What you do and who it's for"],["Real photos","Not stock images"],["The main button","Visible without scrolling"]]},
  {t:"list",k:"Add trust",h:"Remove doubts",items:[["Reviews with names","Real people, real words"],["Prices or 'from' prices","No guessing"],["Location and hours","Easy to find"]]}
 ]},
{slug:"google-business-profile",cat:"Web",pre:"Get found",title:"Google|Business Profile",sub:"Free local marketing",pal:"lime",art:"aurora",
 hook:"The most underrated free marketing tool for local businesses 📍",gift:"our Google profile checklist",
 slides:[
  {t:"big",k:"Why it matters",h:"Local searches often show this before your website.",p:"When people search for a business near them, your profile, photos and reviews can appear on Search and Maps."},
  {t:"list",k:"Set it up right",h:"The basics",items:[["Name, hours, phone","Correct and consistent"],["Real photos","Add new ones every month"],["Posts and offers","Show you're active"]]},
  {t:"list",k:"Reviews",h:"Grow them steadily",items:[["Ask happy customers","Right after a good experience"],["Send the link","Make it one tap"],["Reply to every review","Good and bad"]]}
 ]},
{slug:"mcp-explained",cat:"AI",pre:"Best",title:"MCP|explained",sub:"Plugs for AI",pal:"violet",art:"rings",
 hook:"MCP is the reason AI can now use your tools, not just talk about them 🔌",gift:"our list of MCP servers for business",
 slides:[
  {t:"big",k:"In one line",h:"MCP is like USB for AI.",p:"The Model Context Protocol is an open standard that lets AI apps connect to tools and data in one consistent way."},
  {t:"list",k:"Examples",h:"What you can plug in",items:[["Google Drive","Answers from your own documents"],["Calendar and Slack","Act inside your tools"],["GitHub","Read and change code"]]},
  {t:"list",k:"Stay safe",h:"Before you connect",items:[["Trusted servers only","Know who built it"],["Start read-only","Add write access later"],["Review permissions","Know what the AI can do"]]}
 ]},
{slug:"which-ai-should-i-use",cat:"AI",pre:"AI",title:"Which AI|should I use?",sub:"Claude · ChatGPT · Gemini",pal:"teal",art:"orbs",
 hook:"There's no single best AI. There's the best one for your work 🤖",gift:"our AI comparison scorecard",
 slides:[
  {t:"big",k:"The honest answer",h:"Test with your real work, not demos.",p:"The leading AI assistants are all strong. The right one depends on your tasks, your tools and your data rules."},
  {t:"list",k:"Decide by",h:"Three questions",items:[["What are your tasks?","Writing, analysis, coding, images"],["Which tools do you use?","Pick what connects to them"],["What about privacy?","Check business plans and data settings"]]},
  {t:"steps",k:"Run a fair test",h:"One afternoon",items:[["Same prompt","Give each AI identical instructions"],["Five real tasks","From your actual week"],["Score","Accuracy, tone and speed"]]}
 ]},
{slug:"30-days-of-content",cat:"Marketing",pre:"Marketing",title:"30 days of|content in 1 hour",sub:"With AI",pal:"candy",art:"dots",
 hook:"Plan a whole month of posts in one sitting. Here's the method 📅",gift:"the content-plan prompt",
 slides:[
  {t:"steps",k:"The method",h:"Plan a month in an hour",items:[["Brief the AI","Business, audience and 3 pillars"],["Ask for 30 ideas","In a table with hooks"],["Pick the best 12","Quality over quantity"],["Batch create","One afternoon, done"]]},
  {t:"prompt",k:"The prompt",h:"Copy this",code:"You are a content strategist.\nCreate 30 Instagram post ideas for [business]\nthat sells [offer] to [audience].\nPillars: educate, prove, sell.\nReturn a table: idea, format, hook, call to action."},
  {t:"list",k:"Keep it human",h:"What AI can't do for you",items:[["Your real photos","People trust real faces"],["Your stories","Wins, mistakes, lessons"],["Your voice","Edit every draft"]]}
 ]},
{slug:"look-the-same-everywhere",cat:"Design",pre:"Brand",title:"Look the same|everywhere",sub:"Brand kit basics",pal:"pearl",art:"ribbon",
 hook:"People should recognise your post before they see your name 👁",gift:"a brand kit template",
 slides:[
  {t:"list",k:"Your kit, part 1",h:"The visual basics",items:[["Logo versions","Full, icon and one-colour"],["3–5 colours","With exact codes"],["Two fonts","Headline and body"]]},
  {t:"list",k:"Your kit, part 2",h:"The rest of the system",items:[["Templates","Posts, stories, covers"],["Voice","How you speak and write"],["Photo style","Light, mood and framing"]]},
  {t:"big",k:"Why it matters",h:"Consistency builds recognition.",p:"When every post looks like you, people start to know your brand before they read the name."}
 ]},
{slug:"comment-to-dm",cat:"Marketing",pre:"Growth",title:"Comment|to DM",sub:"Keyword automation",pal:"brand",art:"streaks",
 hook:"You've seen \"comment X and I'll send it\". Here's how it works (and you can test it now) 👇",gift:"this exact setup, explained",
 slides:[
  {t:"steps",k:"How it works",h:"Comment in, DM out",items:[["The post","Asks people to comment one word"],["Detection","A tool spots the keyword"],["The DM","Your link is sent automatically"],["Follow up","You talk to interested people"]]},
  {t:"list",k:"Why it works",h:"Everybody wins",items:[["More comments","Signals the post is engaging"],["Instant delivery","No waiting for a reply"],["Warm leads","People who raised their hand"]]},
  {t:"list",k:"Rules",h:"Do it properly",items:[["Give real value","Something genuinely useful"],["One simple word","Easy to type"],["Follow the platform rules","Use approved messaging tools"]]}
 ]},
{slug:"ai-front-desk",cat:"Agents",pre:"Agents",title:"An AI front|desk, 24/7",sub:"Hotels · clinics · salons",pal:"gold",art:"aurora",
 hook:"What happens to the messages you get after closing time? 🌙",gift:"a free demo built for your business",
 slides:[
  {t:"compare",k:"After hours",h:"Without vs with an agent",a:{l:"Without",x:["Messages wait until morning","Customers book elsewhere","Staff start the day behind"]},b:{l:"With",x:["Instant replies","Details collected, slot held","Team starts with a summary"]}},
  {t:"list",k:"It can",h:"What the agent handles",items:[["Answer FAQs","From your own information"],["Check availability","Live from your calendar"],["Take details and book","Then confirm by message"]]},
  {t:"list",k:"It hands over",h:"What stays human",items:[["Complaints","Always a person"],["Special requests","Your team decides"],["Anything uncertain","It asks rather than guesses"]]}
 ]},
{slug:"is-an-agent-worth-it",cat:"Agents",pre:"Before you buy",title:"Is an AI agent|worth it?",sub:"Do the maths",pal:"lime",art:"waves",
 hook:"Before you spend a cent on AI, do this simple calculation 🧮",gift:"our ROI calculator",
 slides:[
  {t:"steps",k:"Count your hours",h:"Three numbers",items:[["Messages per day","Enquiries, questions, follow-ups"],["Minutes per reply","Including looking things up"],["× 30 days","Hours spent per month"]]},
  {t:"big",k:"Example",h:"40 messages × 3 min = 2 hours a day.",p:"That's about 60 hours a month spent replying, before any follow-ups. Use your own numbers."},
  {t:"list",k:"Then ask",h:"The real question",items:[["What would your team do instead?","Sales, service, growth"],["What happens at night?","How many messages wait?"],["What is one booking worth?","Compare it with the cost"]]}
 ]}
];
