import json
import argparse
from template import Template

def write_functions_to_C_file(functions, c_filepath):
    print("Write function to C file")

def write_function_prototypes_to_H_file(functions, h_filepath):
    print("Write function to H file")



# TODO
# Place functions in C file
# Place function Prototypes in associated header 

def main():
    # Setup to Receive Command Line Args
    parser = argparse.ArgumentParser(description="Build C Functions from Templates")
    parser.add_argument("--json", action="store", dest="template_json", required=True, help="Provide the path of the template funtions JSON")

    # Args list
    given_args = parser.parse_args()
    
    # Extract each argument
    json_path = given_args.template_json

    # Retreive JSON data
    with open(json_path) as template_file:
        template_data = json.load(template_file)

    # TODO: conver JSON data into appropriate objects
    print(template_data)

    temp = Template("ret", "arg", "hello")

if __name__ == "__main__":
    main()

