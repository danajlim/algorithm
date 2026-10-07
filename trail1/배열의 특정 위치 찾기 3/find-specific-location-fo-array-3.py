arr = list(map(int,input().split()))

for i,n in enumerate(arr):
    if n==0:
        print(arr[i-1]+arr[i-2]+arr[i-3])
        break
