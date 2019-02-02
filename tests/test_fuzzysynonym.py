import unittest
from fuzzy_synonym.fuzzy_synonym import FuzzySynonym


class TestFuzzySynonym(unittest.TestCase):
    fixed_tags = ['Python', 'Deep Learning']
    observed_tags = [
        ['python', '深層学習', 'DL'],
        ['Python', 'Deep Learning'],
        ['Python', 'ディープラーニング', 'DL'],
        ['python', 'Deep-Learning'],
        ['python', 'deeplearning', 'DL']
    ]

    fs = FuzzySynonym()

    def test_fuzzy_synonym(self):
        res = self.fs.aggregate(fixed_tags=self.fixed_tags, observed_tags=self.observed_tags)
        self.assertEquals = (res, {"Python": ['python'], "Deep Learning": ['深層学習', 'ディープラーニング', 'Deep-Learning', 'deeplearning', 'DL']})


if __name__ == '__main__':
    unittest.main()
