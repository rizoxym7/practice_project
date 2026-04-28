from files_manager import save_users, load_users

users = []

name = input("name kiriting:")
age = int(input("age kiriting"))

users.append({"name": name, "age": age})

save_users(users)

data = load_users()

for user in data:
    print(user)