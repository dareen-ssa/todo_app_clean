tasks = []

def show_menu():
    print("\n--- To-Do List ---")
    print("1. Add a task")
    print("2. Show tasks")
    print("3. Delete a task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print(f"Task added: {task}")
    elif choice == "2":
        print("\nYour tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
    elif choice == "3":
        task_num = int(input("Enter the task number to delete: "))
        if 0 < task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Task deleted: {removed}")
        else:
            print("Invalid task number!")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
