import unittest

from sudoku import Sudoku


class TestSudoku(unittest.TestCase):

    @staticmethod
    def run_test(sudoku_input):
        try:
            sudoku = Sudoku(sudoku_input)
            print("原始数独盘面：")
            sudoku.print()

            if sudoku.solve():
                print("\n解出的数独盘面：")
                sudoku.print()
            else:
                print("无解。")
        except ValueError as e:
            print(f"输入无效: {e}")

    def test_solve(self):
        # 测试1：简单数独
        print("测试1：简单数独")
        easy_sudoku = "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
        self.run_test(easy_sudoku)

        # 测试2：已解决的数独
        print("\n测试2：已解决数独")
        solved_sudoku = "534678912672195348198342567859761423426853791713924856961537284287419635345286179"
        self.run_test(solved_sudoku)

        # 测试3：无解数独
        print("\n测试3：无解数独")
        unsolvable_sudoku = "530570000600195000098000060800060003400803001700020006060000280000419005000080079"
        self.run_test(unsolvable_sudoku)

        # 测试4：几乎空的数独
        print("\n测试4：几乎空数独")
        nearly_empty_sudoku = "000000000000000000000000000000000000000000000000000000000000000000000000000020003"
        self.run_test(nearly_empty_sudoku)

        # 测试5：无效数独-长度不足
        print("\n测试5：无效数独")
        invalid_sudoku_length = "530070000619500098000060800060003400803001700020006060000280000419005000080079"
        self.run_test(invalid_sudoku_length)

        # 测试6：无效数独-包含非数字字符
        print("\n测试6：无效数独")
        invalid_sudoku_with_abc = "530070000600AV5000098000060800060003400803001700020006060000280000419005000080079"
        self.run_test(invalid_sudoku_with_abc)

    def test_print(self):
        sudoku = Sudoku("530070000600195000098000060800060003400803001700020006060000280000419005000080079")
        sudoku.print()


if __name__ == '__main__':
    unittest.main()
