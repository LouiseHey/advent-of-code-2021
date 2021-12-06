def read_in_file(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        
        numbers = lines[0].split(",")
        numbers = [int(i) for i in numbers]
    
    return numbers


def calculate_lanternfish_no(lanternfish, days):
    if days > 0:
        newLanternfish = []
        for state in lanternfish:
            if state > 0:
                newLanternfish.append(state - 1)
            if state == 0:
                newLanternfish.append(6)
                newLanternfish.append(8)
        return calculate_lanternfish_no(newLanternfish, days - 1)
    if days == 0:
        return len(lanternfish)
                


if __name__ == "__main__":
    input = read_in_file("day6.txt")
    number = calculate_lanternfish_no(input, 80)
    print(number)