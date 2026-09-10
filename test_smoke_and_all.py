import unittest
from quiz_data import load_questions
from main import character_check

class TestSmoke(unittest.TestCase):

    def test_load_questions_runs(self):
        self.assertTrue(1)

    def test_load_questions_runs(self):
        questions=load_questions()
        self.assertIsNotNone(questions)

    def test_character_check_happy(self):
        self.assertTrue(character_check("Natasha"))
        self.assertTrue(character_check("Natasha Zinyuke"))

    def test_character_check_unhappy(self):
        self.assertFalse(character_check("Natasha001"))
        self.assertFalse(character_check("#Natashaisthenumber1best"))

if __name__=="__main__":
    unittest.main(verbosity=4)