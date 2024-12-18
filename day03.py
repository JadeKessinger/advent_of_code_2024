def sum_mul_results_of_all_lines(lines, conditionals=False):
    '''
    Sums the result of the multiplication commands from all lines.

    Inputs:
    - lines: a list of Strings
    - conditionals: a boolean flag representing whether or not we are parsing conditional commands. Default is False.

    Outputs:
    - the sum of all multiplication commands from the input.
    '''
    result = 0
    mul_enabled = True
    for line in lines:
        (line_result, mul_enabled) = parse_muls(line, conditionals, mul_enabled)
        result += line_result

    return result

def parse_muls(line, conditionals, mul_enabled):
    '''
    Parses all multiplying commands and sums the results. A valid mul command takes the form "mul(X,Y)" where X and Y 
    are 1-3 digit numbers. Parses conditional flags if conditionals are enabled, which can enable or disable mul 
    commands.
    
    Inputs:
    - line: a String containing mul commands
    - conditionals: a boolean flag representing whether or not we are parsing conditional commands. 
    - mul_enabled: a boolean flag representing if mul is enabled or disabled at the start of this line.

    Outputs:
    - a tuple of the form (result, mul_enabled) where result is the sum of all valid mul commands.
    '''
    result = 0
    pointer = 0
    shortest_command = "mul(x,y)"
    while pointer < len(line) - len(shortest_command):
        if mul_enabled:
            if line[pointer:pointer+len("mul(")] == "mul(":
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
            elif conditionals == True:
                if line[pointer:pointer+len("don't()")] == "don't()":
                    pointer += len("don't()")
                    mul_enabled = False
                else:
                    pointer += 1
            else:
                pointer += 1
        elif conditionals == True:
            if line[pointer:pointer+len("do()")] == "do()":
                pointer += len("do()")
                mul_enabled = True
            else:
                pointer += 1
    return (result, mul_enabled)

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

f = open("inputs/day03.txt", "r")
lines = []
for line in f:
    lines.append(line)

print("Sum of mul commands: " + str(sum_mul_results_of_all_lines(lines)))
print("Sum of mul commands with conditionals: " + str(sum_mul_results_of_all_lines(lines, conditionals=True)))