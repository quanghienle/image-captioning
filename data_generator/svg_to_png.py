from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import glob


def getFileName(filePath):
    return filePath.split('/')[2].split('.')[0]

def convert_to_png():
    file_names = glob.glob("../dataset/svg_data/*.svg")
    for i in file_names:
        drawing = svg2rlg(i)
        name = f"../dataset/png_data/{getFileName(i)}.png"
        renderPM.drawToFile(drawing, name, fmt="PNG")


