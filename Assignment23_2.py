import multiprocessing
import os
import time

def Even(n):
    sum=0
    for i in range(1,n+1,2):
        sum = sum + i
    print("Process ID:",os.getpid(),"input number",n,"sum of even number",sum)
    return sum

def main():
    Data=[1000000,2000000,3000000,4000000,5000000]
    
    start_time=time.perf_counter()

    p=multiprocessing.Pool()

    result=p.map(Even,Data)

    p.close()
    p.join()

    end_time=time.perf_counter()

    print("result is:",result)

    print(f"time required:{end_time-start_time:.4f}seconds")

if __name__ == "__main__":
    main()

