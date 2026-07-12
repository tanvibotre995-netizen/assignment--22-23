import multiprocessing
import os

def CountPrime(n):
    count = 0

    for i in range(2, n + 1):
        prime = True

        for j in range(2, i):
            if i % j == 0:
                prime = False
                break

        if prime:
            count = count + 1

    print("Process ID:", os.getpid(),
          "Input Number:", n,
          "Prime Count:", count)

    return count

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    p = multiprocessing.Pool()

    result = p.map(CountPrime, Data)

    p.close()
    p.join()

    print("Result:", result)

if __name__ == "__main__":
    main()
