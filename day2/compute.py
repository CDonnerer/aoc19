"""Gravity assist program
"""
import operator

import numpy as np

# Some example inputs used for testing
example_input = [1, 1, 1, 4, 99, 5, 6, 0, 99]
# [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]


def get_operation(opcode):
    if opcode == 1:
        return operator.add
    elif opcode == 2:
        return operator.mul
    else:
        return None


def process_instruction(code, starting_pos=0):
    operation = get_operation(code[starting_pos])
    if operation is None:
        return code

    input1 = code[code[starting_pos + 1]]
    input2 = code[code[starting_pos + 2]]
    output_val = operation(input1, input2)

    code[code[starting_pos + 3]] = output_val

    return code


def process(code):
    opcode = code[0]
    starting_pos = 0

    while opcode != 99:
        code = process_instruction(code, starting_pos)
        starting_pos += 4
        opcode = code[starting_pos]

    return code


def load_input(path="input.dat"):
    return list(np.loadtxt(path, delimiter=",").astype(int))


def main():
    """Load in the masses and Caclculate part one and part two
    """

    for noun in range(0, 99):
        for verb in range(0, 99):
            code = load_input()

            code[1] = noun
            code[2] = verb

            processed_code = process(code)

            if processed_code[0] == 19690720:
                print(f"Processed code: \n{processed_code}")
                print(f"Noun = {noun}, verb = {verb}")
                print(f"Answer: {100 * noun + verb}")


if __name__ == "__main__":
    main()
