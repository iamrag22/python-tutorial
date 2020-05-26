# del always removes at a specific index
# To find the first occurence in list from end, we cant use  a.index("foo", -1)
# as it only looks forward

# b = a.copy() => shallow coppy
# b = a.deepcopy() => deepcopy
# b = a => b has a ref to a. Changes to b will affect a 


# List with composite elements
a = [123, "Hello", 3.45]
print(a)

# Creata a list of characters
print( list("Hello"))

# Copy a list
b = a[:]
print(b)

foo = ["Hello", "World", "Universe", "Hello"]

# Reverse the list
foo.reverse()  # This wont create a new list
# print(foo)

# Append at end
foo.append("MilkyWay")

# Delete at index can be done using pop or delete
del foo[1]
print(foo)
val = foo.pop() # defaults to last position
print("Deleted ", val)

# Remove by value
a = [1,2,3,1,4,5,6,1]

# Removes first occurence
a.remove(1) # Does not create a new list
print(a)

foo = ["Hello", "World", "Hello", "Universe", "Hello"]

# Get Index of ele from beginning
print(foo.index("Hello"))

# Get Index of ele starting from index
print(foo.index("Hello", 3))

# Count of ele
print(foo.count("Hello"))


# Sorting
import random
x = random.sample(range(10,20), 7)
print(x)

# Get a copy o sorted list
y = sorted(x)
print(y)

# In place sort
x.sort()
print(x)

# Reverse sort
a = [1,2,3]
a.sort(reverse=True)
print("Reverse sorted list ", a)
print("Reverse sorted list ", sorted(a, reverse=True))


# Change values by assignment
a = [ 1,2,3]
b = a 
a[1] = 5
print(a,b) # Should be same value


# Print a list from end
a = [1,2,3,4]
for i in reversed(a):
    print(i)

# Print a list using its index
a=[1,2,3,4,5]
for i in range(len(a)):
    print(a[i])

# Combine Multiple lists using zip
# Zip stops when the shortest sequence ends
a= [1,2,3]
b=["x", "y", "z"]

for k,v in zip(a,b):
    print(v," => ", k)


# Tuples : Values don't change
# We can't create tuple directly as (a,b). Instead we should do a,b
# Tuple values can be accessed by [] just like list
a = 'foo','bar'
print(a)

# Loop through tuples
for entry in a:
    print(entry)
# loop using index
for i in range(len(a)):
    print(i, a[i])


def list_comprehension():
    def build_2d_array():
        a = range(1,3)
        b = range(1,4)
        grid = [[r,c] for r in a for c in b]
        print(grid)
    
    build_2d_array()

    def build_2d_boolean_array():
        a = range(3)
        b = range(4)
        grid = [[-1 for col in b] for row in a]
        print(grid)
    build_2d_boolean_array()

    def print_even_nums():
        a =[1,2,3,4,5,6,8]
        b = [num for num in a if num%2==0 ]
        print(b)
    print_even_nums()

    def print_even_odd():
        a =[1,2,3,4,5,6,8]
        b = ["Even" if num%2==0 else "Odd" for num in a]
        print(b)
    print_even_odd()


list_comprehension()