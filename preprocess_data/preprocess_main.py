import os
import preprocess_svg as preprocess_svg
import preprocess_png as preprocess_png

svg_data_path = 'dataset/svg_data'
png_data_path = 'dataset/png_data'
preprocessed_data_path = 'dataset/preprocessed_data'

if not os.path.exists(preprocessed_data_path):
    os.makedirs(preprocessed_data_path)

preprocess_png.encode_and_save_images(png_data_path, preprocessed_data_path)
preprocess_svg.clean_and_save_svg(svg_data_path, preprocessed_data_path)
