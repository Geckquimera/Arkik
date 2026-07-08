#!/usr/bin/env python3
"""
Descarga todas las imágenes reales del sitio (actualmente en los servidores de Wix)
y las guarda en la carpeta /images del proyecto, con los nombres que ya usa el HTML.

Cómo usarlo:
  1. Instala Python 3 si no lo tienes.
  2. Abre una terminal en la carpeta del proyecto (donde está este script, dentro de /scripts).
  3. Corre:  python3 scripts/download-images.py
  4. Cuando termine, sube la carpeta /images completa a tu repositorio de GitHub junto
     con los archivos .html y .css. A partir de ahí el sitio ya NO depende de Wix.

No necesitas correr esto más de una vez.
"""
import os
import urllib.request

IMAGES = {
    # --- comunes a todas las páginas ---
    "logo.png": "https://static.wixstatic.com/media/6ab1eb_b78bdc46f5aa401d97af2fe5b22af91d~mv2.png",
    "footer-logo.jpg": "https://static.wixstatic.com/media/11062b_8f14374b6fe149aab751d12c94c2676ff000.jpg",
    "icon-facebook.png": "https://static.wixstatic.com/media/11062b_2381e8a6e7444f4f902e7b649aa3f0ac~mv2.png",
    "icon-instagram.png": "https://static.wixstatic.com/media/11062b_55e4be1e75564866b6c28290f9a9d271~mv2.png",
    "icon-tiktok.png": "https://static.wixstatic.com/media/11062b_69d309d6dbde492fae325fb0deca6556~mv2.png",
    "icon-whatsapp.png": "https://static.wixstatic.com/media/11062b_1db239e728f641c3a3be5b7ca708f239~mv2.png",

    # --- inicio ---
    "benefits.jpg": "https://static.wixstatic.com/media/6ab1eb_b1ea194286db4d5b937fae99cc98bcb7f000.jpg",
    "sector-industrial.jpg": "https://static.wixstatic.com/media/6ab1eb_f5d4146fad384432bed12614748d4a1a~mv2.jpeg",
    "sector-habitacional.jpg": "https://static.wixstatic.com/media/6ab1eb_d592d1f8c5c64fbaadce5b1ae84f42a2~mv2.jpeg",
    "sector-comercial.jpg": "https://static.wixstatic.com/media/6ab1eb_2f688ae33a0d4c6d92b8f1f235dff326~mv2.jpg",

    # --- construccion ---
    "construccion-residencial.jpg": "https://static.wixstatic.com/media/6ab1eb_da3a6880202247c8ada4953432d20eb9~mv2.jpg",
    "construccion-comercial.jpg": "https://static.wixstatic.com/media/6ab1eb_f92fab8e8c61407a8d2d76cd6ce9ed2d~mv2.jpg",
    "construccion-corporativa.jpg": "https://static.wixstatic.com/media/6ab1eb_8b0f4a1880b74b31b4c840b453ec4c47~mv2.jpg",
    "construccion-recreativa.jpg": "https://static.wixstatic.com/media/6ab1eb_d74a77c11507468ebf2d22ebba8bd4b8~mv2.jpg",

    # --- remodelacion ---
    "remodelacion-residencial.jpg": "https://static.wixstatic.com/media/6ab1eb_c4c5c4a8375d43dea87c1d4b35ac6d87~mv2.jpg",
    "remodelacion-comercial.jpg": "https://static.wixstatic.com/media/nsplsh_d7580debafcd4fa48ce9c480b77a7064~mv2.jpg",
    "remodelacion-cocinas.jpg": "https://static.wixstatic.com/media/6ab1eb_ade2eadd8a1f4ee8b39436d5a9213c6b~mv2.jpg",
    "remodelacion-banos.jpg": "https://static.wixstatic.com/media/6ab1eb_dc274f493e014988a298fd95a471b870~mv2.webp",
    "remodelacion-fachadas.jpg": "https://static.wixstatic.com/media/6ab1eb_fb949e382a7942aebe3a9febe30dd230~mv2.jpg",
    "remodelacion-patios.jpg": "https://static.wixstatic.com/media/6ab1eb_955e3c4e4f764d0a84ed1d933fde0b56~mv2.jpg",

    # --- servicios ---
    "servicio-carpinteria.jpg": "https://static.wixstatic.com/media/6ab1eb_86db7a9392d0453fa51b0ec81c3ec1cc~mv2.jpg",
    "servicio-herreria.jpg": "https://static.wixstatic.com/media/6ab1eb_46d995fc1e294828899d63fad22780f2~mv2.jpg",
    "servicio-canceleria.jpg": "https://static.wixstatic.com/media/6ab1eb_eabadd08375d405c8033cf5c3cd2e4bf~mv2.jpg",
    "servicio-plomeria.jpg": "https://static.wixstatic.com/media/6ab1eb_8d1c710c26c14a088c30d27b2a137e33~mv2.jpg",
    "servicio-iluminacion.jpg": "https://static.wixstatic.com/media/6ab1eb_1b9d14e8bf9340a9abe21a2278f98a08~mv2.jpg",
    "servicio-jardineria.jpg": "https://static.wixstatic.com/media/6ab1eb_86f075f5d0aa4c83a5012ece3cdc29bd~mv2.jpg",

    # --- 3d studio ---
    "3d-showcase.jpg": "https://static.wixstatic.com/media/6ab1eb_cec8fd987a5f4cc3a2e622804186173d~mv2.jpg",
    "3d-plaza-caporal.jpg": "https://static.wixstatic.com/media/6ab1eb_f6effd05ae7a4497ab8ecc47e268d7b1~mv2.jpg",
    "3d-casa-pao.jpg": "https://static.wixstatic.com/media/6ab1eb_f3920b4eaab24dcf9960c9068f3d45fb~mv2.jpg",
    "3d-casa-nayarit-1.jpg": "https://static.wixstatic.com/media/6ab1eb_e78504c6a321441881bcf02fb5feac07~mv2.jpg",
    "3d-desert-house.jpg": "https://static.wixstatic.com/media/6ab1eb_e759314384114487869ace9c44681f9d~mv2.jpg",
}

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    out_dir = os.path.join(project_root, "images")
    os.makedirs(out_dir, exist_ok=True)

    headers = {"User-Agent": "Mozilla/5.0 (compatible; ArkikSiteMigration/1.0)"}
    ok, fail = 0, 0
    for filename, url in IMAGES.items():
        dest = os.path.join(out_dir, filename)
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=20) as resp, open(dest, "wb") as out:
                out.write(resp.read())
            print(f"OK   {filename}")
            ok += 1
        except Exception as e:
            print(f"FAIL {filename}  ({e})")
            fail += 1

    print(f"\nListo: {ok} descargadas, {fail} con error.")
    if fail:
        print("Si alguna falló, ábrela manualmente en el navegador desde la URL en este script y guárdala en /images con el mismo nombre.")

if __name__ == "__main__":
    main()
