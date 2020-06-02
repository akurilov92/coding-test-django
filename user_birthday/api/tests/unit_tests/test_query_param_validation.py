from django.test import SimpleTestCase
from api.query_param_validation import parse_birthday_filter


class TestParseBirthdayFilter(SimpleTestCase):

    def test_parse_birthday_filter_ddmm(self):
        actual = parse_birthday_filter('1812')
        self.assertEquals(actual.day, 18)
        self.assertEquals(actual.month, 12)

    def test_parse_birthday_filter_noleadingzeroes(self):
        actual = parse_birthday_filter('112')
        self.assertEquals(actual.day, 11)
        self.assertEquals(actual.month, 2)

    def test_parse_birthday_filter_leadingzeroes(self):
        actual = parse_birthday_filter('012')
        self.assertEquals(actual.day, 1)
        self.assertEquals(actual.month, 2)
