# 📝 To-Do List App in Python
# Run in VS Code (CLI based)

import os

FILE_NAME = "tasks.txt"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return [line.strip() for line in f.readlines()]
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def view_tasks(tasks):
    if not tasks:
        print("\n📋 No tasks yet!")
    else:
        print("\n===== Your To-Do List =====")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added!")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"❌ Task removed: {removed}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n===== To-Do List Menu =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, try again.")

if __name__ == "__main__":
    main()
