def myPow(x, n):
    if n==1:
        return x
    if n & 1:
        return (x*myPow(x,n-1))
    else:
        return myPow(x*x,n//2)
print(myPow(2,5))