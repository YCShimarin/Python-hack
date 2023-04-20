import json

# membaca file JSON untuk mendapatkan data pengguna yang telah terdaftar
with open("users.json", "r") as f:
    users = json.load(f)

# fungsi untuk mendaftarkan pengguna baru


def register():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    # menambahkan pengguna baru ke dalam data pengguna
    users[username] = {"password": password}
    # menyimpan perubahan data pengguna ke dalam file JSON
    with open("users.json", "w") as f:
        json.dump(users, f,  indent=4)
    print("Registrasi berhasil!")

# fungsi untuk melakukan login


def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    # memeriksa apakah pengguna sudah terdaftar
    if username not in users:
        print("Username tidak terdaftar!")
    # memeriksa apakah password yang dimasukkan sesuai dengan yang terdaftar
    elif password != users[username]["password"]:
        print("Password salah!")
    else:
        print("Login berhasil!")


# program utama
while True:
    print("1. Register")
    print("2. Login")
    print("3. Keluar")
    choice = input("Pilihan: ")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Pilihan tidak valid!")
