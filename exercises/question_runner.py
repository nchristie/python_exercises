from exercises.helpers import run_all_questions, create_question_list, ennumerate_task_list
from exercises.tasks import TASKS, BLURB


def run():
    print(BLURB)

    list_of_remaining_questions = run_all_questions(create_question_list(ennumerate_task_list(TASKS)))

    while list_of_remaining_questions:
        print(f"You got {len(TASKS) - len(list_of_remaining_questions)}/{len(TASKS)} questions right\n")
        if not _user_wants_to_retry_quiz():
            print("\nGame Over\n\n")
            exit()
        else:
            list_of_remaining_questions = run_all_questions(list_of_remaining_questions)

    print(f"You got {len(TASKS)}/{len(TASKS)} questions right\n")
    _bonus()
    exit()


def _bonus():
    print("Congratulations on passsing the quiz!!!")
    print(
        """
                                    .''.
        .''.      .        *''*    :_\/_:     .
        :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
    .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
  :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
  : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
    '..'  ':::'     * /\ *     .'/.\'.   '
        *            *..*         :
    """  # no-qa
    )
    print("\n\n")


def _user_wants_to_retry_quiz():
    ans = input("Do you want to try the questions you got wrong again? (y/n)\n")
    retry = _answer_only_y_or_n(ans)
    if not retry:
        sure = input("Are you sure you want to quit the quiz? (y/n)\n")
        retry = not _answer_only_y_or_n(sure)
    return retry
