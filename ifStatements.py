name = input("Please enter your name : ")
age = int(input("How old are you, {0} ? ".format(name)))
print("{0} is {1} years old.".format(name, age))


if age < 18 :
    print("You are not eligible for voting!")
    print("Please come back in {0} years".format(18-age))
elif 150> age >= 18:
    print("You are eligible for voting!")
else :
    print("You sure you are not dead?")


