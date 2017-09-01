'''
Prompt: Write a program that asks the user how many Fibonnaci numbers to
generate and then generates them. Take this opportunity to think about how you
can use functions. Make sure to ask the user to enter the number of numbers in
the sequence to generate.
'''

from sys import exit

print("This program is generates fibonacci numbers.")
print("How many fibonacci numbers would you like? (integers only, no decimals)")
number = input("> ")

# Check to make sure the user input is a number
try:
    integer = int(number)
except ValueError:
    print("That's not an integer!")
    exit()

# Check to make sure the user input is greater than one
if int(number) <= 0:
    print("Please enter a number greater than or equal to 1")
    exit()

def append_fibonacci(start,stop):
    Fibonacci = [start,start + 1]
    while len(Fibonacci) <= (int(stop)):
        a = int(Fibonacci[-2]) + int(Fibonacci[-1])
        Fibonacci.append(a)
    print(Fibonacci[1:])

append_fibonacci(0,number)
