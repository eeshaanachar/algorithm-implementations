class Sudoku:
    RANGE = 9
    SUBGRID_SIZE = 3


    def __init__(self, board):
        self.board = board


    def view_board(self):
        print()
        for row in self.board:
            for number in row:
                print(number, end="\t")
            print()
        print()


    def is_valid(self, row_index, col_index):

        row = self.board[row_index]
        if row.count(self.board[row_index][col_index]) > 1:
            return False
        
        column = [row[col_index] for row in self.board]
        if column.count(self.board[row_index][col_index]) > 1:
            return False

        row_range = range(row_index % Sudoku.SUBGRID_SIZE * Sudoku.SUBGRID_SIZE, row_index % Sudoku.SUBGRID_SIZE * Sudoku.SUBGRID_SIZE + 3)
        col_range = range(col_index % Sudoku.SUBGRID_SIZE * Sudoku.SUBGRID_SIZE, col_index % Sudoku.SUBGRID_SIZE * Sudoku.SUBGRID_SIZE + 3)
        subgrid = [self.board[i][j] for i in row_range for j in col_range]
        if subgrid.count(self.board[row_index][col_index]) > 1:
            return False

        return True


    def solve(self, i = 0, j = 0):

        if i == Sudoku.RANGE:
            return True
        if j == Sudoku.RANGE:
            return self.solve(i + 1)
        if self.board[i][j] != 0:
            return self.solve(i, j + 1)

        for number in range(1, Sudoku.RANGE + 1):
            self.board[i][j] = number
            if self.is_valid(i, j) and self.solve(i, j + 1):
                return True
        self.board[i][j] = 0
        return False


board1 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
    
]

sudoku = Sudoku(board1)
if sudoku.solve():
    sudoku.view_board()
else:
    print("Unsolvable!")