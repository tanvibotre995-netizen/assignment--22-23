import multiprocessing
import os

def Factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    print("Process ID:", os.getpid(),
          "Input Number:", n,
          "Factorial:", fact)

    return fact

def main():
    Data = [10, 15, 20, 25]

    p = multiprocessing.Pool()

    result = p.map(Factorial, Data)

    p.close()
    p.join()

    print("Result:", result)

if __name__ == "__main__":
    main()
