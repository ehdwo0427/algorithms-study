N = int(input())
word = input()
num_lst = [0] * N

for i in range(N):
    num_lst[i] = int(input())

stack = []

for i in word:
    if 'A' <= i <= 'Z':
        stack.append(num_lst[ord(i) - ord('A')])
    else:
        str2 = stack.pop()
        str1 = stack.pop()
        
        if i == '+':
            stack.append(str1 + str2)
        elif i == '-':
            stack.append(str1 - str2)
        elif i == '*':
            stack.append(str1 * str2)
        elif i == '/':
            stack.append(str1 / str2)
            
print(f"{stack[0]:.2f}")  # 결과를 소수점 둘째 자리까지 출력