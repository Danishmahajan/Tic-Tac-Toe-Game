print("\n ****** TIC TAC TOE GAME *******")
#Importing Libraries
theboard = {'1':" ",'2':" ",'3':" ",'4':" ",'5':" ",'6':" ",'7':" ",'8':" ",'9':" "}

#USER DEFINED FUNCTIONS
def printBoard(board):
    print(board['7']+' | '+ board['8']+' | '+board['9'])
    print('- + - + -')
    print(board['4']+' | '+ board['5']+' | '+board['6'])
    print('- + - + -')
    print(board['1']+' | '+ board['2']+' | '+board['3'])


def playGame():
    player1 = input("\nEnter First Player Name : ")
    player2 = input("\nEnter Second Player Name : ")

    print(player1+':X'+" "+player2 +' :O')
    turn="X"
    count=0
    player = player1
    
    while True:
        printBoard(theboard)
        if count==9:
            print('The Game Ends In a draw')
            break
        if player == player1:
            move = input("Enter Your Move {}:".format(player1))
        else:
            move = input("Enter Your Move {}:".format(player2))

        if move not in theboard.keys():
            print("Invalid Move")
            continue

        if theboard[move]==" ":
            theboard[move]=turn

            #CHECKING FOR WINNER
            winner= checkWin(turn)
            if winner!='':
                printBoard(theboard)
                print("\n Congratulation The winner is ",player )
                
                break
            else:
                count+=1
                if turn=="X":
                    turn="O"
                    player= player2
                else:
                    turn="X"
                    player=player1
        else:
            print("Sorry! This Place Is already Filled ")
            # continue


def checkWin(turn):
    winner= ""
    
    #CHECKING FOR ROWS
    if((theboard['7']==theboard['8']==theboard['9']==turn)or (theboard['4']==theboard['5']==theboard['6']==turn)or(theboard['1']==theboard['2']==theboard['3']==turn)):
        winner = turn
    
    #CHECKING FOR COLUMNS
    if((theboard['7']==theboard['4']==theboard['1']==turn)or(theboard['8']==theboard['5']==theboard['2']==turn)or(theboard['9']==theboard['6']==theboard['3']==turn)):
        winner = turn
    #CHECEKING FOR DIAGONAL
    if((theboard['7']==theboard['5']==theboard['3']==turn)or(theboard['1']==theboard['5']==theboard['9']==turn)):
        winner=turn
    return winner
def Restart():
    again=input("\nDo  You Want Want To Play Again? (Y/N)")
    if again=="y":
        global theboard
        for i,v in theboard.items():
            theboard[i] = " "

        main()
    elif again=="n":
        print("\n *** Thanks For Playing ***")
    else:
        Restart()

def main():
    playGame()
    Restart()

#MAIN LOOP
if __name__== "__main__":
    main()
    Restart()