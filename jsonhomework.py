import json

users = []

users.append({"name" : "Ali", "age" : 20})
users.append({"name" : "Vali", "age" : 21})
users.append({"name" : "Rizo", "age" : 19})
with open("users.json", "w") as file:
    json.dump(users, file)

with open("users.json", "r") as file:
    data = json.load(file)

print("Foydalanuvchilar royxati:")
for user in data:
    print(user)

import json

with open("users.json", "r") as file:
    users = json.load(file)

name = input("Ism kiriting:")
age = int(input("Yosh kiriting:"))

users.append({"name" : name, "age" : age})

with open("users.json", "w") as file:
    json.dump(users, file)

print("Yangi foydalanuvchi qoshildi!")

