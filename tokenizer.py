class Tokenizer():
    def __init__(self, dataset, others):
        self.initVocab(dataset, others)
        self.vocab_size = len(self.vocab)

    def initVocab(self, dataset, others):
        words = others
        for sentence in dataset:
            words += sentence.split(' ')
        words = list(set(words))
        words.sort()
        self.vocab = ['<pad>'] + words

    def word_to_index(self, word):
        return self.vocab.index(word)

    def index_to_word(self, index):
        return self.vocab[index]




