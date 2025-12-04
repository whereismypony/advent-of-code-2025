from typing import List

input = open('day-4\input.txt').read()

grid = [list(line.strip()) for line in input.split('\n') if line.strip()]
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

while True:
    removals_this_round = []
    
    for r in range(rows):
        for c in range(cols):
            cell_value  = grid[r][c]
            if cell_value == '@':
                neighbor_count = count_adjacent_rolls(grid, r, c)
                if neighbor_count < 4:
                    removals_this_round.append((r, c))

    count_this_round = len(removals_this_round)
    
    if count_this_round == 0:
        print(f"No more paper can be moved")
        break
    
    for r, c in removals_this_round:
        grid[r][c] = '.'

    total += count_this_round
    print(f"Removed {count_this_round} paper rolls this round. For a total of: {total}")


print("Total rolls Removed:")
print(total)