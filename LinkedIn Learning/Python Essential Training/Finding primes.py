def allPrimesUpTo(num):
    primes = [2]
    count = 0
    for numbers in range(3, num):
        for items in primes:
            if (numbers % items) == 0:
                break

            elif items != primes[-1]:
                continue

            else:
                primes.append(numbers)
                break
            

    return primes

allPrimesUpTo(100)
