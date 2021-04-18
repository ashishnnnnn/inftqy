"""k = "Abcde"
for i in k:
    print(i.lower())
print(k.lower())    """

string = input()
dict1 = {}
for i in string:
    s = i
    s = s.lower()
    if(s in dict1.keys()):
        dict1[s]+=i 
    else:
        dict1[s] = i
list1 = list(dict1.keys())
list1.sort()
#print(list1)
#print(dict1)
i = 0
j = len(list1)-1
ret = ""
while(i<j):
    ret+=dict1[list1[i]]
    ret+=dict1[list1[j]]
    i+=1
    j-=1
if(i==j):
    ret+=dict1[list1[i]]
print(ret)        