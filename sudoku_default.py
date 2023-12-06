def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j], end=" ")
        print()


def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
        
    for x in range(9):
        if grid[x][col] == num:
            return False
        
    startrow = row - row % 3
    startcol = col - col % 3
    
    for i in range(3):
        for j in range(3):
            if grid[i + startrow][j + startcol] == num:
                return False
    return True


def suduko(grid, row, col):
    if row == M - 1 and col == M:
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return suduko(grid, row, col + 1)
    
    for num in range(1, M + 1, 1):
        if solve(grid, row, col, num):
            grid[row][col] = num
            if suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False


if __name__ == '__main__':
    M = 9
    
    input_grid = [[0, 0, 7, 0, 0, 0, 0, 0, 5],
                  [0, 8, 0, 0, 0, 0, 0, 9, 0],
                  [6, 2, 0, 0, 0, 0, 0, 7, 0],
                  [0, 0, 0, 0, 4, 0, 6, 0, 0],
                  [0, 0, 0, 7, 0, 0, 3, 0, 1],
                  [9, 0, 0, 1, 0, 5, 0, 2, 0],
                  [0, 0, 0, 3, 0, 0, 1, 0, 0],
                  [4, 0, 0, 2, 0, 0, 0, 8, 0],
                  [0, 9, 1, 0, 0, 0, 0, 0, 0]]
    
    if suduko(input_grid, 0, 0):
        puzzle(input_grid)
    else:
        print("Solution does not exist:(")
