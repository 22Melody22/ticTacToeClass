# Tic Tac Toe
import random

def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Does ' + whoGoesFirst() + ' want to be X or O?')
        letter = input().upper()

    # the first element in the tuple is the player's letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'player 2'
    else:
        return 'player 1'

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '


def getPlayerMove(self, board):
    # Let the player type in his move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is ' + self.turn + '\'s next move? (1-9)')
        move = input()
    return int(move)

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

def resetBoard(self):
    self.theBoard = [' '] * 10
    self.player1Letter, self.player2Letter = inputPlayerLetter()
    self.turn = whoGoesFirst()
    print('The ' + self.turn + ' will go first.')
    self.gameIsPlaying = True

def player1Turn(self):
    move = getPlayerMove(self, self.theBoard)
    makeMove(self.theBoard, self.player1Letter, move)

    if isWinner(self.theBoard, self.player1Letter):
        drawBoard(self.theBoard)
        print('Hooray! Player 1 have won the game!')
        self.gameIsPlaying = False
    else:
        if isBoardFull(self.theBoard):
            drawBoard(self.theBoard)
            print('The game is a tie!')
            self.gameIsPlaying = False
        else:
            self.turn = 'player 2'

def player2Turn(self):
    move = getPlayerMove(self, self.theBoard)
    makeMove(self.theBoard, self.player2Letter, move)

    if isWinner(self.theBoard, self.player2Letter):
        drawBoard(self.theBoard)
        print('Yay! Player 2 won!')
        self.gameIsPlaying = False
    else:
        if isBoardFull(self.theBoard):
            drawBoard(self.theBoard)
            print('The game is a tie!')
            self.gameIsPlaying = False
        else:
            self.turn = 'player 1'

def playOneGame(self):
    while self.gameIsPlaying:
        drawBoard(self.theBoard)
        if self.turn == 'player 1':
            # Player 1's turn
            player1Turn(self)
        else:
            # Player 2's turn
            player2Turn(self)

class TicTacToe:
    def __init__(self):
        print("Class initialized")

    def run(self):
        print("Game start!")
        while True:
            # Reset the board
            resetBoard(self)

            # Play one game
            playOneGame(self)

            if not playAgain():
                break
        print("Game over.")

if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")
    TicTacToe().run()