// Render SVG/HTML files to PNG with the pre-installed Playwright Chromium.
// Usage: node scripts/brand/render.js <in.svg|in.html> <out.png> [width height] [--transparent]
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const args = process.argv.slice(2);
  const transparent = args.includes('--transparent');
  const [inp, out, w, h] = args.filter(a => a !== '--transparent');
  const src = fs.readFileSync(inp, 'utf8');
  let W = +w, H = +h;
  if (!W) {
    const m = src.match(/width="(\d+(?:\.\d+)?)"[^>]*height="(\d+(?:\.\d+)?)"/);
    W = Math.round(+m[1]); H = Math.round(+m[2]);
  }
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
  const fileUrl = 'file://' + path.resolve(inp);
  if (inp.endsWith('.html')) await page.goto(fileUrl, { waitUntil: 'networkidle' });
  else await page.setContent(
    `<html><body style="margin:0;background:transparent">` +
    src.replace(/<svg /, `<svg style="display:block;width:${W}px;height:${H}px" `) + `</body></html>`);
  await page.evaluate(() => document.fonts && document.fonts.ready);
  await page.screenshot({ path: out, omitBackground: transparent, clip: { x: 0, y: 0, width: W, height: H } });
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
