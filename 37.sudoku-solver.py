#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def solve(posInd):
            if posInd == len(empty_pos):
                return True
            
            row, col = empty_pos[posInd]

            for value in "123456789":
                valueInd = int(value) - 1
                if exhausted_row[row][valueInd] or exhausted_col[col][valueInd] or exhausted_row_col[row // 3][col // 3][valueInd]:
                    continue
                board[row][col] = value
                exhausted_row[row][valueInd] = exhausted_col[col][valueInd] = exhausted_row_col[row // 3][col // 3][valueInd] = True
                if solve(posInd+1): return True
                exhausted_row[row][valueInd] = exhausted_col[col][valueInd] = exhausted_row_col[row // 3][col // 3][valueInd] = False

            board[row][col] = "."
            return False
        
        exhausted_row, exhausted_col, exhausted_row_col = [[False] * 9 for _ in range(9)], [[False]*9 for _ in range(9)], [[[False]*9 for _ in range(3)] for _ in range(3)]
        empty_pos = []

        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    value = int(board[row][col]) - 1
                    exhausted_row[row][value] = exhausted_col[col][value] = exhausted_row_col[row // 3][col // 3][value] = True
                else:
                    empty_pos.append((row,col))

        return solve(0)
        
        # print(exhausted_row, exhausted_col, exhausted_row_col, sep="\n")

        # def solve():
            
        #     for row in range(9):
        #         for col in range(9):

        #             if board[row][col] == ".":
        #                 for num in range(1, 10):
        #                     num = str(num)
        #                     if num in exhausted_row[row] or num in exhausted_col[col] or num in exhausted_row_col[row//3][col//3]:
        #                         continue
        #                     board[row][col] = num

        #                     exhausted_row[row].add(board[row][col])
        #                     exhausted_col[col].add(board[row][col])
        #                     exhausted_row_col[row//3][col//3].add(board[row][col])

        #                     if (solve()): return True
                            
        #                     exhausted_row[row].remove(board[row][col])
        #                     exhausted_col[col].remove(board[row][col])
        #                     exhausted_row_col[row//3][col//3].remove(board[row][col])
        #                     board[row][col] = "."

        #                 return False
                        

        #     return True
        
        # def solve(r, col):

        #     if col == 9:
        #         return True

        #     for row in range(r, 9):
        #         if board[row][col] == ".":

        #             for num in range(1, 10):
        #                 num = str(num)
        #                 if num in exhausted_row[row] or num in exhausted_col[col] or num in exhausted_row_col[row//3][col//3]:
        #                     continue

        #                 board[row][col] = num

        #                 exhausted_row[row].add(board[row][col])
        #                 exhausted_col[col].add(board[row][col])
        #                 exhausted_row_col[row//3][col//3].add(board[row][col])

        #                 if (solve(row+1, col)): return True
                        
        #                 exhausted_row[row].remove(board[row][col])
        #                 exhausted_col[col].remove(board[row][col])
        #                 exhausted_row_col[row//3][col//3].remove(board[row][col])
        #                 board[row][col] = "."

        #             return False
            
        #     if (solve(0, col+1)): return True
        #     return False

                    

        # return solve(0, 0)



                

        
# @lc code=end

