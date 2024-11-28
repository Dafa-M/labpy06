# Code Program Pengelolaan Daftar Nilai Mahasiswa TI.24.A.3

data_mahasiswa = []

def tambah():
    nama = input("Masukkan nama mahasiswa: ")
    nilai = float(input("Masukkan nilai mahasiswa: "))
    data_mahasiswa.append({"nama": nama, "nilai": nilai})
    print("Data berhasil ditambahkan!")

def tampilkan():
    if not data_mahasiswa:
        print("=" * 34)
        print("--- Belum ada data mahasiswa ---")
        print("=" * 34)
    else:
        print()
        print("--- Daftar Nilai Mahasiswa A.3---")
        print("=" * 34)
        print("| NO |       NAMA       | NILAI |")
        print("-" * 33)
        for i, mahasiswa in enumerate(data_mahasiswa, 1):
            print(f"|{i:3}.| {mahasiswa['nama']:16} | {mahasiswa['nilai']:6}|")
        print("=" * 34)

def hapus(nama):
    global data_mahasiswa
    data_mahasiswa = [m for m in data_mahasiswa if m['nama'] != nama]
    print(f"Data mahasiswa dengan nama '{nama}' telah dihapus.")

def ubah(nama):
    for mahasiswa in data_mahasiswa:
        if mahasiswa['nama'] == nama:
            mahasiswa['nilai'] = float(input(f"Masukkan nilai baru untuk {nama}: "))
            print("Data berhasil diubah!")
            return
    print(f"Data mahasiswa dengan nama '{nama}' tidak ditemukan.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah()
        elif pilihan == "2":
            tampilkan()
        elif pilihan == "3":
            nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
            hapus(nama)
        elif pilihan == "4":
            nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
            ubah(nama)
        elif pilihan == "5":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

menu()
