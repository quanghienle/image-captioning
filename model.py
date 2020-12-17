import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import sequence
from tensorflow.python.keras.models import Sequential, Model
from tensorflow.python.keras.layers import Dense, LSTM, TimeDistributed, Embedding, Activation, RepeatVector, Concatenate

class ImageCaptioningModel():
    def __init__(self, tokenizer, vocal_size, embedding_size, max_text_length):
        self.init_model(vocal_size, embedding_size, max_text_length)
        self.model_checkpoint_callback = None
        self.tokenizer = tokenizer
        self.vocal_size = vocal_size
        self.embedding_size = embedding_size
        self.max_text_length = max_text_length

    def init_model(self, vocal_size, embedding_size, max_text_length):
        # image model
        image_model = Sequential()
        image_model.add(Dense(embedding_size, input_shape=(2048,), activation='relu'))
        image_model.add(RepeatVector(max_text_length))

        # language model
        language_model = Sequential()
        language_model.add(Embedding(input_dim=vocal_size, output_dim=embedding_size,
            input_length=max_text_length))
        language_model.add(LSTM(256, return_sequences=True))
        language_model.add(TimeDistributed(Dense(embedding_size)))

        # join two models
        conca = Concatenate()([image_model.output, language_model.output])
        x = LSTM(128, return_sequences=True)(conca)
        x = LSTM(512, return_sequences=False)(x)
        x = Dense(vocal_size)(x)
        out = Activation('softmax')(x)

        self.model = Model(inputs=[image_model.input, language_model.input], outputs = out)
        self.model.compile(loss='categorical_crossentropy', optimizer='RMSprop', metrics=['accuracy'])

    def add_checkpoint(self, checkpoint_path, load_weights):
        if load_weights:
            self.model.load_weights(checkpoint_path)

        self.model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path, save_weights_only=True, verbose=1)

    def train(self, img_data, in_seq_data, out_seq_data, epochs=10, batch_size=500):
        train_result = self.model.fit(
              [img_data, in_seq_data],
              out_seq_data,
              batch_size=batch_size,
              epochs=epochs,
              callbacks=[self.model_checkpoint_callback])
        return train_result

    def evaluate(self, img_test, in_seq_test, out_seq_test):
        loss, acc = self.model.evaluate([img_test, in_seq_test], out_seq_test) 
        return loss, acc

    def predict(self, image):
        start_word = ["<start>"]
        for i in range(self.max_text_length):
            par_caps = [self.tokenizer.word_to_index(w) for w in start_word]
            par_caps = sequence.pad_sequences([par_caps], maxlen=self.max_text_length, padding='post')
            preds = self.model.predict([np.array([image]).reshape(1,2048), par_caps])
            pred = np.argmax(preds[0], axis=0)
            word_pred = self.tokenizer.index_to_word(pred)
            start_word.append(word_pred)
            
            if word_pred == "<end>":
                break

        svg_string =  ' '.join(start_word)
        return svg_string
                
    def summary(self):
        return self.model.summary()

