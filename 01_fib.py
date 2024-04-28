def caching_fibonacci():
    """
    Function caching_fibonacci:
    Create an empty dictionary called cache

    Function fibonacci(n):
        If n <= 0, return 0
        If n == 1, return 1
        If n is in cache, return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        Return cache[n]

    Return the function fibonacci
    """
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
    return fibonacci


fib = caching_fibonacci()
print(fib(10), fib(15))

assert fib(10) == 55
