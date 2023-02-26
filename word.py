word=input()
low=0
high=0
for i in word:
    if ord(i)>90:
        low+=1
    else:
        high+=1
if high>low:
    print(word.upper())
else:
    print(word.lower())