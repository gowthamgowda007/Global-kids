import re

css_path = r"d:\my\styles.css"
html_path = r"d:\my\global-kids-school (3).html"

def replace_colors(content):
    # Hex
    content = content.replace("#09152a", "#003049")
    content = content.replace("#0d1e38", "#001f30")
    content = content.replace("#152847", "#00507a")
    content = content.replace("#c9933a", "#F77F00")
    content = content.replace("#e8b55a", "#FCBF49")
    
    # Uppercase hex just in case
    content = content.replace("#09152A", "#003049")
    content = content.replace("#0D1E38", "#001f30")
    content = content.replace("#152847", "#00507a")
    content = content.replace("#C9933A", "#F77F00")
    content = content.replace("#E8B55A", "#FCBF49")

    # RGB values used in rgba
    content = content.replace("9,21,42", "0,48,73")
    content = content.replace("201,147,58", "247,127,0")
    
    return content

with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

css = replace_colors(css)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

html = replace_colors(html)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Colors updated successfully.")
