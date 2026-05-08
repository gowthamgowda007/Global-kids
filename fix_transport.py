import re

css_path = r"d:\my\styles.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Fix Safe Transport
css = re.sub(
    r'\.fi-navy\s*\{[^}]*\}', 
    r'.fi-navy { background: url("https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&q=80&w=600") center/cover no-repeat; }', 
    css
)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)
