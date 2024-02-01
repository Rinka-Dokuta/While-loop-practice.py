import winsound
import random

choice = "Word"
while choice != 'q':
    winsound.Beep(random.randrange(200, 1000), random.randrange(200, 1000))
    choice = input("Press 'q' to quit:")
    if choice == 'q':
        break

print("No more beep :(")



num = 6
while num <= 36:
    print(num)
    num += 3
    
