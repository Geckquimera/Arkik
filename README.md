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

Se agregaron 3 efectos que pediste probar (los mismos que viste en el ejemplo de RAIZ), adaptados a los colores de Arkik:

1. **Fondo fijo tipo parallax**: "Inicio" y todas las páginas interiores tienen ahora una foto real de fondo detrás del título, que se queda fija mientras el contenido se desliza encima. En iPhone/Safari este efecto puede no verse igual de fluido por una limitación conocida de ese navegador; en Chrome (Android y escritorio) se ve completo. Si el usuario tiene activada la preferencia "reducir movimiento" del sistema, el sitio lo respeta y desactiva el efecto automáticamente.
2. **Aparición con scroll**: los bloques de texto, tarjetas y secciones aparecen con un fundido y un pequeño desplazamiento hacia arriba conforme entran en pantalla.
3. **Carrusel de imágenes por tarjeta**: la sección "Sectores" en Inicio ahora tiene 2 fotos por tarjeta que rotan automáticamente, con flechas y puntos indicadores, en vez de una sola imagen estática.

Todo esto vive en dos archivos nuevos: `css/style.css` (estilos) y `js/main.js` (comportamiento), sin ninguna librería externa — es JavaScript puro, así que no afecta la velocidad de carga.

## Notas

- **Formulario de cotización**: por ahora no envía datos (GitHub Pages es solo archivos estáticos). Conéctalo gratis con [Formspree](https://formspree.io) o [Web3Forms](https://web3forms.com) cambiando el `action` del `<form>` en `index.html`.
- **Páginas "servicios", "garantías", "construcción", etc. en el sitio original**: algunas tenían texto de plantilla sin terminar en Wix (p. ej. la sección "Nombre del servicio" en Garantías); aquí las dejé con el contenido real que sí estaba publicado.
- El correo de contacto que aparece en pantalla es `grupo.arkik@gmail.com`, pero el enlace real en el sitio original apunta a `arkik.desarrollos@gmail.com`; usé este último como destino real del enlace — avísame si prefieres que use el otro.
- El botón de WhatsApp flotante y el CTA del menú están conectados a tu número: `+52 656 109 5490`.
