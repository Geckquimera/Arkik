# Grupo Arkik — sitio web (independiente de Wix)

Réplica completa de las 9 páginas de grupoarkik.com como HTML/CSS estático, sin ninguna dependencia de Wix una vez que sigas el paso 1 de abajo.

## Estructura

```
index.html                    → Inicio
3d-studio.html                → 3D Studio
construccion.html             → Construcción
remodelacion.html             → Remodelación
servicios.html                → Servicios
inversion.html                → Inversión
legal.html                    → Legal
garantias.html                → Garantías
politicas-privacidad.html     → Políticas y privacidad
terminos-condiciones.html     → Términos y condiciones
css/style.css                 → todos los estilos
js/main.js                    → animaciones (scroll-reveal, carrusel) y menú móvil
images/                       → todas las imágenes (por ahora son PLACEHOLDERS, ver paso 1)
videos/                       → videos de fondo (por ahora son PLACEHOLDERS, ver sección Modernización)
scripts/download-images.py    → descarga las imágenes REALES desde Wix a /images
```

## Paso 1 (importante) — Descargar las imágenes reales

Ahora mismo `/images` tiene imágenes de relleno (rectángulos beige) para que el sitio no se vea roto. Para poner las fotos reales de tu sitio actual:

1. Instala Python 3 si no lo tienes (la mayoría de Mac/Linux ya lo traen; en Windows descárgalo de python.org).
2. Abre una terminal en la carpeta del proyecto.
3. Corre:
   ```
   python3 scripts/download-images.py
   ```
4. Esto descarga ~29 imágenes reales desde los servidores de Wix y las guarda en `/images` con los nombres correctos, sobrescribiendo los placeholders.
5. Solo necesitas hacer esto una vez, antes de subir el proyecto a GitHub.

Después de este paso, el sitio ya no hace **ninguna** llamada a wixstatic.com ni a ningún servicio de Wix: todo (imágenes, estilos, tipografías del sistema) queda en tu propio repositorio, excepto las fuentes de Google Fonts, que se cargan desde Google (si también quieres eliminar esa dependencia, dímelo y te preparo las fuentes para autohospedar).

## Paso 2 — Subir a GitHub

1. Crea un repositorio nuevo (por ejemplo `grupoarkik-web`).
2. Sube TODA la carpeta del proyecto (los `.html`, `css/`, `images/` ya con las fotos reales).
3. **Settings → Pages → Branch: main → carpeta `/root`** → Save.
4. Tu sitio estará en `https://tu-usuario.github.io/grupoarkik-web/`.
5. Si tienes el dominio `grupoarkik.com`: **Settings → Pages → Custom domain** → `www.grupoarkik.com`, y en tu proveedor de DNS agrega un registro CNAME apuntando a `tu-usuario.github.io`.

## Modernización (nuevo)

Se rediseñó el sitio para que sea más minimalista, tomando como referencia el estilo de tu sitio actual en Wix:

1. **Video de fondo en el encabezado**: "Inicio" ahora tiene un `<video>` de fondo (en loop, sin sonido) en vez de una imagen fija, con el texto "De la visión a la realidad / Construimos Contigo" simplificado a un solo botón — igual que tu sitio original.
2. **Video de fondo en "Contáctanos"**: esta sección (que ahora aparece en las 9 páginas, justo arriba del pie de página) también tiene video de fondo, con ubicación, correo y teléfono superpuestos.
3. **Portafolio en abanico**: la sección "Remodelaciones" del Inicio ahora es un collage de fotos que rota sola cada pocos segundos (una grande al centro, más pequeñas a los lados), con el botón punteado "Portafolio" debajo.

**Importante — sobre los videos**: no pude sacar automáticamente los videos reales de tu sitio en Wix (se cargan con JavaScript, distinto a las imágenes). Por eso `/videos` trae 2 videos de relleno (efecto de zoom lento sobre una foto) para que nada se vea roto mientras tanto. Lee `videos/COMO-CONSEGUIR-LOS-VIDEOS.md` — ahí te explico paso a paso cómo bajar los videos reales de tu sitio actual en unos 5 minutos.

## Notas

- **Formulario de cotización**: ahora, al enviarlo, abre la app de correo del visitante (Gmail, Outlook, Mail...) con un mensaje ya redactado y dirigido a `arkik.desarrollos@gmail.com` — el visitante solo tiene que confirmar el envío. Es la opción sin costo y sin backend; su única limitación es que depende de que el visitante tenga una app de correo configurada en su dispositivo (en celular casi siempre la tiene). Si más adelante quieres un formulario "de verdad" que envíe directo sin abrir el correo, se puede conectar gratis con [Formspree](https://formspree.io) o [Web3Forms](https://web3forms.com) — avísame y te lo dejo listo.
- **Páginas "servicios", "garantías", "construcción", etc. en el sitio original**: algunas tenían texto de plantilla sin terminar en Wix (p. ej. la sección "Nombre del servicio" en Garantías); aquí las dejé con el contenido real que sí estaba publicado.
- El correo de contacto que aparece en pantalla es `grupo.arkik@gmail.com`, pero el enlace real en el sitio original apunta a `arkik.desarrollos@gmail.com`; usé este último como destino real del enlace — avísame si prefieres que use el otro.
- El botón de WhatsApp flotante y el CTA del menú están conectados a tu número: `+52 656 109 5490`.
