s = "babad"
n = len(s)
l = ""
c=0

for i in range(n):
    for j in range(i, n):
        sub = s[i:j+1]
        if sub == sub[::-1] and len(sub)>c:
            c=len(sub)
            l=sub
print(l,c)
