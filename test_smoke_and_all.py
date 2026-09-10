import unittest
from quiz_data import load_questions
from main import character_check

class TestSmoke(unittest.TestCase):

    def test_load_questions_runs(self): #smoke test to test that its working
        self.assertTrue(1)

    def test_load_questions_runs(self):# testing that questions are successfully loaded from CSV file
        questions=load_questions()
        self.assertIsNotNone(questions)

    def test_character_check_happy(self): #character checking valid names
        self.assertTrue(character_check("Natasha"))
        self.assertTrue(character_check("Natasha Zinyuke"))

    def test_character_check_unhappy(self): #character checking invalid names that have integer values
        self.assertFalse(character_check("Natasha001"))
        self.assertFalse(character_check("#Natashaisthenumber1best"))

if __name__=="__main__":
    unittest.main(verbosity=2)