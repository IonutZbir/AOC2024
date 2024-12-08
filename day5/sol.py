from typing import Dict, List, Set


class solution:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.input = self.read_input()
    
    def read_input(self) -> tuple[Dict[int, Set[int]], List[int]]:
        with open(self.file_path) as file:
            rules = {}
            seqs = []
            is_after_empty_line = False  # Flag to track lines after the empty line

            for row in file:
                row = row.strip()
                if row == "":
                    # Set the flag to start reading sequences
                    is_after_empty_line = True
                    continue
                
                if not is_after_empty_line:
                    # Parse rules before the empty line
                    pre, post = map(int, row.split("|"))
                    if pre in rules:
                        rules[pre].add(post)
                    else:
                        rules[pre] = {post}
                        rules[post] = set()
                    
                else:
                    # Parse sequences after the empty line
                    seqs.append([int(x) for x in row.split(",")])
            
        return rules, seqs

    def check_order(self, seq: List[int], rules: Dict[int, Set[int]]) -> bool:
        for i in range(1, len(seq)):
            if seq[i] not in rules.get(seq[i - 1], []):
                return False
        return True
    
    def solve1(self) -> int:
        rules, seqs = self.input
        
        s = 0
        for seq in seqs:
            s += seq[len(seq) // 2] if self.check_order(seq, rules) else 0
            
        return s

    def update(self, seq: List[int], rules: Dict[int, Set[int]]) -> List[int]:
        while not self.check_order(seq, rules):
            for i in range(1, len(seq)):
                if seq[i] not in rules.get(seq[i - 1], []):
                    seq[i - 1], seq[i] = seq[i], seq[i - 1]
        return seq
        
    def solve2(self) -> int:
        rules, seqs = self.input
        print(rules)
        
        s = 0
        for i, seq in enumerate(seqs):
            
            if not self.check_order(seq, rules):
                print(f"Seq {i} before update: {seq}")
                seq = self.update(seq, rules)
                s += seq[len(seq) // 2]
                print(f"Seq {i} after update: {seq}")
        return s

file_path = "day5/input/test.txt"
sol = solution(file_path)
s1 = sol.solve1()
s2 = sol.solve2()
print(s2)

            
            