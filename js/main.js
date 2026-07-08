// --- Menú móvil ---
const navToggle = document.getElementById('navToggle');
if (navToggle) {
  navToggle.addEventListener('click', () => {
    document.querySelector('.nav-links').classList.toggle('open');
  });
}

// --- Formulario de cotización: abre el correo del visitante con todo prellenado hacia Arkik ---
const form = document.getElementById('quoteForm');
if (form) {
  const note = document.getElementById('formNote');
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const data = new FormData(form);
    const subject = encodeURIComponent('Solicitud de cotización — ' + (data.get('name') || 'Sitio web'));
    const body = encodeURIComponent(
      `Nombre: ${data.get('name') || ''}\n` +
      `Teléfono: ${data.get('phone') || ''}\n` +
      `Email: ${data.get('email') || ''}\n` +
      `Servicio de interés: ${data.get('service') || ''}\n`
    );
    window.location.href = `mailto:arkik.desarrollos@gmail.com?subject=${subject}&body=${body}`;
    note.classList.add('show');
    form.reset();
  });
}

// --- Scroll reveal: el contenido aparece con fundido al entrar en pantalla ---
const revealEls = document.querySelectorAll('.reveal, .reveal-stagger');
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('in-view');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.15 });
revealEls.forEach(el => revealObserver.observe(el));

// --- Carruseles de imágenes dentro de una misma tarjeta ---
document.querySelectorAll('.card-carousel').forEach(carousel => {
  const track = carousel.querySelector('.carousel-track');
  const slides = Array.from(track.children);
  const dotsWrap = carousel.querySelector('.carousel-dots');
  const prevBtn = carousel.querySelector('.carousel-arrow.prev');
  const nextBtn = carousel.querySelector('.carousel-arrow.next');
  let index = 0;

  if (slides.length <= 1) {
    if (dotsWrap) dotsWrap.style.display = 'none';
    if (prevBtn) prevBtn.style.display = 'none';
    if (nextBtn) nextBtn.style.display = 'none';
    return;
  }

  slides.forEach((_, i) => {
    const dot = document.createElement('button');
    if (i === 0) dot.classList.add('active');
    dot.setAttribute('aria-label', `Ver imagen ${i + 1}`);
    dot.addEventListener('click', () => goTo(i));
    if (dotsWrap) dotsWrap.appendChild(dot);
  });

  function goTo(i) {
    index = (i + slides.length) % slides.length;
    track.style.transform = `translateX(-${index * 100}%)`;
    if (dotsWrap) {
      dotsWrap.querySelectorAll('button').forEach((d, di) => d.classList.toggle('active', di === index));
    }
  }

  if (prevBtn) prevBtn.addEventListener('click', () => goTo(index - 1));
  if (nextBtn) nextBtn.addEventListener('click', () => goTo(index + 1));

  // rotación automática cada 4.5s
  setInterval(() => goTo(index + 1), 4500);
});

// --- Video de fondo: si el archivo no carga, ocultarlo y dejar el color/imagen de respaldo ---
document.querySelectorAll('video[data-bg]').forEach(video => {
  video.addEventListener('error', () => { video.style.display = 'none'; });
});

// --- Portafolio: collage en abanico que se desliza progresivamente (como una banda) ---
const fan = document.querySelector('.portfolio-fan');
if (fan) {
  const images = JSON.parse(fan.dataset.images || '[]');
  const mobile = window.matchMedia('(max-width: 760px)').matches;

  // posición visual según qué tan lejos está una imagen del centro (0 = al frente)
  // todas comparten el mismo centro vertical (ty: -50%) para que la fila quede alineada
  const POSITIONS = {
    0: { w: 340, h: 260, tx: '-50%',  ty: '-50%', scale: 1, opacity: 1,    z: 5 },
    1: { w: 220, h: 180, tx: '20%',   ty: '-50%', scale: 1, opacity: 0.75, z: 4 },
    '-1': { w: 220, h: 180, tx: '-220%', ty: '-50%', scale: 1, opacity: 0.75, z: 4 },
    2: { w: 170, h: 130, tx: '115%',  ty: '-50%', scale: 1, opacity: 0.4,  z: 3 },
    '-2': { w: 170, h: 130, tx: '-345%', ty: '-50%', scale: 1, opacity: 0.4,  z: 3 },
    3: { w: 170, h: 130, tx: '260%',  ty: '-50%', scale: 1, opacity: 0,    z: 2 },
    '-3': { w: 170, h: 130, tx: '-490%', ty: '-50%', scale: 1, opacity: 0,    z: 2 },
  };
  const MOBILE_POSITIONS = {
    0: { w: 220, h: 170, tx: '-50%', ty: '-50%', scale: 1, opacity: 1,    z: 5 },
    1: { w: 150, h: 120, tx: '15%',  ty: '-50%', scale: 1, opacity: 0.7,  z: 4 },
    '-1': { w: 150, h: 120, tx: '-195%', ty: '-50%', scale: 1, opacity: 0.7, z: 4 },
    2: { w: 120, h: 95,  tx: '140%', ty: '-50%', scale: 1, opacity: 0,    z: 3 },
    '-2': { w: 120, h: 95,  tx: '-355%', ty: '-50%', scale: 1, opacity: 0, z: 3 },
    3: { w: 120, h: 95,  tx: '230%', ty: '-50%', scale: 1, opacity: 0,    z: 2 },
    '-3': { w: 120, h: 95,  tx: '-450%', ty: '-50%', scale: 1, opacity: 0, z: 2 },
  };
  const table = mobile ? MOBILE_POSITIONS : POSITIONS;
  const MAX_OFFSET = 3;

  // crea un <div class="fan-item"> por cada imagen, una sola vez
  const items = images.map((src) => {
    const el = document.createElement('div');
    el.className = 'fan-item';
    const img = document.createElement('img');
    img.src = src;
    img.alt = 'Proyecto Arkik';
    img.loading = 'lazy';
    el.appendChild(img);
    fan.appendChild(el);
    return el;
  });

  let centerIndex = 0;

  function place(el, offset, animate) {
    const clamped = Math.max(-MAX_OFFSET, Math.min(MAX_OFFSET, offset));
    const pos = table[clamped];
    el.style.transition = animate ? '' : 'none';
    el.style.width = pos.w + 'px';
    el.style.height = pos.h + 'px';
    el.style.transform = `translate(${pos.tx}, ${pos.ty}) scale(${pos.scale})`;
    el.style.opacity = pos.opacity;
    el.style.zIndex = pos.z;
  }

  function render(animate) {
    const n = images.length;
    items.forEach((el, i) => {
      let offset = i - centerIndex;
      // normaliza al camino más corto (izquierda o derecha) para que la banda no dé vueltas largas
      if (offset > n / 2) offset -= n;
      if (offset < -n / 2) offset += n;
      place(el, offset, animate);
    });
  }

  render(false); // primer pintado, sin animación
  requestAnimationFrame(() => requestAnimationFrame(() => {
    items.forEach(el => { el.style.transition = ''; });
  }));

  if (images.length > 1) {
    setInterval(() => {
      centerIndex = (centerIndex + 1) % images.length;
      render(true);
    }, 3800);
  }
}
