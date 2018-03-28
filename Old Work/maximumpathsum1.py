def rowMax(maxGrid):
    for row in range(rowNum):
        for item in range:
            val = grid[row][item]+grid[row+1][item+1]+grid[row][item+2]+grid[row][item+3]
            if val > maxGrid:
                maxGrid = val
        
            val = grid[item][row]*grid[item + 1][row]*grid[item+2][row]*grid[item+3][row]
            if val > maxGrid:
                maxGrid = val
    return maxGrid
           
            
maxGrid = 0
grid = '''
3
7 4
2 4 6
8 5 9 3'''

grid = grid.splitlines()
rowNum = len(grid)
for row in range(1,rowNum):
    grid[row] = list(map(int, grid[row].split()))
for x in grid:
    print(x)

#print(maxGrid)


































