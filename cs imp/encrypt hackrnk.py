import math
s=input("Enter the string:")
n=""
for ch in s:
    if ch==" ":
        continue
    else:
        n=n+ch
l=len(n)
req=[]
lf=math.ceil(l**0.5)
li=math.floor(l**0.5)
if li*lf>=l:
    for i in range(li):
        req=req+[n[0:lf]]
        n=n[lf:]
else:
    for i in range (lf):
        req=req+[n[0:lf]]
        n=n[lf:]
print(req)  
encrypted=""
for j in req:
    for x in range(len(j)):
        for y in req:
            try:
                h=y[x]
            except IndexError:
                continue
            else:
                encrypted=encrypted+h
        encrypted=encrypted+" "
    break    
print(encrypted)            