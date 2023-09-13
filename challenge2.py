print("1.Apple\n2.Banana\n3.Mango\n4.Kiwi\n5.Exit")
list = ["apple", "banana", "mango", "kiwi"]

while True:
    choice = input("Please select one option from the list:")

    if choice == "5":
        break
    elif choice in list:
        print("You chose {}".format(choice))









