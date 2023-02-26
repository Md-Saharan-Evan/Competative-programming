n=int(input())
sum=0
for i in range(1,n+1):
    opr=(-1)**i
    sum+=opr*i
print(sum)