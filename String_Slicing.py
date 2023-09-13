#         01234567890123
parrot = "norwegian blue"

print(parrot[0:6])
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])

print(parrot[10:14]) #blue
print(parrot[10:])

print(parrot[:4])
print(parrot[4:])

print(parrot[:4]+parrot[4:])

print(parrot[:])

letters = "abcdefghijklmnopqrstuvwxyz"



#negative slicing

print(parrot[-4:2]) #wrong

print(parrot[-13])

print(parrot[2:-5])


print(parrot[0:6:2]) #0 = starting point , 6 = index before the ending point, 2 = slicing index
print(parrot[0:6:3])

number = "2,442,456,757,445,876,256,457,577"
commas = number[1::4]

#slice_back
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[-1:-27:-1]

print(backwards)

print(letters[-10:-13:-1]) #qpo
print(letters[-22:-27:-1]) #edcba
print(letters[-1:-9:-1])

