#!/usr/bin/env python3
"""Word-level redline between two documents (.docx, .pdf, .md or .txt).

    python3 tools/redline.py OLD NEW              # HTML redline on stdout
    python3 tools/redline.py OLD NEW -o out.html
    python3 tools/redline.py OLD NEW --text       # [-deleted-]{+added+} plain text

Use it to produce an independent comparison when checking whether an AI tool's
redline, or a counterparty's comparison, accurately reflects the changes.
"""
import argparse
import difflib
import html
import re
import subprocess
import sys
from pathlib import Path


def load(path):
    p = Path(path)
    if p.suffix.lower() in (".docx", ".odt", ".rtf"):
        cmd = ["pandoc", "-t", "plain", "--wrap=none", str(p)]
    elif p.suffix.lower() == ".pdf":
        cmd = ["pdftotext", "-layout", str(p), "-"]
    else:
        return p.read_text(encoding="utf-8", errors="replace")
    return subprocess.run(cmd, check=True, capture_output=True, text=True).stdout


def tokens(text):
    # Normalize spacing so formatting-only differences (e.g. pandoc's list
    # indentation) don't show as changes, then keep words, punctuation and
    # whitespace as separate tokens so the output preserves paragraph breaks.
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return re.findall(r"\s+|\w+|[^\w\s]", text.strip())


def opcodes(old, new):
    a, b = tokens(old), tokens(new)
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        yield tag, "".join(a[i1:i2]), "".join(b[j1:j2])


def as_text(old, new):
    out = []
    for tag, a, b in opcodes(old, new):
        if tag == "equal":
            out.append(a)
            continue
        if a:
            out.append(f"[-{a}-]")
        if b:
            out.append(f"{{+{b}+}}")
    return "".join(out)


def as_html(old, new, title):
    out = []
    for tag, a, b in opcodes(old, new):
        if tag == "equal":
            out.append(html.escape(a))
            continue
        if a:
            out.append(f"<del>{html.escape(a)}</del>")
        if b:
            out.append(f"<ins>{html.escape(b)}</ins>")
    body = "".join(out).replace("\n", "<br>\n")
    return f"""<!doctype html>
<meta charset="utf-8"><title>{html.escape(title)}</title>
<style>
body{{font:15px/1.6 Georgia,serif;max-width:52rem;margin:2rem auto;padding:0 1rem;background:#fff;color:#111}}
del{{color:#b00020;text-decoration:line-through}}
ins{{color:#0b57d0;text-decoration:underline}}
</style>
<h1>{html.escape(title)}</h1>
<p>Deletions in red strikethrough, additions in blue underline.</p>
{body}
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("old")
    ap.add_argument("new")
    ap.add_argument("-o", "--output")
    ap.add_argument("--text", action="store_true", help="plain-text markers instead of HTML")
    args = ap.parse_args()

    old, new = load(args.old), load(args.new)
    title = f"Redline: {Path(args.old).name} → {Path(args.new).name}"
    result = as_text(old, new) if args.text else as_html(old, new, title)
    if args.output:
        Path(args.output).write_text(result, encoding="utf-8")
    else:
        sys.stdout.write(result)


if __name__ == "__main__":
    main()
