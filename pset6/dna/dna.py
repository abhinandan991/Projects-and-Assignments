import csv
import sys

#Checks for valid command line arguments
if len(sys.argv)!=3:
    sys.exit("Invalid commandline argument.")

#Defines a function to count the longext stream of Gene provided as argument.. Raises error if Gene not present in dna
def counter(g):
    d=open(sys.argv[2],"r")
    line=d.readline()
    lc=[]
    
    fi=line.find(g)
    while fi!=-1:
        c=1
        while(True):
            fi=fi+len(g)
            f=line.find(g,fi)
            if f==fi:
                c=c+1
            else:
                lc.append(c)
                break
        fi=line.find(g,fi)    
    lc.sort()
    d.close()
    return lc[-1]

#loads database into memory 
data=open(sys.argv[1],"r")
database=[]
reader=csv.DictReader(data)
for e in reader:
    database.append(e)
data.close()

#produses a list of Genes in database
q=open(sys.argv[1],"r")
head=q.readline().strip()
head=head.split(",")
head.remove("name")
q.close()

#creates dictionary.. if Gene not in sequence, raises error, thus no match 
sample={}
for w in head:
    sample[w]=0
try:
    
    for i in head:
        sample[i]=counter(i)
except:
    sys.exit("No match")
    
try:
    #compares
    for j in range(len(database)):
       dic=database[j]
       for k in head:
           if int(dic[k])==sample[k]:
               continue
           else:
               break
       else:
           print(dic["name"])
           break
    else:
       print("No match")
except:
    print("No match")

sys.exit(0)
        