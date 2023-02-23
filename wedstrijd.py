import time
primeNumbers = []

numberRange = int(input('give me your range: '))
startTijd = time.time()

def isPrimeNumber(num):
    if num > 1:
        for number in range(2, int(num ** 0.5) + 1):
            if num % number == 0:
                return False
        return True
    return False

for num in range(0, numberRange):
    if isPrimeNumber(num) == True:
        primeNumbers.append(num)


executieTijd = time.time() - startTijd
print(f'i found {len(primeNumbers)} prime numbers in {executieTijd} seconds')