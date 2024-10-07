FILE_PATH = 'projects/todo.txt'

tasks_list = []

while True:
    print("\n--- To DO List Menu ---")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Update Task")
    print("4. View currenct tasks")
    print("5. Quit")

    user_choice = int(input("Enter your choice (1-4): "))

    if user_choice == 1:
        task = input("Enter your list tasks: ")
        tasks_list.append(task)
        print(f"{task} has been added to your task list")

    elif user_choice == 2:
        task = input("Enter the task to remove: ")
        if task in tasks_list:
            tasks_list.remove(task)
            print(f"{task} has been removed from your task list")
        else:
            print(f"'{task}' is not in the task list")

    elif user_choice == 3:
        task = input("Enter the updated task: ")
        if task in tasks_list:
            tasks_list.insert(task)
            print(f"The {task} has been updated")

    elif user_choice == 4:
        if tasks_list:
            print("\nCurrent ToDo List:")
            for i, task in enumerate(tasks_list, 1):
                print(f"{i}. {task}")
        else:
            print("\nThe task list is currently empty.")

    elif user_choice == 4:
        print("\n Quitting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4")

    with open('projects/todo.txt', 'a') as file:
         file.write(f"\n{task} has been added")
