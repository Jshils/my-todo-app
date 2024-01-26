FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    # you can define a default parameter in a function definition
    #Doc strings can be used to print out instructions when the
    # user requests help on a function
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do item in the text file."""
    # All non default parameters must be before default parameters
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# This will only run if the program functions is run directly and not through a call. If run directly the value
# of __name__ is __main__ and is a string. If this function is imported into another program the value of
# __name__ is functions

if __name__ == "__main__":
    print("Hello from functions")
    print(get_todos())