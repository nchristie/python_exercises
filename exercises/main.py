from exercises.helpers import run_questions, bonus, ennumerate_task_list
from exercises.tasks import TASKS

def run():
  print("\n\nFor the following questions remember that lists are zero-indexed. Meaning the first element will be at index 0, the second element at index 1 etc.\n\n")
  score = 0

  retry_dict = ennumerate_task_list(TASKS)
  number_of_questions = len(retry_dict)
  res = run_questions(score, retry_dict, number_of_questions)

  while res['score'] < number_of_questions:

    retry = input("Do you want to try the questions you got wrong again? (y/n)\n")
    while retry.upper() != 'Y' and retry.upper() != 'N':
        retry = input("Please enter y or n\n")

    if retry.upper() != 'Y':
      sure = input("Are you sure you want to quit the quiz? (y/n)\n")
      while sure.upper() != 'Y' and sure.upper() != 'N':
        sure = input("Please enter y or n\n")
      if sure.upper() == 'Y':
        print('\nGame Over\n\n')
        exit()
      print('\n')
    else:
      res = run_questions(res['score'], res['retry_dict'], number_of_questions)

  if res['score'] == number_of_questions:
    bonus()
