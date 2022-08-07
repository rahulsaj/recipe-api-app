from calendar import c
import imp
from django.test import SimpleTestCase
from .calc import sum

class CalcTest(SimpleTestCase):
    """ Test the calc module """
    def test_sum_function(self):
        a = 5
        b = 3
        r = sum(a,b)
        self.assertEqual(r,8)