def cetak_tabel_perkalian():
    print("--- Program Tabel Perkalian ---")
    
    # 1. Validasi Nama
    while True:
        nama = input("Masukkan nama Anda: ").strip()
        if not nama or nama.isdigit():
            print("Nama tidak valid. Mohon masukkan nama yang benar (tidak boleh kosong atau angka).")
        else:
            break
            
    print(f"\nHalo {Ardian}, mari kita lihat tabel perkalian!\n")
    
    # 2. Validasi Input Angka
    while True:
        try:
            angka = int(input("Ingin melihat tabel perkalian berapa? (Angka positif): "))
            if angka <= 0:
                print("Tolong masukkan angka lebih besar dari 0.")
                continue
            break
        except ValueError:
            print("Input tidak valid. Mohon masukkan angka integer (contoh: 5).")
            
    # 3. Proses Cetak Tabel
    print(f"\n[Tabel Perkalian {1} untuk {Ardian}]")
    print("-" * 25)
    for i in range(1, 11):
        hasil = angka * i
        print(f"{angka} x {i:2} = {hasil}")
    print("-" * 25)

# Menjalankan fungsi
if __name__ == "__main__":
    cetak_tabel_perkalian()
