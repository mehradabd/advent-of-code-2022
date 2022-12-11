from typing import Tuple, List, Union
with open('input_day_four.txt') as input_file:
    input = input_file.readlines()

section_assignments = [section.strip('\n') for section in input]

def make_pair(pair: str) -> Union[List[int], List[int]]:
    first_elf, second_elf = pair.split(',')[0],  pair.split(',')[1]
    first_assignment = [int(section) for section in first_elf.split('-')]
    second_assignment = [int(section) for section in second_elf.split('-')]

    return first_assignment, second_assignment

def find_fully_overlap(pair: str) -> Tuple[List]:

    first_assignment, second_assignment = make_pair(pair)

    if first_assignment[0] <= second_assignment[0] and first_assignment[1] >= second_assignment[1]:
        return (first_assignment, second_assignment)
    elif second_assignment[0] <= first_assignment[0] and second_assignment[1] >= first_assignment[1]:
       return (first_assignment, second_assignment)
    else:
         return

fully_overlap_pairs = [find_fully_overlap(pair) for pair in section_assignments]
fully_overlap_pairs = [pair for pair in fully_overlap_pairs if pair != None]
print(len(fully_overlap_pairs))


# ****************************** Part 2 ************************************
def find_overlap(pair: str) -> Tuple[List]:

    first_assignment, second_assignment = make_pair(pair) 

    if first_assignment[0] < second_assignment[0] and first_assignment[1] < second_assignment[0]:
        return 
    elif first_assignment[0] > second_assignment[0] and first_assignment[0] > second_assignment[1]:
       return 
    else:
         return (first_assignment, second_assignment)

overlap_pairs = [find_overlap(pair) for pair in section_assignments]
overlap_pairs = [pair for pair in overlap_pairs if pair != None] 
print(overlap_pairs)
    