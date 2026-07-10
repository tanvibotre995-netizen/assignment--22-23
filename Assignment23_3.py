import multiprocessing
import os
import time

def CountEven(n):
    count = 0

    for i in range(2, n + 1, 2):
        count = count + 1

    print("Process ID:", os.getpid(),
          "Input Number:", n,
          "Even Count:", count)

    return count

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    start_time = time.perf_counter()

    p = multiprocessing.Pool()

    result = p.map(CountEven, Data)

    p.close()
    p.join()

    end_time = time.perf_counter()

    print("Result:", result)
    print(f"Time Required: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()
