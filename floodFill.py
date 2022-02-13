def floodFill(image, sr, sc, newColor):
  visited = []
  ogColor = image[sr][sc]
  def dfs (image,sr,sc,ogColor,newColor,visited):
      print(sr,sc)
      if image[sr][sc] == ogColor:
          image[sr][sc] = newColor
          visited.append([sr,sc])
          if 0 <= sr-1 and sr-1 <len(image) and [sr-1,sc] not in visited:
              if 0 <= sc and sc < len(image[sr]):
                  dfs (image,sr-1,sc,ogColor,newColor,visited)
          if 0 <= sr and sr <len(image) and [sr,sc-1] not in visited:
              if 0 <= sc-1 and sc-1 < len(image[sr]):
                  dfs (image,sr,sc-1,ogColor,newColor,visited)    
          if 0 <= sr and sr <len(image) and [sr,sc+1] not in visited:
              if 0 <= sc+1 and sc+1 < len(image[sr]):
                  dfs (image,sr,sc+1,ogColor,newColor,visited)
          if 0 <= sr+1 and sr+1 <len(image) and [sr+1,sc] not in visited:
              if 0 <= sc and sc < len(image[sr]):
                  dfs (image,sr+1,sc,ogColor,newColor,visited)
          return image
  dfs(image,sr,sc,ogColor,newColor,visited)
  return image


floodFill([[0,0,0],[0,1,1]],1,1,1)
