import io
import ndjson

import fuzzy_synonym.constants as const
import googletrans
import jsonlines


class Translator:
    def __init__(self,
                 dict_path: str = "translator/dictionary.ndjson",
                 src="ja",
                 dest="en"):
        self.src = src
        self.dest = dest
        self.dict_path = dict_path
        self.dict_ja_en = self.__read_dict()
        self.dict_ja_en_update = {}
        self.google_trans = googletrans.Translator()

    def __read_dict(self):
        with open(self.dict_path, 'r') as dict_file:
            dict_ls = ndjson.load(dict_file)
            return {d[self.src]: d[self.dest] for d in dict_ls}

    def __write_dict(self):
        # with open(self.dict_path, 'w') as dict_file:
            # ndjson.dump(self.dict_ja_en_update, dict_file, encoding='utf8')
            # dict_file.write((self.dict_ja_en_update)+'\n')
        with jsonlines.open(self.dict_path, mode='a') as writer:
            writer.write(self.dict_ja_en_update)

    def translate(self, text):
        if text in self.dict_ja_en:
            return self.dict_ja_en[text]
        else:
            res = self.google_trans.translate(text, dest=self.dest, src=self.src)
            self.dict_ja_en.update({text: res.text})
            self.dict_ja_en_update = {self.src: text, self.dest: res.text}
            self.__write_dict()
            self.dict_ja_en_update = {}
            return res.text

