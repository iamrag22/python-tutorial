from collections import defaultdict, OrderedDict, Counter, namedtuple, deque

# Note: Dont use default dict if you are only looking to check the presence of key
# as this will update the dict with missing key
def default_dict_example():
    a = defaultdict(int) # the int represents the default value for each key
    a[1] = 2
    print(a[2]) # This wont throw an exception

default_dict_example()

# Ordered Dictionary is not about soting.  It maintains the insertion order
def ordered_dict_example():
    a = OrderedDict()
    a["foo"] = 10
    a["bar"] = 15
    print(a) # Maintains the insertion order foo, bar

ordered_dict_example()

# Very useful for counting frequency in list, tuple etc
def counter_example():
    a = Counter([10,20,10,15,20,20, 5])
    print(a)

    # Get the 2 most common elements
    print(a.most_common(2))

    # Get all the counts in descending order
    print(a.most_common())

counter_example()

# Named tuple: Access tuple values by name
# the namedtuple() takes 2 parameters, first is the tuple name,
# the second is a string of all tuple entries separated by commas
def named_tuples_example():
    a = namedtuple('a', "Bothell,Redmond,Bellevue")
    zipcodes = a('98012', '98052', '98007')
    print(zipcodes.Bothell)
named_tuples_example()


# Dequeue = Stack + Queue
def deque_example():
    a = deque()

    # Check if empty
    if not a:
        print("Its empty")
    
    # Add to end (right)
    a.append(1)
    a.append(2)
    a.append(3)

    # Add to beginning (left)
    a.appendleft(4)

    # pop from right
    a.pop()

    # pop from left
    a.popleft()

    # Left most 
    print(a[0])

    # Right most
    print(a[-1])

    a.extend([1,10,11,12,1,1])

    # Size
    print(len(a))

    # Remove the first occurence
    a.remove(1)
    
    # Get count of an element
    # Returns 0 if not found
    print(a.count(1))
    
    print(a)

deque_example()