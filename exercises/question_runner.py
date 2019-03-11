from exercises.helpers import (
    run_all_questions,
    bonus,
    create_question_list,
    user_wants_to_retry_quiz,
    ennumerate_task_list,
)
from exercises.tasks import TASKS, BLURB


def run():
    print(BLURB)

    list_of_remaining_questions = run_all_questions(create_question_list(ennumerate_task_list(TASKS)))

    while list_of_remaining_questions:
        print(f"You got {len(TASKS) - len(list_of_remaining_questions)}/{len(TASKS)} questions right\n")
        if not user_wants_to_retry_quiz():
            print("\nGame Over\n\n")
            exit()
        else:
            list_of_remaining_questions = run_all_questions(list_of_remaining_questions)

    print(f"You got {len(TASKS)}/{len(TASKS)} questions right\n")
    bonus()
    exit()
