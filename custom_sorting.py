def simple_example():
    a = [[1,"Foo"], [2,"Bar"], [2,"Aaz"]]

    from operator import itemgetter
    a.sort(key=itemgetter(1)) # sort on second value in a list
    print(a)
simple_example()

def sorting_using_lambda():
    a = [("abc", 10), ("abc", 15), ("ad", 9)]
    # This lambda takes a tuple (condition1, condition2)
    # First sort on condition1 then on condition 2
    a.sort(key =lambda x: (-x[1], x[0]))  
    print(a)
sorting_using_lambda()
