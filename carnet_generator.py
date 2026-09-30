"""
utils/carnet_generator.py
-------------------------
Módulo para diseñar y generar el Carnet Escolar.
Esta funcionalidad no existía en Java y se hace con la librería Pillow (PIL).

¿Cómo pensar este archivo?
  1. Dimensiones estándar: Un carnet tipo tarjeta mide aprox. 85.6mm x 54mm.
     En píxeles a 150 DPI son aprox. 504px de ancho por 318px de alto.
  2. Canvas de imagen:
     img = Image.new("RGB", (ANCHO, ALTO), color_fondo)
     draw = ImageDraw.Draw(img)
  3. Elementos a dibujar:
     - Franja superior (Header con fondo azul oscuro y textos en blanco/amarillo).
     - Rectángulo para la foto o pegar la imagen si estudiante.foto_path existe.
     - Textos con los datos: Nombres, Cédula, Grado, Sección.
     - Franja inferior (Footer con teléfono y director).
     - Guardar la imagen generada: img.save(output_path, "PNG")
"""

import os
from pathlib import Path
from typing import Optional
from PIL import Image, ImageDraw, ImageFont

from models.configuracion import Configuracion
from models.estudiante import Estudiante

# Dimensiones estándar en px (150 DPI)
ANCHO = 504
ALTO  = 318

AZUL_OSCURO = (21, 101, 192)
AZUL_CLARO  = (227, 242, 253)
BLANCO      = (255, 255, 255)
GRIS_TEXTO  = (55, 71, 79)
AMARILLO    = (255, 193, 7)

OUTPUT_DIR = Path(__file__).parent.parent / "assets" / "carnets"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def _obtener_fuente(tamanio: int, negrita: bool = False) -> ImageFont.ImageFont:
    """
    Función auxiliar para cargar fuentes TrueType del sistema si existen,
    o usar ImageFont.load_default() como fallback.
    """
    fuentes_negrita = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
    ]
    fuentes_normal = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "C:/Windows/Fonts/arial.ttf",
    ]
    candidatas = fuentes_negrita if negrita else fuentes_normal
    for path in candidatas:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, tamanio)
            except Exception:
                pass
    return ImageFont.load_default()


def generar_carnet(estudiante: Estudiante, config: Configuracion, output_path: Optional[str] = None) -> str:
    """
    Genera el archivo de imagen PNG con el diseño del carnet escolar.

    TODO Pasante:
      1. Define la ruta final si output_path es None (ej: OUTPUT_DIR / f"{estudiante.cedula}_carnet.png").
      2. Crea una nueva imagen con Image.new("RGB", (ANCHO, ALTO), AZUL_CLARO).
      3. Usa ImageDraw.Draw(img) para:
         - Dibujar el rectángulo del encabezado.
         - Escribir config.nombre_institucion, periodo y el título 'CARNET ESTUDIANTIL'.
         - Si estudiante.foto_path existe y el archivo existe, abre la foto con Image.open(),
           redimensiónala (ej: 106x126) y pégala con img.paste().
           Si no hay foto, dibuja un recuadro o silueta sustituta.
         - Escribir los datos: estudiante.nombre_completo, estudiante.cedula, grado y sección.
         - Dibujar el rectángulo del pie de página con director y teléfono.
      4. Guarda la imagen: img.save(output_path, "PNG")
      5. Retorna la ruta del archivo generado.
    """
    pass


def exportar_pdf(imagen_path: str, pdf_path: Optional[str] = None) -> str:
    """
    Opcional: Convierte el PNG generado en un documento PDF usando reportlab.

    Pista:
      from reportlab.lib.pagesizes import A4
      from reportlab.lib.units import mm
      from reportlab.pdfgen import canvas

      c = canvas.Canvas(pdf_path, pagesize=A4)
      # 85.6 * mm de ancho, 54.0 * mm de alto
      c.drawImage(imagen_path, x, y, width=85.6*mm, height=54.0*mm)
      c.save()
    """
    pass
