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

// Fondo matrix sutil
const canvas = document.getElementById('matrix-bg');
if (canvas) {
    const ctx = canvas.getContext('2d');
    let width, height, columns, drops;

    const chars = '01アイウエオカキクケコサシスセソ$#@%';

    function resize() {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
        const fontSize = 16;
        columns = Math.floor(width / fontSize / 2); // menos columnas = más minimal
        drops = new Array(columns).fill(0).map(() => Math.random() * -50);
    }
    resize();
    window.addEventListener('resize', resize);

    function draw() {
        ctx.fillStyle = 'rgba(10, 10, 10, 0.08)'; // estela suave
        ctx.fillRect(0, 0, width, height);

        ctx.fillStyle = 'rgba(0, 255, 65, 0.25)'; // verde, baja opacidad
        ctx.font = '10px monospace';

        const fontSize = 16;
        const spacing = width / columns;

        drops.forEach((y, i) => {
            const char = chars[Math.floor(Math.random() * chars.length)];
            const x = i * spacing;
            ctx.fillText(char, x, y * fontSize);
            if (y * fontSize > height && Math.random() > 0.98) {
                drops[i] = 0;
            } else {
                drops[i] += 0.4; // velocidad lenta
            }
        });
    }

    setInterval(draw, 60); // menos FPS = más sutil, más liviano
}