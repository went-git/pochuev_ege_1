ans = 0

for i in range(5**8, 5**9):
    num = ''
    i1 = i
    for j in range(9):
        num += str((i1%5)%2)
        i1 //= 5
    if num.count('00') == 2 and num.count('000') == 0:
        ans += 1
print(ans)
