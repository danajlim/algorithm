arr = list(map(int,input().split()))
n = len(arr)

print(sum(arr[1::2]), round(sum(arr[2::3])/(n//3),1))
