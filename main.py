def prepare_data(string):
    return list(map(lambda string: string.split(" "), string.split("\n")))


def solver(string):
    def solve(array, coordinates="11", path=None):
        if path is None:
            path = ["11"]
        clue = array[int(coordinates[0]) - 1][int(coordinates[1]) - 1]
        if clue is None or coordinates == clue:
            return path
        path.append(clue)
        array[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = None
        return solve(array, coordinates=clue, path=path)

    return solve(prepare_data(string))


class Solver(object):
    def __init__(self, string):
        self.input_string = string
        self.path = ["11"]
        self._prepare_data()

    def _prepare_data(self):
        self.input_array = list(
            map(lambda string: string.split(" "), self.input_string.split("\n"))
        )

    def solve(self):
        coordinates = "11"
        while True:
            clue = self.input_array[int(coordinates[0]) - 1][int(coordinates[1]) - 1]
            if clue is None or coordinates == clue:
                return self.path
            self.path.append(clue)
            self.input_array[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = None
            coordinates = clue
