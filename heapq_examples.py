import heapq

class Node(object):
    def __init__(self, name, id):
        self.name = name
        self.id =id 
    def __rep__(self):
        return self.name
    def __lt__(self, other):
        if other is None:
            return -1
        elif self.name!=other.name:
            return self.name<other.name
        else :
            return self.id-other.id
        
def min_heap_example():

    def basic_example():
        a = [7,2,1,4,3, 6, 5]
        # Build heap from existing list
        heapq.heapify(a)
        # print(a)

        # Build min heap from scratch
        a = []
        heapq.heappush(a,5)
        heapq.heappush(a,3)
        heapq.heappush(a,1)
        heapq.heappush(a,8)
        heapq.heappush(a,7)
        heapq.heappush(a,9)

        # Get the peek el
        print(a[0])
        
        # Pop the min element
        print(heapq.heappop(a))

        # Pop and push in 1 operation
        # First removes the min and then adds the new el
        print(heapq.heappushpop(a,4))

        # Get k largest elements
        print(heapq.nlargest(3,a)) # Returns [9,8,7]

        # Get k smallest ele
        print(heapq.nsmallest(3,a)) # Prints [4,5,7]
    
    basic_example()

    def custom_comparision():
        a = []
        heapq.heappush(a, Node("Foo",12))
        heapq.heappush(a, Node("Bar", 20))
        heapq.heappush(a, Node("Bar", 13))
        print(type(a))
        print(a[0].id, a[0].name)
        print(a[1].id, a[1].name)
        print(a[2].id, a[2].name)
        

    custom_comparision()

min_heap_example()


def max_heap_example():
    def basic_example():
        a = []
        heapq.heappush(a,-1)
        heapq.heappush(a, -5)
        heapq.heappush(a, -7)
        heapq.heappush(a, -8)
        print(a)

    basic_example()

max_heap_example()
