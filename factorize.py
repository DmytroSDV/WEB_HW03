import time
import logging
from multiprocessing import Pool, cpu_count

# sync
def s_factorize(numbers: list):
    result = []
    for num in numbers:
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        result.append(factors)
    return result

# input = [1000, 10000, 100000, 1000000, 1000000000]
input = [10, 10, 10, 10, 10]
start_time = time.time()
s_result = s_factorize(input)
end_time = time.time()
s_execution_time = end_time - start_time
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(name)s %(message)s")
logging.debug(f"Synchronous execution: {s_execution_time} sec")

print('\n\n')

# parallel
def parallel_factorize(numbers):
    with Pool(cpu_count()) as pool:
        result = pool.map(s_factorize, numbers)
    return result

# input = [1000, 10000, 100000, 1000000, 1000000000]
input = [10, 10, 10, 10, 10]
start_time = time.time()
result_parallel = parallel_factorize(input)
end_time = time.time()
parallel_execution_time = end_time - start_time
print(f"Parallel execution: {parallel_execution_time} sec")
