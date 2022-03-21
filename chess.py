row = [1, 2, 3, 4, 5, 6, 7, 8]
r = 8
c = 8
d = []
d1 = (r+2, c+2)
d2 = (r-2, c+2)
d3 = (r-2, c-2)
d4 = (r+2, c-2)
d.append(d1)
d.append(d2)
d.append(d3)
d.append(d4)
for i in range(len(d)):
    t1 = d[i]
    if i == len(d) - 1:
        t2 = d[0]
    else:
        t2 = d[i + 1]
    mid = ((t1[0] + t2[0]) // 2, (t1[1] + t2[1]) // 2)
    p1 = ((t1[0] + mid[0]) // 2, (t1[1] + mid[1]) // 2)
    p2 = ((t2[0] + mid[0]) // 2, (t2[1] + mid[1]) // 2)
    if p1[0] in row and p1[1] in row:
        print(p1)
    if p2[0] in row and p2[1] in row:
        print(p2)


