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
            raise ValueError
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
            raise ValueError()
        return (len([i for i in self.finished_orders() if i.programmer == programmer])
                ,len([i for i in self.unfinished_orders() if i.programmer == programmer])
                ,sum([i.workload for i in self.finished_orders() if i.programmer == programmer])
                ,sum([i.workload for i in self.unfinished_orders() if i.programmer == programmer]))

