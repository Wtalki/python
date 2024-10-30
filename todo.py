class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self,task):
        self.tasks.append(task)
        print(f"added task:{task}")

    def view_tasks(self):
        if not self.tasks:
            print("no tasks available")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks,1):
                print(f"{i}.{task}")

    def complete_task(self,task_index):
        if 0<= task_index < len(self.tasks):
            completed_task = self.tasks.pop(task_index)
            print(f"completed task : { completed_task}")

        else:
            print("invalid task numbeer")

def main():
    todo_list=ToDoList()

    while True:
        print("\nto-do list menu")
        print("1. add task")
        print("2.vview tasks")
        print("3. complete task")
        print("4. eits")

        choice = input("choose and option")

        if choice == '1':
            task = input("enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_index = int(input("enter the task number: "))
            todo_list.complete_task(task_index)
        elif choice == '4':
            print("Exiting the program.")
            break

main()