"""
Leet Code Problem # 733 - "Flood Fill"
This problem is much like the problem I was given
on my Skilled mock interview by the Amazon engineer,
and it is also similar to Number of Islands (though it's
easier)
"""

def floodFill(image, sr, sc, newColor):
    def dfs(image, sr, sc, newColor, oldColor):
        if image[sr][sc] != oldColor or image[sr][sc] == newColor:
            return
        image[sr][sc] = newColor
        if sr+1 < len(image):
            dfs(image, sr+1, sc, newColor, oldColor)
        if sc+1 < len(image[sr]):
            dfs(image, sr, sc+1, newColor, oldColor)
        if sr-1 >= 0:
            dfs(image, sr-1, sc, newColor, oldColor)
        if sc-1 >= 0:
            dfs(image, sr, sc-1, newColor, oldColor)

    oldColor = image[sr][sc]
    dfs(image, sr, sc, newColor, oldColor)
        


#image = [[1,1,1],[1,1,0],[1,0,1]]  # use input: 1, 1, 2

image = [[0,0,0],[0,1,1]]  # use input: 1, 1, 1

print(image)
floodFill(image, 1, 1, 1)
print(image)
