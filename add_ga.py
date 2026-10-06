import os

GA_TAG = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-29MQ37RJFB"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-29MQ37RJFB');
</script>
"""

FILES = [
    "index.html",
    "angebote/microsoft-365/index.html",
    "angebote/antiviren/index.html",
    "angebote/vpn/index.html",
    "about/index.html",
    "affiliate/index.html",
    "datenschutz/index.html",
    "impressum/index.html",
]

changed = []
for f in FILES:
    path = os.path.join("/opt/data/software-deals", f)
    with open(path, "r", encoding="utf-8") as fh:
        content = fh.read()
    if "G-29MQ37RJFB" in content:
        print(f"⚠️  {f}: already has gtag")
        continue
    if "</head>" in content:
        new_content = content.replace("</head>", GA_TAG + "</head>", 1)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(new_content)
        print(f"✅ {f}: gtag added")
        changed.append(f)
    else:
        print(f"⚠️  {f}: no </head> found")

print(f"\nTotal: {len(changed)} files updated")
