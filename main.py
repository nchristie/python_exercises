"""
Press run above to start
"""

if input("\n\nPress enter to start\n") != "test":
    from exercises.question_runner import run
    from question_directory.Lesson1ExBooleansPt2 import TASKS, BLURB

    run(TASKS, BLURB)
else:
    from unit_tests.test_instructor_code import *  # noqa

    if __name__ == "__main__":
        unittest.main()  # noqa
