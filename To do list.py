class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        self.tasks.append([task_name, False])
        print(f'Task "{task_name}" added successfully.')

    def mark_done(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index][1] = True
            print(f'Task "{self.tasks[task_index][0]}" marked as done.')
        else:
            print("Invalid task index. Please try again.")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f'Task "{removed_task[0]}" removed successfully.')
        else:
            print("Invalid task index. Please try again.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nCurrent Tasks:")
            for idx, (task, done) in enumerate(self.tasks):
                status = "✓" if done else "✗"
                print(f"{idx}. {task} [{status}]")

def main():
    todo_list = ToDoList()
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Task as Done")
        print("3. Remove Task")
        print("4. View Tasks")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            task_name = input("Enter the task name: ")
            todo_list.add_task(task_name)
        elif choice == "2":
            try:
                task_index = int(input("Enter the task index to mark as done: "))
                todo_list.mark_done(task_index)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "3":
            try:
                task_index = int(input("Enter the task index to remove: "))
                todo_list.remove_task(task_index)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "4":
            todo_list.view_tasks()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
    ""
