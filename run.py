import json
import argparse
import template

def write_functions_to_C_file(functions, c_filepath):
    print("Write function to C file")

def write_function_prototypes_to_H_file(functions, h_filepath):
    print("Write function to H file")



# TODO
# Place functions in C file
# Place function Prototypes in associated header 

def main():
    # # Setup to Receive Command Line Args
    # parser = argparse.ArgumentParser(description="Generate Device Hex Code")
    # parser.add_argument("--template_json", action="store", dest="template_json", required=True, help="Provide the path of the template funtions JSON")

    # # Args list
    # given_args = parser.parse_args()
    
    # # Extract each argument
    # build = given_args.build
    # rand_path = given_args.rand_path
    # config_path = given_args.config_path
    Template()
    print("Hello")

if __name__ == "__main__":
    main()

