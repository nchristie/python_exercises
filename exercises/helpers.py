from collections import namedtuple


def ennumerate_task_list(task_list):
    for i, value in enumerate(task_list, 0):
        task_list[i].insert(0, i + 1)
    return task_list


def _question_tuple_maker(q_num, info, question, answer, prerequisites):
    Task = namedtuple("Task", ["q_num", "info", "question", "answer", "prerequisites"])
    task = Task(q_num, info, question, answer, prerequisites)
    return task


def create_question_list(ennumerated_tasks):
    list_of_remaining_questions = []
    for task_data in ennumerated_tasks:
        task_tuple = _question_tuple_maker(task_data[0], task_data[1], task_data[2], task_data[3], task_data[4])
        list_of_remaining_questions.append(task_tuple)
    return list_of_remaining_questions


def get_input(task_tuple):
    print(task_tuple.info)
    print(f"{task_tuple.q_num}. {task_tuple.question}")
    answer_to_question = input()
    return answer_to_question


def run_all_questions(list_of_remaining_questions):
    remove_list = []
    for task_tuple in list_of_remaining_questions:
        answer_to_question = get_input(task_tuple).replace('"', "'")
        user_output = get_output_for_user(answer_to_question, task_tuple)
        was_correct_answer = is_correct_answer(task_tuple, answer_to_question, user_output)
        if was_correct_answer:
            remove_list.append(task_tuple)
        print(print_correct_or_incorrect(user_output, was_correct_answer))
    for i in remove_list:
        list_of_remaining_questions.remove(i)
    return list_of_remaining_questions


def is_correct_answer(task_tuple, answer_to_question, user_output=None):
    keywords = task_tuple.answer
    was_correct_answer = False
    if answer_to_question and not user_output or "Error" not in user_output:
        was_correct_answer = all(keyword in answer_to_question for keyword in keywords)
    return was_correct_answer


def get_output_for_user(answer_to_question, task_tuple):
    user_output = None
    try:
        user_output = (
            exec(answer_to_question, task_tuple.prerequisites)
            if run_exec(answer_to_question)
            else eval(answer_to_question, task_tuple.prerequisites)
        )
        user_output = str(user_output)
    except Exception as e:
        user_output = f"Error message: {e}"
    if not answer_to_question:
        user_output = None
    return user_output


def print_correct_or_incorrect(user_output, was_correct_answer):
    print_this = ""
    if user_output:
        print_this += "=> {}".format(user_output)
    if was_correct_answer:
        print_this += "\nCorrect\n"
    else:
        print_this += "\nIncorrect\n"
    return print_this


def run_exec(answer_to_question):
    return ("=" in answer_to_question) or ("del" in answer_to_question)


def answer_only_y_or_n(y_n_answer):
    y_n = {"Y": True, "N": False}
    while y_n_answer.upper() != "Y" and y_n_answer.upper() != "N":
        y_n_answer = input("Please enter y or n\n")
    return y_n[y_n_answer.upper()]


def user_wants_to_retry_quiz():
    ans = input("Do you want to try the questions you got wrong again? (y/n)\n")
    retry = answer_only_y_or_n(ans)
    if not retry:
        sure = input("Are you sure you want to quit the quiz? (y/n)\n")
        retry = not answer_only_y_or_n(sure)
    return retry


def bonus():
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
