import re

html_path = r"d:\my\global-kids-school (3).html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Extract CSS
style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
if style_match:
    css_content = style_match.group(1).strip()
    with open(r"d:\my\styles.css", "w", encoding="utf-8") as f:
        f.write(css_content)
    content = content[:style_match.start()] + '<link rel="stylesheet" href="styles.css">' + content[style_match.end():]
    print("Extracted CSS.")

# 2. Extract JS
script_match = re.search(r'<script>(.*?)</script>', content, re.DOTALL)
if script_match:
    js_content = script_match.group(1).strip()
    with open(r"d:\my\script.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    content = content[:script_match.start()] + '<script src="script.js"></script>' + content[script_match.end():]
    print("Extracted JS.")

# 3. Add OG Tags
og_tags = """
<meta property="og:title" content="Global Kids International School">
<meta property="og:description" content="Nurturing curious, confident, and compassionate global citizens since 2009. Admissions open for 2025–26.">
<meta property="og:image" content="https://globalkids.edu.in/og-image.jpg">
<meta property="og:url" content="https://globalkids.edu.in">
"""
content = content.replace('</title>', '</title>\n' + og_tags.strip())
print("Added OG tags.")

# 4. Fix Forms
admissions_form = """      <div class="form-row">
        <div class="form-group">
          <label for="adm-parent-name">Parent Name</label>
          <input type="text" id="adm-parent-name" placeholder="Your full name" required>
        </div>
        <div class="form-group">
          <label for="adm-phone">Phone Number</label>
          <input type="tel" id="adm-phone" placeholder="+91 98765 43210" required>
        </div>
      </div>
      <div class="form-group">
        <label for="adm-email">Email Address</label>
        <input type="email" id="adm-email" placeholder="your@email.com" required>
      </div>
      <div class="form-row">
        <div class="form-group">
          <label for="adm-child-name">Child's Name</label>
          <input type="text" id="adm-child-name" placeholder="Child's full name" required>
        </div>
        <div class="form-group">
          <label for="adm-grade">Applying for Grade</label>
          <select id="adm-grade" required>
            <option value="">Select Grade</option>
            <option>Pre-School (Age 2.5–4)</option>
            <option>Kindergarten</option>
            <option>Grade 1</option><option>Grade 2</option>
            <option>Grade 3</option><option>Grade 4</option>
            <option>Grade 5</option><option>Grade 6</option>
            <option>Grade 7</option><option>Grade 8</option>
            <option>Grade 9</option><option>Grade 10</option>
            <option>Grade 11</option><option>Grade 12</option>
          </select>
        </div>
      </div>
      <div class="form-group">
        <label for="adm-message">Message / Questions</label>
        <textarea id="adm-message" placeholder="Any specific questions or requirements?"></textarea>
      </div>"""

content, count_adm = re.subn(
    r'<div class="form-row">\s*<div class="form-group">\s*<label>Parent Name.*?</textarea>\s*</div>',
    admissions_form,
    content,
    flags=re.DOTALL
)
print(f"Updated Admissions form: {count_adm} match(es)")

contact_form = """      <div class="form-row">
        <div class="form-group">
          <label for="contact-name">Your Name</label>
          <input type="text" id="contact-name" placeholder="Full name" required>
        </div>
        <div class="form-group">
          <label for="contact-phone">Phone</label>
          <input type="tel" id="contact-phone" placeholder="+91 ..." required>
        </div>
      </div>
      <div class="form-group">
        <label for="contact-email">Email</label>
        <input type="email" id="contact-email" placeholder="your@email.com" required>
      </div>
      <div class="form-group">
        <label for="contact-subject">Subject</label>
        <select id="contact-subject" required>
          <option value="">Select subject</option>
          <option>Admission Enquiry</option>
          <option>Fee Structure</option>
          <option>Campus Visit</option>
          <option>Transport Routes</option>
          <option>Other</option>
        </select>
      </div>
      <div class="form-group">
        <label for="contact-message">Message</label>
        <textarea id="contact-message" placeholder="Your message here..." required></textarea>
      </div>"""

content, count_contact = re.subn(
    r'<div class="form-row">\s*<div class="form-group">\s*<label>Your Name.*?</textarea>\s*</div>',
    contact_form,
    content,
    flags=re.DOTALL
)
print(f"Updated Contact form: {count_contact} match(es)")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Saved modifications.")
