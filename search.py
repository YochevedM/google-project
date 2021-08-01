import string

from data.auto_complete_data import AutoCompleteData
from data.words_data import Words_Data
from utils.clean_sentence import clean_sentence
from data.sentences_dict import SentencesCollection

alphabet = string.ascii_lowercase


class Search:
    def __init__(self, sentence_to_search: str) -> None:
        self.__sentence_to_search = sentence_to_search
        self.__input = sentence_to_search
        self.result = []

    def find_substring(self, score: int, s=None) -> None:
        if s:
            self.__sentence_to_search = s
        sentences_dict = SentencesCollection.get_instance()
        format_s = clean_sentence(self.__sentence_to_search)
        words_data = Words_Data.get_instance()
        word_trie = words_data.get_word(self.__sentence_to_search[0].lower())
        suitable_sentences = word_trie.search(format_s)
        for key, value in suitable_sentences.items():
            s = sentences_dict[key]
            self.result.append(AutoCompleteData(s.get_sentence(), s.get_page() + ' ' + str(s.get_line()), value, score))

    def find_replaced(self, index_: int, num_required: int, score: int) -> None:
        for ch in alphabet:
            self.find_substring(score, self.__input[:index_] + ch + self.__input[index_ + 1:])
            if len(self.result) >= num_required:
                return

    def find_added(self, _index: int, num_required: int, score: int) -> None:
        for ch in alphabet:
            self.find_substring(score, self.__input[:_index] + ch + self.__input[_index:])
            if len(self.result) >= num_required:
                return

    def find_deleted(self, index_: int, num_required: int, score: int) -> None:
        self.find_substring(score, self.__input[:index_] + self.__input[index_ + 1:])

    def get_best_k_completions(self, k: int) -> list:
        decrement_scores = {"find_replaced": [5, 4, 3, 2, 1],
                            "find_deleted": [10, 8, 6, 4, 2],
                            "find_added": [10, 8, 6, 4, 2]}
        base_score = len(self.__input) * 2
        self.find_substring(base_score)
        if len(self.result) < k:
            for i in reversed(range(len(self.__input))):
                self.find_replaced(i, k - len(self.result), base_score - decrement_scores["find_replaced"][min(4, i)])
                if len(self.result) == k:
                    break

        if len(self.result) < k:
            for i in reversed(range(len(self.__input))):
                self.find_deleted(i, k - len(self.result), base_score - decrement_scores["find_deleted"][min(4, i)])
                if len(self.result) == k:
                    break

        if len(self.result) < k:
            for i in reversed(range(len(self.__input))):
                self.find_added(i, k - len(self.result), base_score - decrement_scores["find_added"][min(4, i)])
                if len(self.result) == k:
                    break

        return self.result[:k]


def print_result(result: list) -> None:
    if len(result):
        print(f"Here are {len(result)} suggestions")
        for i, sentence in enumerate(result):
            print("{}. {}".format(i + 1, sentence))
    else:
        print("No suggestions")
