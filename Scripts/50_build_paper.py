"""
50_build_paper.py
Build Paper/final_dissertation.pdf and Paper/final_dissertation.docx from
Paper/final_dissertation.md.

Requirements: pandoc (>= 2.19), Python Playwright with Chromium, and the APA 7
CSL file (downloaded automatically from the CSL styles repository if missing).

  python Scripts/50_build_paper.py
"""
import subprocess
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent.parent
PAPER = ROOT / "Paper"
MD = PAPER / "final_dissertation.md"
BUILD = ROOT / "Paper" / "_build"
BUILD.mkdir(exist_ok=True)
CSL = BUILD / "apa.csl"
CSS = BUILD / "apa.css"
HTML = BUILD / "final_dissertation.html"

if not CSL.exists():
    urllib.request.urlretrieve(
        "https://raw.githubusercontent.com/citation-style-language/styles/master/apa.csl", CSL)

CSS.write_text("""
@page { size: Letter; margin: 1in; }
html { font-family: "Times New Roman", Times, "Liberation Serif", serif; font-size: 12pt; }
body { max-width: none; margin: 0; padding: 0; line-height: 2; color: #000; background: #fff; }
p { margin: 0; text-indent: 0.5in; }
li p, td p, th p, blockquote p, figcaption p { text-indent: 0; }
header#title-block-header { height: 9in; display: flex; flex-direction: column;
  justify-content: center; text-align: center; page-break-after: always; }
header h1.title { font-size: 12pt; font-weight: bold; margin: 0; }
header p.subtitle { text-indent: 0; margin: 0; }
header p.author { text-indent: 0; margin-top: 2em; }
h1 { font-size: 12pt; font-weight: bold; text-align: center; margin: 1em 0 0 0; }
h1#abstract { page-break-before: auto; }
h2 { font-size: 12pt; font-weight: bold; text-align: left; margin: 1em 0 0 0; }
h3 { font-size: 12pt; font-weight: bold; font-style: italic; margin: 1em 0 0 0; }
table { border-collapse: collapse; width: 100%; margin: 0.6em 0; font-size: 9.5pt;
  line-height: 1.3; page-break-inside: auto; }
tr { page-break-inside: avoid; }
thead tr { border-top: 1px solid #000; border-bottom: 1px solid #000; }
tbody tr:last-child { border-bottom: 1px solid #000; }
th, td { padding: 2px 5px; vertical-align: top; }
figure { margin: 0.8em 0; text-align: center; page-break-inside: avoid; }
figure img, p > img { max-width: 100%; }
figcaption { font-size: 10pt; line-height: 1.3; font-style: italic; text-align: left; }
p > em:only-child { }
ul, ol { margin: 0.2em 0; }
a { color: inherit; text-decoration: none; }
code { font-family: "Courier New", monospace; font-size: 10pt; }
math[display="block"] { margin: 0.5em 0; }
nav#TOC { page-break-after: always; line-height: 1.5; }
nav#TOC h2 { text-align: center; font-size: 12pt; }
nav#TOC ul { list-style: none; padding-left: 0.3in; margin: 0; }
nav#TOC > ul { padding-left: 0; }
nav#TOC a { text-decoration: none; color: #000; display: flex; }
nav#TOC a .tocpg { margin-left: auto; padding-left: 1em; }
div#refs .csl-entry { padding-left: 0.5in; text-indent: -0.5in; line-height: 2; }
""")

subprocess.run([
    "pandoc", str(MD), "--standalone", "--citeproc", "--csl", str(CSL), "--mathml",
    "--embed-resources", "--css", str(CSS), f"--resource-path={PAPER}:{ROOT}",
    "--metadata", "link-citations=true", "--toc", "--toc-depth=2",
    "--metadata", "toc-title=Contents", "-o", str(HTML)], check=True, cwd=PAPER)

from playwright.sync_api import sync_playwright  # noqa: E402
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    pg.goto(HTML.resolve().as_uri(), wait_until="networkidle")
    pdf_kw = dict(format="Letter",
           margin={"top": "1in", "bottom": "1in", "left": "1in", "right": "1in"},
           display_header_footer=True,
           header_template='<div style="font-size:10pt;font-family:Times New Roman;width:100%;'
                           'text-align:right;margin-right:0.6in;"><span class="pageNumber"></span></div>',
           footer_template="<div></div>", print_background=True)
    # Two-pass contents page numbers: render once, find the page on which each
    # heading starts, write the numbers into the contents list, render again.
    from pypdf import PdfReader
    tmp = BUILD / "pass1.pdf"
    pg.pdf(path=str(tmp), **pdf_kw)
    entries = pg.eval_on_selector_all("nav#TOC a", "els => els.map(e => e.textContent.trim())")
    texts = [" ".join(x.extract_text().split()) for x in PdfReader(str(tmp)).pages]
    toc_first = next(i for i, x in enumerate(texts) if "Contents" in x)
    last_key = " ".join(entries[-1].split())
    toc_last = next(i for i in range(toc_first, len(texts)) if last_key in texts[i])
    nums, start = [], toc_last + 1
    for e in entries:
        key = " ".join(e.split())
        hit = next((i for i in range(start, len(texts)) if key in texts[i]), None)
        nums.append("" if hit is None else str(hit + 1))
        if hit is not None:
            start = hit
    pg.evaluate("""nums => { document.querySelectorAll('nav#TOC a').forEach((a, i) => {
        const s = document.createElement('span'); s.className = 'tocpg'; s.textContent = nums[i];
        a.appendChild(s); }); }""", nums)
    pg.pdf(path=str(PAPER / "final_dissertation.pdf"), **pdf_kw)
    missing = [e for e, n in zip(entries, nums) if not n]
    print("Contents entries without a page:", missing)
    b.close()

# Word styles are taken from Paper/reference.docx (the previous submission's styles).
ref = PAPER / "reference.docx"
cmd = ["pandoc", str(MD), "--citeproc", "--csl", str(CSL), f"--resource-path={PAPER}:{ROOT}",
       "--toc", "--toc-depth=2", "--metadata", "toc-title=Contents",
       "-o", str(PAPER / "final_dissertation.docx")]
if ref.exists():
    cmd += ["--reference-doc", str(ref)]
subprocess.run(cmd, check=True, cwd=PAPER)
print("Built PDF and DOCX")
