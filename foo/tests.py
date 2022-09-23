from django.test import TestCase


class TestStringMethods(TestCase):

    def setUp(self):
        print('Setup mock...')

    def test_1(self):
        print('Assert mock 1...')
        self.assertTrue(True)

    def test_2(self):
        print('Assert mock 2...')
        self.assertTrue(True)

    def tearDown(self):
        print('Tear down mock...')
