

def find_pros(num):
    for i in range(3, int(num**0.5)+1,2):
        if num%i == 0:
            return 2
    return num

def is_ans(num, pros):
    for i in pros:
        if num%i==0 and num//i in pros:
            if str(i).count('2') == 1 and str(num//i).count('2') == 1:
                return max(i, num//i) 
    return 0

n = 6651220+1
pros = set()
pros.add(2)
pros.add(3)
for i in range(5, n, 2):
    pros.add(find_pros(i))

c = 0
while c<5:
    k = is_ans(n, pros)
    if k != 0:
        print(n, k)
        c += 1
    n += 1
