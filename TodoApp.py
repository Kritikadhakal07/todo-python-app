tasks = []

print(" To-Do List")
print("1. Add Task")
print("2. View Task")
print("3. Delete Task")
print("4. Exit")

while True:
    choice = input("\nEnter a choice (1-4): ")

    if choice == '1':
        task = input("Enter a task: ")
        tasks.append(task)
        print(f"Task added: {task}")

    elif choice == '2':
        if not tasks:
            print("There is no task added.")
        else:
            print(" Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == '3':
        if not tasks:
            print(" There is no task to delete.")
        else:
            print("Select a task to delete:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                index = int(input("Enter the index you want to delete: "))
                if 1 <= index <= len(tasks):
                    removed = tasks.pop(index - 1)
                    print(f" Task removed: {removed}")
                else:
                    print(" Invalid index.")
            except ValueError:
                print(" Please enter a valid number.")

    elif choice == '4':
        print(" Exiting To-Do App. Goodbye!")
        break  

    else:
        print(" Invalid choice. Please enter a number between 1–4.")
