def combine(*items, result):
    def dfs(index, current):
        if index == len(items):
            return current == result
    
        if dfs(index + 1, current + items[index]):
            return True
        
        if dfs(index + 1, current * items[index]):
            return True
    
        if index > 0:
            concatenate = int(str(current) + str(items[index]))
            if dfs(index + 1, concatenate):
                return True
    
        return False

    return dfs(1, items[0])

# with open("test_input.txt") as f:
#    data = f.readlines()
with open("input.txt") as f:
    data = f.readlines()

lines = {}
for line in data:
    target,items = line.split(":")
    lines[target] = list(map(int, items.strip().split()))

results = []
for k,v in lines.items():
    if combine(*v, result=int(k)):
        results.append(int(k))

print(sum(results))
    
