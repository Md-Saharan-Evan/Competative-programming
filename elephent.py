x=int(input())
step=x//5
temp=x%5
if temp==0:
    print(step)
else:
    print(step+1)