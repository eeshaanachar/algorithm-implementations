class NQueens:

    def __init__(self, n):
        self.N = n
        self.board = [['.' for _ in range(n)] for __ in range(n)]
        

    def show_board(self):
        print()
        for row in self.board:
            for element in row:
                print(element, end=' ')
            print()
        print()


    def is_valid(self, row_index, col_index):

        if 'Q' in self.board[row_index]:
            return False

        if 'Q' in (row[col_index] for row in self.board):
            return False

        i = max(0, row_index - col_index)
        j = max(0, col_index - row_index)
        diagonals = []
        while i < self.N and j < self.N:
            diagonals.append(self.board[i][j])
            i, j = i + 1, j + 1
        j = min(self.N - 1, col_index + row_index)
        i = row_index - j + col_index
        while i < self.N and j >= 0:
            diagonals.append(self.board[i][j])
            i, j = i + 1, j - 1

        return 'Q' not in diagonals


    def solve(self, n, row_index = 0, col_index = 0):

        if row_index == self.N:
            return self.N == n
        if col_index == self.N:
            return self.solve(n, row_index + 1, 0)
        
        if self.is_valid(row_index, col_index):
            self.board[row_index][col_index] = 'Q'
            if self.solve(n + 1, row_index, col_index + 1):
                return True

        self.board[row_index][col_index] = '.'
        return self.solve(n, row_index, col_index + 1)


obj = NQueens(15)
obj.solve(0)
obj.show_board()