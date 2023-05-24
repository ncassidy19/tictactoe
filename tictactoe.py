class tictactoe:
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]

    currentPlayer = "X"
    winner = None
    gameRunning = True

    def printBoard(board):
        print(board[0] + "|" + board[1] + "|" + board[2])
        print(board[3] + "|" + board[4] + "|" + board[5])
        print(board[6] + "|" + board[7] + "|" + board[8])

    def playerInput(board):
        input1 = int(input("Enter a number (1-9)"))
        if 1 <= input1 <= 9:
            board[input1 - 1] = currentPlayer
        else:
            print("Pick another position")

    def checkHorizontal(board):
        global winner
        if board[0] == board[1] == board[2]:
            winner = board[0]
            return True
        elif board[3] == board[4] == board[5]:
            winner = board[3]
            return True
        elif board[6] == board[7] == board[8]:
            winner = board[6]
            return True

    def checkVertical(board):
        global winner
        if board[0] == board[3] == board[6]:
            winner = board[0]
            return True
        elif board[1] == board[4] == board[7]:
            winner = board[1]
            return True
        elif board[2] == board[5] == board[8]:
            winner = board[2]
            return True

    def checkDiagonal(board):
        global winner
        if board[0] == board[4] == board[8]:
            winner = board[0]
            return True
        elif board[2] == board[4] == board[6]:
            winner = board[2]
            return True

    def checkTie(board):
        global gameRunning
        if "-" not in board:
            printBoard(board)
            print("It's a tie")
            gameRunning = False

    def checkWin():
        if checkHorizontal(board) or checkVertical(board) or checkDiagonal(board):
            print(f"The winner is {winner}")

    def switchPlayer():
        global currentPlayer
        if currentPlayer == "X":
            currentPlayer = "O"
        else:
            currentPlayer = "X"

    while gameRunning:
        printBoard(board)
        playerInput(board)
        checkWin()
        checkTie(board)
        switchPlayer()
