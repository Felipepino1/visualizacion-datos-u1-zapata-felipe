# -*- coding: utf-8 -*-
"""Genera Informe/Informe_U1_Zapata_Felipe.pdf a partir del Markdown.
Si existen Evidencias/viz1.png, viz2.png y viz3.png, las inserta como figuras.
Uso: python Recursos/render_informe.py  (requiere: pip install markdown playwright)
"""
import base64, os, re, markdown
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD = os.path.join(ROOT, "Informe", "Informe_U1_Zapata_Felipe.md")
PDF = os.path.join(ROOT, "Informe", "Informe_U1_Zapata_Felipe.pdf")
FIG = {
    1: ("Gráfico 1 del Boletín ENE N.º 331 (INE, 2026): evolución de la tasa de desocupación según sexo.",
        "https://www.ine.gob.cl/docs/default-source/ocupacion-y-desocupacion/boletines/2026/nacional/ene-nacional-331.pdf"),
    2: ("CO₂ emissions per capita (Our World in Data, 2025).",
        "https://ourworldindata.org/grapher/co-emissions-per-capita"),
    3: ("Gráfico II.9 «Proyección de inflación», IPoM septiembre 2026 (Banco Central de Chile).",
        "https://www.bcentral.cl/web/banco-central/areas/politica-monetaria/informe-de-politica-monetaria"),
}

def figura(m):
    n = int(m.group(1)); cap, url = FIG[n]
    p = os.path.join(ROOT, "Evidencias", f"viz{n}.png")
    if os.path.exists(p):
        b64 = base64.b64encode(open(p, "rb").read()).decode()
        img = f'<img src="data:image/png;base64,{b64}">'
    else:
        img = f'<div class="ph">Insertar captura: Evidencias/viz{n}.png<br><small>{url}</small></div>'
    return f'<figure>{img}<figcaption><b>Figura {n}.</b> {cap} Fuente: {url}</figcaption></figure>'

src = open(MD, encoding="utf-8").read()
src = re.sub(r"\{\{FIGURA:(\d)\}\}", figura, src)
src = re.sub(r"(?<!\])\[([A-ZÁÉÍÓÚÑa-záéíóúñ][^\]\[]{2,40})\](?!\()", r'<span class="nota">\1</span>', src)
body = markdown.markdown(src, extensions=["tables"])

PORTADA = """
<section class="portada">
  <div class="inst">INACAP · Ingeniería en Informática</div>
  <h1 class="t">Construcción de una Base de Conocimiento y Análisis Crítico de la Visualización de Datos</h1>
  <div class="sub">Evaluación Sumativa Unidad 1 · Visualización de Datos<br>Informe: Partes II, III y IV</div>
  <table class="meta">
    <tr><td>Estudiante</td><td>Felipe Zapata Lagos</td></tr>
    <tr><td>Asignatura</td><td>Visualización de Datos</td></tr>
    <tr><td>Carrera</td><td>Ingeniería en Informática</td></tr>
    <tr><td>Docente</td><td>Javier Ignacio Miles Avello</td></tr>
    <tr><td>Fecha</td><td>5 de octubre de 2026</td></tr>
    <tr><td>Repositorio</td><td>github.com/Felipepino1/visualizacion-datos-u1-zapata-felipe</td></tr>
  </table>
</section>"""

CSS = """
@page { size: Letter; margin: 2.2cm 2.2cm 2.4cm; }
body { font-family: 'DejaVu Sans', Arial, sans-serif; font-size: 10.5pt; line-height: 1.5; color: #1d1d1f; }
h1 { font-size: 19pt; color: #b42318; border-bottom: 2px solid #b42318; padding-bottom: 4px; margin-top: 0; page-break-before: always; }
h2 { font-size: 13.5pt; color: #1d1d1f; margin-top: 22px; }
h2, h3 { page-break-after: avoid; }
h3 { font-size: 11pt; color: #b42318; margin: 14px 0 4px; }
p { text-align: justify; margin: 6px 0; }
table { border-collapse: collapse; width: 100%; margin: 8px 0 12px; font-size: 9.5pt; page-break-inside: avoid; }
th, td { border: 1px solid #d0d0d5; padding: 5px 7px; vertical-align: top; text-align: left; }
th { background: #f3f3f5; }
td:first-child { width: 26%; }
.nota { font-style: italic; color: #b42318; }
figure { margin: 10px 0 14px; text-align: center; page-break-inside: avoid; }
figure img { max-width: 100%; max-height: 9cm; border: 1px solid #ddd; }
figcaption { font-size: 8.5pt; color: #555; margin-top: 4px; text-align: left; word-break: break-all; }
.ph { border: 2px dashed #b42318; color: #b42318; padding: 40px 10px; font-weight: bold; }
hr { display: none; }
.portada { height: 23cm; display: flex; flex-direction: column; justify-content: center; }
.portada .inst { font-size: 11pt; letter-spacing: 2px; text-transform: uppercase; color: #b42318; font-weight: bold; }
.portada .t { border: none; font-size: 24pt; color: #1d1d1f; page-break-before: avoid; margin: 18px 0; line-height: 1.25; }
.portada .sub { font-size: 12pt; color: #555; margin-bottom: 40px; }
.portada .meta td { border: none; border-bottom: 1px solid #e5e5ea; padding: 7px 4px; font-size: 10.5pt; }
.portada .meta td:first-child { color: #777; width: 25%; }
"""
html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{PORTADA}{body}</body></html>"
# La introducción no debe empezar en página nueva distinta de la portada → ya fuerza salto por h1
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(); pg.set_content(html, wait_until="load")
    pg.pdf(path=PDF, format="Letter", print_background=True,
           display_header_footer=True, header_template="<span></span>",
           footer_template="<div style='font-size:8px;width:100%;text-align:center;color:#888'>"
                           "Felipe Zapata Lagos · Visualización de Datos U1 · <span class='pageNumber'></span></div>",
           margin={"top": "2.2cm", "bottom": "2.4cm", "left": "2.2cm", "right": "2.2cm"})
    b.close()
print("PDF generado:", PDF)
