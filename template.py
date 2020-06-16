# Function Argument Class
class Arg:
    def __init__(self, arg_name, arg_type):
        self.arg_name = arg_name
        self.arg_type = arg_type

    def get_arg_name(self):
        return arg_name

    def get_arg_type(self):
        return arg_type


# Function Template Class
class Template:

    # return_type -- Type: String
    # arguments -- Type: List of Arg class
    # function_names -- Type: List of Strings
    def __init__(self, return_type, arguments, function_names):
        self.return_type = return_type
        self.arguments = arguments
        self.function_names = function_names


    def generate_functions(self):
        print("generating functions")

    def generate_function_prototypes(self):
        print("generating function prototypes")