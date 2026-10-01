class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        cols = set()
        pos_diag = set()  # (row - col)
        neg_diag = set()  # (row + col)
        
        result = []
        board = [["."] * n for _ in range(n)]
        
        def backtrack(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return
            
            for col in range(n):
                if col in cols or (row - col) in pos_diag or (row + col) in neg_diag:
                    continue
                
                # Place the queen
                cols.add(col)
                pos_diag.add(row - col)
                neg_diag.add(row + col)
                board[row][col] = "Q"
                
                # Recurse to the next row
                backtrack(row + 1)
                
                # Backtrack (remove the queen)
                cols.remove(col)
                pos_diag.remove(row - col)
                neg_diag.remove(row + col)
                board[row][col] = "."
                
        backtrack(0)
        return result