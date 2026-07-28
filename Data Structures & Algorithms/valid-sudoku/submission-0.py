class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        square_set = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                if board[i][j] in row_set[i]:
                    return False
                else:
                    row_set[i].add(board[i][j])
                
                if board[i][j] in col_set[j]:
                    return False
                else:
                    col_set[j].add(board[i][j])
                
                if board[i][j] in square_set[(i // 3) * 3 + (j // 3)]:
                    return False
                else:
                    square_set[(i // 3) * 3 + (j // 3)].add(board[i][j])
        return True