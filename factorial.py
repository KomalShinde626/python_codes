# To take input from the user
num = int(input("Enter a number: "))

factorial = 0

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif the num == 0:
   print("then its factorial is 1.")
#add a condition for that.
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
