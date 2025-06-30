a, b = map(int, input().split())

arr = []
idx = 0
while True:
    if len(arr) >= b:
        break
    arr.extend([idx] * idx)
    idx += 1
print(sum(arr[a -1 : b]))