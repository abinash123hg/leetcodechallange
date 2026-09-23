class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seen = set()
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                
                # Format unique identifiers for row, column, and 3x3 sub-box
                row_item = (val, "row", r)
                col_item = (val, "col", c)
                box_item = (val, "box", r // 3, c // 3)
                
                if row_item in seen or col_item in seen or box_item in seen:
                    return False
                
                seen.add(row_item)
                seen.add(col_item)
                seen.add(box_item)
                
        return True