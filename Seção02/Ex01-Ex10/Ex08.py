"""
Make a program that read two grades of a student, check if the grades are valid and show on screen the average of
these grades. One note valid must be necessarily, a value between 0.0 and 10.0, where case the note does not have a
valid value, this fact must be informed to the user and the program ends.
"""

note_one: float = float(input("Write the first note of a student: "))
note_two: float = float(input("Write teh second note of a student: "))
if note_one >= 0.0 and note_two >= 0.0:
    if note_one <= 10.0 and note_two <= 10.0:
        print(f"The average of these grades is: {(note_one + note_two) / 2}")
    else:
        print("These grades aren't valid!")
else:
    print("These grades aren't valid!")
