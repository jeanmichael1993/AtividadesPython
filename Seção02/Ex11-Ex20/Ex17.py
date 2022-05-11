

larger_base: float = float(input("Write the larger base value: "))
smaller_base: float = float(input("Write the smaller base value: "))
if larger_base > 0 and smaller_base > 0:
    height: float = float(input("Write the height value: "))
    area: float = ((larger_base + smaller_base) * height) / 2
    print(f"The trapeze area value is {area:.2f} ")
else:
    print("Larger base or smaller base invalid!")
