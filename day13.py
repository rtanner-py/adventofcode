from typing import List, Tuple
import numpy as np
import re

def get_data(input: str) -> List[str]:
    with open(input) as f:
        data = f.read()
        groups = data.split("\n\n")
    return groups

def extract_coordinates(group: str) -> List[Tuple[int,int]]:
    pattern = r'X[+=](\d+), Y[+=](\d+)'
    matches = re.findall(pattern, group)
    coordinates = [(int(x), int(y)) for x,y in matches]
    return coordinates    

def solve(input: List[Tuple[int, int]]) -> Tuple[int, int]:
    (x1, y1), (x2, y2), (xprize, yprize) = input
    xprize += 10000000000000 #part 2
    yprize += 10000000000000 #part 2
    x, y = np.linalg.solve([[x1,x2],[y1,y2]], [xprize,yprize])
    return x,y

def main(): 
    test_input = "input_test.txt"
    input = "input.txt"
    groups = get_data(input)
    input = [extract_coordinates(group) for group in groups]
    cost = 0
    solutions = 0
    for group in input:
        x,y = solve(group)
        if abs(x - round(x)) < 0.0001 and abs(y - round(y)) < 0.0001:
            x,y = int(round(x)), int(round(y))
            solutions += 1
            cost += x * 3 + y * 1
    print(f"Possible solutions of {solutions} at a cost of {cost}")

if __name__ == "__main__":
    main()
        
