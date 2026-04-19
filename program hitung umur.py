# Program penghitung umur

umur = int(input("Masukkan umur anda: "))

if umur >= 22 :
    print("anda cukup umur")
elif umur < 18:
    print("anda belum cukup umur")
elif umur < 0:
    print("anda belum lahir")
elif umur > 60:
    print("banyakin ibadah, bentar lagi mati")

print("Program selesai")
