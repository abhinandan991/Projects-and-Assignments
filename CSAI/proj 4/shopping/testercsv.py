f=open("shopping.csv","r")
f.readline()
data=f.readlines()
evidence=[]
label=[]
md={"Jan":0,"Feb":1,"Mar":2,"Apr":3,"May":4,"June":5,"Jul":6,"Aug":7,"Sep":8,"Oct":9,"Nov":10,"Dec":11}
for d in data:
    l=[]
    dl=d.split(",")
    for i in range(len(dl)):
        if i in [0,2,4,11,12,13,14]:
            l.append(int(dl[i]))
            continue
        if i==15:
            if dl[i]=="Returning_Visitor":
                l.append(1)
                continue
            else:
                l.append(0)
                continue
        if i==16:
            if dl[i]=="FALSE":
                l.append(0)
                continue
            else:
                l.append(1)
        if i in [1,3,5,6,7,8,9]:
            l.append(float(dl[i]))
            continue
        if i==10:
            l.append(md[dl[i]])
            continue
        if i==17:
                if dl[i]=="FALSE":
                    label.append(0)
                    continue
                else:
                    label.append(1)
                    continue
    evidence.append(l)
print(evidence[0],label[0])