from typing import List,Tuple, Set
from tqdm import tqdm
import multiprocessing

INPUT = 'input.txt'

with open(INPUT) as f:
    grid = [list(line.rstrip()) for line in f]
   
# #testing
# with open('test_input.txt') as f:
#     grid = [list(line.rstrip()) for line in f]
 
ROWS = len(grid)
COLS = len(grid[0])

# find current position
def find_guard(grid: List[List[int]]) -> Tuple[int,int]:
    for i, row in enumerate(grid):
        for j,col in enumerate(row):
            if col == '^':
                # print(f"Guard found at index ({i},{j})")
                return (i,j)

def valid_position(row: int, col: int) -> bool:
    return 0 <= row < ROWS and 0 <= col < COLS

def next_move(row: int, col: int, direction: str) -> Tuple[int, int]:
    return (row+directions[direction][0], col+directions[direction][1])

def find_obstacles(grid: List[List[int]]) -> List[Tuple[int, int]]:
    obstacles = []
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == '#':
                obstacles.append((i, j))
                #print(f"obstacle found at {i},{j}")
    return obstacles

def simulate_with_obstace(grid: List[List[str]], obstacle: Tuple[int,int], guard_position: Tuple[int,int]) -> bool:
    #print(f"Simulating obstacle at ({obstacle[0]},{obstacle[1]})")
    test_grid = [row[:] for row in grid]
    test_grid[obstacle[0]][obstacle[1]] = "#"
    guard_row, guard_col = guard_position
    direction = "up"
    visited_positions: Set[Tuple[int,int,str]] = set()
    
    while valid_position(*next_move(guard_row,guard_col,direction)):
        next_row, next_col = next_move(guard_row,guard_col, direction)
        if test_grid[next_row][next_col] == '#':
            direction = change_direction[direction]
        else:
            guard_row, guard_col = next_row, next_col
        
        state = (guard_row, guard_col, direction)
        if state in visited_positions:
            return True
        visited_positions.add(state)
    return False

def process_obstacle(position: Tuple[int,int]) -> Tuple[int, int, bool]:
    guard_position = find_guard(grid)
    result = simulate_with_obstace(grid, position, guard_position)
    return position if result else None

directions = {
    "up": (-1,0),
    "right": (0,1),
    "down": (1,0),
    "left": (0,-1)
}

change_direction = {
    'up':'right',
    'right':'down',
    'down': 'left',
    'left':'up'
}

positions = []

guard_row, guard_col = find_guard(grid)
positions = []
positions.append((guard_row, guard_col))
obstacles = find_obstacles(grid)


#print(f"guard row: {guard_row} | guard col {guard_col}")
direction = "up"
#print(f"direction {direction} | details: {directions[direction]}")
while valid_position(*next_move(guard_row, guard_col, direction)):
    next_row, next_col = next_move(guard_row, guard_col, direction)
    if (next_row, next_col) in obstacles:
        direction = change_direction[direction]
        #print(f"Obstacle found, changing to {direction}")
    else:    
        guard_row = next_row
        guard_col = next_col
        if (guard_row, guard_col) not in positions:
            positions.append((guard_row, guard_col))
            #print(f"No obstacle, adding ({guard_row}, {guard_col})")

#print(f"Next position not valid, exiting")
# print(f"Total visits: {len(positions)}")

if __name__ == "__main__":
    empty_positions = [(i,j) for i in range(ROWS) for j in range(COLS) if grid[i][j] == "."]
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = list(tqdm(pool.imap(process_obstacle, empty_positions), total=len(empty_positions)))
        loop_positions = [result for result in results if result]
    print(f"Found loops: {len(loop_positions)}")
