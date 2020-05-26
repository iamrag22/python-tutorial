# Python3 does not have  Integer.max or min. Use sys.maxsize for max and sys.minsize for min
#For custom sorting on objects, dont use comparision.  Instead use
#    1. l.sot(key = lambda x: x.property) # only 1 property
#    2.  l.sort(key =lambda x: (x.property1,x.property2)) # on 2 properties
#    override __eq__(self, other) and any of __lt__, __gt__,__ne__ . For this use @functools.total_ordering
