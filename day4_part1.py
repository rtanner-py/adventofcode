input = "day_4.txt"
word = "XMAS"

with open(input, "r") as f:
    data = f.readlines()
grid = []
for line in data:
    grid.append(list(line.strip()))
  
def count_occurences(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    directions = [
        (0,1),(0,-1), #right, left
        (1,0),(-1,0), #down, up
        (-1,-1),(-1,1), #up left, up right
        (1,-1),(1,1) #down left, down right
    ]

    def is_valid(x,y):
        #checks if co-ordinate out of bounds
        return 0 <= x < rows and 0 <= y < cols

    def find_xmas(x,y,dx,dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx,ny) or grid[nx][ny] != word[i]:
                return False
        return True

    count = 0
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if find_xmas(i,j,dx,dy):
                    count += 1

    return count

occurences = count_occurences(grid, word)
print(occurences)
