import multiprocessing
import os

def Sumpower(n):
    total = 0

    for i in range(1, n + 1):
        total = total + (i **5)

    print("Process ID:", os.getpid(),
          "Input Number:", n,
          "Sum:", total)

    return total

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    p = multiprocessing.Pool()

    result = p.map(Sumpower, Data)

    p.close()
    p.join()

    print("Result:", result)

if __name__ == "__main__":
    main()
