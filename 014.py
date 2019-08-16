"""
Problem 14:
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""

def solution14(mynum):
    def collatz(n):
        return n/2 if n%2 == 0 else 1+3*n

    def chain_length_generator(n):
        chain_length = 1
        while True:
            n = int(collatz(n))
            chain_length += 1
            if n == 1:
                break
        return chain_length

    max_num = 0
    max_chain_length = 0
    for num in reversed(range(1, mynum)):
        # Larger numbers are more likely to have longer chains, so go backwards
        possible_chain_length = chain_length_generator(num)
        if possible_chain_length > max_chain_length:
            max_num = num
            max_chain_length = possible_chain_length
            # don't need this last line, but it's fun to see how long the chain gets

    return max_num, max_chain_length

print(solution14(1000000))