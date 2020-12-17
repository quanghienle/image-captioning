import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import sequence
from tqdm import tqdm

def get_name_from_file(file_name):
    """ get file names from path
        file names here are just numbers that match the png with svg file
    """
    file_number = file_name.split('/')[-1].split('.')[0]
    return int(file_number)


def make_seq(tokenizer, sentence, vocab_size, max_len):
    """ split a sentence into sequences of words and the next words
    """
    partial_seqs = []
    next_words = []

    tokenized_words = [tokenizer.word_to_index(word) for word in sentence.split(' ')]
  
    for i in range(1, len(tokenized_words)):
        partial_seqs.append(tokenized_words[:i])
        next_words.append(tokenized_words[i])

    partial_seqs = sequence.pad_sequences(partial_seqs, max_len, padding='post')
    next_words = tf.keras.utils.to_categorical(next_words, num_classes=vocab_size)

    return (partial_seqs, next_words)


def data_to_seq(tokenizer, images, texts, vocab_size, max_len):
    img = []
    in_seq = []
    out_seq = []

    for idx in tqdm(range(len(texts))):
        padded_seq, next_words = make_seq(tokenizer, texts[idx], vocab_size, max_len)
        for i in range(len(padded_seq)):
            img.append(images[idx])
            in_seq.append(padded_seq[i])
            out_seq.append(next_words[i])
  
    return (np.array(img), np.array(in_seq), np.array(out_seq))


def format_svg(body):
    XML_HEADER = '<?xml version="1.0" standalone="no"?>'
    SVG_TAG = '<svg width="100" height="100" version="1.1" xmlns="http://www.w3.org/2000/svg" style="border:1px solid black" >'
    SVG_END_TAG = '</svg>'
    arr = body.split(' ')[1:-1]

    formatted_body = ''
    for c in ' '.join(arr):
        if c == '<':
            formatted_body +='\n\t'
        formatted_body += c

    formatted_body = formatted_body.replace('< ', '<')

    return f'{XML_HEADER}\n{SVG_TAG}{formatted_body}\n{SVG_END_TAG}'
  

def format_svg_oneline(svg_body):
    XML_HEADER = '<?xml version="1.0" standalone="no"?>'
    SVG_TAG = '<svg width="100" height="100" version="1.1" xmlns="http://www.w3.org/2000/svg">'
    SVG_END_TAG = '</svg>'
    arr = svg_body.split(' ')[1:-1]
    body = ' '.join(arr).replace('< ', '<')
    return f'{XML_HEADER} {SVG_TAG} {body} {SVG_END_TAG}'

