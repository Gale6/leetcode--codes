def exist(board,word):


    directionMatrix = [[-1,0],[1,0],[0,-1],[0,1]]

    def dfs(r,c,visited,indexOfWord):
        if board[r][c] != word[indexOfWord]:
            return False

        if indexOfWord == len(word)-1:
            return True


        for d in directionMatrix:
            nr,nc = r + d[0], c + d[1]

            if 0 <= nr and nr < len(board) and 0 <= nc and nc < len(board[nr]) and [nr,nc] not in visited:
                visited.append([nr,nc])
                if dfs(nr,nc,visited,indexOfWord+1):
                    return True
                visited.pop()
        return False

    for i in range (len(board)):
        for j in range (len(board[i])):
            if board[i][j] == word[0]:
                if dfs(i,j,[[i,j]],0):
                    return True
    return False
board = [["a","b"],["c","d"]]
word = "cdba"
print(exist(board,word))


