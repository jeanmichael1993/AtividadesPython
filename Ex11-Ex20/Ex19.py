"""

Read an value in liters and introduce her in meters cubic m3. A formula of conversion is:
M = L/1000, being L the volume in liters and M the volume in meters cubic .


"""

value_in_liters = float(input("Write value in liters: "))
print(f"{value_in_liters/1000:.2f} meters cubic")

