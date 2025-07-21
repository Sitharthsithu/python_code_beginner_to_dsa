items = [("Tomato", 2.0, 3), ("Potato", 1.5, 10), ("Tomato", 2.0, 2), ("Carrot", 1.0, 8), ("Potato", 1.5, 5)]
c=[]
d=0
for i in items:
    c.append(list(i))
for j in range(len(c)):
    d+=(c[j][1]*c[j][2])
    #print(c)
#print(c[0][1])
print("Total Sales: ${}".format(d))
print("Average Sales: $",d/len(c))

#Total Sales: $47.50
#Average Sales: $9.50
#Best Selling Item: Potato