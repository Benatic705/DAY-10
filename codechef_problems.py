# Problem 1 - Add Two Numbers
a = 10
b = 20
print("Addition:",a+b)

# Problem 2 - Even or Odd
num = 15

if num % 2 == 0:
   print("Even")
else:
   print("Odd")

# Problem 3 - Largest Number
a = 25
b = 40

if a > b:
    print("Largest:", a)
else:
    print("Largest:", b)


# Problem 4 - Factorial

n = 5
fact = 1

for i in range(1,n + 1):
    fact = fact * i

print("Factorial:", fact)

# Problem 5 - Sum of Digits

num = "12345"
total = 0

for digit in num:
    total += int(digit)

print("Sum of Digits:", total)

 
 