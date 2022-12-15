from collections import Counter

with open("input_day_six.txt") as input_file:
    input = input_file.read()


def find_marker(signal: str, marker_length):
    for indx in range(len(signal)):
        sample = set(Counter(signal[indx: indx + marker_length]).values())
        if len(sample) == 1 and 1 in sample:
            print("Marker found at: " , indx + marker_length)
            return indx + marker_length
        else:
            continue

signal_first_marker = find_marker(input, 4)

# *************** Part 2 ***************

signal_first_marker_part_two = find_marker(input, 14)