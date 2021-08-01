class Sentence:
    def __init__(self, sentence: str, page: str, line: int) -> None:
        self.line = line
        self.page = page
        self.sentence = sentence

    def get_line(self) -> int:
        return self.line

    def get_page(self) -> str:
        return self.page

    def get_sentence(self) -> str:
        return self.sentence
