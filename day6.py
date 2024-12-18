from enum import Enum

class Directions(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

def get_distinct_positions(map):
    (position, direction) = get_starting_guard(map)
    (cur_row, cur_col) = position
    visited = set()
    while cur_row >= 0 and cur_row < len(map) and cur_col >= 0 and cur_col < len(map[0]):
        visited.add((cur_row, cur_col))
        if direction == Directions.UP:
            if cur_row != 0 and map[cur_row - 1][cur_col] == "#":
                direction = Directions.RIGHT
            else:
                cur_row -= 1
        elif direction == Directions.RIGHT:
            if cur_col != len(map[0]) - 1 and map[cur_row][cur_col + 1] == "#":
                direction = Directions.DOWN
            else:
                cur_col += 1
        elif direction == Directions.DOWN:
            if cur_row != len(map) - 1 and map[cur_row + 1][cur_col] == "#":
                direction = Directions.LEFT
            else:
                cur_row += 1
        elif direction == Directions.LEFT:
            if cur_col != 0 and map[cur_row][cur_col - 1] == "#":
                direction = Directions.UP
            else:
                cur_col -= 1
    return len(visited)


def get_starting_guard(map):
    for row in range(len(map)):
        if "^" in map[row]:
            return ((row, map[row].index("^")), Directions.UP)
        elif ">" in map[row]:
            return ((row, map[row].index(">")), Directions.RIGHT)
        elif "v" in map[row]:
            return ((row, map[row].index("v")), Directions.DOWN)
        elif "<" in map[row]:
            return ((row, map[row].index("<")), Directions.LEFT)
        
f = open("day6.txt", "r")
map = []
for line in f:
    map.append(line)

print("Distinct guard positions: " + str(get_distinct_positions(map)))