from exercises.helpers import run_questions, bonus, ennumerate_task_list
from exercises.tasks import TASKS

def run():
  print("\n\nFor the following questions remember that lists are zero-indexed. Meaning the first element will be at index 0, the second element at index 1 etc.\n\n")
  score = 0

  retry_dict = ennumerate_task_list(TASKS)
  res = run_questions(score, retry_dict)
  number_of_questions = len(retry_dict)

  #loop_questions_until_complete(res, retry_dict)

  while res['score'] < number_of_questions:
    number_of_questions = len(retry_dict)
    retry = input("Do you want to try the questions you got wrong again? (y/n)\n")
    retry = answer_only_y_or_n(retry)

    if retry.upper() == 'Y':
      res = run_questions(res['score'], res['retry_dict'])
    else:
      sure = input("Are you sure you want to quit the quiz? (y/n)\n")
      sure = answer_only_y_or_n(sure)
      if sure.upper() == 'Y':
        print('\nGame Over\n\n')
        exit()

  if res['score'] == number_of_questions:
    bonus()

def answer_only_y_or_n(y_n_answer):
  while y_n_answer.upper() != 'Y' and y_n_answer.upper() != 'N':
    y_n_answer = input("Please enter y or n\n")
  return y_n_answer


# def loop_questions_until_complete(res, retry_dict):
#   number_of_questions = len(retry_dict)
#   while res['score'] < number_of_questions:
#     number_of_questions = len(retry_dict)
#     retry = input("Do you want to try the questions you got wrong again? (y/n)\n")
#     retry = answer_only_y_or_n(retry)

#   if retry.upper() == 'Y':
#     res = run_questions(res['score'], res['retry_dict'])
#   else:
#     sure = input("Are you sure you want to quit the quiz? (y/n)\n")
#     sure = answer_only_y_or_n(sure)
#     if sure.upper() == 'Y':
#       print('\nGame Over\n\n')
#       exit()
