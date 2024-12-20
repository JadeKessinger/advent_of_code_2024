from enum import Enum

class Guard:
    def __init__(self, txt_map):
        self.map = Map(txt_map)
        self.visited_cells = set()
        self.set_position_and_direction(txt_map)
        self.set_next_cell()

    def set_position_and_direction(self, txt_map):
        for row in range(len(txt_map)):
            if "^" in txt_map[row]:
                self.position = self.map.get_cell(row, txt_map[row].index("^"))
                self.direction = Directions.UP
                break
            elif ">" in txt_map[row]:
                self.position = self.map.get_cell(row, txt_map[row].index(">"))
                self.direction = Directions.RIGHT
                break
            elif "v" in txt_map[row]:
                self.position = self.map.get_cell(row, txt_map[row].index("v"))
                self.direction = Directions.DOWN
                break
            elif "<" in txt_map[row]:
                self.position = self.map.get_cell(row, txt_map[row].index("<"))
                self.direction = Directions.LEFT
                break

    def set_next_cell(self):
        if self.direction == Directions.UP:
            self.next_cell = self.map.get_cell(self.position.row - 1, self.position.col)
        elif self.direction == Directions.RIGHT:
            self.next_cell = self.map.get_cell(self.position.row, self.position.col + 1)
        elif self.direction == Directions.DOWN:
            self.next_cell = self.map.get_cell(self.position.row + 1, self.position.col)
        elif self.direction == Directions.LEFT:
            self.next_cell = self.map.get_cell(self.position.row, self.position.col - 1)
        
    def walk_path(self):
        while self.next_cell != None:
            self.visited_cells.add(self.position)
            self.step()
        self.visited_cells.add(self.position)

    def step(self):
        while self.next_cell.is_obstruction:
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

class Map:
    def __init__(self, txt_map):
        self.height = len(txt_map)
        self.width = len(txt_map[0])

        self.cells = []
        for row in range(len(txt_map)):
            cell_row = []
            for col in range(len(txt_map)):
                is_obstruction = txt_map[row][col] == "#"
                cell_row.append(Cell(row, col, is_obstruction))
            self.cells.append(cell_row)
    
    def get_cell(self, row, col):
        is_in_bounds = (row >= 0 and row < self.height and 
                        col >= 0 and col < self.width)
        if is_in_bounds:
            return self.cells[row][col]
        else:
            return None
        
    def is_cell_in_bounds(self, cell):
        return (cell.row >= 0 and cell.row < self.height and 
                cell.col >= 0 and cell.col < self.width)

class Cell:
    def __init__(self, row, col, is_obstruction):
        self.row = row
        self.col = col
        self.is_obstruction = is_obstruction

    def __eq__(self, other):
        if other == None:
            return False

        return self.row == other.row and self.col == other.col

    def __hash__(self):
        cantor_pairing = (self.row + self.col) * (self.row + self.col + 1) / 2 + self.row
        return hash(cantor_pairing)

class Directions(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

def count_distinct_positions(txt_map):
    guard = Guard(txt_map)
    guard.walk_path()
    return len(guard.visited_cells)
        
f = open("inputs/day06.txt", "r")
map = []
for line in f:
    map.append(line)

print(f"Distinct guard positions: {count_distinct_positions(map)}")
