current = 1
previous = 0
amountorLimit = str(input("Do you want to have the amount of primes or a start to limit: "))


numberarray = []


def fibonacciSequence():
    global current, previous
    next = current + previous
    previous = current
    current = next
    return next
     
def startLimit(valueLimit, startInt):
    for i in range(0, 100000000):
        next = fibonacciSequence()
        if next > valueLimit:
            break
        if next >= startInt:
            numberarray.append(next)


def Amount(fibonacciLimit):
    for i in range(0, 10000000000000):
        next = fibonacciSequence()
        numberarray.append(next)
        if len(numberarray) == fibonacciLimit:
          break     

if amountorLimit == "amount":
    fibonacciLimit = int(input("Type in the amount of fibonacci numbers you want: "))
    Amount(fibonacciLimit)
elif amountorLimit == "start to limit":
    startInt = int(input("Type in the starting number: "))       
    valueLimit = int(input("Type in a value you do not want to exceed: ")) 
    startLimit(valueLimit, startInt)

print(numberarray)

