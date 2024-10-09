# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku[True])

# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku1" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])
# print(daftar_buku)


# musik = {
# "judul 1" : "All we Know",
# "judul 2" : "Something Just Like This"
# }
# print(musik["judul 1"])
# print(musik["judul 2"])

# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "\"Izanami#6848"
#         "Email" : "iniemail@gmail.com"
#     }
# }

# print(Biodata["KRS"][0:])
# print(Biodata["Social Media"]["Email"])

# print(f"nama saya adalah {Biodata["Nama"]}")
# print(f"NIM Saya adalah {Biodata["NIM"]}")
# print(f"Instagram : {Biodata["Social Media"]["Instagram"]}")

# Games = {
#     "Game1" : "PUBG MOBILE",
#     "Game2" : "Mobile Legends",
#     "Game3" : {
#         "nama" : "coc",
#         "genre" : "strategy"
#     }
# }

# print((Games.get('Game 3')).get('genre'))

# games = dict(Sekiro = "Action", Pokemon = "Adventure",
# Valorant = {"nama" : {123 : "informatika"}})

# print(games['Valorant']['nama'][123])


# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }

# #tanpa menggunakan items
# for i in Nilai:
#     print(i)
# print("")

# #menggunakan items
# for mapel, nilai in Nilai.items():
#     print(f"Nilai {mapel} anda adalah {nilai}")

# Film = {
#     "Avenger Endgame" : "Action",
#     "Sherlock Holmes" : "Mystery",
#     "The Conjuring" : "Horror"
# }

# # # #Sebelum Ditambah
# # # # print(Film)

# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller", "Rush Hour" : "Comedy"})

# # #Setelah Ditambah
# # #Pengunnaan del
# # # del Film["Avenger Endgame"]

# # Simpan = Film.pop('Hours')
# # # Film.clear()
# # print(Film)
# # Film["Hours"] = Simpan
# # print(Film)
# print("Jumlah Film = ", len(Film))


# movies = Film.copy()
# print(movies)
# print("Jumlah Film = ", len(movies))

# key = "apel", "jeruk", "mangga", "semangka"
# value = 1,2,3
# buah = dict.fromkeys(key, value)
# print(buah)

# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }
# #menggunakan keys
# for i in Nilai.keys():
#     print(i)
# print("")
# #menggunakan value
# for i in Nilai.values():
#     print(i)

# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai Kimia : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)

# Musik = {
# "The Chainsmoker" : ["All we Know", "The Paris"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
# for song in j:
#     print(song)
# print("")

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     for x, y in value.items():
#         print (x, " : ", y)
# print("")



# Komik = {
#     "Komik_1" : "Boku No Hero",
#     "Komik_2" : "Fire Force",
#     "komik_3" : {
#         "Judul" : 
#         "Vol" : 1,
#         "pencipta"
#     }

# }


mahasiswa = {
    "Nama": "Melchi",
    "Umur": 18,
    "NIM": "2409106117",
    "Jurusan": "Informatika",
    "Angkatan": 2024
}


print("Data Mahasiswa Awal:")
print(mahasiswa)

#menambah data
mahasiswa["IPK"] = float(input("Masukkan nilai IPK: "))
print("Data setelah penambahan item (IPK):")
print(mahasiswa)

#mengubah data
key_ubah = input("Masukkan key yang ingin diubah: ")
if key_ubah in mahasiswa:
    mahasiswa[key_ubah] = input(f"Masukkan nilai baru untuk {key_ubah}: ")
else:
    print("Key tidak ditemukan.")
print("Data setelah perubahan:")
print(mahasiswa)

#menghapus data
key_hapus = input("Masukkan nama key yang ingin dihapus: ")
if key_hapus in mahasiswa:
    del mahasiswa[key_hapus]
else:
    print("Key tidak ditemukan.")
print("Data setelah penghapusan:")
print(mahasiswa)
