n,t=map(int,input().split())
stn=input()
string=[]
for i in stn:
    string.append(i)
i=0
j=0
while len(string)>i:
    if i==len(string)-1:
        i+=1
    else:
        if string[i]=="B" and string[i+1]=="G":
            if j<t:
                string[i],string[i+1]=string[i+1],string[i]
                j+=1
            elif j==t:
                j=0
        else:
            j=0
        i+=1
stn=''
for i in string:
    stn+=i
print(stn)

