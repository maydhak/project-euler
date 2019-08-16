"""
Problem 10:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

# My first solution was to just change the check in the while loop to 'max(primes_found) < 2000000'
# and change 'max' to 'sum' in the last line of the program. But it was taking WAY too long to compute.
# Then I realized n = max(primes_found) and that one of the while loops was really unnecessary. After making
# these changes, the program ran a bit faster but still took quite a while (about half an hour). Still, it does
# give the right result.

def solution10():
    primes_found = {2}
    n = 3
    while n <= 2000000:
        prime = True
        for p in primes_found: # check the new number against all previously found primes
            if p < n/2:  # if the prime divisor > half the number, the quotient will be < 2 and it can no longer be prime; 2 is the smallest prime
                if n % p == 0:
                    prime = False
                    break  # breaks out of checking the number against previously found primes
        if prime:
            primes_found.add(n)
        n += 2  # prime numbers must be odd, so we will increment by 2
    print(sum(primes_found))

# Rewritten version of problem 7 using just one while loop:
def solution7_1():
    primes_found = {2}
    n = 3
    while len(primes_found) < 10001:
        prime = True
        for p in primes_found: # check the new number against all previously found primes
            if p < n/2:  # if the prime divisor > half the number, the quotient will be < 2 and it can no longer be prime; 2 is the smallest prime
                if n % p == 0:
                    prime = False
                    break  # breaks out of checking the number against previously found primes
        if prime:
            primes_found.add(n)
        n += 2  # prime numbers must be odd, so we will increment by 2
    print(max(primes_found))
