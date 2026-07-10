import multiprocessing
import os
import time

def CountOdd(n):
    count = 0

    for i in range(1, n + 1, 2):
        count = count + 1

    print("Process ID:", os.getpid(),
          "Input Number:", n,
          "Odd Count:", count)

    return count

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    start_time = time.perf_counter()

    p = multiprocessing.Pool()

    result = p.map(CountOdd, Data)

    p.close()
    p.join()

    end_time = time.perf_counter()

    print("Result:", result)
    print(f"Time Required: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()
