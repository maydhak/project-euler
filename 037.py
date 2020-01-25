def truncatable_prime(number, primes):
    numstr = str(number)
    end = 1
    truncatable = True
    while end < len(numstr) and truncatable:  # has already been determined to be prime so < will suffice
        slice = numstr[:end]
        if int(slice) not in primes:
            truncatable = False
        end += 1

    end -= 1
    while end > 0 and truncatable:
        slice = numstr[end:]
        if int(slice) not in primes:
            truncatable = False
        end -= 1
    return truncatable


def solution37():
    primes_found = {2}
    n = 3
    truncatable_primes_found = set()
    while len(truncatable_primes_found) < 14:  # 3, 5, 7 are also included using this method but there are only 11 relevant truncatable primes
        prime = True
        for p in primes_found:  # check the new number against all previously found primes
            if p < n/2:  # if the prime divisor > half the number, the quotient will be < 2 and it can no longer be prime; 2 is the smallest prime
                if n % p == 0:
                    prime = False
                    break  # breaks out of checking the number against previously found primes
        if prime:
            primes_found.add(n)
            if truncatable_prime(n, primes_found):
                truncatable_primes_found.add(n)

        n += 2  # prime numbers must be odd, so we will increment by 2
    return sum(truncatable_primes_found)-15  # 15 = sum of 3 + 5 + 7


print(solution37())  # Answer: 748317
