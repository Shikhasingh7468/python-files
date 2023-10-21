import os

class Task:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{status} {self.description}"

    def mark_completed(self):
        self.completed = True

    def mark_incomplete(self):
        self.completed = False

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_id):
        if 1 <= task_id <= len(self.tasks):
            self.tasks.pop(task_id - 1)

    def view_tasks(self):
        return self.tasks

    def view_incomplete_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def view_completed_tasks(self):
        return [task for task in self.tasks if task.completed]

def create_task():
    title = input("Title: ")
    description = input("Description: ")
    return Task(title, description)

def display_tasks(tasks):
    if tasks:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("No tasks.")

def main():
    todo_list = TodoList()

    while True:
       # os.system('clear')  # Clear the screen (for Unix-based systems)

        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View All Tasks")
        print("4. View Incomplete Tasks")
        print("5. View Completed Tasks")
        print("6. Mark Task as Completed")
        print("7. Mark Task as Incomplete")
        print("8. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")

        if choice == "1":
            task = create_task()
            todo_list.add_task(task)
            print("Task added.")
        elif choice == "2":
            task_id = input("Enter the task ID to remove: ")
            try:
                task_id = int(task_id)
                todo_list.remove_task(task_id)
                print("Task removed.")
            except (ValueError, IndexError):
                print("Invalid task ID. Please enter a valid number.")
        elif choice == "3":
            tasks = todo_list.view_tasks()
            print("\nAll Tasks:")
            display_tasks(tasks)
        elif choice == "4":
            incomplete_tasks = todo_list.view_incomplete_tasks()
            print("\nIncomplete Tasks:")
            display_tasks(incomplete_tasks)
        elif choice == "5":
            completed_tasks = todo_list.view_completed_tasks()
            print("\nCompleted Tasks:")
            display_tasks(completed_tasks)
        elif choice == "6":
            task_id = input("Enter the task ID to mark as completed: ")
            try:
                task_id = int(task_id)
                task = todo_list.view_tasks().get(task_id)
                if task:
                    task.mark_completed()
                    print("Task marked as completed.")
                else:
                    print("Task not found.")
            except (ValueError, IndexError):
                print("Invalid task ID. Please enter a valid number.")
        elif choice == "7":
            task_id = input("Enter the task ID to mark as incomplete: ")
            try:
                task_id = int(task_id)
                task = todo_list.view_tasks().get(task_id)
                if task:
                    task.mark_incomplete()
                    print("Task marked as incomplete.")
                else:
                    print("Task not found.")
            except (ValueError, IndexError):
                print("Invalid task ID. Please enter a valid number.")
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
