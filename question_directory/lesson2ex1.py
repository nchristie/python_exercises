"""
TASKS is a list of lists. Each sublist follows this structure:
[
  <string of background information to print>,
  <string of question text>,
  <list of answer keywords>,
  <dictionary of prerequisite conditions>
]


empty object for copy-paste:
[
    "", # background info
    "", # question
    [], # list of required keywords
    {}, # dict or prerequisite conditions
],
"""

BLURB = "\nLesson 2 - Warm Up Exercise\n\n(Feel free to look back over the slides/use Google if you need help on this)\n"

TASKS = [
    [
        "",
        "Subtract one number from another\n\n",
        ["-"],
        {},
    ],
    [
        "",
        "Divide one number by the other\n\n",
        ["/"],
        {},
    ],
    [
        "",
        "Write a line of code which will display a string to the terminal\n\n",
        ["print"],
        {},
    ],
    [
        "", # background info
        "Write a line of code which will display a string to the terminal\n\n", # question
        ['print'], # list of required keywords
        {}, # dict or prerequisite conditions
    ],
    [
        "", # background info
        "Find out how many characters there are in your first name\n\n", # question
        ['len'], # list of required keywords
        {}, # dict or prerequisite conditions
    ],
    [
        "", # background info
        "Check if two values are equal to each other\n\n", # question
        ['=='], # list of required keywords
        {}, # dict or prerequisite conditions
    ],
]
