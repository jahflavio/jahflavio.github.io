gsap.registerPlugin(ScrollTrigger);

document.addEventListener("DOMContentLoaded", () => {
  // Hero Section Animations
  gsap.fromTo(".hero-text", 
    { opacity: 0, y: 50 }, 
    { opacity: 1, y: 0, duration: 1, stagger: 0.2, ease: "power3.out" }
  );

  gsap.fromTo(".hero-image",
    { opacity: 0, scale: 0.9 },
    { opacity: 1, scale: 1, duration: 1.2, delay: 0.5, ease: "power3.out" }
  );

  // Experience Section Scroll Animations
  gsap.utils.toArray('.job-card').forEach((card, i) => {
    gsap.fromTo(card,
      { opacity: 0, x: -50 },
      {
        opacity: 1, x: 0,
        duration: 0.8,
        ease: "power2.out",
        scrollTrigger: {
          trigger: card,
          start: "top 85%",
          toggleActions: "play none none reverse"
        }
      }
    );
  });

  // Skills Scroll Animations
  gsap.utils.toArray('.skill-badge').forEach((badge, i) => {
    gsap.fromTo(badge,
      { opacity: 0, scale: 0.5 },
      {
        opacity: 1, scale: 1,
        duration: 0.5,
        ease: "back.out(1.7)",
        scrollTrigger: {
          trigger: badge,
          start: "top 90%",
          toggleActions: "play none none reverse"
        }
      }
    );
  });
  
  // Certifications Scroll Animations
  gsap.utils.toArray('.cert-card').forEach((cert, i) => {
    gsap.fromTo(cert,
      { opacity: 0, y: 30 },
      {
        opacity: 1, y: 0,
        duration: 0.6,
        ease: "power2.out",
        scrollTrigger: {
          trigger: cert,
          start: "top 90%",
          toggleActions: "play none none reverse"
        }
      }
    );
  });

  // Mobile Menu Toggle
  const mobileMenuBtn = document.getElementById("mobile-menu-btn");
  const mobileMenu = document.getElementById("mobile-menu");
  if (mobileMenuBtn && mobileMenu) {
    mobileMenuBtn.addEventListener("click", () => {
      if (mobileMenu.style.display === "flex") {
        mobileMenu.style.display = "none";
        mobileMenuBtn.innerHTML = '<i class="fas fa-bars text-xl"></i>';
      } else {
        mobileMenu.style.display = "flex";
        mobileMenuBtn.innerHTML = '<i class="fas fa-times text-xl"></i>';
      }
    });
  }
  // Navbar Scroll Effect
  const nav = document.querySelector('.editorial-nav');
  if (nav) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 20) {
        nav.classList.add('scrolled');
      } else {
        nav.classList.remove('scrolled');
      }
    });
  }
});
