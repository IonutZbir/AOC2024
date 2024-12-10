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
                terms.insert(0, val)
                
                equations.append(terms)                
        return equations
    
    def rec_sol(self, eq: List[int], ris) -> bool:
        
        if len(eq) == 2:
            return (eq[0] + eq[1] == ris) or (eq[0] * eq[1] == ris) or (int(str(eq[0]) + str(eq[1])) == ris)
        
        neq = [eq[0] + eq[1]] + eq[2:]

        t1 = self.rec_sol(neq, ris)
        
        neq = [eq[0] * eq[1]] + eq[2:]
        t2 = self.rec_sol(neq, ris)
        
        neq = [int(str(eq[0]) + str(eq[1]))] + eq[2:]
        t3 = self.rec_sol(neq, ris)
        return t1 or t2 or t3    
        
    def solve(self) -> int:
        equations = self.input
        indx = []
        for i, eq in enumerate(equations):
            print(eq)
            if self.rec_sol(eq[1:], eq[0]):
                indx.append(i)
        
        print(indx)    
        return sum(equations[i][0] for i in indx)

file_path = "day7/input/input.txt"
s = Solution(file_path)
s1 = s.solve()
print(s1)