
def fib(n):
    a,b = 0,1
    count = 1
    while count<n:
        a,b = b,a+b
        count += 1
    print(a)
fib(7)