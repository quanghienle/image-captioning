from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import glob


def getFileName(filePath):
    return filePath.split('/')[2].split('.')[0]

def convert_to_png(svg_path, png_path):
    file_names = glob.glob(f"{svg_path}/*.svg")
    for i in file_names:
        drawing = svg2rlg(i)
        name = f"{png_path}/{getFileName(i)}.png"
        renderPM.drawToFile(drawing, name, fmt="PNG")


