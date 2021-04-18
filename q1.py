string = input()
words = ""
special = ""
for i in string:
    if((i>='a' and i<='z') or (i>='A' and i<='Z')):
        words+=i 
    else:
        special+=i 
words = words[::-1]
w = 0
s = 0
final = ""
for i in string:
    if((i>='a' and i<='z') or (i>='A' and i<='Z')):
        final += words[w]
        w+=1
    else:
        final += special[s]
        s+=1
print(final)        