def is_number(var): # Takes a string and tries to convert it to integer or float type
    
    is_input_string = isinstance(var,str)
    if (is_input_string):

        is_input_float = "." in var
        if(is_input_float):
            try:
                print(float(var))
                return float(var)
            except:
                print("The value you've give cannot be converted to a number")
                return None
        else:
            try:
                print(int(var))
                return int(var)
            except:
                print("The value you've give cannot be converted to a number")
                return None
    else:
        print("The value you've given is not a string")
        return None


def main():
    pass

if __name__ == "__main__":
    main()