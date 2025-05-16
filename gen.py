from PIL import Image
from reportlab.pdfgen import canvas
import os

# out dir
os.makedirs("output", exist_ok=True)

# minimal png
def create_minimal_png(path):
    img = Image.new('RGB', (1, 1), color='white')
    img.save(path, format='PNG')

# minimal jpg
def create_minimal_jpg(path):
    img = Image.new('RGB', (1, 1), color='white')
    img.save(path, format='JPEG', quality=1)

# minimal pdf
def create_minimal_pdf(path):
    c = canvas.Canvas(path)
    c.drawString(100, 750, "")  # empty string
    c.save()

# minimal svg
def create_minimal_svg(path):
    svg_content = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg width="1" height="1" version="1.1"
     xmlns="http://www.w3.org/2000/svg">
</svg>'''
    with open(path, 'w', encoding='utf-8') as f:
        f.write(svg_content)

# out file
create_minimal_png("output/minimal.png")
create_minimal_jpg("output/minimal.jpg")
create_minimal_pdf("output/minimal.pdf")
create_minimal_svg("output/minimal.svg")

print("[+]complete! check output dir")

