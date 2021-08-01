from data.word_trie import Word_Trie


class Words_Data:
    instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if Words_Data.instance == None:
            Words_Data()
        return Words_Data.instance

    def __init__(self):
        """ Virtually private constructor. """
        if Words_Data.instance != None:
            raise Exception("This class is a singleton!")
        else:
            Words_Data.instance = self
            self.words = dict()

    def add_sentence(self, letter: chr, sentence: str, index: int, id: int) -> None:
        if not isinstance(letter, str):
            raise ValueError("word has to be string.")
        if letter not in self.words:
            self.words[letter] = Word_Trie()
            self.words[letter].insert(sentence[index:], id, index)
        else:
            self.words[letter].insert(sentence[index:], id, index)

    def get_word(self, word: chr) -> Word_Trie:
        if word not in self.words:
            return
        else:
            return self.words[word]
