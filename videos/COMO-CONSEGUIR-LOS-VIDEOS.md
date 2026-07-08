# Cómo conseguir los videos reales de tu sitio actual (Wix)

A diferencia de las imágenes, **no pude sacar automáticamente las URLs de los videos** que usa tu sitio en Wix: los videos de fondo se cargan con JavaScript y mi herramienta de lectura solo ve el texto e imágenes del HTML, no esa parte. Ahora mismo `/videos` tiene 2 videos de relleno (un zoom lento sobre una foto) para que el sitio no se vea roto mientras tanto.

## Cómo descargar el video real desde tu celular o computadora (5 minutos)

1. Abre **www.grupoarkik.com** en **Chrome** (computadora, no celular — es más fácil con las herramientas de desarrollador).
2. Presiona `F12` (o clic derecho → "Inspeccionar") para abrir las Herramientas de Desarrollador.
3. Ve a la pestaña **Network** (Red).
4. En el cuadro de filtro, escribe `mp4`.
5. Recarga la página (`F5`) con esa pestaña abierta.
6. Verás aparecer uno o dos archivos `.mp4` en la lista (uno para el video del encabezado, otro para el de "Contáctanos" si lo tiene).
7. Haz clic derecho sobre cada uno → **Open in new tab** (Abrir en pestaña nueva), y ahí guarda el video con clic derecho → **Guardar video como...**
8. Renombra los archivos:
   - El video del encabezado (la casa de noche) → `hero.mp4`
   - El video de la sección de contacto (cocina/mesa) → `contacto.mp4`
9. Reemplázalos dentro de la carpeta `/videos` de tu proyecto, antes de subir a GitHub.

## Alternativa más simple (si lo anterior se complica)

Si no encuentras el archivo `.mp4` con ese método (a veces Wix lo sirve en pedazos/streaming y es más difícil de capturar así), puedes:
- Grabar la pantalla mientras el video se reproduce en el sitio (con el celular o con una app como OBS/QuickTime), recortar el clip, y guardarlo como `hero.mp4` / `contacto.mp4`.
- O usarlo tal cual — los videos de relleno con efecto de zoom ya se ven decentes y profesionales, así que no es obligatorio reemplazarlos de inmediato.

## Detalles técnicos para que se vean bien

- Formato: `.mp4` (códec H.264), sin audio (el navegador bloquea el autoplay de videos con sonido de todos modos).
- Duración recomendada: 5–15 segundos en loop.
- Peso recomendado: menos de 5 MB cada uno, para que cargue rápido en celular. Si el archivo pesa mucho, puedes comprimirlo gratis en https://www.freeconvert.com/video-compressor antes de subirlo.
