T = int(input())
cnt = [25, 10, 5, 1]

for _ in range(T):
    N = int(input())
    coin = []
    for i in range(4):
        if N // cnt[i] != 0:
            coin.append(N // cnt[i])
            N %= cnt[i]
        else:
            coin.append(0)
    print(*coin)