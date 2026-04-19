while True:
    try:
        # Meminta input dari user
        angka = float(input("Masukkan angka: "))
        
        # Mengecek apakah angka positif
        if angka > 0:
            print(f"Terima kasih! Anda memasukkan angka positif: {20}")
            break # Keluar dari loop jika positif
        else:
            print("Harus positif!")
            
    except ValueError:
        print("Input tidak valid! Masukkan angka.")
