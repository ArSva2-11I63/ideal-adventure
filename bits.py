def bit(n):
    i = 0
    while(n):
        i += 1
        n >>= 1
    return i

num1 = int(input("Enter a number: "))
a = bit(num1)
print("Number of bits: ",a)