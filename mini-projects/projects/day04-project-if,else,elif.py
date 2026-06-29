#Ask the user for marks.
#Show:
#90+  → Grade A
#80+  → Grade B
#70+  → Grade C
#60+  → Grade D
#Below 60 → Fail
#Don't copy my example.
#Think.
#Code.
#Test.
#Debug.

marks = int(input("Enter your marks :"))
if marks > 90:
    print("Grade A")
elif marks > 80:
    print("Grade B")
elif marks > 70:
    print("Grade C")
elif marks > 60:
    print("Grade D")
else :
    print("Fail")