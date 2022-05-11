"""
Make a program that calculate the weighted average of the 3-evidence grades.
The first and second race has weight 1 and the third has weight 2.
At the end, show the student's average and indicate whether the student has passed or failed.
The rating for approval must be 60 points or more.
"""

note_first: float = float(input("First note: "))
note_second: float = float(input("Second note: "))
note_third: float = float(input("Third note: "))

average: float = ((note_first * 1) + (note_second * 1) + (note_third * 2)) / (1 + 1 + 2)
if average >= 60:
    print(f"Student has passed!")
else:
    print(f"Student has failed!")
