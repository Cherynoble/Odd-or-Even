input1 = int(input('Enter number of odd even checks:'))   # This is the input for the max number the code will count to

print('print(f"type 0 to cancel during process")')   # This will be the cancel value for the printed code when running

print('\n')   # New line to look good
print("def loop1():")  # Defining the loop that will be the number checking code
print("    while True:")  # While true function for the loop
print('        num = int(input("Enter number: "))')  # Input from user to check if a number is odd or even

print(f"        if num == 1:")  # Outside of loop so it can begin with an "if" statement
print('            print("odd")')  # The spaces are for the formatting. They should be correct
print('            continue')

for input1 in range(2, input1+1):  # Starts from 2 because 1 is already printed above. "input+1" final value = input1
    if input1 % 2 == 0:  # Divides and checks for remainder, if = 0 it is even, if not it is odd
        print(f"        elif num == {input1}:", sep='')
        print('            print("even")')
        print('            continue')  # More formatting spaces and continue function to continue looping
    else:
        print(f"        elif num == {input1}:", sep='')
        print('            print("odd")')
        print('            continue')  # Same as above but for odd numbers

print("        elif num == 0:")  # This is the break command
print("            break")

print('\n')  # Formatting
print('def main():')  # The main loop
print('    loop1()')

print('\n')
print('if __name__ == "__main__":')
print('    main()')
