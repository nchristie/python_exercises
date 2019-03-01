from exercises.helpers import check, ennumerate_task_list, question_tuple_maker
from collections import namedtuple
import unittest


class Tests(unittest.TestCase):
    def test_check_fail(self):
        # GIVEN
        answer_to_question = "eggs"
        keywords = "spam"

        # THEN
        self.assertFalse(check(answer_to_question, keywords))

    def test_check_pass(self):
        # GIVEN
        answer_to_question = "clothes[2] 'jacket'"
        keywords = ["clothes", "2", "'jacket'"]

        # THEN
        self.assertTrue(check(answer_to_question, keywords))

    def test_ennumerate_task_list(self):
        # GIVEN
        task_list = [[], [], [], []]

        # WHEN
        expected = [[1], [2], [3], [4]]
        actual = ennumerate_task_list(task_list)

        # THEN
        self.assertEqual(expected, actual)

    def test_question_tuple_maker(self):
        # GIVEN
        Task = namedtuple("Task", ["q_num", "info", "question", "answer"])

        # WHEN
        expected = Task(q_num=1, info="instructions", question="question", answer=["a", "b"])
        actual = question_tuple_maker(1, "instructions", "question", ["a", "b"])

        # THEN
        self.assertEqual(expected, actual)
