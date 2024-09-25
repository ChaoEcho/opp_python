from grid import Grid


class Sudoku:
    def __init__(self, input_str):
        self.grid = Grid(input_str)

    def get_grid(self):
        return self.grid

    def set_grid(self, grid):
        self.grid = grid

    def solve(self):
        for row in range(Grid.GRID_SIZE):
            for col in range(Grid.GRID_SIZE):
                if self.grid.get_row(row)[col] == 0:
                    for num in range(1, Grid.GRID_SIZE + 1):
                        if self.is_valid(row, col, num):
                            self.grid.get_row(row)[col] = num
                            if self.solve():
                                return True
                            self.grid.get_row(row)[col] = 0
                    return False
        return True

    def is_valid(self, row, col, num):
        # 检查行
        if num in self.grid.get_row(row):
            return False
        # 检查列
        if num in self.grid.get_column(col):
            return False
        # 检查3x3小格
        if num in self.grid.get_box(row, col):
            return False
        return True

    def print(self):
        self.grid.print_grid()

    def clone(self):
        new_sudoku = Sudoku('')
        new_sudoku.set_grid(self.grid.clone())
        return new_sudoku

    def __eq__(self, other):
        if isinstance(other, Sudoku):
            return self.grid == other.grid
        return False

    def __hash__(self):
        return hash(self.grid)
