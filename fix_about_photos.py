import re

css_path = r"d:\my\styles.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

css = re.sub(
    r'\.about-img-a\s*\{[^}]*background:\s*url\([^)]+\)[^}]*\}', 
    r'.about-img-a { background: url("https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?auto=format&fit=crop&q=80&w=800") center/cover no-repeat; }', 
    css
)

css = re.sub(
    r'\.about-img-b\s*\{[^}]*background:\s*url\([^)]+\)[^}]*\}', 
    r'.about-img-b { background: url("https://images.unsplash.com/photo-1503676382389-4809596d5290?auto=format&fit=crop&q=80&w=600") center/cover no-repeat; }', 
    css
)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("Updated about section photos.")
