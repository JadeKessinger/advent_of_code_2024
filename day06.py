from enum import Enum
import copy

class Guard:
    def __init__(self, txt_map):
        self.map = Map(txt_map)
        self.visited_cells = {} # Stores the visited cells linked to the directions the guard went after visiting
        self.loop_obstructions = set()
        self.no_loop_obstructions = set()
        self.set_position_and_direction(txt_map)
        self.starting_position = self.position
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
            self.next_cell = self.get_next_cell(self.position, self.direction)
        elif self.direction == Directions.RIGHT:
            self.next_cell = self.get_next_cell(self.position, self.direction)
        elif self.direction == Directions.DOWN:
            self.next_cell = self.get_next_cell(self.position, self.direction)
        elif self.direction == Directions.LEFT:
            self.next_cell = self.get_next_cell(self.position, self.direction)
    
    def get_next_cell(self, cell, direction):
        if direction == Directions.UP:
            return self.map.get_cell(cell.row - 1, cell.col)
        elif direction == Directions.RIGHT:
            return self.map.get_cell(cell.row, cell.col + 1)
        elif direction == Directions.DOWN:
            return self.map.get_cell(cell.row + 1, cell.col)
        elif direction == Directions.LEFT:
            return self.map.get_cell(cell.row, cell.col - 1)
        
    def walk_path(self):

        def add_visited_cell(position, direction):
            if position in self.visited_cells:
                self.visited_cells[position].add(direction)
            else:
                self.visited_cells[position] = {direction}
        
        while self.next_cell != None:
            position_before_step = self.position
            self.step()
            add_visited_cell(position_before_step, self.direction)

        add_visited_cell(self.position, self.direction)

    def step(self):
        while self.next_cell.is_obstruction:
            self.turn()
        
        if (self.next_cell != self.starting_position and 
            self.next_cell not in self.no_loop_obstructions and 
            self.next_cell not in self.loop_obstructions):
            if self.obstruction_would_create_loop():
                self.loop_obstructions.add(self.next_cell)
            else:
                self.no_loop_obstructions.add(self.next_cell)

        self.position = self.next_cell
        self.set_next_cell()

    def turn(self):
        self.direction = self.get_next_direction(self.direction)
        self.set_next_cell()
    
    def get_next_direction(self, direction):
        if direction == Directions.UP:
            return Directions.RIGHT
        elif direction == Directions.RIGHT:
            return Directions.DOWN
        elif direction == Directions.DOWN:
            return Directions.LEFT
        elif direction == Directions.LEFT:
            return Directions.UP

    def obstruction_would_create_loop(self):
        # We check if turning to the right would make us revisit a cell while going in the same direction as before
        visited_cells = copy.deepcopy(self.visited_cells)
        obstruction = self.next_cell
        direction = self.get_next_direction(self.direction)
        position_if_obstructed = self.position
        next_cell = self.get_next_cell(position_if_obstructed, direction)
        while next_cell != None:
            starting_direction = direction
            next_cell = self.get_next_cell(position_if_obstructed, direction)
            while next_cell != None and (next_cell.is_obstruction or next_cell == obstruction):
                direction = self.get_next_direction(direction)
                next_cell = self.get_next_cell(position_if_obstructed, direction)
                if direction == starting_direction: # Boxed in
                    return True

            if position_if_obstructed in visited_cells and direction in visited_cells[position_if_obstructed]:
                return True

            if position_if_obstructed in visited_cells:
                visited_cells[position_if_obstructed].add(direction)
            else:
                visited_cells[position_if_obstructed] = {direction}

            position_if_obstructed = next_cell
        
        return False

class Map:
    def __init__(self, txt_map):
        self.height = len(txt_map)
        self.width = len(txt_map[0].strip())

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
    
    def __str__(self):
        return f"({self.row}, {self.col})"
    
    def __repr__(self):
        return f"({self.row}, {self.col})"

class Directions(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

def count_distinct_positions(txt_map):
    guard = Guard(txt_map)
    guard.walk_path()
    return len(guard.visited_cells)

def count_obstructions(txt_map):
    guard = Guard(txt_map)
    guard.walk_path()
    return len(guard.loop_obstructions)
        
f = open("inputs/day06.txt", "r")
map = []
for line in f:
    map.append(line)

print(f"Distinct guard positions: {count_distinct_positions(map)}")
print(f"Obstructions that would create loops: {count_obstructions}")
