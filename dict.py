# create dict
a = {1:"abc", 2:"def"}
print(a)

# create from list of list of keys
b = [[1, "abc"], [2,"def"]]
print(dict(b))

# Get vs []
# If key is not present, using [] will throw
# Get will return None if optional value is not specified
# Eg for misssing key, hm.get(key) => None and hm.get(key,0) => 0
key = 3
if a.get(key):
    print("Found key", key, " and value ", a[key])
else:
    print("Key not found")

# Loop dictionary
def print_dictionary():
    def print_using_items(a):
        for k,v in a.items():
            print(k,v)

    def print_using_keys(a):
        for key in a.keys():
            print(key, a[key])

    def print_all_values(a):
        for value in a.values():
            print(value)

    a ={
        "Hello" : "World",
        "Space": "Exploration",
        "ML" : "Self Driving"
    }

    print_using_items(a)
    print_using_keys(a)
    print_all_values(a)

print_dictionary()

def zip_dictionaries():

    # Zip dictionaries
    a ={"Hello": 1, "World": 2}
    b ={"Universe": 3, "Kingdom":4}

    for m,n in zip(a,b):
        print(m+n, " => ", a[m]+b[n])

zip_dictionaries()

def dictionary_comprehension():
    # Example 1: Word count
    def word_count(words):
        res ={ word : words.count(word) for word in words}
        print(res)
    
    # Example 2 Character count
    def character_count(word):
        res= { char: word.count(char) for char in word}
        print(res)
    
    words = ["alpha", "beta", "alpha", "gamma"] *3

    word_count(words)
    character_count("Hello")

dictionary_comprehension()