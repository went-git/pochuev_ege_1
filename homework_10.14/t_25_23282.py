def find_pros(num):
    for i in range(3, int(num**0.5)+1,2):
        if num%i == 0:
            return 2
    return num

def is_ans(n):
    mx = 0
    mn = 10**10
    for i in pros:
        if n%i == 0:
            mx = max(i, mx)
            mn = min(i,mn)
    return mn+mx

n = 5400000+1
pros = set()
pros.add(2)
pros.add(3)
for i in range(5, n//2, 2):
    pros.add(find_pros(i))

c = 0
while c<5:
    k = is_ans(n)
    if k > 60_000 and str(k) == str(k)[::-1]:
        print(n, k)
        c += 1
    n += 1
