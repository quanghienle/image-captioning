import svg_generator as svg_generator
import svg_to_png as svg_to_png
import os


#----------------------------------------------
# MAIN
#----------------------------------------------
if not os.path.exists('dataset'):
    os.makedirs('dataset')

svg_data_path = 'dataset/svg_data'
png_data_path = 'dataset/png_data'

if not os.path.exists(svg_data_path):
    os.makedirs(svg_data_path)

if not os.path.exists(png_data_path):
    os.makedirs(png_data_path)

# num_images = int(input("Enter number of images to generate: "))
num_images = 30000
print('------------------------------------\n')

# generate SVG dataset
print("Generating SVG dataset...")
for i in range(num_images):
    svgStr = svg_generator.make_svg()
    text_file = open(f"{svg_data_path}/{i}.svg", "w")
    text_file.write(svgStr)
    text_file.close()
print('DONE.')
print('------------------------------------\n')

# generate PNG dataset
print("Generating PNG dataset...")
svg_to_png.convert_to_png(svg_data_path, png_data_path)
print('DONE.')
print('------------------------------------\n')


