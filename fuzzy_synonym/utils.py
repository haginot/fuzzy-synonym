import fuzzy_synonym.constants as const


def is_acronym(s: str):
    word_len = len(s)
    return const.ACRONYM_MINIMUM_LENGTH <= word_len <= const.ACRONYM_MAXIMUM_LENGTH \
           and sum([str.isupper(c) or not str.isalpha(c) for c in s]) / word_len >= const.ACRONYM_UPPER_RATE

