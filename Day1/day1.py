input = open("calories.txt")
calories  = input.read().split("\n\n")
calorieData =  [calorie.split("\n") for calorie in calories]
totalCalories = [sum([(int(calorie)) for calorie in calorieDataSet]) for calorieDataSet in calorieData]
totalCalories.sort()

print("Part 1: " + totalCalories[-1])
print("Part 2: " + totalCalories[-1] + totalCalories[-2] +  totalCalories[-3])
