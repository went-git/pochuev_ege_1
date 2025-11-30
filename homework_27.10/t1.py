s = 'АКОРСТ'
s = s[::-1]
i = 6**5
ans = ''
for q in s:
    for w in s:
        for e in s:
            for r in s:
                for t in s:
                    sc = q+w+e+r+t
                    if ans == '' and i%2 == 0 and sc[0] not in 'АСТ' and sc.count("О")==2:
                        ans = sc
                        print(i)
                    i -= 1
