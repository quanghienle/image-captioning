import random
import time
import constants as constants


def fill_zeros(num):
    """ add leading zeroes to make sure that every number has 3 digits 
    """
    return str(num).zfill(3)

def dict2string (propDict):
    """ convert a dictionary to a string
    """
    dictStr = ""
    for prop in propDict:
        val = propDict[prop] if isinstance(propDict[prop], str) else fill_zeros(propDict[prop])
        dictStr += f"{prop} = \" {val} \" "
    return dictStr

def convert2svg (type, props):
    """ returns a SVG string given the object type and its attributes
    """
    return f"<{type} {dict2string(props)}/>"

#-------------------------------------------------------
# methods to generate SVG object given
#-------------------------------------------------------

def make_circle (cx, cy, r, border, color):
    return convert2svg("circle", {
            'cx': cx,
            'cy': cy,
            'r': r,
            'stroke': border,
            'fill': color,
            'stroke-width': 1
        })

def make_ellipse (cx, cy, rx, ry, border, color):
    return convert2svg("ellipse", {
            'cx': cx,
            'cy': cy,
            'rx': rx,
            'ry': ry,
            'stroke': border,
            'fill': color,
            'stroke-width': 1
        })

def make_line (x1, y1, x2, y2, color):
    return convert2svg("line", {
            'x1': x1,
            'y1': y1,
            'x2': x2,
            'y2': y2,
            'stroke': color,
            'stroke-width': 1
        })

def make_rect (x, y, width, height, border, color):
    return convert2svg("rect", {
            'x': x,
            'y': y,
            'width': width,
            'height': height,
            'stroke': border,
            'fill': color,
            'stroke-width': 1
        })

def make_path (x1, x2, x3, y, xq, yq, color):
    return convert2svg("path", {
            'd': f"M {fill_zeros(x1)} {fill_zeros(y)} Q {fill_zeros(xq)} {fill_zeros(yq)} , {fill_zeros(x2)} {fill_zeros(y)} T {fill_zeros(x3)} {fill_zeros(y)}",
            'fill': 'none',
            'stroke': color,
            'stroke-width': 1
        })


#-------------------------------------------------------
# methods to generate random SVG objects
#-------------------------------------------------------

def get_max_x(x):
    return min(x, constants.MAX_X-x)

def get_max_y(y):
    return min(y, constants.MAX_Y-y)

def random_curve():
    """ generate random SVG curve
    """
    y = random.randint(10, constants.MAX_Y-10) 
    x1 = random.randint(5, constants.MAX_X//3) 
    x3 = random.randint(x1+10, constants.MAX_X-5) 
    x2 = round((x1+x3)/2)

    xq = round((x1+x2)/2)
    yq = y - random.randint(10, min(y, constants.MAX_Y-y)) 
    yq = max(5, yq)

    border = random.choice(constants.BORDER_COLORS)
    return make_path(x1, x2, x3, y, xq, yq, border)

def random_line ():
    """ generate random SVG line
    """
    x1 = random.randint(8, constants.MAX_X-8) 
    y1 = random.randint(8, constants.MAX_Y-8) 

    x2 = random.randint(8, constants.MAX_X-8) 
    y2 = random.randint(8, constants.MAX_Y-8) 

    border = random.choice(constants.BORDER_COLORS)
    return make_line(x1, y1, x2, y2, border)


def random_ellipse ():
    """ generate random SVG ellipse
    """
    cx = random.randint(8, constants.MAX_X-8) 
    cy = random.randint(8, constants.MAX_Y-8) 

    rx = random.randint(8, get_max_x(cx))
    ry = random.randint(8, get_max_y(cy))

    border = random.choice(constants.BORDER_COLORS)
    body = random.choice(constants.COLORS)

    return make_ellipse(cx, cy, rx, ry, border, body)


def random_circle ():
    """ generate random SVG circle
    """
    cx = random.randint(8, constants.MAX_X-8) 
    cy = random.randint(8, constants.MAX_Y-8) 

    max_r = min(get_max_x(cx), get_max_y(cy))
    r = random.randint(8, max_r)

    border = random.choice(constants.BORDER_COLORS)
    body = random.choice(constants.COLORS)

    return make_circle(cx, cy, r, border, body)


def random_rect ():
    """ generate random SVG rectangle
    """
    x = random.randint(8, constants.MAX_X-8) 
    y = random.randint(8, constants.MAX_Y-8) 

    width = random.randint(5, (get_max_x(x)-2))
    height = random.randint(5, (get_max_y(y)-2))

    border = random.choice(constants.BORDER_COLORS)
    body = random.choice(constants.COLORS)

    return make_rect(x, y, width, height, border, body)


def make_svg ():
    """ generate a complete SVG file
    """
    shapes = ["circle", "ellipse", "rect", "line", "path"]
    random_object = {
            "circle": random_circle, 
            "ellipse": random_ellipse, 
            "rect": random_rect,
            "line": random_line,
            "path": random_curve
    }

    header = "<?xml version=\"1.0\" standalone=\"no\"?>"
    tag = f"<svg width=\"{constants.MAX_X}\" height=\"{constants.MAX_Y}\" version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\">"
    end_tag = "</svg>"

    body = ""

    objCount = random.randint(2, 5)

    for i in range(objCount):
        shape = random.choice(shapes)
        obj = random_object[shape]()
        body += f"\t{obj}\n"

    return f"{header}\n{tag}\n{body}{end_tag}"
