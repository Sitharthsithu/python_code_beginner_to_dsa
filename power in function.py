a=44
b=-2

print(a**b)
def pow(x,n): #x is no. and the n is the power pa
    if n==0:
        return 1
    elif(n>0):
        return x*pow(x,n-1)
    else:
        return 1/pow(x,-n)

d=pow(a,b)
print(d)