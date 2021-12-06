def read_in_file(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        lines = [line.split(" -> ") for line in lines]
        
        finalInput = []
        for line in lines:
            finalPair = []
            for pair in line:
                pair = pair.split(",")
                pair = [int(i) for i in pair]
                finalPair.append(pair)
            finalInput.append(finalPair)
    return finalInput


def calculate_danger_points(input):
    overlap = {}
    
    for line in input:
        x1 = line[0][0]
        y1 = line[0][1]
        x2 = line[1][0]
        y2 = line[1][1]
        
        ymin = min(y1, y2)
        ymax = max(y1, y2)
        xmin = min(x1, x2)
        xmax = max(x1, x2)
            
        
        if x1 == x2:
            while ymin <= ymax:
                coord = (x1, ymin)
                if coord in overlap:
                    overlap[coord] += 1
                else:
                    overlap[coord] = 1
                ymin += 1
                
        elif y1 == y2:
            while xmin <= xmax:
                coord = (xmin, y1)
                if coord in overlap:
                    overlap[coord] += 1
                else:
                    overlap[coord] = 1
                xmin += 1

        else:
            if x1 > x2 and y1 > y2:
                while x1 >= x2 and y1 >= y2:
                    coord = (x1, y1)
                    if coord in overlap:
                        overlap[coord] += 1
                    else:
                        overlap[coord] = 1
                    x1 -= 1
                    y1 -= 1
            elif x1 > x2 and y1 < y2:
                while x1 >= x2 and y1 <= y2:
                    coord = (x1, y1)
                    if coord in overlap:
                        overlap[coord] += 1
                    else:
                        overlap[coord] = 1
                    x1 -= 1
                    y1 += 1
            elif x1 < x2 and y1 > y2:
                while x1 <= x2 and y1 >= y2:
                    coord = (x1, y1)
                    if coord in overlap:
                        overlap[coord] += 1
                    else:
                        overlap[coord] = 1
                    x1 += 1
                    y1 -= 1
            elif x1 < x2 and y1 < y2:
                while x1 <= x2 and y1 <= y2:
                    coord = (x1, y1)
                    if coord in overlap:
                        overlap[coord] += 1
                    else:
                        overlap[coord] = 1
                    x1 += 1
                    y1 += 1
            
    
    count = 0
    for point in overlap:
        if overlap[point] > 1:
            count +=1
                
    return count


if __name__ == "__main__":
    input = read_in_file("day5.txt")
    count = calculate_danger_points(input)
    print(count)