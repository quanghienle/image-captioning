import svg_generator as svg_generator
import svg_to_png as svg_to_png


#----------------------------------------------
# MAIN
#----------------------------------------------

# num_images = int(input("Enter number of images to generate: "))
num_images = 30000
print('------------------------------------\n')

# generate SVG dataset
print("Generating SVG dataset...")
for i in range(num_images):
    svgStr = svg_generator.make_svg()
    text_file = open(f"../dataset/svg_data/{i}.svg", "w")
    text_file.write(svgStr)
    text_file.close()
print('DONE.')
print('------------------------------------\n')

# generate PNG dataset
print("Generating PNG dataset...")
svg_to_png.convert_to_png()
print('DONE.')
print('------------------------------------\n')


