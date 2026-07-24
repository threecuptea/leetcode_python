import asyncio
from concurrent.futures import ThreadPoolExecutor
import time
from multiprocessing import Pool

items = [1, 2, 3, 4, 5, 6]

async def fetch_data(task_id):
    print(f"Starting asyncio Task {task_id}")
    await asyncio.sleep(2)  # Simulates a non-blocking network request
    print(f"Finished asyncio Task {task_id}")

async def asyncio_main():
    tasks = [fetch_data(i) for i in range(1, 4)]
    await asyncio.gather(*tasks)

def fetch_item(item_id):
    print(f"Starting ThreadPoolExecutor task {item_id}")
    time.sleep(1)  # Simulating a network request
    return f"Data from task {item_id}"

def thread_pool_main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(fetch_item, items)
    for result in results:
        print(result)

def compute_heavy_task(number):
    print(f"Process calculating power of {number}")
    return number ** number

def multi_processing_main():
    nums = [1, 2, 3, 4, 5, 6]
    with Pool() as pool:
        results = pool.map(compute_heavy_task, nums)
    print(results)

if __name__ == '__main__':
    asyncio.run(asyncio_main())

    thread_pool_main()

    multi_processing_main()
