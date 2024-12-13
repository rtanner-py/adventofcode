from itertools import combinations

TEST_INPUT = "test_input.txt"
INPUT = "input.txt"

def get_grid(input):
    with open(input) as f:
        return [list(line.rstrip()) for line in f]
    
def valid_position(row: int, col: int) -> bool:
    return 0 <= row < ROWS and 0 <= col < COLS

def find_pairings(grid):
    coordinate_dict = {}
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == '.':
                continue
            if cell not in coordinate_dict:
                coordinate_dict[cell] = []
            coordinate_dict[cell].append((x,y))
    
    all_pairs = []
    for cordinates in coordinate_dict.values():
        all_pairs.extend(combinations(cordinates,2))
    
    return all_pairs

def find_antinodes(grid, pairings):
    antinodes_part1 = set()
    antinodes_part2 = set()
    for pairing in pairings:
        (x1,y1),(x2,y2) = pairing
        dx = x2 - x1
        dy = y2 - y1
        
        if valid_position(x1-dx, y1-dy):
            antinodes_part1.add((x1-dx, y1-dy))
        if valid_position(x2+dx, y2+dy):
            antinodes_part1.add((x2+dx, y2+dy))
                  
        current_x, current_y = x1, y1
        antinodes_part2.add((x1,y1))
        while True:
            current_x -= dx
            current_y -= dy
            if not valid_position(current_x, current_y):
                break
            antinodes_part2.add((current_x, current_y))
        
        current_x, current_y = x1, y1    
        while True:
            current_x += dx
            current_y += dy
            if not valid_position(current_x, current_y):
                break
            antinodes_part2.add((current_x, current_y))
    return antinodes_part1, antinodes_part2
          
grid = get_grid(INPUT)
ROWS = len(grid)
COLS = len(grid[0])
part_1, part_2 = find_antinodes(grid,find_pairings(grid))
print(len(part_1), len(part_2))
