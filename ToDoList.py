Tasks = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter task: ")
    Tasks.append({"task": task, "done": False})
    print("Task added.")

def view_tasks():
    if not Tasks:
        print("No tasks yet.")
    else:
        for i, t in enumerate(Tasks):
            status = "✓" if t["done"] else "✗"
            print(f"{i+1}. {t['task']} [{status}]")

def complete_task():
    view_tasks()
    index = int(input("Enter task number to mark as complete: ")) - 1
    if 0 <= index < len(Tasks):
        Tasks[index]["done"] = True
        print("Task marked as complete.")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(Tasks):
        Tasks.pop(index)
        print("Task deleted.")
    else:
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")