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
                row = [int(num) for num in row]
                board.append(row)
            else:
                boards.append(board)
                board = []
                
    return numbers, boards


def play_bingo(numbers, boards):
    for num in numbers:
        boards = call_number(num, boards)
        winner = check_boards(boards)
        
        if winner != []:
            score = calculate_score(winner, num)
            return score


def call_number(number, boards):
    newBoards = []
    newBoard = []
    
    for board in boards:
        for row in board:
            row = ["X" if i==number else i for i in row]
            newBoard.append(row)
        newBoards.append(newBoard)
        newBoard = []
    return newBoards


def check_boards(boards):
    winningBoards = []
    for board in boards:
        
        for row in board:
            if all(i == "X" for i in row):
                winningBoards.append(board)
                break
            
        transposedBoard = list(zip(*board))
    
        for row in transposedBoard:
            if all(i == "X" for i in row):
                winningBoards.append(board)
                break
    
    winningLength = len(winningBoards)
    
    if winningLength > 1:
        raise error("more than one winning board")
    elif winningLength == 1:
        return winningBoards[0]
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