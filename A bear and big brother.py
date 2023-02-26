Limark,brother=map(int,input().split())
count=0
while(Limark<=brother):
    count+=1
    Limark=Limark*3
    brother=brother*2
print(count)