from django.test import SimpleTestCase
from letter_digit.letter_case_permutation import letter_case_permutation


class TestLetterCasePermutation(SimpleTestCase):

    def test_letter_case_permutation(self):
        expected = ['a2b', 'a2B', 'A2B', 'A2b']
        actual = letter_case_permutation('a2b')
        self.assertEquals(set(expected), set(actual))
