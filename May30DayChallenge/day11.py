class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: 
            return image
        def chng(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: 
                    chng(r-1, c)
                if r+1 < R: 
                    chng(r+1, c)
                if c >= 1: 
                    chng(r, c-1)
                if c+1 < C: 
                    chng(r, c+1)

        chng(sr, sc)
        return image

# Flood fill