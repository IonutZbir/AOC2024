from typing import Tuple


class Solution:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.input = self.read_input()
    
    def read_input(self) -> str:
        with open(self.file_path) as file:
            m = []
            for row in file:
                row = row.strip()
                row = " " + row + " "
                m.append([char for char in row])
            m.append([" "] * len(row))
            m.insert(0, [" "] * len(row))
        return m
    
    def print_map(self, m):
        for row in m:
            print(row)
    
    def solve(self) -> int:
        m = self.input

        rows = len(m)
        cols = len(m[0])
        unique = 0

        # Find the starting position of "^"
        for i in range(rows):
            for j in range(cols):
                if m[i][j] == "^":
                    r, c = i, j
                    m[r][c] = "."
                    break
        
        directions = {
            "^": (-1, 0),  # Up
            ">": (0, 1),   # Right
            "v": (1, 0),   # Down
            "<": (0, -1)   # Left
        }
        current_dir = "^"
        while True:
            # Move in the current direction
            dr, dc = directions[current_dir]
            while m[r][c] in ".X" and 0 <= r < rows and 0 <= c < cols:
                if m[r][c] != "X":
                    unique += 1
                m[r][c] = "X"  # Mark as visited
                r, c = r + dr, c + dc

            # Check the current position or stop
            if 0 <= r < rows and 0 <= c < cols and m[r][c] == "#":
                if current_dir == "^":
                    current_dir = ">"
                    r, c = r + 1, c + 1
                elif current_dir == ">":
                    current_dir = "v"
                    r, c = r + 1, c - 1
                elif current_dir == "v":
                    current_dir = "<"
                    r, c = r - 1, c - 1
                elif current_dir == "<":
                    current_dir = "^"
                    r, c = r - 1, c + 1
            if 0 <= r < rows and 0 <= c < cols and m[r][c] == " ":
                break

        return unique



        
file_path = "day6/input/input.txt"
s = Solution(file_path)
s1 = s.solve()
print(s1)