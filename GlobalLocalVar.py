# Global variable
global_var = 10

def update_global_var():
    # Accessing the global variable
    global global_var
    global_var += 5

def local_variable_example():
    # Local variable
    local_var = 20
    print("Local variable:", local_var)

    # Accessing the global variable
    global_var = 15
    print("Global variable (inside function):", global_var)

# Accessing the global variable before modification
print("Global variable (before modification):", global_var)

# Modifying the global variable
update_global_var()

# Accessing the global variable after modification
print("Global variable (after modification):", global_var)

# Calling the function that uses local variables
local_variable_example()
