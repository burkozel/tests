import unittest
from unittest.mock import patch
import task


class TestSecretary(unittest.TestCase):
    def setUp(self):
        print("тест")

    @patch("aa.input")
    def test_get_name(self, testinp):
        testinp.side_effect = ["10006"]
        self.assertEqual(task.get_name(), "Аристарх Павлов")

    @patch("aa.input")
    def test_delete_doc(self, testinp):
        testinp.side_effect = ["11-2"]
        self.assertEqual(task.delete_doc(), ("11-2", True))

    @patch("aa.input")
    def test_move_to_shelf(self, testinp):
        testinp.side_effect = ["3", "10006"]
        task.move_to_shelf()
        self.assertEqual(task.directories["10006"], ['3'])

    def tearDown(self):
        print("тесты пройдены")