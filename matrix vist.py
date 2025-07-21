a = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

n = len(a)
m = len(a[0])

top = 0
left = 0
right = m - 1
bottom = n - 1
num = 1

while top <= bottom and left <= right:
    for i in range(left, right + 1):
        a[top][i] = num
        num += 1
    top += 1

    for i in range(top, bottom + 1):
        a[i][right] = num
        num += 1
    right -= 1

    if top <= bottom:
        for i in range(right, left - 1, -1):
            a[bottom][i] = num
            num += 1
        bottom -= 1
    if left <= right:
        for i in range(bottom, top - 1, -1):
            a[i][left] = num
            num += 1
        left += 1

for row in a:
    print(row)