memo = {}
def DP_fib(n):
    if n in memo:
        return memo[n]
    if n==0:
        f=0
    elif n<=2:
        f=1
    else:
        f = DP_fib(n-1) + DP_fib(n-2)
    memo[n] = f
    return f
