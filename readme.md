Author: Hien Le (101044264)
Supervisor: Majid Komeili


## COMP4905: Honours Project
## SVG Image Captioning with CNN and LSTM


## Project Structure
  - `data_generator/`
      - `generator_main.py`: runs `svg_generator.py` and `svg_to_png.py` to generate 30,000 SVG and PNG images, and saves them under `/dataset/svg_data/` and `/dataset/png_data/` respectively
      - `constants.py`: stores constants used for generating SVG files, such as colors, width, height...
      - `svg_generator.py`: consists of methods used for generating a SVG file with random objects.
      - `svg_to_png.py`: used to convert a SVG file to and PNG file
  - `preprocess_data/`
      - `preprocess_main.py`: runs `preprocess_svg.py` and `preprocess_png.py` to clean up the dataset, and saves them under `/dataset/preprocessed_data/`
      - `preprocess_svg.py`: cleans SVG data by removing unneccessary characters, and saves them as a single numpy array
      - `preprocess_png.py`: extracts features from PNG data using the pre-trained ResNet-50 model, and saves them as a single numpy array
  - `model_checkpoints/`: stores checkpoints for the model
  - `model.py`: the CNN-LSTM model with the following methods: add_checkpoint, train, evaluate, predict.
  - `tokenizer.py`: used to construct to vocabulary and to convert words to indices and vice versa.
  - `utils.py`: contains useful utility methods like: formating SVG file, get filename, convert SVG string to sequences...
  - `main.py`: main program for this project to load data, construct model, train, evaluate and make predictions.

## Run Instruction

  1. Generate the dataset:
  ```
      $ python3 ./data_generator/generator_main.py
  ```
  this will add 30,000 images under `/dataset/png_data/` and `/dataset/svg_data/`

  2. Preprocess data:
  ```
      $ python3 ./preprocess_data/preprocess_main.py
  ```
  this will preprocess the dataset and create the following files: `/dataset/preprocessed_data/X.pkl` and `/dataset/preprocessed_data/Y.pkl`

  3. Run the model:
  ```
      $ python3 main.py
  ```
  this will load data, construct model, and display options to train/evaluate/predict...











