// Batch 2: 15 posts on private AI, GPUs, servers and creative tech. `hero` = Canva 3D object placed on the cover.
window.POSTS2 = [
{slug:"private-ai-in-your-office",cat:"AI",pre:"Local-first",title:"Private AI|in your office",sub:"Your data stays home",pal:"brand",art:"rings",hero:"server",
 hook:"What if your AI never sent a single customer file to the cloud? 🔒",gift:"our private AI setup checklist",
 slides:[
  {t:"big",k:"The idea",h:"Run the AI on your own machine.",p:"Small open models now run on one GPU workstation or server. Your documents, chats and customer data never leave the building."},
  {t:"list",k:"Why businesses do it",h:"Three big reasons",items:[["Privacy","Client files stay on your network"],["Predictable cost","No per-message API bills"],["Works offline","Even when the internet doesn't"]]},
  {t:"steps",k:"The stack",h:"What we install",items:[["GPU machine","Workstation or small server"],["Ollama","Runs open models locally"],["Open WebUI","A private ChatGPT-style app"],["n8n","Connects it to your tools"]]}
 ]},
{slug:"why-ai-needs-gpus",cat:"Hardware",pre:"Explained",title:"Why AI|needs GPUs",sub:"In plain English",pal:"violet",art:"orbs",hero:"gpu",
 hook:"Your laptop can run AI. So why does everyone want a GPU? 🧠",gift:"a GPU buying guide for AI",
 slides:[
  {t:"compare",k:"CPU vs GPU",h:"A few geniuses vs an army",a:{l:"CPU",x:["A handful of powerful cores","Great at one task at a time","Slow for AI maths"]},b:{l:"GPU",x:["Thousands of small cores","Thousands of sums at once","Built for AI and rendering"]}},
  {t:"list",k:"The number that matters",h:"VRAM decides what fits",items:[["8–12 GB","Small models, image tools"],["16 GB","Most local assistants"],["24–32 GB+","Bigger models and fast video"]]},
  {t:"list",k:"Also great for",h:"One card, many jobs",items:[["3D rendering","Blender Cycles on GPU"],["Video editing","Faster exports and effects"],["AI images and video","Local generation tools"]]}
 ]},
{slug:"rtx-5090-vs-5080",cat:"Hardware",pre:"Which one?",title:"RTX 5090|vs 5080",sub:"For creators and AI",pal:"red",art:"rays",hero:"gpu",
 hook:"Thinking about a new GPU? Read this before you spend the money 💸",gift:"our live South African price guide",
 slides:[
  {t:"compare",k:"Head to head",h:"The real difference",a:{l:"RTX 5080",x:["16 GB VRAM","Great for 4K editing and gaming","Around half the price"]},b:{l:"RTX 5090",x:["32 GB VRAM","Runs bigger local AI models","The fastest consumer card"]}},
  {t:"list",k:"Pick the 5080 if",h:"Most creators",items:[["You edit video and design","16 GB is plenty"],["You use cloud AI","No need for huge VRAM"],["Budget matters","Spend the rest on storage"]]},
  {t:"list",k:"Pick the 5090 if",h:"Power users",items:[["You run AI locally","32 GB fits larger models"],["You render all day","Time saved pays it back"],["You need one card for years","Most headroom"]]}
 ]},
{slug:"build-an-ai-workstation",cat:"Hardware",pre:"Build guide",title:"Build an AI|workstation",sub:"Parts that matter",pal:"teal",art:"silk",hero:"tower",
 hook:"The parts list we start from when a client wants a serious AI machine 🖥",gift:"three ready-made build lists",
 slides:[
  {t:"list",k:"Spend here",h:"Where the money goes",items:[["GPU","The most important part for AI"],["RAM","64 GB or more for big projects"],["Fast NVMe storage","Models and footage load quickly"]]},
  {t:"list",k:"Don't forget",h:"The boring essentials",items:[["A quality power supply","GPUs draw a lot of power"],["Cooling and airflow","Heat slows everything down"],["A UPS","Protects work during load-shedding"]]},
  {t:"steps",k:"Our process",h:"From parts to working",items:[["Spec","Matched to your workload"],["Build","Assembled and cable-managed"],["Stress test","24-hour burn-in"],["Set up","Drivers, CUDA and your apps"]]}
 ]},
{slug:"cloud-or-own-hardware",cat:"Consulting",pre:"Do the maths",title:"Cloud or|own hardware?",sub:"Before you buy a GPU",pal:"gold",art:"waves",hero:"cloud",
 hook:"Renting GPUs vs buying one. Here's how to decide without guessing 🧮",gift:"our cloud vs hardware calculator",
 slides:[
  {t:"compare",k:"The trade-off",h:"Rent vs own",a:{l:"Cloud",x:["No upfront cost","Pay per hour","Scales instantly"]},b:{l:"Own",x:["One upfront cost","Free to run all day","Data stays with you"]}},
  {t:"steps",k:"Quick test",h:"Three numbers",items:[["Hours per month","How much you'll really use it"],["Cloud price per hour","For the GPU you need"],["Hardware price","Plus power and setup"]]},
  {t:"big",k:"Rule of thumb",h:"Used most days? Owning usually wins.",p:"Occasional or unpredictable use favours the cloud. Daily, steady work usually pays off a machine within a year or two. Run your own numbers first."}
 ]},
{slug:"run-an-llm-locally",cat:"AI",pre:"Try it today",title:"Run an AI|model locally",sub:"With Ollama",pal:"lime",art:"pixel",hero:"chip",
 hook:"You can run a private AI on your own computer in about 10 minutes 💻",gift:"our favourite local models list",
 slides:[
  {t:"steps",k:"Setup",h:"Four steps",items:[["Install Ollama","Free for Mac, Windows and Linux"],["Pick a model","Start small, like an 8B model"],["Run it","One command in the terminal"],["Add a chat app","Open WebUI for a friendly screen"]]},
  {t:"prompt",k:"The command",h:"Copy this",code:"ollama run [model-name]\n\n# then just type your question\n>>> Summarise this email in 3 bullet points: [paste]"},
  {t:"list",k:"Good to know",h:"Set expectations",items:[["Smaller than cloud AI","Great for everyday tasks"],["Speed depends on your GPU","More VRAM, bigger models"],["Totally private","Nothing leaves your machine"]]}
 ]},
{slug:"docker-in-5-minutes",cat:"Servers",pre:"Beginner",title:"Docker|in 5 minutes",sub:"Apps in boxes",pal:"ocean",art:"dots",hero:"cubes",
 hook:"Every modern server we install runs on Docker. Here's what it actually is 📦",gift:"our starter docker-compose file",
 slides:[
  {t:"big",k:"In one line",h:"Docker puts each app in its own box.",p:"A container holds an app and everything it needs. It runs the same on your laptop, a server or the cloud."},
  {t:"list",k:"Why we use it",h:"Clean and repeatable",items:[["Install in minutes","One file describes the setup"],["Apps don't clash","Each one in its own box"],["Easy updates and backups","Swap a box, keep your data"]]},
  {t:"prompt",k:"Example",h:"Start an app stack",code:"# docker-compose.yml lists your apps\ndocker compose up -d     # start everything\ndocker compose ps        # check it's running\ndocker compose pull      # get updates"}
 ]},
{slug:"self-host-n8n",cat:"Automation",pre:"Pro",title:"Self-host|n8n",sub:"Unlimited automations",pal:"candy",art:"ribbon",hero:"cubes",
 hook:"Automations without paying per task. Self-hosted n8n explained ⚙️",gift:"5 n8n workflow templates",
 slides:[
  {t:"compare",k:"Hosted vs self-hosted",h:"Who runs it?",a:{l:"Hosted",x:["Zero setup","Monthly plan limits","Data on their servers"]},b:{l:"Self-hosted",x:["Runs on your server","No per-task limits","Data stays with you"]}},
  {t:"steps",k:"What we set up",h:"A safe install",items:[["Server","Small VPS or office machine"],["Docker","n8n plus a database"],["HTTPS and login","Secure from the internet"],["Backups","Workflows saved nightly"]]},
  {t:"list",k:"First automations",h:"Start with these",items:[["New lead → WhatsApp alert","Never miss an enquiry"],["Invoice reminders","Polite and automatic"],["Daily report","Your numbers every morning"]]}
 ]},
{slug:"server-room-basics",cat:"Servers",pre:"Checklist",title:"Server room|basics",sub:"Small office edition",pal:"mono",art:"rings",hero:"server",
 hook:"Your business runs on that box in the corner. Look after it 🗄",gift:"our server room checklist",
 slides:[
  {t:"list",k:"Power",h:"Keep it running",items:[["UPS battery backup","Rides through outages and load-shedding"],["Surge protection","Protects against power spikes"],["Auto-shutdown","Saves data before the battery dies"]]},
  {t:"list",k:"Heat and dust",h:"Keep it cool",items:[["Airflow first","Never in a closed cupboard"],["Monitor temperature","Get alerts when it's hot"],["Clean filters","Dust kills hardware"]]},
  {t:"list",k:"Safety",h:"Keep it safe",items:[["Locked room or rack","Limit who can touch it"],["Labelled cables","Fix problems faster"],["Off-site backups","For fire or theft"]]}
 ]},
{slug:"3-2-1-backups",cat:"Servers",pre:"Never lose files",title:"The 3-2-1|backup rule",sub:"Simple and proven",pal:"ocean",art:"waves",hero:"drives",
 hook:"If your laptop died today, what would you lose? 😬",gift:"a backup plan template",
 slides:[
  {t:"big",k:"The rule",h:"3 copies. 2 types. 1 off-site.",p:"Keep three copies of important data, on two different kinds of storage, with one copy somewhere else."},
  {t:"list",k:"In practice",h:"A simple setup",items:[["Copy 1","Your working files"],["Copy 2","A NAS or external drive in the office"],["Copy 3","Encrypted cloud backup"]]},
  {t:"list",k:"Most people forget",h:"Test your restore",items:[["Restore one file monthly","Prove it works"],["Automate it","Manual backups get skipped"],["Keep old versions","Protects against ransomware"]]}
 ]},
{slug:"render-faster-in-blender",cat:"3D",pre:"Speed up",title:"Render faster|in Blender",sub:"GPU settings that matter",pal:"ember",art:"orbs",hero:"gpu",
 hook:"Waiting hours for a render? These settings fix most of it 🚀",gift:"our Blender render settings preset",
 slides:[
  {t:"steps",k:"Turn on the GPU",h:"First, the big one",items:[["Preferences","Edit → Preferences → System"],["Choose OptiX","For NVIDIA RTX cards"],["Render device","Set Cycles to GPU Compute"]]},
  {t:"list",k:"Then",h:"Quick wins",items:[["Use denoising","Fewer samples, clean result"],["Lower max samples","Start around 128–256"],["Adaptive sampling","Stops early when it's clean"]]},
  {t:"list",k:"Hardware",h:"What speeds it up most",items:[["More VRAM","Bigger scenes fit on the GPU"],["A newer RTX card","Faster ray tracing"],["Fast storage","Textures load quicker"]]}
 ]},
{slug:"ai-video-for-brands",cat:"Video",pre:"Creative",title:"AI video|for brands",sub:"What works now",pal:"violet",art:"streaks",hero:"camera",
 hook:"AI video is everywhere. Here's how brands use it without looking fake 🎬",gift:"our AI video workflow",
 slides:[
  {t:"list",k:"Use AI for",h:"Where it shines",items:[["B-roll and backgrounds","Scenes you can't film"],["Captions and edits","Hours saved per video"],["Voice-overs and translation","Reach more people"]]},
  {t:"list",k:"Keep it real",h:"What should stay human",items:[["Your face and story","People trust people"],["Real products","Show what you actually sell"],["Real results","Never fake testimonials"]]},
  {t:"steps",k:"Our workflow",h:"From idea to Reel",items:[["Script","Hook in the first second"],["Film","Real footage first"],["AI assist","B-roll, captions, sound"],["Edit","Cut for each platform"]]}
 ]},
{slug:"two-factor-everything",cat:"Security",pre:"Do it today",title:"Turn on|2FA everywhere",sub:"Stop most hacks",pal:"red",art:"rings",hero:"shield",
 hook:"One setting blocks most account takeovers. Most people still haven't turned it on 🔐",gift:"our business security checklist",
 slides:[
  {t:"big",k:"The basics",h:"A password alone isn't enough.",p:"Two-factor authentication adds a second check, like a code from an app, so a stolen password isn't enough to get in."},
  {t:"list",k:"Turn it on for",h:"Start with these",items:[["Email","The key to every other account"],["Banking and payments","Protect the money"],["Instagram, WhatsApp, Meta","Protect the brand"]]},
  {t:"list",k:"Do it right",h:"Best options",items:[["Authenticator app","Better than SMS codes"],["Save backup codes","Somewhere safe, offline"],["Use a password manager","Unique password everywhere"]]}
 ]},
{slug:"ai-images-on-brand",cat:"Design",pre:"Creative",title:"On-brand|AI images",sub:"Prompt like a designer",pal:"candy",art:"silk",hero:"chip",
 hook:"Most AI images look generic. Here's how to make them look like YOUR brand 🎨",gift:"our image prompt templates",
 slides:[
  {t:"list",k:"Describe like a designer",h:"Five things to include",items:[["Subject","Exactly what's in the picture"],["Style","3D render, photo, illustration"],["Light","Studio, sunset, neon"],["Colours","Your brand palette"],["Background","Plain backgrounds are easier to use"]]},
  {t:"prompt",k:"Template",h:"Copy this",code:"A [style] of [subject], [lighting],\nin [brand colours], on a [background],\nno text, no logos"},
  {t:"list",k:"Before you post",h:"Check these",items:[["Hands, text and logos","AI often gets them wrong"],["Usage rights","Check the tool's terms"],["Consistency","Same style across posts"]]}
 ]},
{slug:"smart-cameras-for-shops",cat:"Edge AI",pre:"Edge AI",title:"Smart cameras|for shops",sub:"AI on the device",pal:"teal",art:"aurora",hero:"camera",
 hook:"Your security cameras could also count customers and spot empty shelves 📷",gift:"a free edge AI ideas list",
 slides:[
  {t:"big",k:"Edge AI",h:"The AI runs inside the camera box.",p:"A small device like an NVIDIA Jetson analyses video on-site, so footage doesn't need to be streamed to the cloud."},
  {t:"list",k:"Use cases",h:"What it can do",items:[["Count visitors","Busy hours and staffing"],["Shelf alerts","Spot gaps before customers do"],["Queue alerts","Open another till in time"]]},
  {t:"list",k:"Do it responsibly",h:"Privacy first",items:[["Tell customers","Clear signs at the door"],["Count, don't identify","Avoid storing faces"],["Follow local law","Check data protection rules"]]}
 ]}
];
