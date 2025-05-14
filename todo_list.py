#!/usr/bin/python3

import csv, os

# expanduser("~") returns the path to the users home directory ie: /home/USER
path = os.path.expanduser("~")
filename = "todo-list.csv"
file= os.path.join(path, 'scripts', filename)
if not os.path.exists(file):
    with open(file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'task', 'completed'])
        print(f'{file} created')

class TodoItem():
    def __init__(self,id, task, completed):
        self.id = id
        self.task = task
        self.completed = completed
    def to_dict(self):
        return {'id': self.id, 'task': self.task, 'completed': self.completed}

def add_task(task):
    with open(file, "r", newline="") as reader:   
        len_list = csv.DictReader(reader)
        new_id = len(list(len_list))
    todo_item = TodoItem(new_id, task, 'not complete')
    with open(file, "a", newline="") as f:
        fieldnames = ['id', 'task', 'completed']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(todo_item.to_dict())
    display_tasks()

def display_tasks():
    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        print("")
        for num, line in enumerate(reader):
            if line['completed'] == 'complete':
                print(f"{num} - [x] {line['task']}")
            else:
                print(f"{num} - [ ] {line['task']}")
        print("")

def help():
    print("add <task name> - add a new task")
    print("display - display all tasks")
    print("complete <task number>")
    print("exit - close program")

def complete_task(task_num):
    old_data = []
    with open(file, 'r', newline="") as data:
        reader = csv.DictReader(data)
        old_data = [x for x in reader]
    with open(file, 'w') as f:
        fieldnames = ['id', 'task', 'completed']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for index, value in enumerate(old_data):
            if int(task_num) == int(index):
                print(f"{task_num} updated")
                writer.writerow({'id': index,'task': value['task'], "completed": 'complete'})
            else:
                writer.writerow({'id': index,'task': value['task'], "completed": value['completed']})
    display_tasks()

def delete_task(task_num):
    old_data = []
    with open(file, 'r', newline='') as data:
        reader = csv.DictReader(data)
        old_data = [x for x in reader]
    with open(file, 'w') as f:
        fieldnnames = ['id', 'task', 'completed']
        writer = csv.DictWriter(f, fieldnames=fieldnnames)
        writer.writeheader()
        for index, value in enumerate(old_data):
            if int(task_num) == int(index):
                print(f"{task_num} deleted")
            else:
                writer.writerow({'id': index, 'task': value['task'], 'completed': value['completed']})
    display_tasks()


def main():
    print("-- type help for commands")
    display_tasks()
    exit_command = False
    while exit_command == False:
        command = str(input("todo >> "))
        command = command.split(" ", 1)
        match command[0]:
            case "exit":
                exit_command = True
            case "add":
                add_task(command[1])
            case "display":
                display_tasks()
            case "complete":
                complete_task(command[1])
            case "delete":
                delete_task(command[1])
            case "help":
                help()

if __name__ == "__main__":
    main()
