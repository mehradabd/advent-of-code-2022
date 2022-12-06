with open('input_day_two.txt', 'r') as input_file:
    input = input_file.readlines()
play_mapping = {'A': 'X', 'B': 'Y', 'C': 'Z'}
play_points = {'X': 1, 'Y': 2, 'Z': 3}
play_mapping_win = {'X': 'Y', 'Y': 'Z', 'Z': 'X'}
play_mapping_lose = {'X': 'Z', 'Y': 'X', 'Z': 'Y'}
rounds = [round.strip() for round in input]
rounds_homogenous = [(play_mapping[p[0]], p[2]) for p in rounds]

def calculate_score(play: tuple) -> int:
    """
    Calculate scores of rounds in shape of tuples (Elf vs Me)
    """
    play_point = play_points[play[1]]
    if play[0] == play[1]:
        return 3 + play_point
    elif play in [('X', 'Y'), ('Y', 'Z'), ('Z', 'X')]:
        return 6 + play_point
    else:
        return play_point

scores = sum([calculate_score(round) for round in rounds_homogenous])
print(scores)
    
def choose_play(play: tuple) -> str:
    """
    Choose play based on guideline
    """
    if play[1] == 'Y':
        return play[0] 
    elif play[1] == 'Z':
        return play_mapping_win[play[0]]
    elif play[1] == 'X':
        return play_mapping_lose[play[0]]

rounds_homogenous_swapped = [(round[0], choose_play(round)) for round in rounds_homogenous]
scores_part_two = sum([calculate_score(round) for round in rounds_homogenous_swapped])
print(scores_part_two)




