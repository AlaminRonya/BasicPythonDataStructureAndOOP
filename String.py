"""
Md. Al Amin
String is an immutable type
"""
name = "I love Python"
print("Length : ", len(name))
replaceName = name.replace('o', 'u')
print(replaceName)
print("First char : ", name[0])
print("Last char : ", name[len(name) - 1])
print("Last char : ", name[-1])

print("Reverse ->", name[::-1])
print(name.__contains__("Python"))
print(name[0:5])
