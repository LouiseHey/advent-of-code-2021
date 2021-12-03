def read_in_file(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        lines = [list(line) for line in lines]
    return lines

def calculate_rates(input):
    oxygenGenerator = input
    coScrubber = input
    
    digitCount = len(input[0])
    
    for index in range(digitCount):
        if len(oxygenGenerator) == 1 and len(coScrubber) == 1:
            break
        
        if len(oxygenGenerator) > 1:
            oxygenCount = get_count(oxygenGenerator, index)
            oxygenGenerator = get_filtered_input(oxygenGenerator, index, oxygenCount, '0', '1')
        
        if len(coScrubber) > 1:
            scrubberCount = get_count(coScrubber, index)
            coScrubber = get_filtered_input(coScrubber, index, scrubberCount, '1', '0')
                
    coScrubberRating = convert_binary([int(i) for i in coScrubber[0]])
    oxygenGeneratorRating = convert_binary([int(i) for i in oxygenGenerator[0]])
            
    return coScrubberRating, oxygenGeneratorRating


def get_count(input, index):
    count = 0
    
    for binaryNo in input:
        if binaryNo[index] == '1':
            count += 1
        else:
            count -= 1
    return count


def get_filtered_input(input, index, count, negCountCondidtion, otherCondition):
    if count < 0:
        input = [num for num in input if num[index] == negCountCondidtion]
    else:
        input = [num for num in input if num[index] == otherCondition]
        
    return input


def convert_binary(binary):
    binary.reverse()
    total = 0
    
    for index, bit in enumerate(binary):
        total += bit * 2 ** index
        
    return total
        
        
if __name__ == "__main__":
    input = read_in_file("day3.txt")
    scrubber, oxygen = calculate_rates(input)
    print(scrubber * oxygen)