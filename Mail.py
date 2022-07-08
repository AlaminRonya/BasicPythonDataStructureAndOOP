"""
Md. Al Amin
Mail formatting
"""
name = "Python"
mail = """
Hi, {}.
How are you?
"""
print(mail.format(name))
mail = F"""
Hi, {name}.
How are you?
"""
print(mail)
