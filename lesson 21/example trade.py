import asyncio
import time
from aiohttp import ClientSession
import threading
import random
import multiprocessing


# пример
async def fetch_url_data(session, url):
    try:
        async with session.get(url, timeout=60) as response:
            resp = await response.read()
    except Exception as e:
        print(e)
    else:
        return resp
    return


async def fetch_async(loap, r):
    url = "http://www.uefa.com/uefaeuro-2020/"
    tasks = []
    async with ClientSession() as session:
        for i in range(r):
            task = asyncio.ensure_future(fetch_url_data(session, url))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
    return responses


if __name__ == '__main__':
    for ntimes in [1, 10, 50, 100, 500]:
        start_time = time.time()
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(fetch_async(loop, ntimes))
        loop.run_until_complete(future)
        responses = future.result()
        print(f'получено {ntimes} результатов запроса за {time.time() - start_time} секунд')


# ПОТОКИ
def worker(number):  # запустили 5 потоков для совместной работы после их старта
    sleep = random.randrange(1, 10)
    time.sleep(sleep)
    print('I am Worker {}, I slept for {} seconds'.format(number, sleep))


for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    t.start()


# МНОГОПОЦЕССОРНОСТЬ
def cube(n):
    print('the cube is: {}'.format(n * n * n))


def square(n):
    print('the square is: {}'.format(n * n))


if __name__ == "__main__":  # определили объект процесса
    process1 = multiprocessing.Process(target=square, args=(5,))  # таргет представляет ф-цию кот должна быть выполнена
    process2 = multiprocessing.Process(target=cube, args=(5,))  # аргс - аргумент кот должен быть передан внутри ф-ции

    process1.start()
    process2.start()

    process1.join()
    process2.join()
