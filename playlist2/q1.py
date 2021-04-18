string = input()
final = ""
for i in range(len(string)):
    if(string[i] not in string[:i]):
        final+=string[i]
print(final)        