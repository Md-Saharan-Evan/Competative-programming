test=int(input())
for i in range(test):
    a=1
    disit=int(input())
    set=input().split()
    while a==1:
        count=1
        for x in range(disit):
            for y in range(x+1,disit):
                temp=int(set[x])-int(set[y])
                if temp>0:
                    if temp not in set:
                        set.append(temp)
                        a=1
                        count-=1
                        break
        if count==0:
            a=1
        else:
            a=0
    print(len(set))
