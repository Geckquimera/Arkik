// --- Menú móvil ---
const navToggle = document.getElementById('navToggle');
if (navToggle) {
  navToggle.addEventListener('click', () => {
    document.querySelector('.nav-links').classList.toggle('open');
  });
}

// --- Formulario de cotización (sitio estático: solo muestra confirmación) ---
const form = document.getElementById('quoteForm');
if (form) {
  const note = document.getElementById('formNote');
  form.addEventListener('submit', (e) => {
    e.preventDefault();
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
