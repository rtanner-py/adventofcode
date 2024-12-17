#input = "test_input.txt"
input = "input.txt"

with open(input) as f:
    grid = [[int(num) for num in line.strip()] for line in f]

def find_routes(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    
    scores = []
    
    def dfs(x,y, visited, reachable_nines):
        if grid[x][y] == 9:
            reachable_nines.add((x,y))
            return
        
        current = grid[x][y]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == current + 1:
                visited.add((nx,ny))
                dfs(nx,ny,visited,reachable_nines)
                
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                reachable_nines = set()
                visited = set()
                visited.add((i,j))
                dfs(i,j,visited,reachable_nines)
                
                scores.append(len(reachable_nines))
    
    return scores

def part_2(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    paths = []
    
    def dfs(x,y,path):
        if grid[x][y] == 9:
            paths.append(path[:])
            return
    
        current = grid[x][y]
        
        for dx, dy in directions:
            nx,ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == current + 1:
                path.append((nx,ny))
                dfs(nx, ny, path)
                path.pop()
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                dfs(i,j, [(i,j)])
    
    return paths



scores = find_routes(grid)
print(f"Part 1: {sum(scores)}")
paths = part_2(grid)
print(f"Part 2: {len(paths)}")

