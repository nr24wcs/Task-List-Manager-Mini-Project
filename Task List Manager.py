import os
def add_task(task_list, task):
    task_list.append(task)
    print(f'Task "{task}" added successfully!')


def remove_task(task_list, task):
    if task in task_list:
        task_list.remove(task)
        print(f'Task "{task}" removed successfully!')
    else:
        print(f'Task "{task}" not found in the task list.')


def view_tasks(task_list):
    if task_list:
        print("Current task list:")
        for i, task in enumerate(task_list, start=1):
            print(f'{i}. {task}')
    else:
        print("The task list is currently empty.")


def save_tasks_to_file(task_list, filename):
    try:
        with open(filename, 'w') as file:
            for task in task_list:
                file.write(task + '\n')
        print(f'Tasks saved to {filename} successfully!')
    except IOError as e:
        print(f'Error saving tasks to file: {e}')


def load_tasks_from_file(filename):
    task_list = []
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                task_list = [line.strip() for line in file]
            print(f'Tasks loaded from {filename} successfully!')
        except IOError as e:
            print(f'Error loading tasks from file: {e}')
    else:
        print(f'File {filename} not found. Starting with an empty task list.')
    return task_list


def main():
    task_list = []
    filename = 'tasks.txt'
    task_list = load_tasks_from_file(filename)

    while True:
        print("\nTask List Manager")
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Save tasks")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task to add: ")
            add_task(task_list, task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(task_list, task)
        elif choice == '3':
            view_tasks(task_list)
        elif choice == '4':
            save_tasks_to_file(task_list, filename)
        elif choice == '5':
            save_tasks_to_file(task_list, filename)
            print("Exiting the Task List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
