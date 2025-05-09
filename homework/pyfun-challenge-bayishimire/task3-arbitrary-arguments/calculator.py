def add(*args):
#return all sum
    return sum(args)

def multiply(*args):
    #return multiplication of all aruguments
    result = 1
    for num in args:
        result *= num
    return result

def subtraction(*args):
    # Return the difference of all arguments
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def division(*args):
    #Return the division of all arguments."""
    result = args[0]
    for num in args[1:]:
        if num == 0:
            raise ZeroDivisionError("imposible division zero")
        result /= num
    return result

def calculate(*args, **kwargs):
#calculation
    # Check if all args are numbers
    for num in args:
        if not isinstance(num, (int, float)):
            raise TypeError("All arguments must be numbers")
    
    # Ensure at least one argument is provided
    if len(args) == 0:
        raise ValueError("At least one argument is required")
    
    # Get the operation from kwargs
    operation = kwargs.get("operation")
    if not operation:
        raise ValueError("Operation must be specified")
    
    # Perform the specified operation
    if operation == "add":
        return add(*args)
    elif operation == "multiply":
        return multiply(*args)
    elif operation == "subtraction":
        return subtraction(*args)
    elif operation == "division":
        return division(*args)
    else:
        raise ValueError("Invalid operation specified")

if __name__ == "__main__":
    # Test the calculator function
    try:
        number1=int(input("Enter the first number: "))
        number2=int(input("Enter the second number: "))
        number3=int(input("Enter the third number: "))
        print("Choose an operation: add, multiply, subtraction, division")  

        print(calculate(number1, number2, number3, operation="add"))
        print(calculate(number1, number2, number3, operation="subtraction"))
        print(calculate(number1, number2, number3, operation="multiply"))     
        print(calculate(number1, number2, number3, operation="division"))   
    except Exception as e:
        print(f"Error: {e}")
              