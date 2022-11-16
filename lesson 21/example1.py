import time
import asyncio


# обычное решение которое выполняется за 6 секунд
def fun1(x):
    print(x ** 2)
    time.sleep(3)  # заснет на 3 секунды и только потом доделает
    print('fun1 завершена')


def fun2(x):
    print(x ** 0.5)
    time.sleep(3)
    print('fun2 завершена')


def main():
    fun1(4)
    fun2(4)


print(time.strftime('%X'))

main()

print(time.strftime('%X'))


# асинхронные функции выполнятся за 3 секунды
async def fun_1(x):
    print(x ** 2)
    await asyncio.sleep(3)
    print('fun1 завершена')


async def fun_2(x):
    print(x ** 0.5)
    await asyncio.sleep(3)
    print('fun2 завершена')


async def main():
    task_1 = asyncio.create_task(fun_1(4))  # корутину асинхронной функции fun1 обернули задачей task1
    task_2 = asyncio.create_task(fun_2(4))  # создали конкурентную задачу из функции fun2

    await task_1  # в асинхронной функции main обозначили точку переключения к задаче task1
    await task_2  # запустили task2


print(time.strftime('%X'))

asyncio.run(main())  # В asyncio.run нужно передавать асинхронную функцию с эвейтами на задачи, а не на корутины

print(time.strftime('%X'))


# через цикл событий (будет давать ошибку)
async def fun1_(x):
    print(x ** 2)
    await asyncio.sleep(3)
    print('fun1 завершена')


async def fun2_(x):
    print(x ** 0.5)
    await asyncio.sleep(3)
    print('fun2 завершена')


print(time.strftime('%X'))

loop = asyncio.get_event_loop()  # цикл событий
task1 = loop.create_task(fun1_(4))
task2 = loop.create_task(fun2_(4))
loop.run_until_complete(asyncio.wait([task1, task2]))

print(time.strftime('%X'))
