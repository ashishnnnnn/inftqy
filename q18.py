list1 = []
dict1 = {}
for i in range(4):
    list2 = list(input().split())
    list1.append(list2)
    dict1[10-len(list2)] = i
num = int(input())
k = 0
for ele in list1:
    k+=(10-len(ele)) 

if(k<num):
    print(-1)
else:
    keys = list(dict1.keys())
    keys.sort()
    keys = keys[::-1]
    i = 0
    while(1):
        if(num==0):
            break
        kk = keys[i]
        while(num>0):
            if(len(list1[dict1[kk]])==10):
                break
            kkk = list1[dict1[kk]][-1]
            intt = int(kkk[1:])
            char = kkk[0]
            num-=1
            print(char+str(intt+1),end=" ")
            list1[dict1[kk]].append(char+str(intt+1))
        i+=1    