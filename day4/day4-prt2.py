from os import error


def read_in_file(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        
        numbers = lines.pop(0)
        numbers = numbers.split(",")
        numbers = [int(num) for num in numbers]
        
        lines.pop(0)
        lines = [line.split() for line in lines]
        
        boards = []
        board = []
        
        for row in lines:
            if row != []:
                board.append([int(num) for num in row])
            else:
                boards.append(board)
                board = []
                
    return numbers, boards


def play_bingo(numbers, boards):
    finalWinner = []
    
    for num in numbers:
        if finalWinner == []:
            boards = call_number(num, boards)
            finalWinner = check_boards(boards)
        else:
            finalWinner = call_number(num, [finalWinner])[0]
            complete = check_boards([finalWinner])
            
            if complete == []:
                return calculate_score(finalWinner, num)


def call_number(number, boards):
    newBoards = []
    
    for board in boards:
        newBoard = []
        for row in board:
            row = ["X" if i==number else i for i in row]
            newBoard.append(row)
        newBoards.append(newBoard)
    return newBoards


def check_boards(boards):
    nonWinningBoards = []
    
    for board in boards:
        win = False
        
        for row in board:
            if all(i == "X" for i in row):
                win = True
                break

        transposedBoard = list(zip(*board))
        for row in transposedBoard:
            if all(i == "X" for i in row):
                win = True
                break
            
        if win != True:
            nonWinningBoards.append(board)
                
    nonWinningLength = len(nonWinningBoards)

    if nonWinningLength == 1:
        return nonWinningBoards[0]
    else:
        return []
    
    
def calculate_score(board, winningNum):
    score = 0
    for row in board:
        for i in row:
            if i != "X":
                score += i
    score = winningNum * score
    return score


if __name__ == "__main__":
    numbers, boards = read_in_file("day4.txt")
    score = play_bingo(numbers, boards)
    print(score)