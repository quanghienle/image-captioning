import glob
import numpy as np
import pickle

import utils as utils

def get_svg_arr():
    svg_images = glob.glob('../dataset/svg_data/*.svg')
    svg_arr = [None] * len(svg_images)
    for i in svg_images:
        f = open(i, 'r')
        svg_arr[utils.get_name_from_file(i)] = f.read()

    return np.array(svg_arr)


def remove_header(svg_text):
    """ Remove svg header tag since they are all the same for every file
    """
    lines = svg_text.split('\n')
    lines = lines[2:-1]
    lines.sort()
    return ' '.join(lines)


def clean_up_char(c):
    """ Adding some space to make it easier for splitting into words
    """
    if c == '\t':
      return ''
    elif c == '<':
      return '< '
    else:
      return c


def formatSVG(svg):
    """ Combine and clean up the svg text data into a better format
    """
    trimmed_svg = remove_header(svg)
    sentence = ''.join([clean_up_char(c) for c in trimmed_svg])
    return f'<start> {sentence} <end>'

def clean_and_save_svg():
    print('Cleaning SVG data...')
    svg_data = get_svg_arr()
    clean_data = np.array([formatSVG(svg) for svg in svg_data])

    print('Saving clean SVG data to dataset/preprocessed_data/Y.pkl')
    with open('../dataset/preprocessed_data/Y.pkl','wb') as f:
        pickle.dump(clean_data, f)

    print('DONE')


