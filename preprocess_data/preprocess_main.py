import os
import preprocess_svg as preprocess_svg
import preprocess_png as preprocess_png

if not os.path.exists('./dataset/preprocessed_data'):
    os.makedirs('./dataset/preprocessed_data')

preprocess_png.encode_and_save_images()
preprocess_svg.clean_and_save_svg()
