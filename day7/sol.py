from typing import List, Dict
import math


class Solution:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.input = self.read_input()
        
    def read_input(self) -> Dict[int, List[int]]:
        with open(self.file_path) as file:
            equations = []
            for row in file:
                row = row.strip()
                row = row.split(": ")
                val = int(row[0])
                terms = row[1].split(" ")
                terms = [int(x) for x in terms]
                
                equations.append((val, terms))                
        return equations
    
    def rec_sol(self, ris, eq, rc=0) -> bool:
        # rc is the current result
        
        if len(eq) == 0:
            return
                
        if ris == rc:
            return True
        
        if len(eq) == 1:
            return (eq[0] + rc == ris) or (eq[0] * rc == ris)
        
        if len(eq) == 2:
            t1 = (rc + eq[0] + eq[1] == ris) or (rc + eq[0] * eq[1] == ris)
            t2 = (rc * eq[0] + eq[1] == ris) or (rc * eq[0] * eq[1] == ris)
            return t1 or t2
            
        rcp = eq[0] + eq[1]
        rcm = eq[0] * eq[1]
        
        t1 = self.rec_sol(ris, eq[2:], rc + rcp) or self.rec_sol(ris, eq[2:], rc + rcm)
        t2 = self.rec_sol(ris, eq[2:], rc * rcp) or self.rec_sol(ris, eq[2:], rc * rcm)
        
        return t1 or t2
        
    def solve(self) -> int:
        equations = self.input
        s = 0
        indx = []
        for i, (ris, eq) in enumerate(equations):
            if self.rec_sol(ris, eq):
                indx.append(i)
        
        print(indx)
            
        return sum(equations[i][0] for i in indx)

file_path = "day7/input/test.txt"
s = Solution(file_path)
s1 = s.solve()
print(s1)