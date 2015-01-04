def DP_fib(n):
    memo = {}
    def fib(n):
        if n in memo:  
            return memo[n]
        if n<=2:
            f=1
        else:
            f = fib(n-1) + fib(n-2)
        memo[n] = f
        print "memo[" + str(n)+ "]=" + str(f)
        return f
    print fib(n)
