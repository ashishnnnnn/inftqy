import itertools
s = int(input())
list1 = list(map(int,input().split()))
list2 = list(itertools.combinations(list1,4))
k = 0
for li in list2:
    if(sum(li)==s):
        k+=1
print(k)        