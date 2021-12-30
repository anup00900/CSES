def move(arr):
    ans=0
    for i in range(1,len(arr)):
        if arr[i-1]>arr[i]:
            ans = ans + (arr[i-1]-arr[i])
            arr[i]=(arr[i-1])
            
    return ans
    
n = int(input())
l=list(map(int,input().strip().split()))[:n]
    
print(move(l))