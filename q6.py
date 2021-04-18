x = int(input())
list1 = list(map(int,input().split()))

dict1 = {}
for i in list1:
    if(i in dict1.keys()):
        dict1[i]+=1
    else:
        dict1[i] = 1
list1 = list(dict1.values())
list1.sort()
length = len(list1)
for i in list1:
    if(x>=i):
        x-=i
        length-=1
    else:
        break   
print(length)                 