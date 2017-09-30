a = [0, 1]
for n in range(2, 10):
    a.append(5*a[n-1] - 6*a[n-2])
print(a)