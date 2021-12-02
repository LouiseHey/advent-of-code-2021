def read_in_file(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        lines = [line.split(" ") for line in lines]
        
    return lines

def calculate_position(input):
    horPosition = 0
    verPosition = 0
    
    horMovement = {"forward": 1}
    verMovement = {"down": 1, "up": -1}
    
    for instruction in input:
        direction = instruction[0]
        increment = int(instruction[1])
        
        if direction in horMovement:
            horPosition += increment * horMovement[direction]
        elif direction in verMovement:
            verPosition += increment * verMovement[direction]
            
    return horPosition, verPosition


if __name__ == "__main__":
    input = read_in_file("day2.txt")
    hor, ver = calculate_position(input)
    print(hor * ver)