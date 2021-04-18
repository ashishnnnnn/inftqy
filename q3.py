string = input()
le = -1
for i in range(len(string)):
    for j in range(i+1,len(string)):
        stringg = string[i:j]
        #print(stringg)
        if(len(stringg)>2 and len(set(stringg))==len(stringg)):
            if(le<len(stringg)):
                le = len(stringg)
print(le)

