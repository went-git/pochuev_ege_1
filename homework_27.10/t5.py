ans = ''
s = '0123456789'
s1 = '13579'
s2 = '02468'
for q in s[1:]:
    for w in s:
        for e in s:
            for r in s:
                for t in s:
                    sc = q+w+e+r+t
                    suit = True
                    for i in range(4):
                        if (sc[i] in s1 and sc[i+1] in s1) or(sc[i] in s2 and sc[i+1] in s2):
                            suit = False
                            break
                    if suit and (int(sc)-10000+1)%15 == 0:
                        ans = int(sc)-10000+1
print(ans)
