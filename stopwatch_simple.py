import time

running = False
start_time = 0
elapsed = 0

while True:
    print("\n1.Start  2.Stop  3.Reset  4.Display  5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        if running:
            print("Error: Already running.")
        else:
            start_time = time.time()
            running = True
            print("Stopwatch started.")

    elif choice == "2":
        if not running:
            print("Error: Not started yet.")
        else:
            elapsed = elapsed + (time.time() - start_time)
            running = False
            print("Stopped. Elapsed:", round(elapsed, 2), "s")

    elif choice == "3":
        elapsed = 0
        running = False
        print("Stopwatch reset. Elapsed: 0.00 s")

    elif choice == "4":
        print("Elapsed:", round(elapsed, 2), "s")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Enter 1 to 5.")
