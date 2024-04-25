def display_menu():
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Mark Task as Completed")
    print("4. Display Tasks")
    print("5. Quit")

def add_task(tasks):
    task = input("Enter task to add: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def delete_task(tasks):
    index = int(input("Enter index of task to delete: ")) - 1
    if 0 <= index < len(tasks):
        deleted_task = tasks.pop(index)
        print(f"Task '{deleted_task}' deleted.")
    else:
        print("Invalid task index.")

def mark_completed(tasks):
    index = int(input("Enter index of task to mark as completed: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index] += " (Completed)"
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

def display_tasks(tasks):
    if tasks:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("\nYour To-Do List is empty.")

def main():
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            delete_task(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            display_tasks(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
