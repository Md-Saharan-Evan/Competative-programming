name=input()
temp=[]
for i in name:
    if i in temp:
        continue
    else:
        temp.append(i)
if len(temp)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
