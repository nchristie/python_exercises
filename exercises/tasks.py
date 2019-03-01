CLOTHES = ["shirt", "trousers", "blouse", "socks", "leggins", "shorts"]
SHOES = ["sneakers", "heels", "flip-flops"]

PRINT_CLOTHES = "clothes = {}".format(CLOTHES)
PRINT_SHOES = "shoes = {}".format(SHOES)

TASKS = [
    [PRINT_CLOTHES, "Can you change the third element to be 'jacket' instead?\n\n", ["clothes", "2", "'jacket'"]],
    [PRINT_CLOTHES, "Can you change the last element to be 'hat' insted?\n\n", ["clothes", "-1", "'hat'"]],
    [
        PRINT_CLOTHES,
        "Can you change the second-to-last element to be the same as the first element?\n\n",
        ["clothes", "-2", "0"],
    ],
    [PRINT_CLOTHES, "Can you append 'jumper' to the list?\n\n", ["clothes", "append", ".", "('jumper')"]],
    [
        "You have another list, " + PRINT_SHOES,
        "Can you add all the items from SHOES to CLOTHES and re-assign to CLOTHES?\n\n",
        ["clothes", "=", "+", "shoes"],
    ],
    [PRINT_SHOES, "Can you mutiply this list by 5?\n", ["shoes", "*", "5"]],
    [PRINT_CLOTHES, "Can you remove the second element from the list?\n\n", ["del", "clothes", "[1]"]],
    [
        PRINT_CLOTHES,
        "Can you remove the element 'shorts' from the list without knowing its index?\n\n",
        ["clothes", "('shorts')", ".", "remove"],
    ],
]
