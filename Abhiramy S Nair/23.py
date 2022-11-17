n=input("Enter the strings")
dict={}
for i in n:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
print(dict)
