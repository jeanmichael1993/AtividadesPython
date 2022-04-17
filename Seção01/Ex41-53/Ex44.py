"""
Get the step height of a ladder and the height the user wants to reach by climbing the ladder.
Calculate and show how many steps the user must climb to reach his goal.

"""

step_height: float = float(input("Write the step height: "))
height_user: float = float(input("Write the height user: "))
steps = height_user / step_height
if int(steps) == 1:
    if height_user > step_height:
        print(f"Will be {int(steps + 1)} steps")
    elif height_user <= step_height:
        print(f"Will be {int(steps)} steps")
elif int(steps) == 0 and height_user < step_height:
    print(f"Will be {int(steps + 1)} steps")
else:
    print(f"Will be {int(steps)} steps")
