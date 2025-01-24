def OddEven(n):
    if (n^1) == n + 1:
        return True
    else:
        return False
    
num1 = int(input("Enter a number: "))

if OddEven(num1):
    print(num1,"is even.")
else:
    print(num1,"is odd.")
    