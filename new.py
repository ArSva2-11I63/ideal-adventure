def linear(n):
    iteration = 0
    for i in range (1, n+1):
        iteration+=1
    print("Total iterations done by the code when n = {} is {}.\n".format(n, iteration))

linear(1)
linear(10)
linear(100)

print("The time taken increases with increase in n value")


