import unittest
from fuzzy_synonym.translator import Translator


class TestTranslator(unittest.TestCase):

    tr = Translator("./tests/translator/dictionary.ndjson")

    def test_tralslate(self):
        self.assertEqual(self.tr.translate('機械学習'), 'Machine learning')
        self.assertEqual(self.tr.translate('深層学習'), 'Deep learning')
        self.assertEqual(self.tr.translate('ブロックチェーン'), 'Block chain')


if __name__ == '__main__':
    unittest.main()
