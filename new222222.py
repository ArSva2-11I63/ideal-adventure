num1 = int(input("Enter number"))
num2 = int(input("Enter another number:"))

num3 = num1
num4 = num2

while num2:
    numStore = num2
    num2 = num1%num2
    num1 = numStore

print("HCF of {} and {} is {}".format(num3, num4, num1))

LCM = num3 * num4 /  num1
print("LCM of {} and {} is {}".format(num3, num4, LCM))