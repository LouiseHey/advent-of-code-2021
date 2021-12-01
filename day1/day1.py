filename = "day1.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    
numbers = [int(i) for i in lines]

increased = 0
decreased = 0
same = 0

for index in range(len(numbers) - 1):
    if numbers[index + 1] > numbers[index]:
        increased += 1
    elif numbers[index + 1] < numbers[index]:
        decreased += 1
    else:
        same += 1
        
print("increaded: " + str(increased))
print("decreased: " + str(decreased))
print("same: " + str(same))