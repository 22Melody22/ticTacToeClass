# Tic Tac Toe
import random

class Board:
    def __init__(self):
        print("Board initialized")
        self.board = [' '] * 10

    def drawBoard(self):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')

    def isSpaceFree(self, move):
        # Return true if the passed move is free on the passed board.
        return self.board[move] == ' '

    def makeMove(self, move, letter):
        self.board[move] = letter

    def isBoardFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(i):
                return False
        return True

    def isWinner(self, letter):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((self.board[7] == letter and self.board[8] == letter and self.board[9] == letter) or # across the top
        (self.board[4] == letter and self.board[5] == letter and self.board[6] == letter) or # across the middle
        (self.board[1] == letter and self.board[2] == letter and self.board[3] == letter) or # across the bottom
        (self.board[7] == letter and self.board[4] == letter and self.board[1] == letter) or # down the left side
        (self.board[8] == letter and self.board[5] == letter and self.board[2] == letter) or # down the middle
        (self.board[9] == letter and self.board[6] == letter and self.board[3] == letter) or # down the right side
        (self.board[7] == letter and self.board[5] == letter and self.board[3] == letter) or # diagonal
        (self.board[9] == letter and self.board[5] == letter and self.board[1] == letter)) # diagonal


class Player:
    def __init__(self, letter, name):
        self.playerName = name
        self.letter = letter

    def getPlayerMove(self, board):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not board.isSpaceFree(int(move)):
            print('What is ' + self.playerName + '\'s next move? (1-9)')
            move = input()
        return int(move)

    def playerTurn(self, board):
        move = self.getPlayerMove(board)
        board.makeMove(move, self.letter)

        if board.isWinner(self.letter):
            board.drawBoard()
            print('Hooray! ' + self.playerName + ' has won the game!')
            return False
        else:
            if board.isBoardFull():
                board.drawBoard()
                print('The game is a tie!')
                return False
            else:
                return True

class TicTacToe:
    def __init__(self):
        print("Class initialized")

    def resetGame(self):
        self.theBoard = Board()
        self.turn = self.whoGoesFirst()
        print('The ' + self.turn + ' will go first.')
        self.player1Letter, self.player2Letter = self.inputPlayerLetter()
        self.player1 = Player(self.player1Letter, 'player 1')
        self.player2 = Player(self.player2Letter, 'player 2')
        self.gameIsPlaying = True

    def whoGoesFirst(self):
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return 'player 2'
        else:
            return 'player 1'

    def inputPlayerLetter(self):
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Does ' + self.turn + ' want to be X or O?')
            letter = input().upper()

        # the first element in the tuple is the player's letter, the second is the computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def playOneGame(self):
        while self.gameIsPlaying:
            self.theBoard.drawBoard()
            if self.turn == 'player 1':
                # Player 1's turn
                if self.player1.playerTurn(self.theBoard):
                    self.turn = 'player 2'
                else:
                    self.gameIsPlaying = False
            else:
                # Player 2's turn
                if self.player2.playerTurn(self.theBoard):
                    self.turn = 'player 1'
                else:
                    self.gameIsPlaying = False

    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    def run(self):
        print("Game start!")
        while True:
            # Reset the board
            self.resetGame()

            # Play one game
            self.playOneGame()

            if not self.playAgain():
                break
        print("Game over.")

if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")
    TicTacToe().run()