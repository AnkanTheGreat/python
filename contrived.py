numbers = [1,45,22,12,60]

for number in numbers:
    if number % 8 == 0:
        #reject the list
        print("The numbers are unacceptable")
        break
else:
    print("All the numbers are fine")