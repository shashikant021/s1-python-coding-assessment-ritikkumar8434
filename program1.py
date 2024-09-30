class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        # Dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        
        # Function to perform DFS and mark the visited land
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W':
                return
            # Mark this land as visited
            grid[r][c] = 'W'
            # Explore all 4 directions
            dfs(r - 1, c)  # Up
            dfs(r + 1, c)  # Down
            dfs(r, c - 1)  # Left
            dfs(r, c + 1)  # Right
        
        # Count of islands
        island_count = 0
        
        # Iterate over the grid
        for r in range(rows):
            for c in range(cols):
            
                if grid[r][c] == 'L':
                    island_count += 1
                    dfs(r, c)
        
        return island_count
