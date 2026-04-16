class Fibonacci:
    """Class for calculating Fibonacci sequence"""
    
    def __init__(self, n, m):
        self.n = n
        self.m = m
        
    def fib(self):
        F = []
        a = 0
        b = 1
        F.append(a)
        for n in range(0, self.n-1):
            c = a + b
            a = b
            b = c
            F.append(a)
        return F

    def nth(self):
        F = self.fib()
        return F[-1]
        
    def dividable(self):
        F = self.fib()
        A = []
        for a in F:
            if a % self.m == 0:
                A.append(a)
        return A