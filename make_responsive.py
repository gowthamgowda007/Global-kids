import re

css_path = r"d:\my\styles.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

mobile_css = """
@media (max-width: 768px) {
  /* Reduce padding on cards for mobile screens to save space */
  .why-card { padding: 20px 16px; }
  .tcard { padding: 20px 16px; }
  .adm-form { padding: 24px 16px; }
  .contact-form { padding: 24px 16px; }
  .prog-content { padding: 18px 16px; }
  .facility-body { padding: 16px 14px; }
  .teacher-body { padding: 16px 14px; }
  
  /* Shrink contact cards */
  .cinfo-card { padding: 16px; }
  .wa-btn { margin-top: 12px; font-size: 13px; padding: 12px 20px; width: 100%; justify-content: center; }
  
  /* Typography adjustments */
  .section-title { font-size: 28px !important; margin-bottom: 12px; }
  .section-desc { font-size: 14px; line-height: 1.6; }
  
  /* Reduce layout gaps */
  .hero-inner { gap: 32px; }
  .about-layout { gap: 32px; }
  .admissions-inner { gap: 32px; }
  .contact-layout { gap: 32px; }
}

@media (max-width: 520px) {
  .section-title { font-size: 24px !important; }
  .hero-desc { font-size: 14.5px; line-height: 1.6; }
  .hstat-num { font-size: 20px; }
  .btn-gold, .btn-ghost, .btn-form, .btn-dark { padding: 12px 20px; font-size: 13px; }
}
"""

css += mobile_css

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("Added responsive padding and typography rules.")
