/* =============================================================================
   ISMS CORE - Landing Page Scripts
   ============================================================================= */

document.addEventListener('DOMContentLoaded', () => {
    // Navigation scroll effect
    const nav = document.getElementById('nav');
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;

        if (currentScroll > 50) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }

        lastScroll = currentScroll;
    });

    // Mobile navigation toggle
    const navToggle = document.getElementById('nav-toggle');
    const navMenu = document.getElementById('nav-menu');

    navToggle.addEventListener('click', () => {
        navToggle.classList.toggle('active');
        navMenu.classList.toggle('active');
    });

    // Close mobile menu on link click
    navMenu.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            navToggle.classList.remove('active');
            navMenu.classList.remove('active');
        });
    });

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const offset = 80; // Account for fixed nav
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - offset;
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Animate progress bars on scroll
    const progressBars = document.querySelectorAll('.progress-fill');
    const animateOnScroll = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.width = entry.target.style.width || '0%';
            }
        });
    }, { threshold: 0.5 });

    progressBars.forEach(bar => {
        const width = bar.style.width;
        bar.style.width = '0%';
        animateOnScroll.observe(bar);

        // Re-animate when visible
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    setTimeout(() => {
                        bar.style.width = width;
                    }, 200);
                }
            });
        }, { threshold: 0.3 });
        observer.observe(bar);
    });

    // Fade in elements on scroll
    const fadeElements = document.querySelectorAll('.feature, .framework-card, .progress-card, .timeline-item, .arch-item');
    const fadeObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

    fadeElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        fadeObserver.observe(el);
    });

    // Counter animation for stats
    const animateCounter = (el, target, duration = 1500) => {
        let start = 0;
        const increment = target / (duration / 16);
        const isPercentage = el.textContent.includes('%');
        const isRatio = el.textContent.includes('/');

        if (isRatio) return; // Don't animate ratios

        const updateCounter = () => {
            start += increment;
            if (start < target) {
                el.textContent = isPercentage ?
                    Math.floor(start) + '%' :
                    Math.floor(start) + (el.textContent.includes('+') ? '+' : '');
                requestAnimationFrame(updateCounter);
            } else {
                el.textContent = isPercentage ?
                    target + '%' :
                    target + (el.dataset.suffix || '');
            }
        };

        updateCounter();
    };

    // Observe stat values for animation
    const statValues = document.querySelectorAll('.stat-value, .metric-value');
    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !entry.target.dataset.animated) {
                entry.target.dataset.animated = 'true';
                const text = entry.target.textContent;
                const num = parseFloat(text.replace(/[^0-9.]/g, ''));

                if (!isNaN(num) && !text.includes('/')) {
                    if (text.includes('K')) {
                        entry.target.dataset.suffix = 'K+';
                        animateCounter(entry.target, num);
                    } else if (text.includes('%')) {
                        animateCounter(entry.target, num);
                    } else if (text.includes('+')) {
                        entry.target.dataset.suffix = '+';
                        animateCounter(entry.target, num);
                    }
                }
            }
        });
    }, { threshold: 0.5 });

    statValues.forEach(stat => counterObserver.observe(stat));

    // Parallax effect for hero background
    const heroBg = document.querySelector('.hero-bg');
    if (heroBg) {
        window.addEventListener('scroll', () => {
            const scroll = window.pageYOffset;
            heroBg.style.transform = `translateY(${scroll * 0.3}px)`;
        });
    }

    // Add keyboard navigation support
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && navMenu.classList.contains('active')) {
            navToggle.classList.remove('active');
            navMenu.classList.remove('active');
        }
    });

    console.log('🎋 ISMS CORE - Where bamboo antennas actually work.');
});
