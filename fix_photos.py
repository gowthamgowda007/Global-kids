import re

css_path = r"d:\my\styles.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Fix Campus photo (using a very reliable image ID for a building/campus)
css = re.sub(
    r'\.gal-item:nth-child\(1\)\s*\{[^}]*\}', 
    r'.gal-item:nth-child(1) { grid-column: span 2; grid-row: span 2; background: url("https://images.unsplash.com/photo-1541829070764-84a7d30dd3f3?auto=format&fit=crop&q=80&w=800") center/cover no-repeat; }', 
    css
)

# Fix Performing Arts
css = re.sub(
    r'\.fi-purple\s*\{[^}]*\}', 
    r'.fi-purple { background: url("https://images.unsplash.com/photo-1514525253161-7a46d19cd819?auto=format&fit=crop&q=80&w=600") center/cover no-repeat; }', 
    css
)

# Fix Safe Transport (using a clear school bus image)
css = re.sub(
    r'\.fi-navy\s*\{[^}]*\}', 
    r'.fi-navy { background: url("https://images.unsplash.com/photo-1518655048521-f130df041f66?auto=format&fit=crop&q=80&w=600") center/cover no-repeat; }', 
    css
)

# Fix Teachers positions (align background closer to top to show faces properly)
css = re.sub(r'(\.tp1\s*\{[^}]*background:\s*url\([^)]+\))\s+center/cover', r'\1 center 15%/cover', css)
css = re.sub(r'(\.tp2\s*\{[^}]*background:\s*url\([^)]+\))\s+center/cover', r'\1 center 15%/cover', css)
css = re.sub(r'(\.tp3\s*\{[^}]*background:\s*url\([^)]+\))\s+center/cover', r'\1 center 15%/cover', css)
css = re.sub(r'(\.tp4\s*\{[^}]*background:\s*url\([^)]+\))\s+center/cover', r'\1 center 15%/cover', css)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("Fixed missing photos and aligned faculty photos.")
