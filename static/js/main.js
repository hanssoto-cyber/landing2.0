gsap.registerPlugin(ScrollTrigger);


// Typewriter en el hero
const typewriterEl = document.getElementById('typewriter');
if (typewriterEl) {
    const texto = 'Hola, soy Hans';
    let i = 0;
    const escribir = () => {
        if (i < texto.length) {
            typewriterEl.textContent += texto.charAt(i);
            i++;
            setTimeout(escribir, 80);
        }
    };
    escribir();
}

// Scroll reveal
const elementosReveal = document.querySelectorAll('[data-reveal]');
if (elementosReveal.length > 0) {
    gsap.set(elementosReveal, { opacity: 0, y: 30 });

    elementosReveal.forEach((el) => {
        gsap.to(el, {
            opacity: 1,
            y: 0,
            duration: 0.6,
            ease: 'power2.out',
            scrollTrigger: {
                trigger: el,
                start: 'top 85%',
                toggleActions: 'play none none none',
            },
        });
    });
}

// Contador animado en stats
const contadores = document.querySelectorAll('[data-counter]');
if (contadores.length > 0) {
    contadores.forEach((el) => {
        const valorFinal = parseInt(el.getAttribute('data-counter'), 10);
        const obj = { val: 0 };

        gsap.to(obj, {
            val: valorFinal,
            duration: 1.5,
            ease: 'power1.out',
            snap: { val: 1 },
            scrollTrigger: {
                trigger: el,
                start: 'top 85%',
                toggleActions: 'play none none none',
            },
            onUpdate: () => {
                el.textContent = obj.val;
            },
        });
    });
}