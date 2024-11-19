"""
    # Day 96 is about AsincOI in python...
        Asynchronous I/O, or async for short, is a programming pattern 
        that allows for high-performance I/O operations in a concurrent 
        and non-blocking manner. 

        In Python, async programming is achieved through the use of 
        the asyncio module and asynchronous functions.


        Async IO is a powerful programming pattern that allows for high-performance 
        and concurrent I/O operations in Python. With the asyncio module and 
        asynchronous functions, you can write efficient and scalable code that 
        can handle large amounts of data and I/O operations without blocking 
        the main thread. Whether you're working on web applications, network services, 
        or data processing pipelines, async IO is an essential tool for any Python developer.
"""

import asyncio

async def my_async_function():
    # asynchronous code here
    await asyncio.sleep(1)
    return "Hello, Async World!"

async def main():
    result = await my_async_function()
    print(result)

asyncio.run(main())