import time
import concurrent.futures
from funkcja_prime import  znajdz_sume_liczb_pierwszych

numbers = [(1,10_000),(3,50_000),(5_000,100_000),(4,900),(8_000,15_000),(95_000,133_000)]


def run_heavy_function(params):
    return znajdz_sume_liczb_pierwszych(*params)

def synchronicznie():
    starttime = time.time()
    for pairs in numbers:
        prime_suma = znajdz_sume_liczb_pierwszych(*pairs)
        print(prime_suma)
    endtime = time.time()
    print(f'całkowity czas wykonanie sum -> synchronicznie: {endtime-starttime} s')

def asynchronicznie():
    starttime = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
        wynik = executor.map(run_heavy_function,numbers)
    print(list(wynik))
    endtime = time.time()
    print(f'całkowity czas wykonanie sum -> asynchronicznie: {endtime - starttime} s')

def main():
    synchronicznie()
    print('_'*35)
    asynchronicznie()

if __name__ == '__main__':
    main()
