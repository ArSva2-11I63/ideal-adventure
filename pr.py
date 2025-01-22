from math import sqrt
num = int(input("Enter a number to see if it is prime: "))
for i in range (2, int(sqrt(num) + 1)):
    if num % i == 0:
        print("Number is not prime.")
        break
    else:
        print("Number is prime.")


        


