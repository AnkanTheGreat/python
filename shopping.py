shopping_list = ["milk", "pasta", "eggs", "bread" , "sooji", "rice"]

# for item in shopping_list:
#     if item != "sooji":
#         print("Buy " + item)

for item in shopping_list :
    if item == "sooji":
        continue
    print("Buy "+ item)

