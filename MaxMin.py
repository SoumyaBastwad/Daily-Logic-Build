numbers = [10, 25, 5, 30, 15]

maximum = numbers[0]
minimum = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] > maximum:
        maximum = numbers[i]

    if numbers[i] < minimum:
        minimum = numbers[i]

print("Maximum number:", maximum)
print("Minimum number:", minimum)


