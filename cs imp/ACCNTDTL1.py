import csv

opt=1
while opt!=0:
    print('''Enter 1 to INSERT details for the new account:
    Enter 2 to DELETE an account:
    Enter 3 to PRINT the details of the account:
    Enter 4 to WITHDRAW money from the account:
    Enter 5 to DEPOSIT money into the account:
    Enter 6 to change the MOBILE NUMBER of the account:
    Enter 0 to EXIT the program:    ''')
    opt=int(input("Enter the option number:"))         
    if opt==1:
        fout=open("C:\\Users\\abhin\\OneDrive\\Documents\\AccntDT","a")
        csvobj=csv.writer(fout)
        a=input("Enter the new account number:")
        n=input("Enetr the name for the new account:")
        m=input("Enter the mobile number for the account:")
        b=input("Enter the starting balance for the account:")
        rec=[a,n,m,b]
        csvobj.writerow(rec)
        fout.close()
        print("Account added")
    if opt in (2,3,4,5,6):
        acc=input("Enter the account number:")
        if opt==2:
            import os
            fout=open("C:\\Users\\abhin\\OneDrive\\Documents\\AccntDT1","w")
            csvobj=csv.writer(fout)
            fin=open("C:\\Users\\abhin\\OneDrive\\Documents\\AccntDT","r")
            obj=csv.reader(fin)
            for row in obj:
                l=list(row)
                if l==[]:
                    continue
                elif l[0]!=acc:
                    csvobj.writerow(row)
            fin.close() 
            fout.close()
            os.remove("C:\\Users\\abhin\\OneDrive\\Documents\\AccntDT")
            os.rename("C:\\Users\\abhin\\OneDrive\\Documents\\AccntDT1","C:\\Users\\abhin\\OneDrive\\Documents\\AccntDT")
            print("Account deleted")
        if opt==3:
            fin=open("C:\\Users\\abhin\\OneDrive\\Documents\\AccntDT","r")
            csvobj=csv.reader(fin)
            for row in csvobj:
                l=list(row)
                if l==[]:
                    continue
                elif l[0]==acc:
                    print("The account number is:",l[0])
                    print("The Name of the account holder is:", l[1])
                    print("The Mobile number linked is:",l[2])
                    print("The Balance in the account is:",l[3])
            fin.close()
        if opt==4:
            import os
            fout=open("C:\\Users\\abhin\\OneDrive\\Documents\\AccntDT1","w")
            csvobj=csv.writer(fout)
            fin=open("C:\\Users\\abhin\\OneDrive\\Documents\\AccntDT","r")
            obj=csv.reader(fin)
            for row in obj:
                l=list(row)
                if l==[]:
                    continue
                elif l[0]!=acc:
                    csvobj.writerow(row)
                if l[0]==acc:
                    if l[-1]=="0":
                        print("No money to withdraw")
                    else:
                        rec=[l[0],l[1],l[2]]
                        wi=int(input("Enter the money to be withdrawn:"))
                        bal=int(l[-1])-wi
                        bal=[str(bal)]
                        rec=rec+bal
                        csvobj.writerow(rec)
            fin.close() 
            fout.close()
            os.remove("C:\\Users\\abhin\\OneDrive\\Documents\\AccntDT")
            os.rename("C:\\Users\\abhin\\OneDrive\\Documents\\AccntDT1","C:\\Users\\abhin\\OneDrive\\Documents\\AccntDT")
        if opt==5:
            import os
            fout=open("C:\\Users\\abhin\\OneDrive\\Documents\\AccntDT1","w")
            csvobj=csv.writer(fout)
            fin=open("C:\\Users\\abhin\\OneDrive\\Documents\\AccntDT","r")
            obj=csv.reader(fin)
            for row in obj:
                l=list(row)
                if l==[]:
                    continue
                elif l[0]!=acc:
                    csvobj.writerow(row)
                if l[0]==acc:
                    rec=[l[0],l[1],l[2]]
                    wl=int(input("Enter the money to be deposited:"))
                    bal=int(l[-1])+wl
                    bal=[str(bal)]
                    rec=rec+bal
                    csvobj.writerow(rec)
            fin.close() 
            fout.close()
            os.remove("C:\\Users\\abhin\\OneDrive\\Documents\\AccntDT")
            os.rename("C:\\Users\\abhin\\OneDrive\\Documents\\AccntDT1","C:\\Users\\abhin\\OneDrive\\Documents\\AccntDT")
        if opt==6:
            import os
            fout=open("C:\\Users\\abhin\\OneDrive\\Documents\\AccntDT1","w")
            csvobj=csv.writer(fout)
            fin=open("C:\\Users\\abhin\\OneDrive\\Documents\\AccntDT","r")
            obj=csv.reader(fin)
            for row in obj:
                l=list(row)
                if l==[]:
                    continue
                elif l[0]!=acc:
                    csvobj.writerow(row)
                if l[0]==acc:
                    rec=[l[0],l[1]]
                    tl=input("Enter the new phone number:")
                    rec=rec+[tl]+[l[-1]]
                    csvobj.writerow(rec)
            fin.close() 
            fout.close()
            os.remove("C:\\Users\\abhin\\OneDrive\\Documents\\AccntDT")
            os.rename("C:\\Users\\abhin\\OneDrive\\Documents\\AccntDT1","C:\\Users\\abhin\\OneDrive\\Documents\\AccntDT")
            print("Number upadted")
            
                    
        
        
