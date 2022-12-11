from string import ascii_lowercase, ascii_uppercase
with open('input_day_three.txt', 'r') as input_file:
    input = input_file.readlines()
list(ascii_lowercase)
list(ascii_uppercase)

priority_mapping = {letter: value for letter, value in zip(list(ascii_lowercase), list(range(1, 27)))}
priority_mapping.update({letter: value for letter, value in zip(list(ascii_uppercase), list(range(27, 53)))})
priority_mapping.update({None: 0})

rucksacks = [sack.strip('\n') for sack in input]
error_items = []
for sack in rucksacks:
    sack_lenght_half = int(len(sack) / 2)
    error_items.extend(list(set(sack[: sack_lenght_half]) & set(sack[sack_lenght_half:])))

error_sum = sum([priority_mapping[error_item] for error_item in error_items])
print(error_sum)


# ************************* Second part ******************************
badges = []
import more_itertools
elf_groups = list(more_itertools.chunked(rucksacks, 3))
for group in elf_groups:
    first_elf = set(group[0])
    second_elf = set(group[1])
    third_elf = set(group[2])
    badges.append(list(first_elf & second_elf & third_elf))

group_sums = sum([priority_mapping[badge[0]] for badge in badges])
print(group_sums)