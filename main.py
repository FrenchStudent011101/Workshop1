class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})

    def delete_task(self, task_index):
        del self.tasks[task_index]

    def complete_task(self, task_index):
        self.tasks[task_index]['completed'] = True

    def show_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            for index, task in enumerate(self.tasks):
                status = 'Complete' if task['completed'] else 'Incomplete'
                print(f"{index + 1}. [{status}] {task['task']}")


def main():
    todo_list = TodoList()

    while True:
        print("\nTODO List Options:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Complete Task")
        print("4. Show Tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task to add: ")
            todo_list.add_task(task)
            print("Task added successfully.")
        elif choice == '2':
            todo_list.show_tasks()
            task_index = int(input("Enter task index to delete: ")) - 1
            todo_list.delete_task(task_index)
            print("Task deleted successfully.")
        elif choice == '3':
            todo_list.show_tasks()
            task_index = int(input("Enter task index to mark as complete: ")) - 1
            todo_list.complete_task(task_index)
            print("Task marked as complete.")
        elif choice == '4':
            todo_list.show_tasks()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
