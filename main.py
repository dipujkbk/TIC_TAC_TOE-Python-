def printBoard(xState, zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    


    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")


def sum(a, b, c):
    return a+b+c

def checkWin(xState, zState):
    wins = [[0,1,2], [3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8], [2,4,6]]
    for w in wins:
        if(sum(xState[w[0]], xState[w[1]], xState[w[2]]) == 3):
            print("X wins the game. ")
            return 1

        if(sum(zState[w[0]], zState[w[1]], zState[w[2]]) == 3):
            print("O wins the game. ")
            return 0
    return -1


if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0 ,0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0 ,0, 0]
    turn = 1 #1 for x and 0 for O
    print("Welcome To Tic Tac Toe")
    cnt = 0
    while(cnt < 9):
        printBoard(xState, zState)
        if(turn == 1):
            print("X's Chance")
            value = int(input("Please enter the position: "))
            xState[value] = 1
        else:
            print("O's Chance")
            value = int(input("Please enter the position: "))
            zState[value] = 1

        cnt +=1
        cwin = checkWin(xState, zState)
        if(cwin != -1 or cnt == 9):
            printBoard(xState,zState)
            print("Match Over")
            break

        
        turn  = 1-turn  #to change turn value
        

    
    