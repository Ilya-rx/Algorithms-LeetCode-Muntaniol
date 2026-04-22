class Solution:
    def climbStairs(self, n: int) -> int:
        # если ступенек 1 или 2
        if n <= 2:
            return n
        
        # начальные значения
        a = 1
        b = 2
        
        # считаем дальше
        for i in range(3, n + 1):
            c = a + b
            a = b
            b = c
        
        return b