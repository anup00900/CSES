def r(n):
    j=n[0]
    m=1
    c=1
    for i in range(1,len(n)):
        if n[i] == j:
            c=c+1 
        else:
            m=max(m,c)
            j=n[i]
            c=1
            
    return max(m,c) 

print(r(input().strip()))
