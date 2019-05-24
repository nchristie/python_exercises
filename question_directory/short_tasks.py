BLURB = "These tasks aren't for students"

CLOTHES = ["shirt", "trousers", "blouse", "socks", "leggings", "shorts"]
SHOES = ["sneakers", "heels", "flip-flops"]

PRINT_CLOTHES = "clothes = {}".format(CLOTHES)
PRINT_SHOES = "shoes = {}".format(SHOES)

SHORT_TASKS = [
    [
        PRINT_CLOTHES,
        "Can you change the third element to be 'jacket' instead?\n\n",
        ["clothes", "2", "'jacket'"],
        {"clothes": CLOTHES},
    ],
    [
        PRINT_CLOTHES,
        "Can you remove the second element from the list?\n\n",
        ["del", "clothes", "[1]"],
        {"clothes": CLOTHES},
    ],
    [
        PRINT_CLOTHES,
        "Can you remove the element 'shorts' from the list without knowing its index?\n\n",
        ["clothes", "('shorts')", ".", "remove"],
        {"clothes": CLOTHES},
    ],
]


TEST_TASKS = [
    ["", "type a\n\n", ["a"], {"a": 1}],
    ["", 'type "b"\n\n', ["b"], {"b": 2}],
    ["", 'type "c"\n\n', ["c"], {"c": 3}],
]
