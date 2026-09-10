import unittest
from quiz_data import load_questions

class TestSmoke(unittest.TestCase):

    def test_load_questions_runs(self):
        self.assertTrue(1)

    def test_load_questions_runs(self):
        questions=load_questions()
        self.assertIsNotNone(questions)


if __name__=="__main__":
    unittest.main(verbosity=2)