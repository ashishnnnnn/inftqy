string = input()
str1 = ""
str2 = ""
if(len(string)%2==0):
    str1 = string[:len(string)//2]
    str2 = string[len(string)//2:]
else:
    str1 =  string[:len(string)//2]
    str2 = string[len(string)//2+1:]
print(str1,str2)    
k = 0
while(len(str1)>0):

    if(str1==str2):
        k = len(str1)
        break
    else:
        if(len(str1)==1):
            break
        str1 = str1[:len(str1)-1]
        str2 = str2[1:len(str2)]
print(k)