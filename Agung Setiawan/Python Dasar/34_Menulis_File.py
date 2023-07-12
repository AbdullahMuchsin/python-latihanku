file = open("Database/data_1.txt", mode="a")

print(file.readable())
print(file.writable())

file.write("Kura - kura\n")

file.close()