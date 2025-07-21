#Input: s = "the sky is blue"
#Output: "blue is sky the"


s = "the sky is blue"
c=[]
for i in s.split():
    c.append(i)
d=c[::-1]
print(" ".join(d))


s = "the sky is blue"
c=[]
for i in s.split():
    c.append(i)
d=c[::-1]
for s in d:
    print(s, end=" ")