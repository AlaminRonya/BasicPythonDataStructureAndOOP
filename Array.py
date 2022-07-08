"""
Md. Al Amin
Array
"""
# importing "array" for array creations
import array as arr
# array with int type
ar1 = arr.array('i', [1, 2, 3, 4, 5])
for i in ar1:
    print(i)

ar2 = arr.array('i', [])
n = 5
for i in range(0, n):
    ar2.append(int(input()))

print(ar2)
print(type(ar2))


