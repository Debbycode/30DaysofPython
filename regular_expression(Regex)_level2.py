print('======================One===================')

import re

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"

def is_valid_variable(name):
    return re.match(pattern, name) is not None

# Example usage
print(is_valid_variable("valid_variable_name"))  # Output: True
print(is_valid_variable("1invalid_variable_name"))  # Output: False
print(is_valid_variable("validVariableName"))  # Output: True
print(is_valid_variable("_valid_variable_name"))  # Output: True
print(is_valid_variable("valid-variable-name"))  # Output: False
