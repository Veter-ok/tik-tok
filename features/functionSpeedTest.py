# python3 -m cProfile functionSpeedTest.py
def test():
    i = 0
    for _ in range(10_000_000):
        i += 1

def factorial(x):
    ans = 1
    for i in range(2, x):
        ans *= i


test()
factorial(100_000)