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
    {}, # dict of variables to set up before question
],
"""

BLURB = "\nLesson 2 - Exercise 2\n\
\nImagine you've got clients who are interested in the share prices of Google and Facebook.\nThe variables we're using for these questions will be:\ngoogle_up\nfacebook_up\nFor each question the respective values of google_up and facebook_up will either be True or False. Keep an eye on their values (set before each question is asked) in order to get the right anwers."

TASKS = [
    [
        "\ngoogle_up = False\nfacebook_up = False\n",  # background info
        "What would the output of this statement be now?\n\ngoogle_up and facebook_up\n",  # question
        ["False"],  # list of required keywords
        {"google_up": False, "facebook_up": False},  # dict of variables to set up before question
    ],
    [
        "\ngoogle_up = False\nfacebook_up = False\n",  # background info
        "How about this statement now?\n\ngoogle_up or facebook_up\n",  # question
        ["False"],  # list of required keywords
        {"google_up": False, "facebook_up": False},  # dict of variables to set up before question
    ],
    [
        "\ngoogle_up = False\nfacebook_up = False\n",  # background info
        "And this one?\n\nnot google_up\n",  # question
        ["True"],  # list of required keywords
        {"google_up": False, "facebook_up": False},  # dict of variables to set up before question
    ],
    [
        "\ngoogle_up = False\nfacebook_up = True\n",  # background info
        "What result do you expect from this statement? \ngoogle_up and facebook_up\n (Note that we've changed the values assigned to google_up and facebook_up above)\n",  # question
        ["False"],  # list of required keywords
        {"google_up": False, "facebook_up": True},  # dict of variables to set up before question
    ],
    [
        "\ngoogle_up = False\nfacebook_up = True\n",  # background info
        "google_up or facebook_up\n",  # question
        ["True"],  # list of required keywords
        {"google_up": False, "facebook_up": True},  # dict of variables to set up before question
    ],
    [
        "\ngoogle_up = False\nfacebook_up = True\n",  # background info
        "not facebook_up\n",  # question
        ["False"],  # list of required keywords
        {"google_up": False, "facebook_up": True},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        "Write one line of code using a Boolean operator (and, or, not) which will display True if Google's price is up and Facebook's price is up, and False if not\n",  # question
        ["google", "facebook", "and"],  # list of required keywords
        {"google_up": True, "facebook_up": True},  # dict of variables to set up before question
    ],
    [
        "\ngoogle_up = True\nfacebook_up = True\n",  # background info
        "A client wants to know if the share price of Google or Facebook rises\nHow would you write code to check for this?\nRemember, it *must* include a Boolean operator (and, or, not)\n",  # question
        ["google", "facebook", "or"],  # list of required keywords
        {"google_up": True, "facebook_up": True},  # dict of variables to set up before question
    ],
    [
        "\ngoogle_up = True\nfacebook_up = True\n",  # background info
        "Another client wants to know if Google's share price hasn't risen that day and doesn't mind what Facebook did that day.\n\nSome ways to do this would be to write\ngoogle_up == False\ngoogle_up != True\nCan you find another way?\n",  # question
        ["google", "not"],  # list of required keywords
        {"google_up": True, "facebook_up": True},  # dict of variables to set up before question
    ],
]
