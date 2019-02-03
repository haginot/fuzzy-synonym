class TagDict:
    def __init__(self,
                 fixed_tags=[]):
        self.__tags = {k: set() for k in fixed_tags}
        self.__jp_tags = dict()

    def add(self, word, synonym):
        if word in self.__tags:
            self.__tags[word].add(synonym)
        else:
            self.__tags[word] = set(synonym)

    def find(self, word):
        if word in self.__tags:
            return self.__tags[word]
        else:
            return None

    def add_jp(self, src, dest):
        self.__jp_tags[src] = dest

    def find_jp(self, word):
        if word in self.__jp_tags:
            return self.__jp_tags[word]
        else:
            return None

