import random
numbers = [2,5,7,2,4,6,3,2]

# limit_down = 0
# limit_up = len(numbers) - 1

# hasil = random.randint(limit_down,limit_up)

# print(f"Angka yang muncul adalah {numbers[hasil]}")

hasil = random.choice(numbers) # Pakai choice agar simpel untuk cari list acak
print(hasil)