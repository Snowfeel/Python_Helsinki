# Write your solution here
# If you use the classes made in the previous exercise, copy them here
# Write your solution here:
class Task:
    id = 1

    def __init__(self,description:str,name:str,time:int):
        self.description = description
        self.programmer = name
        self.workload = time
        self.finished = False
        self.id = Task.id
        Task.id += 1

    def is_finished(self):
        return self.finished

    def mark_finished(self):
        self.finished = True
        
    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {'FINISHED' if self.is_finished() else 'NOT FINISHED'}"

class OrderBook:
    def __init__(self):
        self.tasks = []

    def add_order(self,description:str,name:str,time:int): 
        self.tasks.append(Task(description,name,time))

    def all_orders(self):
        return self.tasks

    def programmers(self):
        return list(set(i.programmer for i in self.tasks))

    def mark_finished(self, id: int):
        if id not in [i.id for i in self.all_orders()]:
            raise ValueError()
        else:
            for i in self.all_orders():
                if i.id == id:
                    i.mark_finished()

    
    def finished_orders(self):
        return [task for task in self.tasks if task.is_finished()]

    def unfinished_orders(self):
        return [task for task in self.tasks if not task.is_finished()]

    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            print('erroneous input')
        finished = len([i for i in self.finished_orders() if i.programmer == programmer])
        unfinished = len([i for i in self.unfinished_orders() if i.programmer == programmer])
        done = sum([i.workload for i in self.finished_orders() if i.programmer == programmer])
        undone = sum([i.workload for i in self.unfinished_orders() if i.programmer == programmer])

        return f"tasks: finished {finished} not finished {unfinished}, hours: done {done} scheduled {undone}"

t = OrderBook()
print('commands:')
print('0 exit')
print('1 add order')
print('2 list finished tasks')
print('3 list unfinished tasks')      
print('4 mark task as finished') 
print('5 programmers') 
print('6 status of programmer')
print()
while(True):
    command = input('command: ')
    if command == '0':
        break
    if command == '1':
        try:
            description = input('description: ')
            programmer_workload = input('programmer and workload estimate: ').strip().split(' ')
            t.add_order(description,programmer_workload[0],int(programmer_workload[1]))
            print('added!')
        except:
            print('erroneous input')

    elif command == '2':
        finished_task = t.finished_orders()
        if len(finished_task) == 0:
            print('no finished tasks')
        else: 
            for i in finished_task:
                print(i)
    elif command == '3':
        unfinished_task = t.unfinished_orders()
        if len(unfinished_task) == 0:
            print('no unfinished tasks')
        else: 
            for i in unfinished_task:
                print(i)
    elif command == '4':
        try:
            id = int(input('id: '))
            t.mark_finished(id)
            print('marked as finished')
        except:
            print('erroneous input')
    elif command == '5':
        for i in t.programmers():
            print(i)
    elif command == '6':
        programmer = input('programmer: ')
        print(t.status_of_programmer(programmer))