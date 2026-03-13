gsap.registerPlugin(ScrollTrigger);

// --- Advanced Text Splitting Animation ---
const text = new SplitType('.scroll-text', { types: 'chars' });

gsap.from(text.chars, {
    opacity: 0,
    y: 100,
    rotateX: -90,
    stagger: 0.05,
    duration: 1.5,
    ease: "back.out(1.7)",
    delay: 1
});

// --- Hero Cinematic Flow ---
gsap.from(".hero-video-bg", {
    scale: 1.5,
    duration: 3,
    ease: "power2.out"
});

gsap.from(".hero-content p", {
    opacity: 0,
    letterSpacing: "30px",
    duration: 2,
    ease: "power3.out"
});

// --- Scroll Logic for Header ---
ScrollTrigger.create({
    start: "top -100",
    onUpdate: (self) => {
        const header = document.querySelector('header');
        if (self.direction === 1) { // Down
            header.classList.add('header-blur');
            document.body.setAttribute('data-scroll-dir', 'down');
        } else if (self.scroll() < 100) {
            header.classList.remove('header-blur');
            document.body.setAttribute('data-scroll-dir', 'up');
        }
    }
});

// --- Reveal Logic (Generic) ---
const revealsUp = document.querySelectorAll('.reveal-up');
revealsUp.forEach(el => {
    gsap.from(el, {
        scrollTrigger: {
            trigger: el,
            start: "top 85%",
            toggleActions: "play none none reverse"
        },
        y: 80,
        opacity: 0,
        duration: 1.5,
        ease: "expo.out"
    });
});

// --- Split Section Animations ---
gsap.from(".reveal-left", {
    scrollTrigger: {
        trigger: ".split-section",
        start: "top 70%",
    },
    x: -150,
    opacity: 0,
    duration: 2,
    ease: "power4.out"
});

gsap.from(".reveal-right", {
    scrollTrigger: {
        trigger: ".split-section",
        start: "top 70%",
    },
    x: 150,
    opacity: 0,
    duration: 2,
    ease: "power4.out",
    delay: 0.3
});

// --- Parallax Hover for Perfumes ---
const cards = document.querySelectorAll('.item-perfume');
cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
        const { left, top, width, height } = card.getBoundingClientRect();
        const x = (e.clientX - left) / width - 0.5;
        const y = (e.clientY - top) / height - 0.5;

        gsap.to(card, {
            rotationY: x * 30,
            rotationX: -y * 30,
            perspective: 1000,
            duration: 0.6,
            ease: "power3.out"
        });
    });

    card.addEventListener('mouseleave', () => {
        gsap.to(card, {
            rotationY: 0,
            rotationX: 0,
            duration: 1.2,
            ease: "elastic.out(1, 0.4)"
        });
    });
});

// --- Custom "Liquid" Scroll Feel ---
window.addEventListener('wheel', (e) => {
    // This is a subtle tilt of the whole body content on scroll
    const tilt = e.deltaY > 0 ? 0.5 : -0.5;
    gsap.to("main", {
        skewY: tilt,
        duration: 0.8,
        ease: "power3.out",
        overwrite: true,
        onComplete: () => {
            gsap.to("main", { skewY: 0, duration: 1.2, ease: "expo.out" });
        }
    });
}, { passive: true });

// --- Form Submission Simulation ---
const accessForm = document.querySelector('#access-form');
const formSuccess = document.querySelector('#form-success');

if (accessForm) {
    accessForm.addEventListener('submit', (e) => {
        e.preventDefault();
        accessForm.style.display = 'none';
        formSuccess.style.display = 'block';

        gsap.from(formSuccess, {
            opacity: 0,
            y: 20,
            duration: 1,
            ease: "power3.out"
        });
    });
}

// --- Back to Top Logic ---
const backToTop = document.querySelector('#backToTop');
window.addEventListener('scroll', () => {
    if (window.pageYOffset > 400) {
        backToTop.classList.add('show');
    } else {
        backToTop.classList.remove('show');
    }
});

// --- Smooth Scroll for All Anchors ---
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            window.scrollTo({
                top: target.offsetTop,
                behavior: 'smooth'
            });
        }
    });
});

// --- Catalogue Filtering Logic ---
const filterButtons = document.querySelectorAll('.filter-btn');
const perfumeItems = document.querySelectorAll('.item-perfume');

filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
        const filter = btn.getAttribute('data-filter');

        // Update active state
        filterButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        // Filter items with GSAP
        gsap.to(perfumeItems, {
            opacity: 0,
            scale: 0.8,
            duration: 0.4,
            ease: "power2.in",
            onComplete: () => {
                perfumeItems.forEach(item => {
                    if (filter === 'all' || item.classList.contains(filter)) {
                        item.classList.remove('hidden');
                    } else {
                        item.classList.add('hidden');
                    }
                });

                // Re-reveal filtered items
                gsap.to('.item-perfume:not(.hidden)', {
                    opacity: 1,
                    scale: 1,
                    duration: 0.6,
                    stagger: 0.1,
                    ease: "power2.out"
                });

                // Refresh scrolltrigger as heights might change
                ScrollTrigger.refresh();
            }
        });
    });
});
