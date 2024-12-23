# Notes for Day 16 of Advent of Code (2024)

## Heap queue (heapq)

Link: 
For examples: https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
For applications: https://www.geeksforgeeks.org/applications-of-heap-data-structure/

For this problem:
Graph algorithms: Heaps are used in graph algorithms such as Prim’s Algorithm, Dijkstra’s algorithm., and the A* search algorithm.

heappush(heap, ele): This function is used to insert the element mentioned in its arguments into a heap. 
The order is adjusted, so that heap structure is maintained.

heappop(heap): This function is used to remove and return the smallest element from the heap. 
The order is adjusted, so that heap structure is maintained.

## A* Algorithm
- Approximates the shortest path in real-life situations (maps and games) where they can be hinderances.
- Popular technique in path-finding and graph traversals

### Implementation
You have a start cell (S) and an end cell (E) and you want to get from S to E as quickly as possible.
the A* search algorithm works by, at each step, picking the node with the lowest f-value (which is a parameter equal to g + h), and then processes that cell.

g: the movement cost to get from S to any particular square on a grid, following the path generated to get there
h: the estimated movement cost to move from that square to E (a Heuristic value)

It uses two lists (open and closed, like Dijkstra): (from geeksforgeeks)
- Initialised the open and clost lists
- Put the starting node on open list (leave f at 0)
- While the open list is not empty
    - find the node with the least f on the open list (q)
    - pop q off the open list
    - generate q's 8 successors and set their parents to q  ***Note that 8 references when you can move diagonally in a grid, we only need 4 for day 16***
    - for each successor
        - if succesor is goal, stop search
        - else, compute g and h for successor (successor.g = q.g + distance between q and successor; successor.h = disance between successor and goal)
        - successor.f = successor.g + successor.h
        - if a node with the same position as successor is in the open list, which has a lower f than the successor, skip this successor
        - if a node with the same position as successor is in the closed list, which has a lower f than the successor, skip this successor
        - otherwise, add the node to the open list
    - end for loop
    - push q on to the closed list

### Dijkstra
Dijkstra’s algorithm is a shortest-path algorithm that finds the shortest path from a starting node to all other nodes in a graph. 
It uses a greedy approach, progressively selecting the node with the smallest known distance from the start node. 
The algorithm does not use heuristics and guarantees the optimal path in graphs with non-negative edge weights.

### Pros and cons
Pros:
Guaranteed to find the optimal path if the heuristic is admissible.
Balances exploration and exploitation using both path cost and heuristic.

Cons:
Can be computationally expensive for large search spaces.
Performance depends heavily on the heuristic function.

### Comparisons
A* vs Dijkstra: A* is more efficient because it uses a heuristic to prioritize nodes, while Dijkstra explores all nodes equally.
A* vs Greedy Best-First Search: A* guarantees optimality, unlike Greedy Best-First, which may find suboptimal paths.

## Pseudocode

### Dijkstra
```
def dijkstra(start, graph):
    if start not in graph:
        return None, None
        
    # Initialize data structures
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.add(start, 0)
    
    while not priority_queue.empty():
        current_node = priority_queue.remove()
        
        # Skip if we've already processed this node
        if current_node in visited:
            continue
            
        visited.add(current_node)
        
        # Stop if current distance is infinite (unreachable)
        if distances[current_node] == float('inf'):
            break
            
        for neighbor, weight in graph[current_node]:
            # Skip invalid edges
            if weight < 0:
                continue
                
            if neighbor not in graph:
                continue
                
            tentative_distance = distances[current_node] + weight
            
            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance
                previous_nodes[neighbor] = current_node
                
                # Update priority if node already in queue, otherwise add it
                if neighbor in priority_queue:
                    priority_queue.update_priority(neighbor, tentative_distance)
                else:
                    priority_queue.add(neighbor, tentative_distance)
    
    return distances, previous_nodes

def reconstruct_path(previous_nodes, start, goal):
    if not previous_nodes or goal not in previous_nodes:
        return None
        
    if start not in previous_nodes:
        return None
        
    path = []
    current_node = goal
    
    # Check if goal is reachable
    if previous_nodes[goal] is None and goal != start:
        return None
        
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
        
        # Detect cycles to prevent infinite loops
        if current_node in path:
            return None
            
    # Verify the path starts at the correct node
    if path[-1] != start:
        return None
        
    return path[::-1]
```

### A*
```
def A_star_search(start, goal):
    if not is_valid(start) or not is_valid(goal):
        return None
    
    if start == goal:
        return [start]
        
    open_list = PriorityQueue()
    open_list.add(start, 0)
    closed_set = set()
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while not open_list.empty():
        current = open_list.remove()
        
        if current == goal:
            return reconstruct_path(came_from, current)
            
        closed_set.add(current)

        for neighbor in neighbors(current):
            if not is_traversable(neighbor) or neighbor in closed_set:
                continue
                
            tentative_g_score = g_score[current] + cost(current, neighbor)
            
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                
                if neighbor not in open_list:
                    open_list.add(neighbor, f_score[neighbor])
                else:
                    open_list.update_priority(neighbor, f_score[neighbor])

    return None

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]
```
