from pandas import DataFrame
from typing import List, Dict
from collections import deque

with open('input_day_five.txt') as input_file:
    input = input_file.readlines()


cargo_stack = {
    '1': deque(['B', 'S', 'V', 'Z', 'G', 'P', 'W']),
    '2': deque(['J', 'V', 'B', 'C', 'Z', 'F']),
    '3': deque(['V', 'L', 'M', 'H', 'N', 'Z', 'D', 'C']),
    '4': deque(['L', 'D', 'M', 'Z', 'P', 'F', 'J', 'B']),
    '5': deque(['V', 'F', 'C', 'G', 'J', 'B', 'Q', 'H']),
    '6': deque(['G', 'F', 'Q', 'T', 'S', 'L', 'B']),
    '7': deque(['L', 'G', 'C', 'Z', 'V']),
    '8': deque(['N', 'L', 'G']),
    '9': deque(['J', 'F', 'H', 'C'])
    }


def get_top_crates(cargo_stack: Dict[str, deque]) -> str:
    top_crates = []
    for crate in cargo_stack.values():
        try:
            top_crates.append(crate.pop())
        except IndexError:
            print('Skipping this crate! no crate found')
            continue
    return ''.join(top_crates)

rearrengments = input[10: ]
rearrengments = [command.strip("\n") for command in rearrengments]
moves = []
for command in rearrengments:
    moves_in_command = []
    for move in command.split():
        if move.isnumeric():
            moves_in_command.append(int(move))
    moves.append(moves_in_command)

# *************** Part One ***************

cargo_stack_part_one = cargo_stack.copy()
for command in moves:
    for _ in range(command[0]):
        cargo_stack[str(command[2])].append(cargo_stack_part_one[str(command[1])].pop())

print(get_top_crates(cargo_stack_part_one))

# *************** Part two ***************
cargo_stack_part_two = cargo_stack.copy()
for command in moves:
    movement = []
    for _ in range(command[0]):
        movement.append(cargo_stack_part_two[str(command[1])].pop())
    cargo_stack[str(command[2])].extend(movement[::-1]) 

print(get_top_crates(cargo_stack_part_two))

    