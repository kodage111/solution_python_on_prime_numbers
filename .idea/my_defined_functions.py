def primeNumbers(endRange):
    primeNumbers = []
    for number in range(2, endRange):
        primeNumber = number
        # primeNumbers.append(number)
        if(number == 2):
            primeNumbers.append(primeNumber)
        elif(number%2 == 1):
            for n in range(2, 10):
                if(number%n == 0 and n != number):
                    primeNumber = None
                    break
            if(primeNumber != None): primeNumbers.append(primeNumber)
    return primeNumbers