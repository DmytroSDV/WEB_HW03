# import time

# def factorize(*numbers):
#     result = []
#     for item in numbers:
#         temp_list = []
#         for i in range(1, item + 1):
#             if item % i == 0:
#                 temp_list.append(i)
#         result.append(temp_list)
#     return result

# def test_factorize():
#     a, b, c, d = factorize(128, 255, 99999, 10651060)
    
#     assert a == [1, 2, 4, 8, 16, 32, 64, 128]
#     assert b == [1, 3, 5, 15, 17, 51, 85, 255]
#     assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
#     assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    
# start_time = time.time()
# test_factorize()
# end_time = time.time()
# print(end_time - start_time)


import multiprocessing
import time

def factorize_worker(number, output):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    output.put(factors)

def factorize_parallel(numbers):
    processes = []
    results = multiprocessing.Queue()

    for number in numbers:
        process = multiprocessing.Process(target=factorize_worker, args=(number, results))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    return [results.get() for _ in numbers]

def test_factorize_parallel():    
    a, b, c, d  = factorize_parallel((128, 255, 99999, 10651060))

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

if __name__ == "__main__":
    start_time = time.time()
    test_factorize_parallel()
    end_time = time.time()
    print(end_time - start_time)
