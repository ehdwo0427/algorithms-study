num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
x, b = map(str, input().split())

x = x[::-1]
result = 0

for i in range(len(x)):
    result += (int(b) ** i) * (num.index(x[i]))
print(result)