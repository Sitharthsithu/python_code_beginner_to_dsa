#Input: n = 19
#Output: True
#19 is Happy Number,
#1^2 + 9^2 = 82
#8^2 + 2^2 = 68
#6^2 + 8^2 = 100
#1^2 + 0^2 + 0^2 = 1
#As we reached to 1, 19 is a Happy Number.

#Input: n = 20
#Output: False


#def separate(n):
#    c=list(str(n))
#    print(c)
#    d=c[0]
#    e=c[1]
#    happy(d,e)

#def happy(d,e):
#    d,e=d**2,e**2
#    f=d+e
#    separate(f)
    
#print(separate(19))




def is_happy_recursive(n, seen=set()):
    if n == 1:
        return True
    if n in seen:
        return False
    seen.add(n)
    new_n = sum(int(d)**2 for d in str(n))
    return is_happy_recursive(new_n, seen)

print(is_happy_recursive(19))  




