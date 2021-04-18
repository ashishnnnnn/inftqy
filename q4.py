string = input()
list1 = string.split(",")
list2 = []
for ele in list1:
    value,number = ele.split(":")
    k = 0
    for i in number:
        k+=(int(i)*int(i))
    if(k%2==0):
        value = value[len(value)-2:] + value[:len(value)-2]
        list2.append(value)
    else:
        value = value[1:]+value[:1]
        list2.append(value)
print(" ".join(x for x in list2))              