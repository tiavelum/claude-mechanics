"""List every cited source page with the statements that cite it, for re-reading page by page.

Usage: python3 list-sources.py
"""

from statements import all_statements

by_url = {}
for sid, s in all_statements().items():
    for url in s["urls"]:
        by_url.setdefault(url, []).append(sid)

for url in sorted(by_url):
    print(url)
    print("  " + ", ".join(by_url[url]))

observed = [sid for sid, s in all_statements().items() if s["label"] == "observed"]
print(f"\n{len(by_url)} pages; observed statements to re-test: {', '.join(observed)}")
