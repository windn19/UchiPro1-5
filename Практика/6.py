import asyncio


async def counter_1(stop):
    i = 0
    while i <= stop:
        await asyncio.sleep(1)
        print(f'counter_1: {i}')
        i += 1


async def counter_2(stop):
    j = 0
    while j <= stop:
        await asyncio.sleep(1)
        print(f'counter_2: {j}')
        j += 1


async def main():
    task1 = asyncio.create_task(counter_1(2))
    task2 = asyncio.create_task(counter_2(3))
    await task1
    await task2

asyncio.run(main())