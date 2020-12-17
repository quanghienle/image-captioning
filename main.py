import pickle
from sklearn.model_selection import train_test_split

from model import ImageCaptioningModel
from tokenizer import Tokenizer
import data_generator.constants as constants
import utils as utils


# Load dataset
print('\nLoading data...')
X = pickle.load( open( './dataset/preprocessed_data/X.pkl', 'rb' ), encoding='bytes')
Y = pickle.load( open( './dataset/preprocessed_data/Y.pkl', 'rb' ), encoding='bytes')

# split dataset into train set and test set with the ratio of 0.2
print('\nSplitting data...')
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=111)


# Initialize tokenizer
print('\nInitializing Tokenizer...')
all_colors = constants.COLORS
all_numbers = [str(i).zfill(3) for i in range(101)]
tokenizer = Tokenizer(y_train, all_colors + all_numbers)

# Constants
VOCAB_SIZE = tokenizer.vocab_size
MAX_TEXT_LENGTH = 300
EMBEDDING_SIZE = 256


# Initialize the model
print('\nInitializing Model...')
model = ImageCaptioningModel(tokenizer, VOCAB_SIZE, EMBEDDING_SIZE, MAX_TEXT_LENGTH)

# Add checkpoints
print('\nAdding Checkpoints...')
checkpoint_path = './model_checkpoints/model_1'
model.add_checkpoint(checkpoint_path, True)


def start_training():
    print('\n\nPreparing data...')
    img_train, in_seq_train, out_seq_train = utils.data_to_seq(tokenizer, X_train, y_train, VOCAB_SIZE, MAX_TEXT_LENGTH)
    print('\n\nStart training...')
    train_result = model.train(img_train, in_seq_train, out_seq_train, 50, 500)


def start_evaluating():
    print('\n\nPreparing data...')
    img_test, in_seq_test, out_seq_test = utils.data_to_seq(tokenizer, X_test, y_test, VOCAB_SIZE, MAX_TEXT_LENGTH)
    print('\n\nStart evaluating...')
    loss, accu = model.evaluate(img_test, in_seq_test, out_seq_test)

def view_prediction():
    # use test data to check the prediction
    # index must be between 0 to 5999
    img_index = -1
    while img_index<0 or img_index>5999:
        img_index = int(input('\nEnter a test data index between 0 and 5999: '))

    print('\n\nMaking a prediction...\n')
    pred = model.predict(X_test[img_index])
    print(f'Label:\n{utils.format_svg(y_test[img_index])}')
    print(f'\nPrediction:\n{utils.format_svg(pred)}')

def view_data_shapes():
    print(f'\n\nX_train shape: {X_train.shape}, y_train shape: {y_train.shape}')
    print(f'X_test shape: {X_test.shape}, y_test shape: {y_test.shape}')


def view_vocab():
    print(tokenizer.vocab)


def view_model_summary():
    print(model.summary())

def exit_program():
    print('Exiting...')



########################################################
# MAIN
########################################################

options = {
        1: view_data_shapes,
        2: view_vocab,
        3: view_model_summary,
        4: start_training,
        5: start_evaluating,
        6: view_prediction,
        7: exit_program
}


option = -1
while option != 7:
    print('\n\nEnter one of the following options:')
    print('1. View data dimensions')
    print('2. View vocabulary')
    print('3. View model summary')
    print('4. Train model')
    print('5. Evaluate model')
    print('6. Make a prediction')
    print('7. Exit')

    option = int(input('> '))
    options[option]()
        
