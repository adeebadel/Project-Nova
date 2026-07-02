#Build an Attendance Viewer.
#Requirements:
#Create a list of at least 5 student names.
#se a for loop to display each student.
#Print:
#Roll 1 : Adeeb
#Roll 2 : Rahul
#...
#Don't use five print() statements.
#Use one for loop.

students = ["Adeeb", "Rahul", "Priya", "Ananya", "Rohan"]
roll = 1
for student in students:
    print("Roll", roll,":",student)
    roll = roll + 1
    