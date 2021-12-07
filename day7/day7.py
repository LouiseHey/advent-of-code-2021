def read_in_file(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        
        numbers = lines[0].split(",")
        numbers = [int(i) for i in numbers]
    
    return numbers


def calculate_fuel_cost(positions):
    costs = {}
    
    for possiblePosition in range(max(positions)):
        fuelCount = 0
        for crabPosition in positions:
            fuelCount += abs(crabPosition - possiblePosition)
        costs[possiblePosition] = fuelCount
        
    return min(costs.values())


if __name__ == "__main__":
    input = read_in_file("day7.txt")
    fuelCost = calculate_fuel_cost(input)
    print(fuelCost)