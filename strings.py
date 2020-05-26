# Python strings are immutable

# String operations

a = "Hello World"

# Substring
print(a[3:len(a)])

# Get last 3 chars
print(a[len(a)-3:])

# Reverse
print("Reverse ", a[::-1])

# Combine multiple strings
c = "-".join(b)
print(c)

# Find first occurence
a = "foobarfoo"
print(a.find("foo"))

# Look for first occuence startig at an index
print(a.find("foo", 2))

# Find last occuerence
print(a.rfind("foo"))

# Count
print("abcabcabcdefghi".count("abc"))

# Convert CAse
print(a.upper())
print(a.lower())

# Replace
# Replace by default replaces all occurences
print(a.replace("foo", "goo"))

# Replace only first n occurences
print("abcabcabc".replace("abc", "def", 2))


# String equality/comparison
a = "Hello"
b = "hello"
c = "Hello"
print(a==b, a is b)
print(a==c, a is c)

# Split a string
b = "Hello World".split(" ")
print(b)

#split on \  requires an extra \ 
hoo =r"hello\world\univ".split("\\")
print(hoo)
