a = 5
b = 1245
digits = [int(ch) for ch in str(b)]
e = a*(a+1)//2
s = sum(digits)
m = e-s
print(m)