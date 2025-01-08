def printnumber(n):
    print("The value of n is",n)
    iteration = 0
    for i in range(0, n+1):
        for j in range (0, n+1):
            iteration +=1

    print("Total number of iterations is {}x{} = {}".format(n, n, n*n))
    print("\n")

printnumber(1)
printnumber(5)
printnumber(10)

print("\nThe time taken increases with increase in n^2")