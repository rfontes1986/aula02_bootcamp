calculator_input = input("Please fill out a basic calculation in the form of 'x' OP 'y': ")

try:
    if str('+') in calculator_input:
        parts = calculator_input.split(str('+'))
        a = int(parts[0])
        b = int(parts[1])
        c = int (parts[2])
        calculator_output = a + b + c
    elif str('-') in calculator_input:
        parts = calculator_input.split(str('-'))
        a = int(parts[0])
        b = int(parts[1])
        calculator_output = a - b
    elif str('*') in calculator_input:
        parts = calculator_input.split(str('*'))
        a = int(parts[0])
        b = int(parts[1])
        calculator_output = a * b
    elif str('/') in calculator_input:
        parts = calculator_input.split(str('/'))
        a = int(parts[0])
        b = int(parts[1])
        if b == 0:
            calculator_output = "Not possible, deviding by zero is not allowed!"
        else:
            calculator_output = a / b
    elif str('^') in calculator_input:
        parts = calculator_input.split(str('^'))
        a = int(parts[0])
        b = int(parts[1])
        calculator_output = a ** b

    print (calculator_input, "=", calculator_output)

except NameError, ValueError:
    print ("Error!")