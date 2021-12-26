def mi(n):
    l = list(map(int,input().strip().split()))[:n-1]
    u = (n*(n+1))//2
    #print(l)
    su=0
    for i in l:
        su=su+i
    ans = u-su    
    return(ans)
    

an = mi(int(input().strip()))
print(an)