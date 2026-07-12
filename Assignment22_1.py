import multiprocessing
import os

def Sumsquare(n):
    total = 0

    for i in range(1, n + 1):
        total = total + (i * i)

    print("Process ID:", os.getpid(),
          "Input Number:", n,
          "Sum of Cube:", total)

    return total

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    p = multiprocessing.Pool()

    result = p.map(Sumsquare, Data)

    p.close()
    p.join()

    print("Result:", result)

if __name__ == "__main__":
    main()
