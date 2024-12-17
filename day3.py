def sum_mul_results_of_all_lines(lines):
    '''
    Sums the result of the multiplication commands from all lines.

    Inputs:
    - lines: a list of Strings

    Outputs:
    - the sum of all multiplication commands in lines
    '''
    result = 0
    for line in lines:
        result += parse_muls(line)
    return result

def parse_muls(line):
    '''
    Parses all multiplying commands and sums the results. A valid mul command takes the form "mul(X,Y)" where X and Y 
    are 1-3 digit numbers.
    
    Inputs:
    - line: a String containing mul commands

    Outputs:
    - the sum of all valid mul commands
    '''
    result = 0
    pointer = 0
    shortest_mul_command = "mul(x,y)"
    while pointer < len(line) - len(shortest_mul_command):
        if line[pointer:pointer+4] == "mul(":
            pointer += len("mul(")
            x = parse_one_to_three_digit_number(line[pointer:pointer+3])
            if x != "":
                pointer += len(x)
                if line[pointer] == ",":
                    pointer += len(",")
                    y = parse_one_to_three_digit_number(line[pointer:pointer+3])
                    if y != "":
                        pointer += len(y)
                        if line[pointer] == ")":
                            pointer += len(")")
                            result += int(x) * int(y)
        else:
            pointer += 1
    return result

def parse_one_to_three_digit_number(s):
    '''
    Parses a one to three digit number from String s, reading from the beginning of the String only.

    Inputs:
    - s: a String representation of a one to three digit number

    Outputs:
    - the String representation of the 1 to 3 digit number.
    '''
    number = ""
    for char in s:
        if char.isdigit():
            number += char
        else:
            break
    return number

f = open("day3.txt", "r")

print("Sum of mul commands: " + str(sum_mul_results_of_all_lines(f)))