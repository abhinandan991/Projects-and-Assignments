n=int(input("Enter the pattern generator:"))
l=list(range(n))
i=1
if n%2==0:
    while i<n:
        for j in range(int(n/2)):
            print(" "*((l[-i])-1), "*"*(i+l[i-1]), " "*((l[-i])-1), " "*((n+l[n-1])-2), end=" ")
        print()
        i=i+1
    print("*"*((n*(n+l[n-1]))-1))
    k=n-1     
    while k>0:
        for m in range(int(n/2)):
            print( " "*((n+l[n-1])-2), " "*(l[-k]-1), "*"*(k+l[k-1]), " "*((l[-k])-1), end=" ")
        print()
        k=k-1
else:
    while i<n:
        for j in range((int(n/2)+1)):
            print(" "*((l[-i])-1), "*"*(i+l[i-1]), " "*((l[-i])-1), " "*((n+l[n-1])-3), end=" ")
        print()
        i=i+1
    print("*"*((n*(n+l[n-1]))-2))
    k=n-1     
    while k>0:
        for m in range(int(n/2)):
            print( " "*((n+l[n-1])-2), " "*(l[-k]-1), "*"*(k+l[k-1]), " "*((l[-k])-1), end=" ")
        print()
        k=k-1
