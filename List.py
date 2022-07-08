"""
@author Md. Al Amin
TODO  Lists are mutable.
This means we can change an
item in a list by accessing it directly
as part of the assignment statement.
"""
lists = ["Java", "Python"]
print(lists)
print(lists[0])
del lists[1]
print(lists)
lists.append("C++")
print(lists)
lists.insert(0, "C")
print("C" in lists)
print("C" not in lists)
lists.clear()
print(lists)
