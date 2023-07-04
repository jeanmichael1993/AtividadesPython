
list: int = ([x for x in range(1000, 9999+1)])
for item in list:
    converter: str = str(item)
    if (int(converter[0:2]) + int(converter[2:4])) ** 2 == item:
        print(f'{converter[0:2]} + {converter[2:4]} == {item}')

