"""
New attempt of Flood Fill
problem - trying to review
DFS for matrix problems
"""

def flood_fill(image, sr, sc, new_color):
    def dfs(image, sr, sc, new_color, old_color):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[sr]) or image[sr][sc] == new_color or image[sr][sc] != old_color:
            return
        image[sr][sc] = new_color
        dfs(image, sr+1, sc, new_color, old_color)
        dfs(image, sr, sc+1, new_color, old_color)
        dfs(image, sr-1, sc, new_color, old_color)
        dfs(image, sr, sc-1, new_color, old_color)

    dfs(image, sr, sc, new_color, image[sr][sc]) 

    return image



"""
TEST CASES
"""

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1

"""
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
"""

print(flood_fill(image, sr, sc, 2))
