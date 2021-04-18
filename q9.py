def solve(num):
    s = num
    t = 0 
    while(num>0):
        t+=(num%10)
        num = num//10
    if(s%t==0):
        return True
    return False        

k = int(input())
list1 = []
for i in range(k):
    list2 = list(map(int,input().split()))
    list1.append(list2)

c = len(list1[0])    
t = 0     
for i in range(k-1):
    for j in range(c-1):
        if(solve(list1[i][j]) and solve(list1[i][j+1]) and solve(list1[i+1][j]) and solve(list1[i+1][j+1])):
            t+=1
print(t)                