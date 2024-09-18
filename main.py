# Thayer Yang
# 18 SEP 2024
# IPO Intro

#Input
num1 = float(input('Enter a number: (Example 7)\n'))
num2  = float(input('Enter another number: (Example: 4)\n'))

#Process
total = num1+num2

#Output
print(f'First number entered was: {num1}')
print(f'Second number entered was: {num2}')
print()
print(f'The sum of {num1} and {num2} is: {total}')

#Multiplication
num3 = float(input('Enter another number to multiply by: \n'))

new_total = total*num3

print(f'{total} times {num3} produces {new_total}')

#Subtraction
num4 = float(input('Enter another number to subtract by:\n'))

total = new_total

new_total = total - num4
print(f'{total} minus {num4} has a difference of {new_total}')

#Division
num5 = float(input('Enter a number to divide by (This value will be rounded):\n'))
total = new_total
new_total = total // num5
print(f'{total} divided by {num5} results in {new_total} rounded up')

#Exponents
num6 = float(input('Enter one last number:\n'))
total = new_total
new_total = total ** num6
print(f'{total} exponentiated to the power of {num6} equals {new_total}')



