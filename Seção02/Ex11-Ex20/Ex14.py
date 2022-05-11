"""
A student's final grade is calculated from three grades assigned between the ranger from 0 to 10, respectively,
to a laboratory work, a semiannual evaluation, and a final exam.
The average of the three notes mentioned above follows the weights: Laboratory Work: 2; Semiannual evaluation : 3;
Final exam: 5. According to the result, show on the screen if the student is disapproved (average between 0 and 2.9),
recovery (between 3 and 4.9) or if it was approved. Do all the necessary checks.
"""

laboratory_work: float = float(input("Laboratory work note's: "))
semiannual_evaluation: float = float(input("Semiannual evaluation note's: "))
final_exam: float = float(input("Final exam note's: "))

if 0 <= laboratory_work <= 10 and 0 <= semiannual_evaluation <= 10 and 0 <= final_exam <= 10:
        average: float = ((laboratory_work * 2) + (semiannual_evaluation * 3) + (final_exam * 5)) / (2 + 3 + 5)
        if 0 <= average <= 2.9:
            print(f"Student was disapproved!")
        elif 3 <= average <= 4.9:
            print(f"Student is recovery!")
        else:
            print(f"Student was approved!")
else:
    print("Number invalid!")
