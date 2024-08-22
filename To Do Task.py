import os

def display_menu():
    print("\n===== To-Do List Menu =====")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Quit")

def view_todo_list():
    with open("todo.txt", "r") as file:
        tasks = file.readlines()
        if not tasks:
            print("Your to-do list is empty.")
        else:
            print("\n===== To-Do List =====")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")

def add_task():
    task = input("Enter the task: ")
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")

def update_task():
    view_todo_list()
    task_number = int(input("Enter the task number to update: "))
    
    with open("todo.txt", "r") as file:
        tasks = file.readlines()

    if 1 <= task_number <= len(tasks):
        updated_task = input("Enter the updated task: ")
        tasks[task_number - 1] = updated_task + "\n"
        
        with open("todo.txt", "w") as file:
            file.writelines(tasks)
        
        print("Task updated successfully.")
    else:
        print("Invalid task number.")

def delete_task():
    view_todo_list()
    task_number = int(input("Enter the task number to delete: "))

    with open("todo.txt", "r") as file:
        tasks = file.readlines()

    if 1 <= task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)

        with open("todo.txt", "w") as file:
            file.writelines(tasks)
        
        print(f"Task '{deleted_task.strip()}' deleted successfully.")
    else:
        print("Invalid task number.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_todo_list()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    if not os.path.exists("todo.txt"):
        with open("todo.txt", "w"):
            pass
    main()
