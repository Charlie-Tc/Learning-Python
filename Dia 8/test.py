import unittest
from program_test import number_impair,titles

class TestProgram(unittest.TestCase):

    def Test_file(self):
        impairs = 3
        self.assertEquals(number_impair(), impairs)

    '''def test_title(self):
        words = 'pepe'
        words_title = titles(words)
        self.assertEquals(words_title, 'Pepe')'''



if __name__ == '__main__':
    unittest.main()