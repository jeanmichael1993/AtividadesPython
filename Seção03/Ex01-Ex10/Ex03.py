import time
import os

cls = lambda: os.system('cls')
x: int = 10
while x > 0:
    print(x)
    x -= 1
    time.sleep(1)
    cls()

