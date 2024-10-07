import os

# Define a file path to save the tasks
FILE_PATH = 'projects/todo.txt'

# Task list (in-memory)
tasks_list = []

# Load tasks from the file (if it exists)
if os.path.exists(FILE_PATH):
    with open(FILE_PATH, 'r') as file:
        for line in file:
            task_data = line.strip().split(',')
            task = {'id': int(task_data[0]), 'name': task_data[1], 'status': task_data[2]}
            tasks_list.append(task)

# Start main loop for the To-Do List program
while True:
    print("\nTo-Do List Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Remove Task")
    print("5. Mark Task as Completed")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        # View all tasks
        if tasks_list:
            print("\nTo-Do List:")
            for task in tasks_list:
                print(f"ID: {task['id']} | Name: {task['name']} | Status: {task['status']}")
        else:
            print("\nNo tasks found!")

    elif choice == '2':
        # Add a new task
        task_name = input("Enter task name: ")
        new_task = {
            'id': len(tasks_list) + 1,
            'name': task_name,
            'status': 'Incomplete'
        }
        tasks_list.append(new_task)

        # Save tasks to the file
        with open(FILE_PATH, 'w') as file:
            for task in tasks_list:
                line = f"{task['id']},{task['name']},{task['status']}\n"
                file.write(line)

        print(f"Task '{task_name}' added successfully!")

    elif choice == '3':
        # Update a task
        task_id = int(input("Enter task ID to update: "))
        new_name = input("Enter new task name (press Enter to skip): ") or None
        new_status = input("Enter new status (Incomplete/Completed) (press Enter to skip): ") or None

        for task in tasks_list:
            if task['id'] == task_id:
                if new_name:
                    task['name'] = new_name
                if new_status:
                    task['status'] = new_status

                # Save updated tasks to the file
                with open(FILE_PATH, 'w') as file:
                    for task in tasks_list:
                        line = f"{task['id']},{task['name']},{task['status']}\n"
                        file.write(line)

                print(f"Task ID {task_id} updated successfully!")
                break
        else:
            print(f"Task with ID {task_id} not found.")

    elif choice == '4':
        # Remove a task by ID
        task_id = int(input("Enter task ID to remove: "))
        tasks_list = [task for task in tasks_list if task['id'] != task_id]

        # Save updated tasks to the file
        with open(FILE_PATH, 'w') as file:
            for task in tasks_list:
                line = f"{task['id']},{task['name']},{task['status']}\n"
                file.write(line)

        print(f"Task with ID {task_id} removed successfully!")

    elif choice == '5':
        # Mark task as completed
        task_id = int(input("Enter task ID to mark as completed: "))
        for task in tasks_list:
            if task['id'] == task_id:
                task['status'] = 'Completed'

                # Save updated tasks to the file
                with open(FILE_PATH, 'w') as file:
                    for task in tasks_list:
                        line = f"{task['id']},{task['name']},{task['status']}\n"
                        file.write(line)

                print(f"Task ID {task_id} marked as completed!")
                break
        else:
            print(f"Task with ID {task_id} not found.")

    elif choice == '6':
        # Exit the program
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")