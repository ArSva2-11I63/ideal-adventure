def prim(n):
    prime = [True for i in range(n+1)]
    currentNumber=2
    while(currentNumber**2 <=n):
        if prime[currentNumber] == True:
            for i in range(currentNumber ** 2, n + 1, currentNumber):
                prime[i] = False
        currentNumber += 1
    for p in range(n+1):
        if prime[p]:
            print(p)
        
n = int(input("Enter a number:"))

prim(n)
