import unittest
from fuzzy_synonym.translator import Translator


class TestTranslator(unittest.TestCase):

    tr = Translator("/fuzzy_synonym/translator/dictionary.ndjson")

    def test_tralslate(self):
        self.assertEqual(self.tr.translate('機械学習'), 'Machine Learning')


if __name__ == '__main__':
    unittest.main()
