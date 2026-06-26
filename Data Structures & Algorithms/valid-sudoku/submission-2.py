from collections import Counter
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            counts = Counter(row)
            for ch, cnt in counts.items():
                if ch != "." and cnt > 1:
                    return False

        # Check columns
        for j in range(9):
            col = [board[i][j] for i in range(9)]
            counts = Counter(col)
            for ch, cnt in counts.items():
                if ch != "." and cnt > 1:
                    return False

        # Check 3×3 sub-boxes
        for box_row in range(3):          # which row of boxes (0, 1, 2)
            for box_col in range(3):      # which column of boxes (0, 1, 2)
                seen = set()
                for i in range(box_row * 3, box_row * 3 + 3):
                    for j in range(box_col * 3, box_col * 3 + 3):
                        ch = board[i][j]
                        if ch != "." and ch in seen:
                            return False
                        seen.add(ch)

        return True
