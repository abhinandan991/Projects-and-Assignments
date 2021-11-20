def checksum(n):
    c = 0
    p1 = 0
    p2 = 0
    i=n
    while i>0:
        x=i%10
        if ((c%2)==0):
            p1=p1+x
        else:
            x=(x*2)
            j=x
            while j>0:
                f = (j%10)
                p2=p2+(f)
                j=j//10
        c=c+1
        i=i//10
    p3 = p1 + p2
    if ((p3%10)==0):
        #Returns 1 if checksum is satisfied
        return 1
    else:
        #Resturns 0 if checksum is not satisfied
        return 0

n = int(input("Enter the credit card number:"))
if checksum(n)==1:
    #Evaluating card type as per conditions
    if ((n//100000000000000)==51 or (n//100000000000000)==52 or (n//100000000000000)==53 or (n//100000000000000)==54 or (n//100000000000000)==55):
        print("MASTERCARD");
    elif ((n//10000000000000)==34 or (n//10000000000000)==37):
        print("AMEX");
    elif ((n//1000000000000)==4):
        print("VISA")
    elif ((n//1000000000000000)==4):
        print("VISA")
    else:
        print("INVALID")
else:
    print("INVALID")
    