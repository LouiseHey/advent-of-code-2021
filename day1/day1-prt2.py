filename = "day1.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    
numbers = [int(i) for i in lines]

## calculate sums
sums = []

for index in range(len(numbers) - 2):
    sums.append(numbers[index] + numbers[index + 1] + numbers[index + 2])
    

increased = 0
decreased = 0
same = 0

for index in range(len(sums) - 1):
    if sums[index + 1] > sums[index]:
        increased += 1
    elif sums[index + 1] < sums[index]:
        decreased += 1
    else:
        same += 1
        
print("increased: " + str(increased))
print("decreased: " + str(decreased))
print("same: " + str(same))