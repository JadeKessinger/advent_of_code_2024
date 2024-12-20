from enum import Enum

class Directions(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

class Guard:
    def __init__(self, position, direction, map):
        self.position = position
        self.direction = direction
        self.map = map
        self.cell = self.set_next_cell()

    def set_next_cell(self):
        if self.direction == Directions.UP:
            self.next_cell = Cell(self.position.row - 1, self.position.col, self.map)
        elif self.direction == Directions.RIGHT:
            self.next_cell = Cell(self.position.row, self.position.col + 1, self.map)
        elif self.direction == Directions.DOWN:
            self.next_cell = Cell(self.position.row + 1, self.position.col, self.map)
        elif self.direction == Directions.LEFT:
            self.next_cell = Cell(self.position.row, self.position.col - 1, self.map)

    def step(self):
        if not self.position.is_in_bounds():
            raise Exception("Guard cannot take a step when out of bounds")
        
        while self.next_cell.is_obstruction():
            self.turn()
        
        self.position = self.next_cell
        self.set_next_cell()

    def turn(self):
        if self.direction == Directions.UP:
            self.direction = Directions.RIGHT
        elif self.direction == Directions.RIGHT:
            self.direction = Directions.DOWN
        elif self.direction == Directions.DOWN:
            self.direction = Directions.LEFT
        elif self.direction == Directions.LEFT:
            self.direction = Directions.UP
        self.set_next_cell()

class Cell:
    def __init__(self, row, col, map):
        self.row = row
        self.col = col
        self.map = map
    
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
    
    def __hash__(self):
        cantor_pairing = (self.row + self.col) * (self.row + self.col + 1) / 2 + self.row
        return hash(cantor_pairing)
    
    def is_in_bounds(self):
        return (self.row >= 0 and self.row < len(self.map) and 
                self.col >= 0 and self.col < len(self.map[0]))
    
    def is_obstruction(self):
        if self.is_in_bounds():
            return self.map[self.row][self.col] == "#"
        else:
            return False

def get_distinct_positions(map):
    guard = get_starting_guard(map)
    visited_cells = set()

    while guard.position.is_in_bounds():
        visited_cells.add(guard.position)
        guard.step()
    
    return visited_cells

def get_starting_guard(map):
    for row in range(len(map)):
        if "^" in map[row]:
            position = Cell(row, map[row].index("^"), map)
            direction = Directions.UP
            return Guard(position, direction, map)
        elif ">" in map[row]:
            position = Cell(row, map[row].index(">"), map)
            direction = Directions.RIGHT
            return Guard(position, direction, map)
        elif "v" in map[row]:
            position = Cell(row, map[row].index("v"), map)
            direction = Directions.DOWN
            return Guard(position, direction, map)
        elif "<" in map[row]:
            position = Cell(row, map[row].index("<"), map)
            direction = Directions.LEFT
            return Guard(position, direction, map)
    raise Exception("No guard exists on the map!")
        
f = open("inputs/day06_test.txt", "r")
map = []
for line in f:
    map.append(line)

print(f"Distinct guard positions: {len(get_distinct_positions(map))}")
