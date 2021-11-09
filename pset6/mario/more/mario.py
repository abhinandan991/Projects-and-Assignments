while (True):
    #askes for half height
    n=input("Height: ")
    #checks whether given value is integer compatible
    try:
        n=int(n)
    except:
        continue
    #checks whether given input is within 1 and 8
    if n>=1 and n<=8:
        break
    
#prints for n-1 lines    
for i in range(1,n):
    print(" "*(n-i-1), "#"*i, "", "#"*i)
#prints last line    
print("#"*n, "", "#"*n)    