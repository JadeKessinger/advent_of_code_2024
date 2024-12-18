from collections import deque

def min_steps_to_exit(bytes):
    grid = simulate_falling_bytes(bytes)

    position = (0, 0)
    steps = 0
    visited = set()
    queue = deque([(position, steps)])
    def bfs():
        while queue:
            (position, steps) = queue.popleft()
            print(position)
            
            (x, y) = position
            if position == (70, 70):
                return steps
            elif x >= 0 and x < 71 and y >= 0 and y < 71 and position not in visited and grid[y][x] == '.':
                visited.add(position)
                queue.append(((x, y - 1), steps + 1))
                queue.append(((x + 1, y), steps + 1))
                queue.append(((x, y + 1), steps + 1))
                queue.append(((x - 1, y), steps + 1))
            
    return bfs()

def simulate_falling_bytes(bytes):
    grid = [["." for _ in range(71)] for _ in range(71)]
    for byte_num in range(1024):
        (x, y) = bytes[byte_num]
        grid[y][x] = "#"
    
    return grid

f = open("inputs/day18.txt", "r")
falling_bytes = []
for line in f:
    falling_bytes.append((int(line[0:line.index(",")]), int(line[line.index(",") + 1:])))

print("Minimum steps to exit: " + str(min_steps_to_exit(falling_bytes)))