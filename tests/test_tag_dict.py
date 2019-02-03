import unittest
from fuzzy_synonym.tag_dict import TagDict


class TestTagDict(unittest.TestCase):
    tag_dict = TagDict(['Python', 'Go', 'Rust'])

    def test_add(self):
        self.tag_dict.add('Go', 'Go-Lang')
        self.assertIn('Go-Lang', self.tag_dict.find('Go'))
        self.assertEquals(len(self.tag_dict.find('Go')), 1)
        self.assertEquals(len(self.tag_dict.find('Python')), 0)

    def test_add_jp(self):
        self.tag_dict.add_jp('GoLang', 'Go言語')
        self.assertEqual('Go言語', self.tag_dict.find_jp('GoLang'))
        self.assertFalse(self.tag_dict.find_jp('Python'))


if __name__ == '__main__':
    unittest.main()

