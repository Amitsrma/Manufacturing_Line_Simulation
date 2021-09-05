# Manual cell numbers
MANUAL_CELLS = (2, 7)

# Automated cells setup times in seconds
WORKCELL_SETUP_TIMES = {
    1: {"A": 25, "B": 20, "C": 17},
    3: {"A": 52, "B": 21, "C": 34},
    4: {"A": 35, "B": 22, "C": 24},
    5: {"A": 29, "B": 14, "C": 37},
    6: {"A": 31, "B": 24, "C": 51}
}

# Manual cells setup times, triangular distribution. In seconds
MANUAL_WORKCELL_SETUP_TIMES = {
    2: {
        "A": (36, 45, 52),
        "B": (21, 32, 39),
        "C": (32, 36, 42)
        },
    7: {
        "A": (27, 35, 41),
        "B": (31, 39, 43),
        "C": (22, 27, 38)
    }
}
