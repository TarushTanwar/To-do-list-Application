# Todo list application

tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})

def view_tasks():
    if tasks:
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else " "
            print(f"{i}. [{status}] {task['task']}")
    else:
        print("No tasks in the to-do list.")

def mark_completed(task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def remove_task(task_number):
    if 1 <= task_number <= len(tasks):
        del tasks[task_number - 1]
        print("Task removed.")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\n===== To-Do List Application =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
            print("Task added to the to-do list.")
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            task_number = int(input("Enter the task number to mark as completed: "))
            mark_completed(task_number)
        elif choice == "4":
            view_tasks()
            task_number = int(input("Enter the task number to remove: "))
            remove_task(task_number)
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
