ans = 0

for i in range(12**4, 12**5):
    num = ''
    i1 = i
    for j in range(5):
        num += str((i1%12)%2)
        i1 //= 12
    if num.count('11') <= 2 and num.count('1111')==0:
        ans += 1
print(ans)
