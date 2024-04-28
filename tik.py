import tkinter as tk
import tkinter.messagebox as messagebox
import random

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("300x300")
        self.board = [' ']*9
        self.current_player = 'X'
        self.create_widgets()

    def create_widgets(self):
        self.buttons = []
        for i in range(9):
            row = i // 3
            col = i % 3
            button = tk.Button(self, text="", font=('Helvetica', 20), width=4, height=2,
                               command=lambda idx=i: self.make_move(idx))
            button.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(button)

    def make_move(self, idx):
        if self.board[idx] == ' ':
            self.board[idx] = self.current_player
            self.buttons[idx].config(text=self.current_player)
            if self.check_win(self.current_player):
                messagebox.showinfo("Game Over", f"{self.current_player} wins!")
                self.reset_board()
            elif self.check_tie():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                if self.current_player == 'O':
                    self.make_ai_move()

    def make_ai_move(self):
        available_moves = [pos for pos in range(9) if self.board[pos] == ' ']
        move = random.choice(available_moves)
        self.make_move(move)

    def check_win(self, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]               # diagonals
        ]
        for condition in win_conditions:
            if all(self.board[pos] == player for pos in condition):
                return True
        return False

    def check_tie(self):
        return all(cell != ' ' for cell in self.board)

    def reset_board(self):
        self.board = [' ']*9
        for button in self.buttons:
            button.config(text="")
        self.current_player = 'X'

if __name__ == "__main__":
    app = TicTacToe()
    app.mainloop()
