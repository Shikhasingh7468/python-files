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

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def view_tasks(self):
        return self.tasks

    def view_incomplete_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def view_completed_tasks(self):
        return [task for task in self.tasks if task.completed]



def create_task(title,description):
    title = input("Title:")
    description = input("Description: ")
    return Task(title, description)

def main():
    todo_list = TodoList()

    while True:
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
            task = create_task(title,description)
            todo_list.add_task(task)
            print("Task added.")
        elif choice == "2":
            title = input("Enter the task to remove: ")
            task_to_remove = None
            for task in todo_list.tasks:
                if task.title == title:
                    task_to_remove = task
                    break
            if task_to_remove:
                todo_list.remove_task(task_to_remove)
                print("Task removed.")
            else:
                print("Task not found.")
        elif choice == "3":
            tasks = todo_list.view_tasks()
            if tasks:
                print("\nAll Tasks:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")
            else:
                print("No tasks.")
        elif choice == "4":
            incomplete_tasks = todo_list.view_incomplete_tasks()
            if incomplete_tasks:
                print("\nIncomplete Tasks:")
                for idx, task in enumerate(incomplete_tasks, start=1):
                    print(f"{idx}. {task}")
            else:
                print("No incomplete tasks.")
        elif choice == "5":
            completed_tasks = todo_list.view_completed_tasks()
            if completed_tasks:
                print("\nCompleted Tasks:")
                for idx, task in enumerate(completed_tasks, start=1):
                    print(f"{idx}. {task}")
            else:
                print("No completed tasks.")
        elif choice == "6":
            description = input("Enter the task to mark as completed: ")
            for task in todo_list.tasks:
                if task.description == description:
                    task.mark_completed()
                    print("Task marked as completed.")
                    break
            else:
                print("Task not found.")
        elif choice == "7":
            description = input("Enter the task to mark as incomplete: ")
            for task in todo_list.tasks:
                if task.description == description:
                    task.mark_incomplete()
                    print("Task marked as incomplete.")
                    break
            else:
                print("Task not found.")
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
