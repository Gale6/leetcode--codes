def orangesRotting(grid):
        directionMatrix = [[-1,0],[1,0],[0,-1],[0,1]]
        fresh = 0
        rottenPos = []
        time = 0
        for i in range (len(grid)):
                for j in range(len(grid[i])):
                        if grid[i][j] == 1:
                                fresh += 1
                        elif grid[i][j] == 2:
                                rottenPos.append([i,j])
        while len(rottenPos) > 0:
                print(rottenPos)
                for r in range (len(rottenPos)):
                        x,y = rottenPos.pop(0)
                        for d in directionMatrix:
                                newX,newY = x + d[0], y + d[1]
                                if 0 <= newX and newX < len(grid) and 0 <= newY and newY < len(grid[newX]) and grid[newX][newY] == 1:
                                        grid[newX][newY] = 2
                                        rottenPos.append([newX,newY])
                                        fresh -= 1
                if len(rottenPos) >0:
                        time += 1
        if fresh != 0:
                return -1
        else:
                return time




print(orangesRotting([[0,2]]))