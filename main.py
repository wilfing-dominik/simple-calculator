def is_number(var): # Takes a string and tries to convert it to integer, float or complex type
    
    is_input_string = isinstance(var,str)
    if (is_input_string):

        is_input_float = "." in var
        if(is_input_float):
            try: # if this try block completes, that means the input is valid as a float type
                return float(var)
            except:
                print("The value you've given cannot be converted to a number")
                return None
        else:
            try: # if this try block completes, that means the input is valid as a integer type
                return int(var)
            except:
                try: # if this try block completes, that means the input is valid as a complex type
                    return complex(var)
                except:
                    print("The value you've given cannot be converted to a number")
                    return None
            
    else:
        print("The value you've given is not a string")
        return None


def valid_operator(op): # takes a string, if it's amongst the valid operator symbols, it returns true
    if op in ("+", "-", "*", "/"): return True
    return False
        

def ask_for_a_number(force_valid_input):
    while True:
        user_input = input("Enter a number: ")
        number = is_number(user_input)

        is_input_valid = number != None

        if not force_valid_input or is_input_valid:
            return number
    

def main():
    ask_for_a_number(True)


if __name__ == "__main__":
    main()