from typing import List

input = open('day-4\input.txt').read()

grid = [line.strip() for line in input.strip().split('\n') if line.strip()]
rows = len(grid)
cols = len(grid[0])

total = 0

neighbor_offset = [ (-1, -1), (-1, 0), (-1, 1),
                    (0, -1),           (0, 1),
                    (1, -1),  (1, 0),  (1, 1)]

def count_adjacent_rolls(grid: List[str], row: int, col: int) -> int: 
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for r_offset, c_offset in neighbor_offset:
        n_row, n_col = row + r_offset, col + c_offset

        # boundary check
        if 0 <= n_row < rows and 0 <= n_col < cols:
            if grid[n_row][n_col] == '@':
                count += 1

    return count

for r in range(rows):
        for c in range(cols):
            cell_value  = grid[r][c]
            
            if cell_value != '@':
                continue
            
            neighbor_count = count_adjacent_rolls(grid, r, c)
            
            if neighbor_count < 4:
                total += 1

print("Total rolls with less than 4 adjacent rolls:")
print(total)