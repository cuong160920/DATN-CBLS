a = [1, 3, 4]
b = a.copy()

b[1] += 1

print(a)
print(b)

a = b.copy()

a[1] += 1
print(a)