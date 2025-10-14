def find_pros(num):
    for i in range(3, int(num**0.5)+1,2):
        if num%i == 0:
            return 2
    return num

def sm(num):
    for i in pros:
        if num%i == 0 and num//i in pros:
            return num//i + i
    return 0


n = 5400000+1
c = 0
pros = set()
pros.add(2)
pros.add(3)
for i in range(5, n, 2):
    pros.add(find_pros(i))

while c<5:
    k = sm(n)
    if k > 60000  and str(k) == str(k)[::-1]:
        print(n, k)
        c += 1
    n += 1
