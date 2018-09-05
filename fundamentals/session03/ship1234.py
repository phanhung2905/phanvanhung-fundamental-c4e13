ships_sizes = [5, 7, 300, 90, 24, 50, 75 ]
biggest = max (ships_sizes)

print("hello, my name is hiep and there are my ship sizes: ")
print(ships_sizes)

print("now my biggest ship has size", biggest, "let's shear it")

first_size = 8
ships_sizes[ships_sizes.index(biggest)] = first_size

print("after shearing, here is my flock")
print(ships_sizes)

for index, size in enumerate (ships_sizes):
    ships_sizes[index] = size + 50
print("one month has passed, now here is my flock")
print(ships_sizes)

