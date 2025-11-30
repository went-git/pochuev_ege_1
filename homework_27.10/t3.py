ans = 0

for i in range(7**4, 7**5):
    num = ''
    i1 = i
    for j in range(5):
        num += str((i1%7)%2)
        i1 //= 7
    if num.count('00') >= 2 and num.count('000') == 0:
        ans += 1
print(ans)
