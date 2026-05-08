// ── Navbar scroll ──────────────────────────
  const navbar = document.getElementById('navbar');
  window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 50);
    document.getElementById('scrollTop').classList.toggle('visible', window.scrollY > 400);
  }, { passive: true });

  // ── Mobile menu ────────────────────────────
  let menuOpen = false;
  function toggleMenu() {
    menuOpen = !menuOpen;
    const menu = document.getElementById('mobileMenu');
    const ham = document.getElementById('hamburger');
    menu.classList.toggle('open', menuOpen);
    ham.classList.toggle('active', menuOpen);
  }
  function closeMenu() {
    menuOpen = false;
    document.getElementById('mobileMenu').classList.remove('open');
    document.getElementById('hamburger').classList.remove('active');
  }

  // ── Intersection observer: fade-in ─────────
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => entry.target.classList.add('visible'), i * 90);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

  // ── Counter animation ──────────────────────
  function animateCounter(el, target) {
    const suffix = el.textContent.replace(/\d+/, '').trim();
    let start = 0;
    const duration = 2000;
    const step = Math.ceil(target / (duration / 16));
    const timer = setInterval(() => {
      start = Math.min(start + step, target);
      el.textContent = start.toLocaleString() + suffix;
      if (start >= target) clearInterval(timer);
    }, 16);
  }

  const counterObs = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.querySelectorAll('[data-target]').forEach(el => {
          animateCounter(el, parseInt(el.dataset.target));
        });
        counterObs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });

  document.querySelectorAll('#stats, #hero').forEach(el => counterObs.observe(el));

  // ── Smooth scroll for anchor links ─────────
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const target = document.querySelector(a.getAttribute('href'));
      if (target) {
        e.preventDefault();
        closeMenu();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // ── Form handlers ──────────────────────────
  function handleAdmission() {
    alert('✅ Thank you! Your admission enquiry has been submitted.\n\nOur admissions team will contact you within 24 hours.\n\nYou can also reach us on WhatsApp: +91 98765 43210');
  }

  function handleContact() {
    alert('✅ Thank you for your message!\n\nWe will get back to you within 1 business day.\n\nFor urgent queries: +91 98765 43210');
  }