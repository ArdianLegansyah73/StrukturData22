# Program penghitung umur

umur = int(input("Masukkan umur anda: "))#untuk menerima input dari user

if umur >= 22 :#jika lebih dari atau sama dengan 22 maka jalankan kode di bawah
    print("anda cukup umur")
elif umur < 18: #di cek kalau kondisi sebelumnya tidak terpenuhi jika umur kurang dari 18
    print("anda belum cukup umur")
elif umur < 0: #komdisi ini tidak akan pernah jlan,karena umur 18 sudah menangkap semua angka negatif
    print("anda belum lahir")
elif umur > 60: #karena sebelumnya umur 22 maka umur 60 sudah masuk kondisi pertama jika kondisi ini tidak pernah dijalankan
    print("banyakin ibadah, bentar lagi mati")

print("Program selesai")
