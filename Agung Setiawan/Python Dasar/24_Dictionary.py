data = {
    "name" : "Abdullah Muchsin",
    "age" : 18,
    "is_admin" : False
}

print(data)
print(data["age"])
print(data.get("is_admin"))

print(data.get("hobi"))
print(data.get("hobi", "Tidak ada variable hobi"))

data["hobi"] = "Menulis"
data["name"] = "Abdullah_Muchsin"

print(data)
print(data.get("hobi", "Tidak ada variable hobi"))
print(data['name'])

