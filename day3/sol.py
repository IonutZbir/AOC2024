import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(message)s',
)

OPAR = "("
CPAR = ")"
COMMA = ","
MUL = "mul"
DO = "do()"
DONT = "don't()"

digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

class Solution:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.input = self.read_input()
    
    def read_input(self) -> str:
        file = open(self.file_path)
        inp = file.read()
        return inp
    
    def sol(self) -> int:
        data = self.input
        cursor = 0
        l = []

        while cursor < len(data):
            if data[cursor: cursor + 3] == MUL:
                cursor += 3
                if cursor < len(data) and data[cursor] == OPAR:
                    cursor += 1
                    a = ""
                    while cursor < len(data) and data[cursor] in digits:
                        a += data[cursor]
                        cursor += 1
                    
                    if cursor < len(data) and data[cursor] == COMMA:
                        cursor += 1
                        b = ""
                        while cursor < len(data) and data[cursor] in digits:
                            b += data[cursor]
                            cursor += 1

                        if cursor < len(data) and data[cursor] == CPAR:
                            cursor += 1 
                            if a and b:
                                l.append(int(a) * int(b))
            else:
                cursor += 1 

        return sum(l)
    
    def sol2(self) -> int:
        data = self.input
        lenght = len(data)
        cursor = 0
        l = []
        
        # logging.info(f"{data:}, {lenght}")
        
        do = True
        while cursor < lenght:
            if data[cursor: cursor + len(DONT)] == DONT:
                cursor += len(DONT)
                do = False
            elif data[cursor: cursor + len(DO)] == DO:
                cursor += len(DO)
                do = True
            elif data[cursor: cursor + len(MUL)] == MUL and do:
                cursor += len(MUL)
                if cursor < lenght and data[cursor] == OPAR:
                    cursor += 1
                    a = ""
                    while cursor < lenght and data[cursor] in digits:
                        a += data[cursor]
                        cursor += 1
                    
                    if cursor < lenght and data[cursor] == COMMA:
                        cursor += 1
                        b = ""
                        while cursor < lenght and data[cursor] in digits:
                            b += data[cursor]
                            cursor += 1

                        if cursor < lenght and data[cursor] == CPAR:
                            cursor += 1 
                            if a and b:
                                l.append(int(a) * int(b))
            else:
                cursor += 1 

        return sum(l)

file_path = "input/input.txt"
sol = Solution(file_path)
s1 = sol.sol()
s2 = sol.sol2()

print(s1, s2)