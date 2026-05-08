import re

css_path = r"d:\my\styles.css"
html_path = r"d:\my\global-kids-school (3).html"

with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# About
css = re.sub(
    r'\.about-img-a\s*\{[^}]*background:\s*linear-gradient[^;]*;',
    r'.about-img-a {\n  background: url("https://images.unsplash.com/photo-1577896851231-70ef18881754?auto=format&fit=crop&q=80&w=800") center/cover no-repeat;',
    css
)
css = re.sub(
    r'\.about-img-b\s*\{[^}]*background:\s*linear-gradient[^;]*;',
    r'.about-img-b {\n  background: url("https://images.unsplash.com/photo-1509062522246-3755977927d7?auto=format&fit=crop&q=80&w=600") center/cover no-repeat;',
    css
)

# Programs
css = re.sub(r'\.p1\s*\{[^}]*\}', r'.p1 { background: url("https://images.unsplash.com/photo-1587691592099-24045742c181?auto=format&fit=crop&q=80&w=600") center/cover no-repeat; }', css)
css = re.sub(r'\.p2\s*\{[^}]*\}', r'.p2 { background: url("https://images.unsplash.com/photo-1503676260728-1c00da094a0b?auto=format&fit=crop&q=80&w=600") center/cover no-repeat; }', css)
css = re.sub(r'\.p3\s*\{[^}]*\}', r'.p3 { background: url("https://images.unsplash.com/photo-1427504494785-3a9ca7044f45?auto=format&fit=crop&q=80&w=600") center/cover no-repeat; }', css)
css = re.sub(r'\.p4\s*\{[^}]*\}', r'.p4 { background: url("https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&q=80&w=600") center/cover no-repeat; }', css)

# Facilities
css = re.sub(r'\.fi-blue\s*\{[^}]*\}', r'.fi-blue { background: url("https://images.unsplash.com/photo-1516321497487-e288fb19713f?auto=format&fit=crop&q=80&w=600") center/cover no-repeat; }', css)
css = re.sub(r'\.fi-green\s*\{[^}]*\}', r'.fi-green { background: url("https://images.unsplash.com/photo-1461896836934-ffe607ba8211?auto=format&fit=crop&q=80&w=600") center/cover no-repeat; }', css)
css = re.sub(r'\.fi-purple\s*\{[^}]*\}', r'.fi-purple { background: url("https://images.unsplash.com/photo-1507676184212-d0330a15183c?auto=format&fit=crop&q=80&w=600") center/cover no-repeat; }', css)
css = re.sub(r'\.fi-orange\s*\{[^}]*\}', r'.fi-orange { background: url("https://images.unsplash.com/photo-1532094349884-543bc11b234d?auto=format&fit=crop&q=80&w=600") center/cover no-repeat; }', css)
css = re.sub(r'\.fi-teal\s*\{[^}]*\}', r'.fi-teal { background: url("https://images.unsplash.com/photo-1507842217343-583bb7270b66?auto=format&fit=crop&q=80&w=600") center/cover no-repeat; }', css)
css = re.sub(r'\.fi-navy\s*\{[^}]*\}', r'.fi-navy { background: url("https://images.unsplash.com/photo-1557223562-6c77ef1607bf?auto=format&fit=crop&q=80&w=600") center/cover no-repeat; }', css)

# Gallery
css = re.sub(r'\.gal-item:nth-child\(1\)\s*\{[^}]*\}', r'.gal-item:nth-child(1) { grid-column: span 2; grid-row: span 2; background: url("https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&q=80&w=800") center/cover no-repeat; }', css)
css = re.sub(r'\.gal-item:nth-child\(2\)\s*\{[^}]*\}', r'.gal-item:nth-child(2) { background: url("https://images.unsplash.com/photo-1509062522246-3755977927d7?auto=format&fit=crop&q=80&w=800") center/cover no-repeat; }', css)
css = re.sub(r'\.gal-item:nth-child\(3\)\s*\{[^}]*\}', r'.gal-item:nth-child(3) { background: url("https://images.unsplash.com/photo-1540569014015-19a7be504e3a?auto=format&fit=crop&q=80&w=800") center/cover no-repeat; }', css)
css = re.sub(r'\.gal-item:nth-child\(4\)\s*\{[^}]*\}', r'.gal-item:nth-child(4) { background: url("https://images.unsplash.com/photo-1497633762265-9d179a990aa6?auto=format&fit=crop&q=80&w=800") center/cover no-repeat; }', css)
css = re.sub(r'\.gal-item:nth-child\(5\)\s*\{[^}]*\}', r'.gal-item:nth-child(5) { background: url("https://images.unsplash.com/photo-1577896851231-70ef18881754?auto=format&fit=crop&q=80&w=800") center/cover no-repeat; }', css)

# Teachers
css = re.sub(r'\.tp1\s*\{[^}]*\}', r'.tp1 { background: url("https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&q=80&w=400") center/cover no-repeat; }', css)
css = re.sub(r'\.tp2\s*\{[^}]*\}', r'.tp2 { background: url("https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&q=80&w=400") center/cover no-repeat; }', css)
css = re.sub(r'\.tp3\s*\{[^}]*\}', r'.tp3 { background: url("https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?auto=format&fit=crop&q=80&w=400") center/cover no-repeat; }', css)
css = re.sub(r'\.tp4\s*\{[^}]*\}', r'.tp4 { background: url("https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&q=80&w=400") center/cover no-repeat; }', css)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

# HTML Emoji Removal
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace emojis inside elements
html = re.sub(r'<div class="about-img-a">🏫</div>', r'<div class="about-img-a"></div>', html)
html = re.sub(r'<div class="about-img-b">📚</div>', r'<div class="about-img-b"></div>', html)

html = re.sub(r'<div class="prog-bg p1">🎠</div>', r'<div class="prog-bg p1"></div>', html)
html = re.sub(r'<div class="prog-bg p2">📖</div>', r'<div class="prog-bg p2"></div>', html)
html = re.sub(r'<div class="prog-bg p3">🔬</div>', r'<div class="prog-bg p3"></div>', html)
html = re.sub(r'<div class="prog-bg p4">🏛️</div>', r'<div class="prog-bg p4"></div>', html)

html = re.sub(r'<div class="facility-img fi-blue">🖥️</div>', r'<div class="facility-img fi-blue"></div>', html)
html = re.sub(r'<div class="facility-img fi-green">⚽</div>', r'<div class="facility-img fi-green"></div>', html)
html = re.sub(r'<div class="facility-img fi-purple">🎭</div>', r'<div class="facility-img fi-purple"></div>', html)
html = re.sub(r'<div class="facility-img fi-orange">🔬</div>', r'<div class="facility-img fi-orange"></div>', html)
html = re.sub(r'<div class="facility-img fi-teal">📚</div>', r'<div class="facility-img fi-teal"></div>', html)
html = re.sub(r'<div class="facility-img fi-navy">🚌</div>', r'<div class="facility-img fi-navy"></div>', html)

html = re.sub(r'<div class="gal-item">🏫<div class="gal-over">', r'<div class="gal-item"><div class="gal-over">', html)
html = re.sub(r'<div class="gal-item">🧪<div class="gal-over">', r'<div class="gal-item"><div class="gal-over">', html)
html = re.sub(r'<div class="gal-item">⚽<div class="gal-over">', r'<div class="gal-item"><div class="gal-over">', html)
html = re.sub(r'<div class="gal-item">🎭<div class="gal-over">', r'<div class="gal-item"><div class="gal-over">', html)
html = re.sub(r'<div class="gal-item">🎨<div class="gal-over">', r'<div class="gal-item"><div class="gal-over">', html)

html = re.sub(r'<div class="teacher-photo tp1">👩‍🏫</div>', r'<div class="teacher-photo tp1"></div>', html)
html = re.sub(r'<div class="teacher-photo tp2">👨‍🏫</div>', r'<div class="teacher-photo tp2"></div>', html)
html = re.sub(r'<div class="teacher-photo tp3">👩‍🎨</div>', r'<div class="teacher-photo tp3"></div>', html)
html = re.sub(r'<div class="teacher-photo tp4">👨‍💻</div>', r'<div class="teacher-photo tp4"></div>', html)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Photos added successfully.")
