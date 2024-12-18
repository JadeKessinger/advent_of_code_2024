def word_search(word, puzzle):
    '''
    Returns the number of times the inputted word is found in the word search puzzle.
    
    Inputs:
    - word: a String of the word to search for in the puzzle
    - puzzle: a list of Strings representing a word search puzzle
    
    Outputs:
    - the number of times the word is found in the puzzle
    '''
    result = 0
    
    # Count all words starting from each letter in the puzzle
    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            
            # Check all possible directions
            for row_change in range(-1, 2):
                for col_change in range(-1, 2):
                    
                    if not(row_change == 0 and col_change == 0) and is_word_in_direction((col_change, row_change), (col, row), word, puzzle):
                        result += 1
    
    return result

def is_word_in_direction(direction, coordinate, word, puzzle):
    '''
    Checks if a given word appears in the puzzle at the given coordinate when going in the provided direction.

    Inputs:
    - direction: an Integer tuple of the form (col_change, row_change) where col_change is the change in columns and 
    row_change is the change in rows when heading in this direction
    - coordinate: an Integer tuple representing the starting coordinate of the form (col, row)
    - word: a String of the word to search for in the puzzle
    - puzzle: a list of Strings representing a word search puzzle

    Outputs: 
    - a Boolean representing if the word existed in the provided direction from the given coordinate in the puzzle.
    '''
    (col, row) = coordinate
    if word == "":
        return True
    elif row < 0 or row >= len(puzzle) or col < 0 or col >= len(puzzle[row]) or puzzle[row][col] != word[0]:
        return False
    else:
        (col_change, row_change) = direction
        return is_word_in_direction(direction, (col + col_change, row + row_change), word[1:], puzzle)
    
def x_mas_search(puzzle):
    '''
    Counts how many times X-MAS appears in the puzzle, where X-MAS is two MAS words on the diagonals that share the "A"
    and form a cross.

    Inputs:
    - puzzle: a list of Strings representing a word search puzzle

    Outputs: how many times X-MAS appears in the puzzle
    '''
    result = 0
    for row in range(1, len(puzzle) - 1):
        for col in range(1, len(puzzle[row]) - 1):
            if puzzle[row][col] == "A":
                if (((puzzle[row-1][col-1] == "M" and puzzle[row+1][col+1] == "S") or 
                     (puzzle[row-1][col-1] == "S" and puzzle[row+1][col+1] == "M")) and
                    ((puzzle[row-1][col+1] == "M" and puzzle[row+1][col-1] == "S") or
                     (puzzle[row-1][col+1] == "S" and puzzle[row+1][col-1] == "M"))):
                    result += 1

    return result
    
f = open("inputs/day04.txt", "r")
puzzle = []
for line in f:
    puzzle.append(line)

print("XMAS Word Search: " + str(word_search("XMAS", puzzle)))
print("X-MAS Word Search: " + str(x_mas_search(puzzle)))