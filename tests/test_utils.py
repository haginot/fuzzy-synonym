import unittest
from fuzzy_synonym import utils

class TestUtils(unittest.TestCase):

    def test_is_acronym(self):
        bool_acronym = [utils.is_acronym(s) for s in ['B2B', 'Wi-Fi', 'NoSQL', 'Hadoop', 'NumPy']]
        self.assertEqual(bool_acronym, [True, True, True, False, False])

if __name__ == '__main__':
    unittest.main()