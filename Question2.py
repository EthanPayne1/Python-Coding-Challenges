
def convert_to_float(input_str: str, default: float) -> float:
    # Write a function that takes a string that may be a float, 
    # and returns either the converted string as float or the default value provided as an argument if the string does not represent a float.

    try:
        return float(input_str)
    except ValueError:
        print("String does not represent a float: ")
        return 0.0
    
input_str = input("Enter the string: ")
default = float(input("Enter float point: "))
ans = convert_to_float(input_str,default)  
print("Converted Float: " , ans)