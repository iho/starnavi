from main import solver, Solver


input_string1 = """34 21 32 41 25
14 42 43 14 31
54 45 52 42 23
33 15 51 31 35
21 52 33 13 23"""

input_string2 = """55 14 25 52 21
44 31 11 53 43
24 13 45 12 34
42 22 43 32 41
51 23 33 54 15"""

result1 = [
    "11",
    "34",
    "42",
    "15",
    "25",
    "31",
    "54",
    "13",
    "32",
    "45",
    "35",
    "23",
    "43",
    "51",
    "21",
    "14",
    "41",
    "33",
    "52",
]
result2 = ["11", "55", "15", "21", "44", "32", "13", "25", "43"]


def test_functional_solver1():
    assert solver(input_string1) == result1


def test_functional_solver2():
    assert solver(input_string2) == result2


def test_oop_solver1():
    solver = Solver(input_string1)
    assert solver.solve() == result1


def test_oop_solver2():
    solver = Solver(input_string2)
    assert solver.solve() == result2
