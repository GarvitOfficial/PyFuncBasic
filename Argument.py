def positional_args(arg1, arg2):
    print("Positional arguments:")
    print("arg1:", arg1)
    print("arg2:", arg2)

def default_args(arg1, arg2=10):
    print("Default arguments:")
    print("arg1:", arg1)
    print("arg2:", arg2)

def keyword_args(arg1, arg2):
    print("Keyword arguments:")
    print("arg1:", arg1)
    print("arg2:", arg2)

def variable_args(arg1, *args):
    print("Variable arguments:")
    print("arg1:", arg1)
    print("args:", args)

def keyword_variable_args(arg1, **kwargs):
    print("Keyword variable arguments:")
    print("arg1:", arg1)
    print("kwargs:", kwargs)

# Function call with positional arguments
positional_args("Hello", "World")

# Function call with default arguments
default_args("Hello")
default_args("Hello", 20)

# Function call with keyword arguments
keyword_args(arg2="World", arg1="Hello")

# Function call with variable arguments
variable_args("Hello", "World", "Python", "Programming")

# Function call with keyword variable arguments
keyword_variable_args("Hello", name="John", age=30, city="New York")
