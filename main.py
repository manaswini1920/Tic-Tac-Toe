# printing board
# take user input
# check win
# switch player
# check win or tie

from win_loss_check import checkWin

class TicTacToe:
    def __init__(self):
        self.board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        self.game_running = True
        self.winner = None
        self.current_player = 'X'

    def checkTie(self):
        if '-' not in self.board:
            self.game_running = False
            print('tie')

    def print_board(self):
        print(self.board[0] + '|' + self.board[1] + '|' + self.board[2])
        print(self.board[3] + '|' + self.board[4] + '|' + self.board[5])
        print(self.board[6] + '|' + self.board[7] + '|' + self.board[8])

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def user_input(self, board):
        inp = int(input('enter number from 1-9 for player : '+self.current_player))
        if 1 <= inp <= 9 and self.board[inp - 1] == '-':
            self.board[inp - 1] = self.current_player
        else:
            print('entered position is already filled')
        checkWin(self.board)
        self.checkTie(self.board)
        self.switch_player()

    def run_game(self):
        while self.game_running:
            self.print_board(self.board)
            self.user_input(self.board)



tc = TicTacToe()
tc.run_game()
