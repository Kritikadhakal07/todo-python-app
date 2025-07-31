TASKS_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f" Task added: {task}")

def view_task(tasks):
    if not tasks:
        print(" There is no task added.")
    else:
        print(" Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task(tasks):
    if not tasks:
        print(" There is no task to delete.")
    else:
        print(" Select a task to delete:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        try:
            index = int(input("Enter the task number: "))
            if 1 <= index <= len(tasks):
                deleted_task = tasks.pop(index - 1)
                save_tasks(tasks)
                print(f" Task deleted: {deleted_task}")
            else:
                print(" Invalid task number.")
        except ValueError:
            print(" Invalid input. Please enter a valid number.")

def Main():
    tasks = load_tasks()
    print("\n Welcome to my To-Do List App")
    while True:
        print("\n1. Add Task\n2. View Task\n3. Delete Task\n4. Exit")
        choice = input("Enter a choice (1-4): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print(" Exiting app. Goodbye!")
            break
        else:
            print(" Invalid choice. Please try again.")

if __name__ == "__main__":
    Main()
