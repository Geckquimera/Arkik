import os

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Barlow+Condensed:wght@500;600;700&family=Barlow:wght@400;500;600&display=swap" rel="stylesheet">'

NAV_ITEMS = [
    ("index.html", "Inicio"),
    ("3d-studio.html", "3D Studio"),
    ("construccion.html", "Construcción"),
    ("remodelacion.html", "Remodelación"),
    ("servicios.html", "Servicios"),
    ("inversion.html", "Inversión"),
    ("legal.html", "Legal"),
    ("garantias.html", "Garantías"),
    ("politicas-privacidad.html", "Políticas y privacidad"),
    ("terminos-condiciones.html", "Términos y condiciones"),
]

def header(active):
    links = ""
    for href, label in NAV_ITEMS:
        cls = ' class="active"' if href == active else ""
        links += f'<li><a href="{href}"{cls}>{label}</a></li>\n'
    return f'''<header>
  <div class="nav">
    <a href="index.html" class="logo"><img src="images/logo.png" alt="Arkik Desarrollos"></a>
    <ul class="nav-links">
      {links}
    </ul>
    <a class="nav-cta" href="https://api.whatsapp.com/send?phone=526561095490" target="_blank" rel="noopener">Pide tu presupuesto</a>
    <button class="nav-toggle" id="navToggle" aria-label="Abrir menú">☰</button>
  </div>
</header>'''

FOOTER = '''<footer>
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <div class="footer-logo"><img src="images/footer-logo.jpg" alt="Arkik Desarrollos"></div>
        <p style="max-width:280px;">Construcción y remodelaciones en Ciudad Juárez. De la visión a la realidad.</p>
        <div class="socials">
          <a href="https://www.facebook.com/profile.php?id=61581260662167" target="_blank" rel="noopener" aria-label="Facebook"><img src="images/icon-facebook.png" alt=""></a>
          <a href="https://www.instagram.com/arkik_3d_studio/" target="_blank" rel="noopener" aria-label="Instagram"><img src="images/icon-instagram.png" alt=""></a>
          <a href="https://www.tiktok.com/@arkik_desarrollos" target="_blank" rel="noopener" aria-label="TikTok"><img src="images/icon-tiktok.png" alt=""></a>
          <a href="https://api.whatsapp.com/send?phone=526561095490" target="_blank" rel="noopener" aria-label="WhatsApp"><img src="images/icon-whatsapp.png" alt=""></a>
        </div>
      </div>
      <div>
        <h4>Contáctanos</h4>
        <ul>
          <li><a href="https://maps.app.goo.gl/6qmCh1wCLA6KnDSu8" target="_blank" rel="noopener">Parque Real #8124, Col. Los Parques, Ciudad Juárez, 32440</a></li>
          <li><a href="mailto:arkik.desarrollos@gmail.com">grupo.arkik@gmail.com</a></li>
          <li><a href="tel:+526561095490">+52 656 109 5490</a></li>
        </ul>
      </div>
      <div>
        <h4>Legal</h4>
        <ul>
          <li><a href="legal.html">Legal</a></li>
          <li><a href="garantias.html">Garantías</a></li>
          <li><a href="politicas-privacidad.html">Políticas y privacidad</a></li>
          <li><a href="terminos-condiciones.html">Términos y condiciones</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2020–2026 Arkik Desarrollos. Todos los derechos reservados.</span>
      <span>Ciudad Juárez, Chihuahua, México</span>
    </div>
  </div>
</footer>

<a class="wa-float" href="https://api.whatsapp.com/send?phone=526561095490" target="_blank" rel="noopener" aria-label="Escríbenos por WhatsApp">☎</a>

<script src="js/main.js"></script>'''

def page(title, description, active, body, extra_head=""):
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
{FONTS}
<link rel="stylesheet" href="css/style.css">
{extra_head}
</head>
<body>
{header(active)}
<main>
{body}
</main>
{FOOTER}
</body>
</html>'''

def hero_style(image):
    return f' style="background-image:url(\'images/{image}\')"'

OUT = "/home/claude/site"

# ---------- INDEX ----------
index_body = '''
<section class="hero" id="inicio" style="background-image:url('images/benefits.jpg')">
  <div class="hero-inner">
    <p class="eyebrow">Arkik Desarrollos · Ciudad Juárez</p>
    <h1>De la visión<br>a la <em>realidad</em>.</h1>
    <p class="tagline">Construimos contigo</p>
    <div>
      <a class="btn-primary" href="https://api.whatsapp.com/send?phone=526561095490" target="_blank" rel="noopener">Pide tu presupuesto</a>
      <a class="btn-outline" href="#contacto">Ver servicios</a>
    </div>
    <div class="hero-stats">
      <div><div class="num">4+</div><div class="label">Años de trayectoria</div></div>
      <div><div class="num">3</div><div class="label">Sectores atendidos</div></div>
      <div><div class="num">100%</div><div class="label">Presupuestos desglosados</div></div>
    </div>
  </div>
</section>

<section id="especialidades">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Nos especializamos en</p>
      <h2>Gestión y ejecución de proyectos de construcción</h2>
      <p>Con eficiencia, calidad y cumplimiento de normativas. Aquí hay algunos aspectos clave que diferencian a una construcción.</p>
    </div>
    <div class="specs-grid reveal-stagger">
      <div class="spec-card">
        <p class="tag">Tipo de proyectos</p>
        <ul><li>Residencial, comercial, industrial.</li><li>Remodelaciones, obra nueva o mantenimiento.</li></ul>
      </div>
      <div class="spec-card">
        <p class="tag">Experiencia</p>
        <div class="big">+4 años</div>
        <ul style="margin-top:10px;"><li>Trayectoria comprobable en Ciudad Juárez</li></ul>
      </div>
      <div class="spec-card">
        <p class="tag">Equipo profesional</p>
        <ul><li>Arquitecto y especialista en área</li><li>Profesionistas certificados</li><li>Presupuestos precisos y conceptos desglosados</li></ul>
      </div>
    </div>
  </div>
</section>

<section class="services-band" id="construccion">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Construcciones · Arkik Desarrollos</p>
      <h2>Del diseño a la supervisión de obra</h2>
      <p>Creando proyectos de alto impacto, sobresaliendo de la competencia y ofreciendo un servicio único, personalizado y siempre actualizando a nuestros clientes. Ofrecemos servicios integrales, desde el diseño hasta la supervisión de la construcción, con enfoque en innovación y sostenibilidad.</p>
    </div>
    <div class="services-list reveal-stagger">
      <div class="service-item"><p class="idx">01</p><h3>Planificación</h3><p>Planificación y gestión del proyecto.</p></div>
      <div class="service-item"><p class="idx">02</p><h3>Construcción</h3><p>Construcción y ejecución de obra.</p></div>
      <div class="service-item"><p class="idx">03</p><h3>Acabados</h3><p>Acabados y detalles finales.</p></div>
      <div class="service-item"><p class="idx">04</p><h3>Supervisión</h3><p>Supervisión y control de calidad.</p></div>
    </div>
  </div>
</section>

<section id="servicios">
  <div class="wrap benefits reveal">
    <img src="images/benefits.jpg" alt="Obra de construcción Arkik Desarrollos" loading="lazy">
    <div>
      <p class="eyebrow">Beneficios</p>
      <h2>¿Qué obra tienes en mente?</h2>
      <ul>
        <li>Reducción de costos y tiempos de ejecución</li>
        <li>Coordinación eficiente de materiales y recursos</li>
        <li>Cumplimiento de normativas de construcción</li>
        <li>Garantía y calidad en la obra</li>
      </ul>
      <p style="color:var(--muted);margin-bottom:24px;">Si necesitas un contratista de construcción para tu proyecto, te podemos ayudar con soluciones personalizadas.</p>
      <a class="btn-primary" href="#contacto">Cotizar mi proyecto</a>
    </div>
  </div>
</section>

<section class="sectors">
  <div class="wrap">
    <div class="section-head reveal"><p class="eyebrow">Sectores</p><h2>Proyectos en todos los frentes</h2></div>
    <div class="sector-grid reveal-stagger">
      <div class="sector-card card-carousel">
        <div class="carousel-track">
          <img src="images/sector-industrial.jpg" alt="Sector Industrial" loading="lazy">
          <img src="images/construccion-corporativa.jpg" alt="Proyecto industrial Arkik" loading="lazy">
        </div>
        <button class="carousel-arrow prev" aria-label="Anterior">‹</button>
        <button class="carousel-arrow next" aria-label="Siguiente">›</button>
        <div class="carousel-dots"></div>
        <div class="label">Sector Industrial</div>
      </div>
      <div class="sector-card card-carousel">
        <div class="carousel-track">
          <img src="images/sector-habitacional.jpg" alt="Sector Habitacional" loading="lazy">
          <img src="images/construccion-residencial.jpg" alt="Proyecto habitacional Arkik" loading="lazy">
        </div>
        <button class="carousel-arrow prev" aria-label="Anterior">‹</button>
        <button class="carousel-arrow next" aria-label="Siguiente">›</button>
        <div class="carousel-dots"></div>
        <div class="label">Sector Habitacional</div>
      </div>
      <div class="sector-card card-carousel">
        <div class="carousel-track">
          <img src="images/sector-comercial.jpg" alt="Sector Comercial" loading="lazy">
          <img src="images/construccion-comercial.jpg" alt="Proyecto comercial Arkik" loading="lazy">
        </div>
        <button class="carousel-arrow prev" aria-label="Anterior">‹</button>
        <button class="carousel-arrow next" aria-label="Siguiente">›</button>
        <div class="carousel-dots"></div>
        <div class="label">Sector Comercial</div>
      </div>
    </div>
  </div>
</section>

<section class="portfolio-cta reveal" id="remodelacion">
  <div class="wrap">
    <p class="eyebrow" style="justify-content:center;color:var(--amber);">Remodelaciones</p>
    <h2>Descarga nuestro portafolio completo</h2>
    <a class="btn-primary" href="https://www.grupoarkik.com/_files/ugd/6ab1eb_3b5ccdfc936b4402ac11c60393402bea.pdf" target="_blank" rel="noopener">Ver portafolio (PDF)</a>
  </div>
</section>

<section class="form-section" id="contacto">
  <div class="wrap form-layout reveal">
    <div>
      <p class="eyebrow">Cotización</p>
      <h2>Llena el formulario para recibir información</h2>
      <p style="color:var(--muted);margin-top:16px;">Regístrate y obtén tu cotización en tiempo récord.</p>
    </div>
    <form id="quoteForm">
      <div class="field"><label for="name">Nombre</label><input type="text" id="name" name="name" required></div>
      <div class="field"><label for="phone">Teléfono</label><input type="tel" id="phone" name="phone" required></div>
      <div class="field"><label for="email">Email</label><input type="email" id="email" name="email" required></div>
      <div class="field">
        <label for="service">Servicios de Arkik Desarrollos</label>
        <select id="service" name="service">
          <option value="">Elige servicio de interés</option>
          <option>Construcción</option><option>Remodelación</option><option>3D Studio</option><option>Inversión</option>
        </select>
      </div>
      <div class="checkbox-row"><input type="checkbox" id="terms" required><label for="terms">Acepto los términos y condiciones</label></div>
      <button type="submit" class="submit-btn">Cotizar mi proyecto</button>
      <p class="form-note" id="formNote">Gracias, un asesor te contactará en breve.</p>
    </form>
  </div>
</section>
'''
with open(f"{OUT}/index.html", "w") as f:
    f.write(page("Construcción y Remodelaciones | Arkik Desarrollos | Ciudad Juárez",
                 "Conoce los proyectos donde hemos colaborado. Construcción, remodelación y desarrollos en Ciudad Juárez. ARKIK DESARROLLOS.",
                 "index.html", index_body))

# ---------- CONSTRUCCION ----------
construccion_body = '''
<section class="page-hero" style="background-image:url('images/construccion-comercial.jpg')">
  <div class="wrap">
    <p class="eyebrow">Construcción</p>
    <h1>Nuestro trabajo</h1>
    <p class="tagline">Proyectos residenciales, comerciales, corporativos y recreativos, ejecutados con precisión de principio a fin.</p>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="content-grid reveal">
      <div><h3>Construcción Residencial</h3><p>Creamos viviendas que se adaptan a cada estilo de vida, desde casas familiares hasta residencias de alto lujo. Diseñamos y construimos pensando en funcionalidad, confort y estética, ofreciendo proyectos llave en mano.</p></div>
      <div class="img-col"><img src="images/construccion-residencial.jpg" alt="Construcción residencial" loading="lazy"></div>
    </div>
    <div class="content-grid reverse reveal">
      <div><h3>Construcción Comercial</h3><p>Desarrollamos locales, restaurantes y plazas comerciales con enfoque en la experiencia del cliente y la eficiencia operativa. Espacios modernos que impulsan la imagen y productividad de tu negocio.</p></div>
      <div class="img-col"><img src="images/construccion-comercial.jpg" alt="Construcción comercial" loading="lazy"></div>
    </div>
    <div class="content-grid reveal">
      <div><h3>Construcción Corporativa</h3><p>Diseñamos y construimos oficinas, coworkings y espacios empresariales pensados para maximizar la productividad y proyectar profesionalismo. Cada proyecto refleja la identidad y necesidades de cada empresa.</p></div>
      <div class="img-col"><img src="images/construccion-corporativa.jpg" alt="Construcción corporativa" loading="lazy"></div>
    </div>
    <div class="content-grid reverse reveal">
      <div><h3>Construcción Recreativa</h3><p>Creamos áreas sociales, gimnasios, canchas, terrazas y espacios recreativos que elevan el estilo de vida. Proyectos que combinan diseño, comodidad y funcionalidad en un mismo lugar.</p></div>
      <div class="img-col"><img src="images/construccion-recreativa.jpg" alt="Construcción recreativa" loading="lazy"></div>
    </div>
  </div>
</section>
<section class="portfolio-cta reveal">
  <div class="wrap"><h2>¿Tienes un proyecto de construcción en mente?</h2>
  <a class="btn-primary" href="https://api.whatsapp.com/send?phone=526561095490" target="_blank" rel="noopener">Pide tu presupuesto</a></div>
</section>
'''
with open(f"{OUT}/construccion.html", "w") as f:
    f.write(page("Construcción | Grupo Arkik", "Construcción residencial, comercial, corporativa y recreativa en Ciudad Juárez.", "construccion.html", construccion_body))

# ---------- REMODELACION ----------
remodelacion_body = '''
<section class="page-hero" style="background-image:url('images/remodelacion-fachadas.jpg')">
  <div class="wrap">
    <p class="eyebrow">Remodelación</p>
    <h1>Nuestro trabajo</h1>
    <p class="tagline">En Arkik transformamos tus espacios con proyectos de remodelación personalizados, cuidando cada detalle para que el resultado refleje tu estilo y necesidades.</p>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="content-grid reveal">
      <div><h3>Remodelación Residencial</h3><p>Renovamos y transformamos casas y departamentos completos, adaptándolos a nuevos estilos de vida, mejorando su funcionalidad y aumentando su valor.</p></div>
      <div class="img-col"><img src="images/remodelacion-residencial.jpg" alt="Remodelación residencial" loading="lazy"></div>
    </div>
    <div class="content-grid reverse reveal">
      <div><h3>Remodelación Comercial</h3><p>Rediseñamos locales, oficinas y restaurantes para proyectar una imagen moderna y funcional, que atraiga clientes y optimice la operación del negocio.</p></div>
      <div class="img-col"><img src="images/remodelacion-comercial.jpg" alt="Remodelación comercial" loading="lazy"></div>
    </div>
    <div class="content-grid reveal">
      <div><h3>Remodelación de Cocinas</h3><p>Creamos cocinas modernas, funcionales y estéticas. Desde la distribución y mobiliario hasta acabados e iluminación, diseñamos espacios listos para disfrutarse.</p></div>
      <div class="img-col"><img src="images/remodelacion-cocinas.jpg" alt="Remodelación de cocinas" loading="lazy"></div>
    </div>
    <div class="content-grid reverse reveal">
      <div><h3>Remodelación de Baños</h3><p>Transformamos baños en espacios cómodos, prácticos y elegantes. Optimizamos cada detalle: sanitarios, regaderas, acabados y almacenamiento.</p></div>
      <div class="img-col"><img src="images/remodelacion-banos.jpg" alt="Remodelación de baños" loading="lazy"></div>
    </div>
    <div class="content-grid reveal">
      <div><h3>Remodelación de Fachadas</h3><p>Renovamos la cara principal de tu casa o negocio con diseños modernos y materiales de alta calidad. Aumenta la plusvalía y mejora la primera impresión.</p></div>
      <div class="img-col"><img src="images/remodelacion-fachadas.jpg" alt="Remodelación de fachadas" loading="lazy"></div>
    </div>
    <div class="content-grid reverse reveal">
      <div><h3>Remodelación de Patios</h3><p>Rediseñamos áreas exteriores para crear espacios de convivencia y descanso. Jardines, terrazas, pérgolas y asadores que convierten tu patio en el corazón social de tu hogar.</p></div>
      <div class="img-col"><img src="images/remodelacion-patios.jpg" alt="Remodelación de patios" loading="lazy"></div>
    </div>
  </div>
</section>
<section class="portfolio-cta reveal">
  <div class="wrap"><h2>Descarga nuestro portafolio completo</h2>
  <a class="btn-primary" href="https://www.grupoarkik.com/_files/ugd/6ab1eb_3b5ccdfc936b4402ac11c60393402bea.pdf" target="_blank" rel="noopener">Ver portafolio (PDF)</a></div>
</section>
'''
with open(f"{OUT}/remodelacion.html", "w") as f:
    f.write(page("Remodelación | Grupo Arkik", "Remodelación residencial, comercial, cocinas, baños, fachadas y patios en Ciudad Juárez.", "remodelacion.html", remodelacion_body))

# ---------- SERVICIOS ----------
servicios_items = [
    ("Carpintería", "servicio-carpinteria.jpg", "Ofrecemos servicios de carpintería de alta calidad, diseñados para satisfacer tus necesidades. Nuestro equipo de expertos se especializa en la creación de muebles, reparaciones y remodelaciones, utilizando materiales duraderos y técnicas artesanales."),
    ("Herrería", "servicio-herreria.jpg", "Especializados en la creación y reparación de estructuras metálicas personalizadas. Combinamos técnica y creatividad para garantizar resultados duraderos y estéticamente atractivos: barandillas, rejas y muebles de hierro forjado."),
    ("Cancelería", "servicio-canceleria.jpg", "Soluciones personalizadas para tus proyectos de cancelería, con una amplia gama de productos de alta calidad diseñados para mejorar la funcionalidad de tus espacios."),
    ("Plomería", "servicio-plomeria.jpg", "Servicio especializado en la creación y mantenimiento de estructuras acuáticas como muros llorones, fuentes y espejos de agua, con soluciones personalizadas y funcionamiento eficiente."),
    ("Iluminación", "servicio-iluminacion.jpg", "Soluciones de iluminación innovadoras y personalizadas para cada espacio. Desde la selección de luminarias hasta la instalación, garantizamos un servicio profesional y de calidad."),
    ("Paisajismo y Jardinería", "servicio-jardineria.jpg", "Diseños de paisajismo y jardinería que transforman tu espacio exterior en un oasis de belleza natural, con plantas de alta calidad y técnicas sostenibles, desde la planificación hasta el mantenimiento."),
]
cards = ""
for name, img, desc in servicios_items:
    cards += f'<div class="card"><img src="images/{img}" alt="{name}" loading="lazy"><div class="card-body"><h3>{name}</h3><p>{desc}</p></div></div>\n'

servicios_body = f'''
<section class="page-hero" style="background-image:url('images/servicio-herreria.jpg')">
  <div class="wrap">
    <p class="eyebrow">Servicios profesionales</p>
    <h1>Soluciones integrales para cada espacio</h1>
    <p class="tagline">Además de la construcción y remodelación, contamos con expertos en carpintería, herrería, cancelería, electricidad y plomería, garantizando soluciones integrales y de calidad.</p>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="card-grid reveal-stagger">
      {cards}
    </div>
  </div>
</section>
<section class="portfolio-cta reveal">
  <div class="wrap"><h2>Confía en nosotros para transformar tus espacios</h2>
  <a class="btn-primary" href="https://api.whatsapp.com/send?phone=526561095490" target="_blank" rel="noopener">Pide tu presupuesto</a></div>
</section>
'''
with open(f"{OUT}/servicios.html", "w") as f:
    f.write(page("Servicios | Grupo Arkik", "Carpintería, herrería, cancelería, plomería, iluminación y jardinería en Ciudad Juárez.", "servicios.html", servicios_body))

# ---------- 3D STUDIO ----------
studio_body = '''
<section class="page-hero" style="background-image:url('images/3d-showcase.jpg')">
  <div class="wrap">
    <p class="eyebrow">Arkik 3D Studio</p>
    <h1>Transformamos ideas en realidad 3D</h1>
    <p class="tagline">Desarrollo integral de proyectos arquitectónicos con renders fotorrealistas, modelado 3D avanzado y recorridos virtuales inmersivos que impulsan la toma de decisiones.</p>
    <div style="margin-top:28px;"><a class="btn-primary" href="https://api.whatsapp.com/send?phone=526561095490" target="_blank" rel="noopener">Iniciar proyecto</a></div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="stats-row reveal-stagger">
      <div class="stat"><div class="num">+100</div><div class="label">Proyectos completados</div></div>
      <div class="stat"><div class="num">+80</div><div class="label">Clientes felices</div></div>
      <div class="stat"><div class="num">4K</div><div class="label">Calidad ultra HD</div></div>
    </div>
    <div class="section-head reveal">
      <p class="eyebrow">Nuestros servicios</p>
      <h2>Soluciones arquitectónicas integrales</h2>
      <p>Acompañamos cada etapa de tu proyecto con herramientas de visualización avanzada y documentación técnica profesional.</p>
    </div>
    <div class="services-list reveal-stagger" style="margin-bottom:56px;">
      <div class="service-item" style="border-color:var(--steel);"><h3>Diseño Arquitectónico</h3><p style="color:var(--muted);">Planos arquitectónicos y proyectos ejecutivos detallados que cumplen con normativas y optimizan funcionalidad.</p></div>
      <div class="service-item" style="border-color:var(--steel);"><h3>Renders Fotorrealistas</h3><p style="color:var(--muted);">Visualizaciones fotorrealistas en ultra definición que dan vida a tus conceptos antes de la construcción.</p></div>
      <div class="service-item" style="border-color:var(--steel);"><h3>Recorridos Virtuales</h3><p style="color:var(--muted);">Experiencias inmersivas e interactivas que permiten explorar espacios antes de su construcción.</p></div>
      <div class="service-item" style="border-color:var(--steel);"><h3>Modelado 3D</h3><p style="color:var(--muted);">Modelos tridimensionales precisos y detallados para análisis técnico y presentaciones profesionales.</p></div>
    </div>
    <img src="images/3d-showcase.jpg" alt="Visualización 3D Arkik Studio" loading="lazy" style="border-radius:2px;margin-bottom:56px;" class="reveal">
    <div class="section-head reveal">
      <p class="eyebrow">Proyectos destacados</p>
      <h2>Transformando espacios, creando experiencias</h2>
    </div>
    <div class="card-grid reveal-stagger">
      <div class="card"><img src="images/3d-plaza-caporal.jpg" alt="Plaza Caporal" loading="lazy"><div class="card-body"><h3>Plaza Caporal</h3><p>Diseño minimalista con vegetación. Un espacio único que fusiona modernidad y naturaleza.</p></div></div>
      <div class="card"><img src="images/3d-casa-pao.jpg" alt="Casa PAO" loading="lazy"><div class="card-body"><h3>Casa PAO</h3><p>Convierte tu patio en un espacio social perfecto, con asador para momentos inolvidables al aire libre.</p></div></div>
      <div class="card"><img src="images/3d-casa-nayarit-1.jpg" alt="Casa Nayarit" loading="lazy"><div class="card-body"><h3>Casa Nayarit</h3><p>Diseño arquitectónico que combina confort y estilo, con cada detalle pensado para un resultado moderno y acogedor.</p></div></div>
      <div class="card"><img src="images/3d-desert-house.jpg" alt="Desert House" loading="lazy"><div class="card-body"><h3>Desert House</h3><p>Arquitectura en el ecosistema desértico de Chihuahua, con materiales de alta calidad y espacios amplios y bien iluminados.</p></div></div>
    </div>
  </div>
</section>
<section class="portfolio-cta reveal">
  <div class="wrap"><h2>Cada proyecto es único, cada resultado es excepcional</h2>
  <a class="btn-primary" href="https://api.whatsapp.com/send?phone=526561095490" target="_blank" rel="noopener">Ver portafolio</a></div>
</section>
'''
with open(f"{OUT}/3d-studio.html", "w") as f:
    f.write(page("3D Studio | Grupo Arkik", "Renders fotorrealistas, modelado 3D y recorridos virtuales para proyectos arquitectónicos.", "3d-studio.html", studio_body))

# ---------- INVERSION ----------
inversion_body = '''
<section class="page-hero" style="background-image:url('images/construccion-corporativa.jpg')">
  <div class="wrap">
    <p class="eyebrow">Invierte en Grupo Arkik</p>
    <h1>Construimos proyectos, creamos valor, compartimos resultados</h1>
    <p class="tagline">Invierte en Arkik Desarrollos y forma parte de una empresa en crecimiento, con un modelo de negocio sólido, transparente y rentable.</p>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="list-block reveal">
      <h3>¿Por qué invertir en Arkik?</h3>
      <ul>
        <li>Ser parte de una empresa diversificada en construcción, remodelación, diseño y proyectos propios.</li>
        <li>Acceder a un modelo con márgenes de utilidad comprobados del 30%.</li>
        <li>Confiar en un equipo con visión y experiencia.</li>
        <li>Tener seguridad y transparencia en cada etapa de la inversión.</li>
      </ul>
    </div>
    <div class="list-block reveal">
      <h3>Nuestro plan de crecimiento</h3>
      <p class="lead">La inversión se destina a fortalecer áreas clave que impulsan la consolidación y expansión de la empresa:</p>
      <ul>
        <li>Marketing estratégico → posicionamiento y alcance de marca.</li>
        <li>Contratación de personal clave → equipo especializado para escalar operaciones.</li>
        <li>Apertura de oficinas → presencia en nuevas plazas y mejor atención a clientes.</li>
        <li>Flujo operativo → estabilidad y liquidez para proyectos en curso.</li>
        <li>Proyectos propios → desarrollos que fortalecen el valor y rentabilidad de la empresa.</li>
      </ul>
    </div>
    <div class="list-block reveal">
      <h3>Modelo de retorno</h3>
      <ul>
        <li>Retorno estimado: 10% anual durante 5 años.</li>
        <li>Alternativas: participación accionaria o retorno fijo ligado a utilidades.</li>
        <li>Respaldo con contratos legales y reportes periódicos.</li>
      </ul>
    </div>
    <div class="list-block reveal">
      <h3>Resultados y trayectoria</h3>
      <div class="stats-row reveal-stagger">
        <div class="stat"><div class="num">32</div><div class="label">Proyectos en 5 años</div></div>
        <div class="stat"><div class="num">22</div><div class="label">Proyectos solo en 2025</div></div>
        <div class="stat"><div class="num">20%</div><div class="label">Margen neto promedio</div></div>
      </div>
      <p class="lead">Ingresos anuales consolidados en un rango de $1 a $3 millones de pesos, con crecimiento constante año tras año. Proyecciones 2026: superar los 30 proyectos anuales y consolidar nuevas oficinas.</p>
    </div>
    <div class="list-block reveal">
      <h3>Beneficios para el inversionista</h3>
      <ul>
        <li>Inversión en una empresa diversificada y sólida.</li>
        <li>Seguridad legal con contratos claros.</li>
        <li>Transparencia: acceso a reportes y estados financieros.</li>
        <li>Participación en el crecimiento de Arkik a largo plazo.</li>
      </ul>
    </div>
  </div>
</section>
<section class="portfolio-cta reveal">
  <div class="wrap"><h2>Tu confianza es la base de nuestro crecimiento</h2>
  <a class="btn-primary" href="https://api.whatsapp.com/send?phone=526561095490" target="_blank" rel="noopener">Quiero más información</a></div>
</section>
'''
with open(f"{OUT}/inversion.html", "w") as f:
    f.write(page("Inversión | Grupo Arkik", "Invierte en Arkik Desarrollos: modelo de negocio sólido, transparente y rentable.", "inversion.html", inversion_body))

# ---------- LEGAL PAGES ----------
def legal_page(slug, title, eyebrow, intro, blocks, closing):
    b = ""
    for h, items in blocks:
        lis = "".join(f"<li>{i}</li>" for i in items)
        b += f'<div class="list-block reveal"><h3>{h}</h3><ul>{lis}</ul></div>\n'
    body = f'''
<section class="page-hero" style="background-image:url('images/benefits.jpg')">
  <div class="wrap">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{title}</h1>
    <p class="tagline">{intro}</p>
  </div>
</section>
<section class="legal-page">
  <div class="wrap">
    {b}
  </div>
</section>
<section class="portfolio-cta reveal">
  <div class="wrap"><h2>Vamos a trabajar juntos</h2><p style="max-width:640px;margin:0 auto 24px;color:#D9DCE0;">{closing}</p>
  <a class="btn-primary" href="https://api.whatsapp.com/send?phone=526561095490" target="_blank" rel="noopener">Contáctanos</a></div>
</section>
'''
    with open(f"{OUT}/{slug}.html", "w") as f:
        f.write(page(f"{title} | Grupo Arkik", f"{title} de Arkik Desarrollos.", f"{slug}.html", body))

legal_page(
    "legal", "Legal", "Legal",
    "En Grupo Arkik operamos con estricto apego a la legislación mexicana y a las normativas locales de construcción. Cada proyecto está respaldado por contratos formales, permisos y documentos oficiales.",
    [
        ("Cumplimiento normativo", [
            "Nuestras obras se realizan conforme a la Ley de Obra Pública y a los reglamentos municipales de construcción.",
            "Respetamos las disposiciones en materia de Protección Civil, seguridad en obra y normatividad técnica aplicable.",
            "Tramitamos licencias, permisos y autorizaciones necesarios para la ejecución de cada proyecto (Anexos 6 y 7).",
        ]),
        ("Contratos y documentación", [
            "Todos los proyectos se formalizan mediante un Contrato de Obra a Precio Alzado o documentos equivalentes, que definen alcances, tiempos y costos (Cláusula Primera y Anexos 1–4).",
            "Cada contrato incluye anexos como programas de obra, presupuestos, planos aprobados, formatos de aditivas y actas de recepción.",
            "La documentación contractual tiene validez jurídica y protege a ambas partes contra incumplimientos.",
        ]),
        ("Relación laboral y responsabilidades", [
            "No existe relación laboral entre el cliente y Arkik; cada parte mantiene independencia legal (Cláusula XIV).",
            "Los trabajadores y subcontratistas que participan en la obra responden únicamente ante Arkik.",
            "Se utilizan cartas de deslinde y contratos de prestación de servicios para dejar constancia de estas condiciones (Anexos 9 y 14).",
        ]),
        ("Confidencialidad y comunicación", [
            "Toda información técnica, económica o personal se maneja bajo estricta confidencialidad (Cláusula XV).",
            "Las instrucciones y cambios deben comunicarse únicamente a través de los canales autorizados por contrato (Cláusula XVI y XXVIII).",
            "Cualquier acuerdo informal carece de validez jurídica.",
        ]),
        ("Seguros y responsabilidad civil", [
            "Según la naturaleza de la obra, puede contratarse una póliza de seguro de responsabilidad civil o daños a terceros (Cláusula XXX, Anexo 20).",
            "En caso de incumplimiento contractual, se contemplan pagos por daños y perjuicios conforme a la legislación mexicana (Cláusula XX).",
        ]),
        ("Jurisdicción y resolución de conflictos", [
            "Cualquier controversia se resolverá primero de forma amistosa entre las partes.",
            "Si no hay acuerdo, será atendida por los tribunales competentes de Ciudad Juárez, Chihuahua, México (Cláusula XIX).",
            "El contrato se rige en todo momento por la legislación mexicana vigente.",
        ]),
    ],
    "Con Arkik, cada proyecto está respaldado legalmente. Nuestros procesos garantizan que tu inversión y tu obra cuenten con un marco jurídico sólido, con transparencia, formalidad y apego total a la ley."
)

legal_page(
    "garantias", "Garantías", "Garantías",
    "Respaldamos la calidad de nuestro trabajo con garantías claras y específicas para cada etapa y especialidad de la obra. Con Arkik, tu inversión y tu proyecto están protegidos incluso después de la entrega.",
    [
        ("Cobertura general", [
            "Hasta 2 años desde la entrega de la obra (Cláusula Vigésima Tercera y Anexo 12).",
            "Aplica siempre que no haya reparaciones de terceros o incumplimiento de pagos.",
        ]),
        ("Tiempos de garantía por especialidad", [
            "Terracerías: 6 meses.",
            "Cimentación: 12 meses.",
            "Estructura: 12 meses.",
            "Mampostería: 12 meses.",
            "Instalaciones (eléctrica, hidráulica, sanitaria, gas): 3 meses.",
            "Acabados: 6 meses.",
            "Aislamientos e impermeabilización: 12 meses.",
            "Carpintería y herrería: 6 meses.",
            "Cancelería: 3 meses.",
            "Jardinería: 1 mes.",
            "Equipos y mobiliario: 2 meses.",
            "Sistemas especiales: 6 meses.",
        ]),
        ("Procedimiento", [
            "Solicitud escrita del cliente.",
            "Verificación técnica.",
            "Reparación o reposición según contrato.",
        ]),
    ],
    "Tu tranquilidad es parte de nuestro compromiso. En Arkik no solo entregamos obras, entregamos confianza, con atención postventa que nos distingue en el mercado."
)

legal_page(
    "politicas-privacidad", "Políticas y Privacidad", "Políticas y privacidad",
    "En Grupo Arkik nos regimos por principios de transparencia, responsabilidad y confidencialidad en el manejo de la información compartida durante cada proyecto.",
    [
        ("Nuestras políticas", [
            "Comunicación formal: toda instrucción, cambio o solicitud debe hacerse a través de los canales oficiales establecidos en contrato, evitando acuerdos informales (Cláusulas XIII, XVI y XXVIII).",
            "Pagos y formas de pago: se establecen métodos aceptados y condiciones claras (Cláusulas VI, VII y VIII).",
            "Acceso y seguridad en obra: el manejo de llaves y accesos se realiza con control y responsabilidad (Cláusula V).",
            "Confidencialidad: toda la información compartida es tratada con estricta reserva (Cláusula XV).",
            "Protección de datos: cumplimos con lineamientos de privacidad y resguardo seguro de la información del cliente y del proyecto.",
        ]),
        ("Privacidad de la información", [
            "Solo se usa para la gestión del proyecto, contratos y trámites.",
            "Nunca se comparte con terceros sin autorización expresa.",
            "El cliente puede solicitar la actualización o eliminación de sus datos en cualquier momento.",
        ]),
        ("Protección de datos", [
            "Acceso restringido solo al personal autorizado.",
            "Uso exclusivo para los fines establecidos en contrato.",
            "Resguardo seguro de documentos físicos y digitales.",
        ]),
        ("Derechos del cliente", [
            "Actualizar o rectificar datos.",
            "Solicitar confidencialidad estricta.",
            "Revocar autorización de uso de información no esencial.",
        ]),
    ],
    "En Arkik trabajamos con reglas claras y cuidamos la información de nuestros clientes con el mismo compromiso con el que construimos sus proyectos."
)

legal_page(
    "terminos-condiciones", "Términos y Condiciones", "Términos y condiciones",
    "En Grupo Arkik trabajamos bajo términos y condiciones claros que buscan asegurar una relación justa, profesional y transparente con nuestros clientes.",
    [
        ("Objeto y alcance del contrato", [
            "Cada obra se detalla en la Cláusula Primera (Objeto del contrato) e incluye planos, presupuestos, cronogramas y anexos técnicos.",
            "El alcance abarca desde estudios preliminares hasta la entrega final, según lo estipulado en el contrato y anexos.",
        ]),
        ("Obligaciones de las partes", [
            "Contratista (Arkik): ejecutar la obra conforme a los planos, calendario y normatividad aplicable; informar avances y garantizar la calidad del trabajo (Cláusula XI).",
            "Contratante (cliente): realizar pagos en tiempo, proporcionar información, colaborar en accesos y autorizaciones, y recibir la obra concluida (Cláusula XII).",
        ]),
        ("Pagos y métodos de pago", [
            "La contraprestación total se fija en contrato (Cláusulas VI y VII).",
            "Métodos aceptados: efectivo, transferencia, depósito, cheque o tarjeta (Cláusula VIII).",
            "Se aplican condiciones específicas como recargos por tarjeta o responsabilidad en caso de cheques sin fondos.",
        ]),
        ("Modificaciones y trabajos adicionales", [
            "Cualquier cambio, ajuste o trabajo extra debe documentarse mediante una Aditiva (Cláusula XVII y Anexo 11).",
            "Ninguna instrucción informal será válida sin este procedimiento.",
        ]),
        ("Retrasos y penalizaciones", [
            "Por parte de Arkik: descuento del 5% de honorarios por semana de retraso (Cláusula XVIII).",
            "Por parte del cliente: pago de costos por días perdidos de personal y contratista (Cláusula XVIII).",
            "Por fuerza mayor: se consideran causas justificadas (clima, proveedores, accidentes, etc.).",
        ]),
        ("Recepción de la obra", [
            "El cliente cuenta con 15 días para revisar la obra y emitir observaciones (Cláusula XXII).",
            "En caso de aceptación tácita (sin observaciones), se considera entregada y recibida.",
            "La aceptación no exime responsabilidades por vicios ocultos, los cuales están cubiertos por garantía.",
        ]),
        ("Comunicación formal", [
            "Todas las notificaciones se realizan por escrito en los domicilios o correos señalados (Cláusula XIII).",
            "No se reconocen acuerdos verbales ni negociaciones directas con trabajadores de obra (Cláusula XXVIII).",
        ]),
    ],
    "En Arkik creemos que los acuerdos claros son la base de cada proyecto. Nuestros términos y condiciones están diseñados para dar certeza, confianza y seguridad."
)

print("Todas las páginas generadas.")

