from Mod_Arithmetic import do_add, do_divide, do_divide_int, do_modulus, do_multiply, do_power, do_sub
import Mod_Arithmetic

while True:
    number_1 = input("First Number: ") # asks for first number
    if number_1.lower() == 'quit': # available when user wants to exit the program
        break 
    number_2 = input("Second Number: ") # asks for second number
    if number_2.lower() == 'quit': 
        break

    print ('''              
          1 - Addition
          2 - Subtraction   
          3 - Multiplication    
          4 - Division  
          5 - Exponential Notation (First Number = Base; Second Number = Exponent)
          quit - Exits the program  
        ''') # displays the available operations
    
    operation = input('Operation: ').lower()
    print ("\n") # new line

    if operation == str(1): # addition
        print(f'Sum: {do_add(float(number_1), float(number_2))}')

    elif operation == str(2): # subtraction
        print(f'Difference: {do_sub(float(number_1), float(number_2))}')

    elif operation == str(3): # multiplication
        print(f'Product: {do_multiply(float(number_1), float(number_2))}')

    elif operation == str(4): # division
        print(f'Quotient: {do_divide(float(number_1), float(number_2))}') # display a quotient with a float 
        print(f'Integer: {int(do_divide_int(float(number_1), float(number_2)))}') # display a whole integer quotient
        print(f'Remainder: {int(do_modulus(float(number_1), float(number_2)))}') # display the remainder of the operation

    elif operation == str(5): # exponential notation
        print(f'Product: {do_power(float(number_1), float(number_2))}')
    elif operation.lower() == 'quit': # exit program
        break
    else:
        print ("Please type the correct input") # returns to the while loop to look for correct input
    
    while True:
        print ("\n")
        decision = input('Do you want to compute another set of numbers? (Y/N): ').lower()
        if decision == 'y':
            print ("\n")
            break # returns to initial while loop
        elif decision == 'n':
            quit() # terminate program
        else:
            print ('Please insert the correct input :)')
            continue # returns to while loop (line 43)
     

    