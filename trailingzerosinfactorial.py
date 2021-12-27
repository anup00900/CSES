def f(n):
    c=0
    while n:
        c=c+n//5
        n=n//5
    print(c) 

f(int(input().strip()))  