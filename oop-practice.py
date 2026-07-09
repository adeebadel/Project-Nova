class Task:

    def __init__(self, name, priority):

        self.name = name
        self.priority = priority
        self.status = "Pending"

    def show(self):

        print("\n====== TASK ======")
        print("Name     :", self.name)
        print("Priority :", self.priority)
        print("Status   :", self.status)


task1 = Task("Learn Python", "High")
task2 = Task("Gym", "Medium")

task1.show()
task2.show()

class Task:

    def __init__(self, name, priority):

        self.name = name
        self.priority = priority
        self.status = "Pending"

    def complete(self):

        self.status = "Completed"

    def rename(self, new_name):

        self.name = new_name

    def show(self):

        print("\n====== TASK ======")
        print("Name     :", self.name)
        print("Priority :", self.priority)
        print("Status   :", self.status)


task = Task("Python Practice", "High")

task.show()

task.complete()

task.rename("Advanced Python")

task.show()