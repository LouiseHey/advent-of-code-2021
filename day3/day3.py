def read_in_file(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        lines = [list(line) for line in lines]
    return lines

def calculate_rates(input):
    gammaList = []
    epsilonList = []
    
    digitCount = len(input[0])
    count = 0
    
    for index in range(digitCount):
        for binaryNo in input:
            if binaryNo[index] == '1':
                count += 1
            else:
                count -= 1

        if count > 0:
            gammaList.append(1)
            epsilonList.append(0)
        elif count < 0:
            gammaList.append(0)
            epsilonList.append(1)
        
        count = 0
    
    return convert_binary(gammaList), convert_binary(epsilonList)
    
def convert_binary(binary):
    binary.reverse()
    total = 0
    
    for index, bit in enumerate(binary):
        total += bit * 2 ** index
        
    return total
        
        
if __name__ == "__main__":
    input = read_in_file("day3.txt")
    epsilon, gamma = calculate_rates(input)
    print(epsilon * gamma)