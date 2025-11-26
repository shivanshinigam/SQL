
import time
import argparse
from threading import Thread

# Task 1
def task_1():
    print("Task 1: Basic threading")

    def say(name):
        time.sleep(2)
        print("Hello", name)

    print("Running normally:")
    say("Asha")
    say("Rohan")
    say("Simran")

    print("\nRunning with threads:")
    threads = []
    for n in ["Asha", "Rohan", "Simran"]:
        t = Thread(target=say, args=(n,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("done!")


# Task 2
def task_2():
    print("Task 2: Multiple workers")

    def work(num):
        print(f"Task {num} started")
        time.sleep(1)
        print(f"Task {num} finished")

    threads = []

    for i in range(1, 6):
        t = Thread(target=work, args=(i,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("all tasks done!")



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", type=int, help="Run specific task )")
    parser.add_argument("--list", action="store_true", help="list all tasks")
    args = parser.parse_args()

    if args.list:
        print("Available tasks:")
        print("task1: basic threads ")
        print("task2: 5 worker threads")
        return

    if args.task == 1:
        task_1()
    elif args.task == 2:
        task_2()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
