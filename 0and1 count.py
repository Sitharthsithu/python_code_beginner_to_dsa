
a=[0,0,1,0,1,0,1,0,1,0,1]
count=maxcount=ocount=omaxcount=0
for i in a:
    if i==0:
        ocount+=1
        count=0
        
        if omaxcount<ocount:
            omaxcount=ocount
            
    elif(i==1):
        count+=1
        ocount=0
        
        if maxcount<count:
            maxcount=count

print(max(maxcount,omaxcount))