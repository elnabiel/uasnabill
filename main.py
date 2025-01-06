from data.dataatlet import Atlet, DataAtlet
from view.input_from import InputForm
from view.atlet import ViewAtlet

data_atlet = DataAtlet()

while True:
    print("\n=== Menu Data Atlet ===")
    print("1. Tambah Atlet")
    print("2. Hapus Atlet")
    print("3. Ubah Data Atlet")
    print("4. Tampilkan Data Atlet")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        id_atlet, nama, cabang, umur = InputForm.input_data()
        atlet = Atlet(id_atlet, nama, cabang, umur)
        data_atlet.tambah_atlet(atlet)
        print("Atlet berhasil ditambahkan!")

    elif pilihan == '2':
        id_atlet = input("Masukkan ID Atlet yang akan dihapus: ")
        data_atlet.hapus_atlet(id_atlet)
        print("Atlet berhasil dihapus!")

    elif pilihan == '3':
        id_atlet = input("Masukkan ID Atlet yang akan diubah: ")
        nama_baru = input("Masukkan Nama Baru: ")
        cabang_baru = input("Masukkan Cabang Baru: ")
        umur_baru = int(input("Masukkan Umur Baru: "))
        data_atlet.ubah_atlet(id_atlet, nama_baru, cabang_baru, umur_baru)
        print("Data atlet berhasil diubah!")

    elif pilihan == '4':
        ViewAtlet.tampilkan_data(data_atlet.daftar_atlet)

    elif pilihan == '5':
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")