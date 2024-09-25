class Grid:
    # 常量，数独的长/宽，固定为9
    GRID_SIZE = 9
    # 常量，3x3小格的长/宽，固定为3
    BOX_SIZE = 3

    def __init__(self, input_str):
        # 1.检查输入字符串长度是否为81
        if len(input_str) != self.GRID_SIZE * self.GRID_SIZE:
            raise ValueError(f"输入字符串长度必须为 {self.GRID_SIZE * self.GRID_SIZE}。")

        self.grid = [[0] * self.GRID_SIZE for _ in range(self.GRID_SIZE)]
        # 2.解析输入字符串到grid数组
        self.parse(input_str)

    def parse(self, input_str):
        for i in range(self.GRID_SIZE * self.GRID_SIZE):
            ch = input_str[i]
            # 检查输入字符串只能包含数字（0-9）
            if not ('0' <= ch <= '9'):
                raise ValueError("输入字符串只能包含数字（0-9）。")
            self.grid[i // self.GRID_SIZE][i % self.GRID_SIZE] = 0 if ch == '0' else int(ch)

    def get_row(self, row):
        return self.grid[row]

    def get_column(self, col):
        return [self.grid[i][col] for i in range(self.GRID_SIZE)]

    def get_box(self, row, col):
        box = []
        # 计算3x3小格的起始行号和列号
        box_row_start = (row // self.BOX_SIZE) * self.BOX_SIZE
        box_col_start = (col // self.BOX_SIZE) * self.BOX_SIZE
        for i in range(box_row_start, box_row_start + self.BOX_SIZE):
            for j in range(box_col_start, box_col_start + self.BOX_SIZE):
                box.append(self.grid[i][j])
        return box

    def print_grid(self):
        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                print(self.grid[i][j], end=" ")
            print()

    def __str__(self):
        return ''.join(str(self.grid[i][j]) for i in range(self.GRID_SIZE) for j in range(self.GRID_SIZE))

    def __eq__(self, other):
        if isinstance(other, Grid):
            return all(self.grid[i] == other.grid[i] for i in range(self.GRID_SIZE))
        return False

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.grid))

    def clone(self):
        new_grid = Grid('')
        new_grid.grid = [row[:] for row in self.grid]
        return new_grid
