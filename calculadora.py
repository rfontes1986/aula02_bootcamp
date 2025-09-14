calculator_input = input("Please fill out a basic calculation in the form of 'x' OP 'y': ")

parts = calculator_input.split(('+'))

a = int(parts[0])
b = int(parts[1])

calculator_output = a + b

print (calculator_input, "=", calculator_output)