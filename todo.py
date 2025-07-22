# todo.py

tasks = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks):
            status = "✅" if task['done'] else "❌"
            print(f"{i+1}. {task['task']} [{status}]")

def add_task():
    task_name = input("Enter new task: ")
    tasks.append({"task": task_name, "done": False})
    print("Task added successfully.")

def mark_done():
    view_tasks()
    index = int(input("Enter task number to mark done: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]['done'] = True
        print("Marked as done.")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Deleted: {removed['task']}")
    else:
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
