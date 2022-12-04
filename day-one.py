with open('input_day_one.txt', 'r') as input_file:
    input = input_file.readlines()
    
calories_aggregated = []
calories = [calorie.strip('\n') for calorie in input]
counter = 0
for indx, calorie in enumerate(calories):
    if calorie == '':
        sum_list = calories[counter: indx]
        calories_aggregated.append(sum([int(calorie_to_be_sum) for calorie_to_be_sum in sum_list]))
        counter = indx + 1
    else: 
        continue

# Elf with most calories (Work out is highly recommended to this fella!)
print(max(calories_aggregated))


calories_sorted = sorted(calories_aggregated, reverse=True)
top_3_calorie_intakers_sum = sum(calories_sorted[0:3])

# Top calorie intakers
print(top_3_calorie_intakers_sum)