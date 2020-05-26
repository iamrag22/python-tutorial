# Notes
# None is not False. Empty lists, string, dict evaluate to False but are not None
# use "is None" for None check

def none_example():

    def none_example(a):
        if a is None:
            print("This is None")
        elif a:
            print("This is not empty and is True") 
        else:
            print("This is empty")

    none_example(None)
    none_example("abc")
    none_example([])

none_example()

# Default parameters are resolved at compile time and not run time
# The correct usage is to initialize the default param to None
# Be aware of using mutable types in default parameters

def default_paramaters_example():
    def default_paramaters_wrong_usage(name, stuff=[]):
        stuff.append(name) 
        print(stuff)
    
    default_paramaters_wrong_usage("Hello") # stuff has ["Hello"]
    default_paramaters_wrong_usage("World") # stuff has ["Hello, "World]

    def default_paramaters_correct_usage(name, stuff=None):
        if stuff is None:
            stuff=[]
        stuff.append("Hello")
        print(stuff)
    
    default_paramaters_correct_usage("Hello")
    default_paramaters_correct_usage("World")

default_paramaters_example()


def arguments_example():
    def positional_arguments(foo, bar, zoo):
        print(foo, bar, zoo)
    
    # Variable tuple of args should always come at the the end
    def positional_arguments_args(foo_string, bar_string, *args):
        print(foo_string, bar_string)

        for param in args:
            print(param)
    
    positional_arguments_args("foo", "bar", [1,2,3], {"a":1,"b":2})

    # Order of parameters: positional -> *args -> **kwargs
    def positional_arguments_kwargs_example(foo_string, *args, **kwargs):
        print(foo_string)
        
        for item in args:
            print(item)
        
        for k,v in kwargs.items():
            print(k, v)
        
    # Don;t wrap the kwargs inside {} Specify them as key1=value1, key2=value2..
    positional_arguments_kwargs_example("foo", 1,2,3, name="Hello", city="Bothell")
arguments_example()

def function_with_func_parameters_examples():
    def concat_strings(*args):
        res = " ".join(list(args[0]))
        print(res)

    def function_with_func_parameters(func, *args):
        return func(args)

    # inbuilt function sum()
    function_with_func_parameters(sum, 1,2,3,4)
    
    # user defined functions
    function_with_func_parameters(concat_strings, "Hello", "World")


def lambda_example():
    def helper_func(word, func):
        res= func(word)
        print(res)
    
    helper_func("heLlo", lambda x: x.upper())

lambda_example()
