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