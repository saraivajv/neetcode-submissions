class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        frescas = 0

        def getRotten(r, c):
            nonlocal frescas
            if(r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] != 1):
                return
            grid[r][c] = 2
            frescas -= 1
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                elif grid[r][c] == 1:
                    frescas += 1
        if frescas == 0:
            return 0
        contador = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2

                getRotten(r+1, c)
                getRotten(r-1, c)
                getRotten(r, c+1)
                getRotten(r, c-1)
            if q:
                contador += 1
        return contador if frescas == 0 else -1
                

