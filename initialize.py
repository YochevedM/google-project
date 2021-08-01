import os

from config import data_url
from data.sentence import Sentence
from data.sentences_dict import SentencesCollection
from data.words_data import Words_Data
from utils.clean_sentence import clean_sentence


def insert_sentence(sentence: str, page: str, line: int) -> None:
    word_data = Words_Data.get_instance()
    s = Sentence(sentence, page, line)
    format = clean_sentence(sentence)
    id = SentencesCollection.get_instance().add(s)
    # add to words
    for i in range(len(sentence)):
        if sentence[i] != " ":
            word_data.add_sentence(sentence[i].lower(), format, i, id)


def find_txt_files(path: str) -> list:
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))
    return files


def read_files(files: list) -> None:
    for f in files:
        with open(f, encoding="utf8") as file:
            lines = file.readlines()
            for i in range(len(lines)):
                insert_sentence(lines[i], os.path.basename(f)[:-4], i)


def init():
    fiels = find_txt_files(data_url)
    read_files(fiels)
