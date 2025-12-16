import gmpy2
import random
import time
import sys
sys.set_int_max_str_digits(12000)

def big_prime(num_digits, time_limit):
    start_time = time.time()
    lower = gmpy2.mpz(10)**(num_digits - 1) + 1
    upper = gmpy2.mpz(10)**num_digits - 1
    
    while time.time() - start_time < time_limit:
        n = random.randint(lower, upper)
        if n % 2 == 0:
            n += 1

        if gmpy2.is_prime(n, 40): 
            print(f"{time.time() - start_time:.2f}")
            return n

    
    raise TimeoutError("Time out")

try:
    prime = big_prime(5000, 30000)
    print(prime)
    print(len(str(prime)))
except Exception as e:
    print(f"Error: {e}")
