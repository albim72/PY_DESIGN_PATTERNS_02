import time

#przykład 1
def pomiarczasu(funkcja):
    def wrapper():
        wynik = []
        starttime = time.perf_counter()
        print(f'czas startu pomiaru {starttime} s')
        funkcja()
        endtime = time.perf_counter()

        print(f"czas zakończenia pomiaru: {endtime} s")
        wynik.append(endtime - starttime)
        print(f'czas wykonania funkcji: {wynik[0]} s')
    return wrapper


def sleepdec(funkcja):
    def wrapper(*args):
        time.sleep(3)
        return funkcja(*args)
    return wrapper

@sleepdec
@pomiarczasu
def big_nb():
    sum([i**2 for i in range(10_000_000)])

big_nb()

@sleepdec
def info(k):
    return 9*k



print(info(451))

#przykład 2

def debug(funkcja):
    def wrapper(*args,**kwargs):
        print(f'wołana funkcja to: {funkcja.__name__}')
        funkcja(*args)
    return wrapper

@debug
def kody(k):
    print(f'kod nr 5: {k}')

kody(22567)
