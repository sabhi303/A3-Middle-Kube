import time
import sys

def get_primes(start, end):
    if start < 1 or end < 1:
        print("Only positive numbers expected!")
        exit(-3)
    if start < 2:
        start = 2
    primes = []
    start_time = time.time()
    for i in range(start, end + 1):
        # Check if i is prime
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    end_time = time.time()
    return {
        "primes": primes,
        "time": end_time - start_time
    }

def main():
    if len(sys.argv) >= 3:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
    else:
        start = 1
        end = 99999
    result = get_primes(start, end)
    print(f"Execution time for calculating prime numbers between {start} and {end} is {result['time']} seconds")

if __name__ == "__main__":
    main()
