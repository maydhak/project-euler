"""
Problem 7:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10,001st prime number?
"""
def solution7():
    primes_found = {2}
    n = 3
    while len(primes_found) < 10001:
        prime = True  # assume the number is prime to start with
        while prime:
            for p in primes_found: # check the new number against all previously found primes
                if p < n/2:  # if the prime divisor > half the number, the quotient will be < 2 and it can no longer be prime; 2 is the smallest prime
                    if n % p == 0:
                        prime = False
                        break  # breaks out of checking the number against previously found primes
            if prime:
                primes_found.add(n)
                break  # breaks out of checking this particular number
        n += 2  # prime numbers must be odd, so we will increment by 2
    print(max(primes_found))