string = input()
list1 = string.split(",")
list2 = []
for i in list1:
    list2.append(int(i))
five = -1
eight = -1
for i in range(len(list2)):
    if(list2[i]==5):
        five = i
        break

for i in range(len(list2)):
    if(list2[i]==8):
        eight = i 
if(five==-1 or eight==-1):
    print("Nothing")
else:
    sum = 0
    for i in range(five):
        sum+=list2[i]
    for i in range(eight+1,len(list2)):
        sum+=list2[i]
    k = ""
    for i in range(five,eight+1):
        k+=str(list2[i])
    k = int(k)+sum
    print(k)                            