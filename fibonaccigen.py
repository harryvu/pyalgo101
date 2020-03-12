class FibonacciMemoized:
    def __init__(self):
        self.memo = []

    def fib(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif len(self.memo) < n:
            self.memo.append(self.fib(n-1) + self.fib(n-2))
        
        return self.memo[n-2]

Fib = FibonacciMemoized()
print("fib(5): {}".format(Fib.fib(5)))
print("fib(10): {}".format(Fib.fib(10)))
print("fib(15): {}".format(Fib.fib(15)))