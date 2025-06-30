N = int(input())

arr = list(i for i in range(11))

if N < 11:
    print(arr[N])
    exit(0)

for i in range(11, 100):
    st = str(i)
    