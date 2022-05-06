# Author:   Douglas Gromek
# Creation: 1/22/22
# Purpose:  A barebones implementation of the Sieve of Eratosthenes using
#           numpy that outputs the total number of primes in a range and
#           computes the local machine time needed for the calculation


import math
import numpy as np
import time
start_time = time.time()


def sieve_of_eratosthenes(max_num):
    primes = []
    flags = np.ones(max_num, dtype=bool)
    flags[0] = flags[1] = False

    for i in range(2, math.floor(math.sqrt(max_num))):
        if flags[i]:
            flags[i ** 2::i] = False

    for index, val in enumerate(flags):
        if val:
            primes.append(index)

    return primes


def main():
    max_num = 1000
    result = sieve_of_eratosthenes(max_num)
    print('Total Prime Numbers in (0 -', str(max_num) + '):    ', len(result))
    print(f'___ {time.time() - start_time:.6f} seconds ___')


if __name__ == '__main__':
    main()