import logging
from typing import List, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(message)s',
    filename="log.txt",
    filemode="w"
)

class Solution:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.input = self.read_input()
    
    def read_input(self) -> List[List[int]]:
        l2 = []
        try:
            with open(self.file_path) as file:
                for r in file:
                    l2.append(list(map(int, r.split())))
        except FileNotFoundError:
            logging.error(f"File {self.file_path} not found.")
            raise
        except ValueError as e:
            logging.error(f"Invalid data in file: {e}")
            raise
        return l2

    def is_increasing(self, r: List[int]) -> bool:
        for i in range(len(r) - 1):
            s = r[i] - r[i + 1]
            if s >= 0 or s < -3:
                return False
        return True
        
    def is_decreasing(self, r: List[int]) -> bool:
        for i in range(len(r) - 1):
            s = r[i] - r[i + 1]
            if s <= 0 or s > 3:
                return False
        return True
    
    def can_be_safe(self, r: List[int]) -> bool:
        # Try removing one element and check if the row becomes safe
        for i in range(len(r)):
            modified_row = r[:i] + r[i+1:]
            if self.is_increasing(modified_row) or self.is_decreasing(modified_row):
                logging.info(f"Row after removal of {r[i]} is safe: {modified_row}")
                return True
        logging.info(f"Row {r} cannot be made safe by removing one level.")
        return False
    
    def sol1(self) -> int:
        inp = self.input
        safe = 0
        for r in inp:
            safe += 1 if self.is_increasing(r) or self.is_decreasing(r) else 0
        return safe

    def sol2(self) -> int:
        inp = self.input
        safe = 0
        for r in inp:
            logging.info(f"Processing row: {r}")
            if self.is_increasing(r) or self.is_decreasing(r):
                safe += 1
                logging.info("Row is safe.")
            elif self.can_be_safe(r):
                logging.info(f"Row can be adjusted to be safe: {r}")
                safe += 1
        return safe

if __name__ == "__main__":
    file = "input/input.txt"
    s = Solution(file)
    s1 = s.sol1()
    s2 = s.sol2()
    print(f"Solution 1 (safe rows): {s1}")
    print(f"Solution 2 (safe rows): {s2}")
