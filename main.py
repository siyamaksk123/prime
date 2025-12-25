import gmpy2
import random
import time
import sys
from concurrent.futures import ProcessPoolExecutor

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
            return n, time.time() - start_time
    return "fail", "fail"

def find_prime_parallel():
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(big_prime, 10000, 300) for _ in range(8)]
        
        for future in futures:
            try:
                prime, time1 = future.result(timeout=305)
                if prime != "fail":
                    print(time1)
                    print(prime)
                    print(len(str(prime)))
                    for f in futures:
                        f.cancel()
                    return prime, time1
            except Exception as e:
                continue
    
    return "fail", "fail"

if __name__ == "__main__":
    prime, time1 = find_prime_parallel()
