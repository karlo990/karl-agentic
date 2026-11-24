#!/usr/bin/env node
// Renders every post in posts.js into five 1080×1350 JPGs (Instagram 4:5),
// small previews for the Studio page, and studio/posts.json with captions.
//
//   cd studio-src && npm install && npx playwright install chromium   (first time)
//   node render.js                 # all posts
//   node render.js comment-to-dm   # one post
//
// Then run `python3 scripts/build.py` from the repo root to refresh the /studio page.
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const { chromium } = require('playwright');

const ROOT = path.resolve(__dirname, '..');
const OUT = path.join(ROOT, 'assets', 'studio');
const sandbox = { window: {} };
vm.runInNewContext(fs.readFileSync(path.join(__dirname, 'posts.js'), 'utf8'), sandbox);
vm.runInNewContext(fs.readFileSync(path.join(__dirname, 'posts2.js'), 'utf8'), sandbox);
const POSTS = sandbox.window.POSTS.concat(sandbox.window.POSTS2 || []);

const TAGS = {
  Hardware: '#NVIDIA #GPU #AIworkstation #PCbuild #TechSouthAfrica',
  Servers: '#Servers #Docker #SelfHosted #ITsupport #SmallBusinessIT',
  Consulting: '#TechConsulting #AIstrategy #CloudComputing #SmallBusiness #GPU',
  Video: '#VideoMarketing #AIvideo #Reels #ContentCreation #VideoEditing',
  Security: '#CyberSecurity #2FA #BusinessSecurity #PasswordManager #ITsecurity',
  'Edge AI': '#EdgeAI #Jetson #RetailTech #ComputerVision #SmartCameras',
  Agents: '#AIagents #AIautomation #SmallBusiness #CustomerService #WhatsAppBusiness',
  Sales: '#SalesTips #LeadGeneration #AIagents #SmallBusiness #Automation',
  AI: '#AI #PromptEngineering #ClaudeAI #ChatGPT #AItools',
  Marketing: '#MarketingTips #ContentStrategy #InstagramTips #SocialMediaMarketing #ContentCreator',
  Design: '#GraphicDesign #DesignTips #BrandDesign #Typography #DesignInspiration',
  '3D': '#Blender3D #3DDesign #ProductRender #3DArt #Blender',
  Automation: '#Automation #NoCode #Zapier #n8n #Productivity',
  Code: '#GitHub #WebDevelopment #CodingForBeginners #Developer #Vercel',
  Web: '#WebDesign #WebsiteTips #SmallBusiness #LocalSEO #Vercel',
};

function caption(p) {
  const s2 = p.slides[0], s3 = p.slides[1];
  const plain = (t) => t.replace(/\|/g, ' ');
  const bullets = (s3.items || s2.items || []).slice(0, 4).map((it) => `• ${it[0]}: ${it[1]}`).join('\n');
  return [
    p.hook,
    '',
    plain(s2.h),
    bullets,
    '',
    `💬 Comment "AGENT" and we'll send you ${p.gift}.`,
    '📌 Save this for later and share it with someone who needs it.',
    '',
    TAGS[p.cat] || '#AIagents',
  ].join('\n');
}

(async () => {
  const only = process.argv.slice(2);
  const list = only.length ? POSTS.filter((p) => only.includes(p.slug)) : POSTS;
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 5400, height: 1350 } });
  const thumbs = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  const tpl = 'file://' + path.join(__dirname, 'template.html');
  for (const p of list) {
    const dir = path.join(OUT, p.slug);
    fs.mkdirSync(dir, { recursive: true });
    await page.goto(tpl + '#' + p.slug);
    await page.reload();
    await page.waitForSelector('body[data-ready="1"]', { timeout: 60000 });
    await page.waitForTimeout(300);
    for (let i = 0; i < 5; i++) {
      const file = path.join(dir, `${p.slug}-${i + 1}.jpg`);
      await page.screenshot({ path: file, type: 'jpeg', quality: 83, clip: { x: i * 1080, y: 0, width: 1080, height: 1350 } });
      // 360×450 preview for the Studio page
      const b64 = fs.readFileSync(file).toString('base64');
      await thumbs.setContent(`<body style="margin:0"><img id="t" src="data:image/jpeg;base64,${b64}" style="width:360px;height:450px;display:block"></body>`);
      await thumbs.locator('#t').screenshot({ path: path.join(dir, `thumb-${i + 1}.jpg`), type: 'jpeg', quality: 78 });
    }
    process.stdout.write(`✓ ${p.slug}\n`);
  }
  await browser.close();

  const meta = POSTS.map((p) => ({
    slug: p.slug, cat: p.cat, pre: p.pre, title: p.title.replace(/\|/g, ' '), sub: p.sub, gift: p.gift,
    caption: caption(p),
    images: [1, 2, 3, 4, 5].map((n) => `/assets/studio/${p.slug}/${p.slug}-${n}.jpg`),
    thumbs: [1, 2, 3, 4, 5].map((n) => `/assets/studio/${p.slug}/thumb-${n}.jpg`),
  }));
  fs.mkdirSync(path.join(ROOT, 'studio'), { recursive: true });
  fs.writeFileSync(path.join(ROOT, 'studio', 'posts.json'), JSON.stringify(meta, null, 1));
  console.log(`\n${list.length} posts rendered, studio/posts.json written.`);
})();
