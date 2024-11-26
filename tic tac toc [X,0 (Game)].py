def sum(a, b, c):
    return a + b + c

def printBoard(xState, yState):
    zero = 'x' if xState[0] else ('O' if yState[0] else ' ')
    one = 'x' if xState[1] else ('O' if yState[1] else ' ')
    two = 'x' if xState[2] else ('O' if yState[2] else ' ')
    three = 'x' if xState[3] else ('O' if yState[3] else ' ')
    four = 'x' if xState[4] else ('O' if yState[4] else ' ')
    five = 'x' if xState[5] else ('O' if yState[5] else ' ')
    six = 'x' if xState[6] else ('O' if yState[6] else ' ')
    seven = 'x' if xState[7] else ('O' if yState[7] else ' ')
    eight = 'x' if xState[8] else ('O' if yState[8] else ' ')
    
    print(f"{zero} | {one} | {two}")
    print("---------")
    print(f"{three} | {four} | {five}")
    print("---------")
    print(f"{six} | {seven} | {eight}")

def checkwin(xState, yState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("X Won the match")
            return 1
        if sum(yState[win[0]], yState[win[1]], yState[win[2]]) == 3:
            print("O Won the match")
            return 0
    
    return -1

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    yState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  
    
    print("Welcome to TIC TAC TOE")
    
    while True:
        printBoard(xState, yState)
        
        if turn == 1:
            print("X's Chance")
            value = int(input("Please enter a value: "))
            xState[value] = 1
        else:
            print("O's Chance")
            value = int(input("Please enter the value: "))
            yState[value] = 1
        
        cwin = checkwin(xState, yState)
        
        if cwin != -1:
            print("Match Over")
            break
        
        turn = 1 - turn