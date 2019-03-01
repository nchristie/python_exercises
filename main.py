"""
Press run above to start
"""

if input("\n\nPress enter to start\n") != "test":
    from exercises.question_runner import run

    run()
else:
    from unit_tests.test_instructor_code import *

    if __name__ == "__main__":
        unittest.main()
