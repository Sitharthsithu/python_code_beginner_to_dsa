#s=str(input("Enter the String:"))
#key=int(input("Enter the key value:"))

s="Priya"
key=1
ord(i)

def encoding(s):
    c=[]
    d=[]
    e=""
    for i in s:
        c.append(ord(i))
    #print(c)

    for i in c:
        i+=key
        d.append(i)
    #print(d)
        
    for i in d:
       e+=chr(i)
    return(e)
    
print("The encoded string:",encoding(s))

k=encoding(s)


def decoding(k):
    f=[]
    g=[]
    h=""
    for i in k:
        f.append(ord(i))
    #print(c)

    for i in f:
        i-=key
        g.append(i)
    #print(d)
        
    for i in g:
       h+=chr(i)
    return(h)

print("The decoded string:",decoding(encoding(s)))