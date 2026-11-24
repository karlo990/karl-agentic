// Renders hiring.html into eight 1080×1350 JPGs.
const path=require('path');const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1200,height:1400}});
await p.goto('file://'+path.join(__dirname,'hiring.html'));await p.waitForSelector('body[data-ready]');await p.waitForTimeout(300);
const out=process.argv[2]||path.join(__dirname,'..','assets','hire','slides');require('fs').mkdirSync(out,{recursive:true});
const n=await p.locator('.s').count();for(let i=0;i<n;i++)await p.locator('.s').nth(i).screenshot({path:`${out}/karl-agentic-hiring-${i+1}.jpg`,type:'jpeg',quality:90});
console.log(n,'slides');await b.close()})();
