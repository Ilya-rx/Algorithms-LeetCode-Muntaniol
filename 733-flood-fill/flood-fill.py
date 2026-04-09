from collections import deque

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        rows, cols = len(image), len(image[0])
        start_color = image[sr][sc]
        if start_color == color:
            return image

        queue = deque()
        queue.append((sr, sc))

        while queue:
            r, c = queue.popleft()
            if image[r][c] != start_color:
                continue
            image[r][c] = color
            if r > 0:
                queue.append((r-1, c))
            if r < rows-1:
                queue.append((r+1, c))
            if c > 0:
                queue.append((r, c-1))
            if c < cols-1:
                queue.append((r, c+1))
        return image