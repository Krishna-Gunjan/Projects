import os

class Tic_Tac_Toe:
    def __init__(self):
        self.board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.move_number = 1
        for i in self.board:
                    print('|'.join(map(str, i)))


    def get_move(self):
        self.possible_moves = [i for i in range(1, 10)]
        while True:
            try:
                if self.move_number % 2 == 0:
                    print("It is the \"O\" player's turn.")
                else:
                    print("It is the \"X\" player's turn.")
                if not self.possible_moves:
                    print("It's a tie!")
                    return  
    
                self.move = int(input("Enter the index value of the square to place your mark: "))
                if 1 <= self.move <= 9:
                    if self.move in self.possible_moves:
                        self.possible_moves.pop(self.move - 1)
                        break
                os.system('cls')
                print("Invalid Input! Please try again.")
            except ValueError:
                os.system('cls')
                print("Invalid Input! Please try again.")
        play.update_move()


    def update_move(self):
        row = (self.move - 1)//3 
        coloumn = (self.move - 1)%3

        if self.move_number%2 == 0:
            self.board[row][coloumn] = 'O'
        else:
            self.board[row][coloumn] = 'X'
        os.system('cls')
        for i in self.board:
            print('|'.join(map(str, i)))
        self.move_number += 1

        play.check()
    
    def check(self):
        self.values = ['X', 'O']
        rows = len(self.board)
        cols = len(self.board[0]) if rows > 0 else 0
        for i in range(rows):
            for j in range(cols):
                for value in self.values:
                    if self.board[i][j] == value:
                        if j + 2 < cols and all(self.board[i][j + k] == value for k in range(3)):
                            self.declare_winner(value)
                            return
                        if i + 2 < rows and all(self.board[i + k][j] == value for k in range(3)):
                            self.declare_winner(value)
                            return
                        if i + 2 < rows and j + 2 < cols and all(self.board[i + k][j + k] == value for k in range(3)):
                            self.declare_winner(value)
                            return
                        if i + 2 < rows and j - 2 >= 0 and all(self.board[i + k][j - k] == value for k in range(3)):
                            self.declare_winner(value)
                            return
    
        if self.move_number > 9:
            print("It's a tie!")
            return
    
        play.get_move()

def declare_winner(self, value):
    if value == 'X':
        print("\"X\" Wins!")
    else:
        print("\"O\" Wins!")
    exit()

        
        

if __name__ == '__main__':
    play = Tic_Tac_Toe()
    play.get_move()