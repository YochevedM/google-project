class AutoCompleteData:
    def __init__(self, completed_sentence: str, source_text: str, offset: int, score: int) -> None:
        self.completed_sentence = completed_sentence
        self.source_text = source_text
        self.offset = offset
        self.score = score

    def __str__(self):
        return "{} ({}), offset: {}, score: {}".format(self.completed_sentence, self.source_text, self.offset,
                                                       self.score)
