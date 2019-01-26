import os
import ndjson
import fuzzy_synonym.constants as const


class Translator:
    def __init__(self,
                 dict_path: str = "translator/dictionary.ndjson",
                 src="ja",
                 dest="en"
                 ):
        self.src = src
        self.dest = dest
        self.dict_path = dict_path
        self.dict_ja_en = self.read_dict()

    def read_dict(self):
        with open(self.dict_path, 'r') as dict_file:
            dict_ls = ndjson.load(dict_file)
            return {d[self.src]: d[self.dest] for d in dict_ls}

    def weite_dict(self):
        pass

    def translate(self, text):
        if text in self.dict_ja_en:
            return self.dict_ja_en[text]
        else:
            return 'Unknown'

