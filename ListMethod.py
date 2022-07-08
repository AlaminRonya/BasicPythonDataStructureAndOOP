"""
@author Md. Al Amin
TODO  Lists of Method
"""
lists = [1, -1, -20, 20]
print(lists)
lists.sort()
print(lists)
lists.sort(reverse=True)
print(lists)
print(lists[0:2])
print(lists.pop())
copyOfList = lists.copy()
print(copyOfList)
