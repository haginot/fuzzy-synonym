from fuzzy_synonym.tag_dict import TagDict


class FuzzySynonym:
    def __init__(self,
                 fixed_tags = []):
        tag_dict = TagDict(fixed_tags)

    def aggregate(self,
                  fixed_tags,
                  observed_tags):
        pass
