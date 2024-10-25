def allPrimesUpTo(num):
    primes = [2]
    count = 0
    for numbers in range(3, num):
        for items in primes:
            if (numbers % items) == 0:
                break


            elif  items != primes[-1]:
                continue

            elif  count == 3:
                primes.append(numbers)
                break


            else:
                primes.append(numbers)
                count += 1
                break
            

    return primes

allPrimesUpTo(100)
