import itertools

from data.sentence import Sentence


class SentencesCollection:
    instance = None
    id = itertools.count(start=1)

    @staticmethod
    def get_instance():
        """ Static access method. """
        if SentencesCollection.instance == None:
            SentencesCollection()
        return SentencesCollection.instance

    def __init__(self):
        """ Virtually private constructor. """
        if SentencesCollection.instance != None:
            raise Exception("This class is a singleton!")
        else:
            SentencesCollection.instance = self
            self.sentences = dict()

    def add(self, sentence: Sentence) -> int:
        id = next(SentencesCollection.id)
        self.sentences[id] = sentence
        return id

    def get_dict(self) -> dict:
        return self.sentences

    def __getitem__(self, key) -> Sentence:
        return self.sentences[key]
