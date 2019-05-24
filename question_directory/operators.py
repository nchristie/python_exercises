# TASKS is a list of lists. Each sublist follows this structure:
# [
#   <string of background information to print>,
#   <string of question text>,
#   <list of answer keywords>,
#   <dictionary of prerequisite conditions>
# ]

"""
empty object for copy-paste:
[
    "", # background info
    "", # question
    [], # list of required keywords
    {}, # dict of prerequisite conditions
],
"""

BLURB = "\nOperators\n\nPractice using operators\n"

TASKS = [
    [
        "",  # background info
        "Write a calculation which will output 343 added to 645",  # question
        ["343", "+", "645"],  # list of required keywords
        {},  # dict of prerequisite conditions
    ]
]
