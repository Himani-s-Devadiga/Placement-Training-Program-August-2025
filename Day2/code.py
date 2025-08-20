# Sum of Digits of a Number
num = int(input("Enter a number: "))
sum_digits = 0
while num > 0:
    digit = num % 10
    sum_digits += digit
    num //= 10
print("Sum of digits:", sum_digits)

# Check Armstrong Number
num = int(input("Enter a number: "))
sum_digits = 0
temp = num
length = len(str(num))
while temp > 0:
    digit = temp % 10
    sum_digits += digit ** length
    temp //= 10
if sum_digits == num:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")

#--> Print Armstrong Numbers Between 1 and 1000
num = 1
while num <= 1000:
    temp = num
    sum_digits = 0
    length = len(str(num))
    while temp > 0:
        digit = temp % 10
        sum_digits += digit ** length
        temp //= 10
    if sum_digits == num:
        print(f"{num} is an Armstrong number")
    num += 1

4. String and ASCII Manipulations
# Assigning string
str1 = "Python"
print(str1)  # Output: Python

# Using str as function (illustration)
x = 100
y = str(x)
print(y)  # Output: '100'

# ASCII codes
r = "Python"
for char in r:
    print(ord(char))  # prints ASCII of each character

5. Lists, Tuples, and Data Structures
# List manipulation
a = [1,2,3,5]
if a.sort() == sorted(a):
    print("Sorted")
else:
    print("Not sorted")

# Tuple example
t = (5, 0)
print(t*2)  # Tuple repeated twice

# Dictionary example
data = {
    'name': 'Sumanth',
    'branch': 'CSE',
    'Skills': 'Python'
}
print(data['name'])
print(data.get('branch'))
print(data.get('email'))  # None if key doesn't exist

6. String Operations
st1 = "Python Learning"
st2 = st1[:5]*2 + st1[:4]
st3 = st2[:5//2] + "3"
print(st3)

Notes

Unicode characters: 1,62,000 total; ASCII codes for capital and small letters: 255 codes.

isinstance() can be used to check type of variables.

Loops and conditionals are essential for algorithms like Armstrong number, sum of digits, etc.
