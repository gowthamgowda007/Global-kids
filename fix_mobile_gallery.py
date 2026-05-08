import re

css_path = r"d:\my\styles.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Fix mobile view for gallery
css = re.sub(
    r'\.gallery-mosaic\s*\{\s*grid-template-columns:\s*1fr 1fr;\s*grid-template-rows:\s*auto;\s*\}', 
    r'.gallery-mosaic { grid-template-columns: 1fr 1fr; grid-auto-rows: 150px; }', 
    css
)

# In the media query, gal-item:nth-child(1) should span 1 row, not 2
# It's currently right after .gallery-mosaic in the media query
css = re.sub(
    r'(\.gallery-mosaic\s*\{\s*grid-template-columns:\s*1fr 1fr;\s*grid-auto-rows:\s*150px;\s*\})\s*\n\s*\.gal-item:nth-child\(1\)\s*\{[^}]*\}',
    r'\1\n  .gal-item:nth-child(1) { grid-column: span 2; grid-row: span 1; }',
    css
)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("Fixed gallery mobile view.")
