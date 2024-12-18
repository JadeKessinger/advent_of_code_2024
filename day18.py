from collections import deque

def min_steps_to_exit(num_bytes, bytes):
    grid = simulate_falling_bytes(num_bytes, bytes)

    position = (0, 0)
    steps = 0
    visited = set()
    queue = deque([(position, steps)])
    def bfs():
        while queue:
            (position, steps) = queue.popleft()
            (x, y) = position

            if position == (70, 70):
                return steps
            elif x >= 0 and x < 71 and y >= 0 and y < 71 and position not in visited and grid[y][x] == '.':
                visited.add(position)
                queue.append(((x, y - 1), steps + 1))
                queue.append(((x + 1, y), steps + 1))
                queue.append(((x, y + 1), steps + 1))
                queue.append(((x - 1, y), steps + 1))
        return None
            
    return bfs()

def simulate_falling_bytes(num_bytes, bytes):
    grid = [["." for _ in range(71)] for _ in range(71)]
    for byte_num in range(num_bytes):
        (x, y) = bytes[byte_num]
        grid[y][x] = "#"
    
    return grid

def find_first_cut_off_byte(bytes):
    fallen_bytes = 0
    while min_steps_to_exit(fallen_bytes, bytes) != None:
        fallen_bytes += 1
    
    return bytes[fallen_bytes-1]

f = open("inputs/day18.txt", "r")
falling_bytes = []
for line in f:
    falling_bytes.append((int(line[0:line.index(",")]), int(line[line.index(",") + 1:])))

print("Minimum steps to exit: " + str(min_steps_to_exit(1024, falling_bytes)))
print("First byte to cut off all paths: " + str(find_first_cut_off_byte(falling_bytes)))