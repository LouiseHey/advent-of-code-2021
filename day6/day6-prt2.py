def read_in_file(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        
        numbers = lines[0].split(",")
        numbers = [int(i) for i in numbers]
    
    return numbers


def calculate_lanternfish_no(lanternfishdict, days):
    if days > 0:
        newfishdict = {k: 0 for k in range(9)}
        for key in lanternfishdict:
            if key == 0:
                newfishdict[6] += lanternfishdict[key]
                newfishdict[8] += lanternfishdict[key]
            else:
                newfishdict[key - 1] += lanternfishdict[key]
        return calculate_lanternfish_no(newfishdict, days - 1)
        
    return(sum(lanternfishdict.values()))

        
def get_fish_dict(lanternfish):
    fishdict = {}
    for i in range(9):
        fishdict[i] = lanternfish.count(i)
    return fishdict
        

if __name__ == "__main__":
    input = read_in_file("day6.txt")
    fishdict = get_fish_dict(input)
    number = calculate_lanternfish_no(fishdict, 256)
    print(number)