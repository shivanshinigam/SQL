import warnings
warnings.filterwarnings("ignore", category=Warning)

import argparse
import requests
import asyncio
import aiohttp


URL_USER = "https://jsonplaceholder.typicode.com/users/1"
URL_POST = "https://jsonplaceholder.typicode.com/posts/"


# Task 1: Simple GET using requests
def task_1():
    print("Task 1: Simple GET request using requests")
    print("Calling:", URL_USER)

    try:
        response = requests.get(URL_USER, timeout=5)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print("Network error:", e)
        return

    print("\nUser Info:")
    print("Name:", data.get("name"))
    print("Email:", data.get("email"))
    print("City:", data.get("address", {}).get("city"))




# Task 2: Async GET using aiohttp (multiple calls)

async def fetch_post(session, post_id):
    url = URL_POST + str(post_id)
    try:
        async with session.get(url, timeout=5) as resp:
            resp.raise_for_status()
            data = await resp.json()
            print(f"[Post {post_id}] Title:", data.get("title"))
            return data
    except Exception as e:
        print(f"[Post {post_id}] Network error:", e)


async def task_2_async():
    print("Task 2: Async GET using aiohttp (fetch 3 posts)")
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_post(session, i) for i in [1, 2, 3]]
        await asyncio.gather(*tasks)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", type=int, help="Select task: 1 or 2")
    parser.add_argument("--list", action="store_true", help="List tasks")
    args = parser.parse_args()

    if args.list:
        print("Available API tasks:")
        print("task1: simple GET using requests")
        print("task2: async GET using aiohttp")
        return

    if args.task == 1:
        task_1()
    elif args.task == 2:
        asyncio.run(task_2_async())
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
