import itertools
from itertools import permutations

def solve(ele):
    stri = ""
    for i in ele:
        stri = i+stri
    return int(stri)    

inp = input()
list1 = inp.split(",")
list2 = list(set(list(permutations(list1,3))))
print(list2)
k = 0
for ele in list2:
    k = max(k,solve(ele))
print(k,len(list2))    