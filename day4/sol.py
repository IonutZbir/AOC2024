import pprint as pp

XMAS = "XMAS"
SAMX = "SAMX"


class Solution:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.input = self.read_input()

    def read_input(self):

        inp = []
        with open(self.file_path) as file:
            for r in file:
                r = list(r.replace("\n", "#"))
                r.append("#")
                r.append("#")
                r.append("#")
                r.insert(0, "#")
                r.insert(0, "#")
                r.insert(0, "#")
                r.insert(0, "#")
                n = len(r)
                inp.append(r)

            inp.append(["#"] * n)
            inp.append(["#"] * n)
            inp.append(["#"] * n)
            inp.append(["#"] * n)
            inp.insert(0, ["#"] * n)
            inp.insert(0, ["#"] * n)
            inp.insert(0, ["#"] * n)
            inp.insert(0, ["#"] * n)

        return inp

    def visit(self, r, c, data) -> int:
        directions = [
            (0, 1),  # Right
            (0, -1),  # Left
            (1, 0),  # Down
            (-1, 0),  # Up
            (1, 1),  # Diagonal (bottom-right)
            (-1, -1),  # Diagonal (top-left)
            (1, -1),  # Diagonal (bottom-left)
            (-1, 1),  # Diagonal (top-right)
        ]

        counter = 0
        target = "XMAS"
        for dr, dc in directions:
            pattern = ""
            for i in range(len(target)):  # 4 characters in "XMAS"
                nr, nc = r + i * dr, c + i * dc
                if 0 <= nr < len(data) and 0 <= nc < len(data[0]):  # Bounds check
                    pattern += data[nr][nc]
                else:
                    break

            if pattern == target:
                counter += 1

        return counter

    def sol(self) -> int:
        data = self.input
        n = len(data)
        m = len(data[0])

        counter = 0

        for r in range(n):
            for c in range(m):
                char = data[r][c]

                if char == "X":
                    counter += self.visit(r, c, data)

        return counter

    def visit2(self, r, c, data) -> int:

        counter = 0
        targets = ["MAS", "SAM"]

        pattern = ""
        for i in range(len(targets[0])):
            pattern += data[r + i][c + i]

        if data[r][c + 2] == "S" and data[r + 2][c] == "M" and pattern in targets:
            counter += 1

        if data[r][c + 2] == "M" and data[r + 2][c] == "S" and pattern in targets:
            counter += 1

        return counter

    def sol2(self) -> int:
        data = self.input
        n = len(data)
        m = len(data[0])

        counter = 0

        for r in range(n):
            for c in range(m):
                char = data[r][c]

                if char == "M" or char == "S":
                    counter += self.visit2(r, c, data)

        return counter


if __name__ == "__main__":
    data = [
        ["X", "Z", "S", "S"],
        ["C", "M", "A", "L"],
        ["C", "M", "A", "L"],
        ["X", "Z", "X", "S"],
    ]

    file_path = "input/input.txt"
    s = Solution(file_path)
    s1 = s.sol()
    s2 = s.sol2()
    print(s1, s2)
