while True: #perulangan tanpa batas true artinya benar,jadi program akan jalan
    try:    #untuk menangani error
        # Meminta input dari user
        angka = float(input("Masukkan angka: ")) #float untuk mengubah input angka desimal
        
        # Mengecek apakah angka positif
        if angka > 0: #mengecek apakah angka lebih dari 0 positif
            print(f"Terima kasih! Anda memasukkan angka positif: {20}")
            break # Keluar dari loop jika positif
        else: # kondisi if tidak terpenuhi
            print("Harus positif!") #output kalau angka nol atau negatif program mengulang lagi le atas loop
            
    except ValueError:
        print("Input tidak valid! Masukkan angka.")
