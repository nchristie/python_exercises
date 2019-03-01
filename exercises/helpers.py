from collections import namedtuple


def ennumerate_task_list(task_list):
    for i, value in enumerate(task_list, 0):
        task_list[i].insert(0, i + 1)
    return task_list


def question_tuple_maker(q_num, info, question, answer):
    Task = namedtuple("Task", ["q_num", "info", "question", "answer"])
    task = Task(q_num, info, question, answer)
    return task


def run_questions(score, retry_dict, number_of_questions):
    remove_list = []
    for i in retry_dict:
        task = question_tuple_maker(i[0], i[1], i[2], i[3])
        print(task.info)
        print("{}. ".format(task.q_num), end="")
        answer_to_question = input(task.question)
        if check(answer_to_question, task.answer):
            remove_list.append(i)
            score += 1
    for i in remove_list:
        retry_dict.remove(i)
    print("You got {}/{} questions right\n".format(score, number_of_questions))
    return {"score": score, "retry_dict": retry_dict}


def check(question, keywords=None):
    try:
        if type(keywords) == dict:
            keywords = keywords.keys()
        if all(keyword in question for keyword in keywords):
            print("=> ", end="")
            print("\nCorrect\n")
            return True
        else:
            print("\nIncorrect\n")
            return False
    except Exception as e:
        print("\nIncorrect\n", e)
        return False


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
    """
    )
    print("\n\n")
