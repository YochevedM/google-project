def clean_sentence(sentence):
    comma_sen = " ".join(sentence.lower().split(","))
    return " ".join(comma_sen.split())
