import requests
import json

# Kirim permintaan GET ke API dan simpan respons sebagai objek response
response = requests.get("https://api.myquran.com/v1/sholat/jadwal/0314/2023/04/17")

# Ubah respons menjadi objek Python dengan format JSON
data = json.loads(response.text)

# Simpan data dalam file JSON dengan format yang rapi
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

print(json.dumps(data, indent=4))






# # Ubah respons menjadi objek Python
# data = response.json()

# # Simpan objek Python ke file JSON
# with open("data.json", "w") as outfile:
#     json.dump(data, outfile)
