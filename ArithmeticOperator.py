"""
@author Md. Al Amin
TODO  Logical Operators and(&&), or(||), not(!)
TODO Ternary Operators=> condition ? val1 : val2;
"""
a, b, c = 2, 2, 3

val = "Equals" if a == b and b == c else "Not Equals"
print(val)
val = "Equals" if a == b or b == c else "Not Equals"
print(val)
val = "Equals" if not a == b else "Not Equals"
print(val)
