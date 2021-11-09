import random
s=input("Enter the string:")
l=[]
x=0
length=len(s)
while x<(length**length):
    st=""
    for i in range(length):
        st=st+random.choice(s)
    if st not in l:
        l.append(st)
    else:
        continue 
    x=len(l) 
final=[]    
for h in range(len(l)):
    a=l[h]
    for g in range(len(a)):
        if a.count(a[g])>1:
            break
        else:
            continue
    else:
        final.append(a)           
final.sort()
q=final.index(s)
try:
    print(final[q+1])
except IndexError:
    print("no answer")    
