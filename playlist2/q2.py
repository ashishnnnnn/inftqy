list1 = list(map(int,input().split()))
kk = 0
listt = []
list1.sort()
print(list1)
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        f = list1[i]
        s = list1[j]
        temp = []
        for k in range(j+1,len(list1)):
            if(list1[k]==f+s):
                temp.append(f)
                f = s
                s = list1[k]
        temp.append(f)
        temp.append(s)       
        if(len(temp)>kk):
            kk = len(temp)
            listt = temp
print(kk)
print(listt)
