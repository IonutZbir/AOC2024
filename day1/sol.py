from typing import List, Tuple

class Solution:
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.input = self.read_input()

    def read_input(self) -> Tuple[List[int], List[int]]:
        l1, l2 = [], []
        with open(self.file_path) as file:
            for r in file:
                r = r.split(" "*3)
                l1.append(int(r[0]))
                l2.append(int(r[1]))
        return l1, l2

    def sol1(self) -> int:
        out = 0
        l1, l2 = self.input
        l1.sort()
        l2.sort()
        for x, y in zip(l1, l2):
            out += abs(x - y)
        return out

    def sol2(self) -> int:
        freq = {}

        l1, l2 = self.input
        
        for x in l1:
            f = freq.get(x, 0)
            for y in l2:
                if x == y:
                    f += 1
            freq[x] = f
        return sum((k * v for k, v in freq.items()))

if __name__ == "__main__":
    file = "input/input1.txt"
    sol = Solution(file)
    print(sol.sol1())
    print(sol.sol2())