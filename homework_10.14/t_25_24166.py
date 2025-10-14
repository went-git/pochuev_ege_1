def find_pros(num):
    for i in range(3, int(num**0.5)+1,2):
        if num%i == 0:
            return 2
    return num

def find_ans(num, pros):
    arr = []
    for i in pros:
        while num%i==0:
            arr += [i]
            num //= i
    if len(arr) == 4:
        return sum(arr)
    else:
        return 0

            
n = 7305678+1
pros = set()
pros.add(2)
pros.add(3)
for i in range(5, n//2, 2):
    pros.add(find_pros(i))
    
c = 0
while c<5:
    k = find_ans(n, pros)
    if k != 0:
        if str(k) == str(k)[::-1]:
            print(n, k)
            c += 1
    n += 1
