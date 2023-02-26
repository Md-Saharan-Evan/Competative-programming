n,h=map(int,input().split())
person=input().split()
ans=0
for i in person:
    if int(i)>h:
        ans+=2
    else:
        ans+=1
print(ans)