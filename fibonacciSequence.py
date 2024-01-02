current = 1
previous = 0

fibonacciLimit = int(input("Type in the amount of fibonacci numbers you want: "))
valueLimit = input("Type in a value you do not want to exceed: ")


if valueLimit == "None":
    valueLimit = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    int(valueLimit) 
else:
    print("Invalid input")       

def fibonacciSequence():
    global current, previous
    next = current + previous
    previous = current
    current = next
    return next

for i in range(0, fibonacciLimit):
    next = fibonacciSequence()
    if next > valueLimit:
        break
    else:
        print(next)
        i += 1

# Print the last valid Fibonacci number
if next <= valueLimit:
    print(next)
