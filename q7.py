#Not easy
x = list(map(int,input().split()))
t = 2
for i in range(len(x)):
    for j in range(i+1,len(x)):
        first = x[i]
        second = x[j]
        ele = 2
        for k in range(j+1,len(x)):
            third = x[k]
            if(third==first+second):
                ele+=1
                first = second
                second = third
        if(t<ele):
            t = ele
print(t)                    