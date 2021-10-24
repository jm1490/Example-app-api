from django.test import TestCase

from app.cal import add

class CalcTests(TestCase):

    def test_add_numbers(self):
        "test that two numbers are added together"
        self.asertEqual(add(3,8),11)
        
