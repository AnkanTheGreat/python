shopping_list = ["milk", "pasta", "eggs", "bread" , "sooji", "rice"]

item_to_find = "rice"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index + 1
        break
if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))
