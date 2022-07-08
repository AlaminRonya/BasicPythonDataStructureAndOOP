import keyword

# class Computer:
#     def __init__(self, cpu, ram):
#         self.cpu = cpu
#         self.ram = ram
#
#     def config(self):
#         print("Config is ", self.cpu, self.ram)
#
#
# a = "15"
# c = Computer("Dell", "8gb")
# c1 = Computer("Hp", "8gb")
# Computer.config(c)
# Computer.config(c1)
# print("\n")
# c.config()
# c1.config()

t = (("Al Amin", 4, 5), 4, "ek")
print(type(t))
arr = ["alamin", "Saima", "Jahangir"]
arr1 = ["Akash", "Book"]
arr.extend(arr1)
print(arr[:-1])
print(arr[1:-1])
print(arr)

name: str = "Md. Al Amin Islam"


def hello() -> str:
    return "Hello Python"


newName = name.replace("M", "a")
search = "in" in name
print("Search===>", search)
search = "in" not in name
print("Search is not ===>", search)
print(name)
print(newName)
print(hello())

longStr = "Md. Al Amin" \
          " Islam" \
          " Rony"
print(longStr)
secondName= "Rony"
longStr = """
Hello, {} {}
How are you?
It was nice talking to you.
"""

print(longStr.format(name, secondName))
longStr = f"""
Hello, {name} {secondName}
How are you?
It was nice talking to you.
"""

print(longStr)

print(keyword.kwlist)
