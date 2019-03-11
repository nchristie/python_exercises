from exercises.helpers import is_correct_answer, ennumerate_task_list, _question_tuple_maker
from collections import namedtuple
import unittest


class Tests(unittest.TestCase):
    # SETUP
    Task = namedtuple("Task", ["q_num", "info", "question", "answer", "prerequisites"])

    generic_task_tuple = Task(
        q_num=1, info="instructions", question="question", answer=["a", "b"], prerequisites={"a": "a", "b": "b"}
    )

    def test_check_fail(self):
        # WHEN
        answer_to_question = "xyz"

        # THEN
        self.assertFalse(is_correct_answer(self.generic_task_tuple, answer_to_question))

    def test_check_pass(self):
        # WHEN
        answer_to_question = "a + b"

        # THEN
        self.assertTrue(is_correct_answer(self.generic_task_tuple, answer_to_question))

    def test_check_pass_del(self):
        # GIVEN
        clothes = ["shirt", "trousers", "blouse", "socks", "leggings", "shorts"]
        keywords = ["del", "clothes", "[1]"]
        prerequisites = {"clothes": clothes}

        task_tuple = self.Task(
            q_num=1, info="instructions", question="question", answer=keywords, prerequisites=prerequisites
        )

        # WHEN
        answer_to_question = "del clothes[1]"

        # THEN
        self.assertTrue(is_correct_answer(task_tuple, answer_to_question))

    def test_check_fail_no_answer(self):
        # GIVEN
        clothes = ["shirt", "trousers", "blouse", "socks", "leggings", "shorts"]
        keywords = ["del", "clothes", "[1]"]
        prerequisites = {"clothes": clothes}

        task_tuple = self.Task(
            q_num=1, info="instructions", question="question", answer=keywords, prerequisites=prerequisites
        )

        # WHEN
        answer_to_question = None

        # THEN
        self.assertFalse(is_correct_answer(task_tuple, answer_to_question))

    def test_check_fail_no_answer_no_exception(self):
        # GIVEN
        clothes = ["shirt", "trousers", "blouse", "socks", "leggings", "shorts"]
        keywords = ["del", "clothes", "[1]"]
        prerequisites = {"clothes": clothes}

        # WHEN
        task_tuple = self.Task(
            q_num=1, info="instructions", question="question", answer=keywords, prerequisites=prerequisites
        )

        answer_to_question = None

        # THEN
        try:
            is_correct_answer(task_tuple, answer_to_question)
        except Exception as e:
            print(e)
            self.fail("is_correct_answer() raised exception on answer_to_question = None")

    def test_check_pass_double_quotes(self):
        # GIVEN
        clothes = ["a", "b", "c"]
        keywords = ["clothes", "2", "'jacket'"]
        prerequisites = {"clothes": clothes}

        # WHEN
        task_tuple = self.Task(q_num=1, info="", question="", answer=keywords, prerequisites=prerequisites)

        answer_to_question = 'clothes[2] = "jacket"'

        # THEN
        self.assertTrue(is_correct_answer(task_tuple, answer_to_question))

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

        # WHEN
        expected = self.Task(
            q_num=1, info="instructions", question="question", answer=["a", "b"], prerequisites="prerequisites"
        )
        actual = _question_tuple_maker(1, "instructions", "question", ["a", "b"], "prerequisites")

        # THEN
        self.assertEqual(expected, actual)
