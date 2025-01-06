## Nama    :Mochamad Nabil Kurnia
## Kelas   :TI.24.A4
## NIM     : 312410307
## Matkul  : Bahasa Pemrograman
## Project UAS Semester 1

![Screenshot 2025-01-06 133248](https://github.com/user-attachments/assets/feccb230-61aa-4278-b6ab-49bce3d5f2fb)

# dengan kode program

# Data

(dataatlet.py)

```python
class Atlet:
    def __init__(self, id_atlet, nama, cabang, umur):
        self.id_atlet = id_atlet
        self.nama = nama
        self.cabang = cabang
        self.umur = umur

class DataAtlet:
    def __init__(self):
        self.daftar_atlet = []

    def tambah_atlet(self, atlet):
        self.daftar_atlet.append(atlet)

    def hapus_atlet(self, id_atlet):
        self.daftar_atlet = [a for a in self.daftar_atlet if a.id_atlet != id_atlet]

    def ubah_atlet(self, id_atlet, nama_baru, cabang_baru, umur_baru):
        for atlet in self.daftar_atlet:
            if atlet.id_atlet == id_atlet:
                atlet.nama = nama_baru
                atlet.cabang = cabang_baru
                atlet.umur = umur_baru

    def cari_atlet(self, id_atlet):
        for atlet in self.daftar_atlet:
            if atlet.id_atlet == id_atlet:
                return atlet
        return None
  ````

# View

(atlet.py)

```python
class ViewAtlet:
    @staticmethod
    def tampilkan_data(data):
        print("\nDaftar Atlet:")
        print("-----------------------------------------------------------\n")
        print("| ID Atlet    | Nama              | Cabang         | Umur |\n")
        print("-----------------------------------------------------------\n")
        for atlet in data:
            print(f"| {atlet.id_atlet:<11} | {atlet.nama:<17} | {atlet.cabang:<14} | {atlet.umur:<4} |\n")
        print("-----------------------------------------------------------")
````



(input_from.py)

```python
class InputForm:
    @staticmethod
    def input_data():
        id_atlet = input("Masukkan ID Atlet: ")
        nama = input("Masukkan Nama Atlet: ")
        cabang = input("Masukkan Cabang Olahraga: ")
        umur = input("Masukkan Umur Atlet: ")
        return id_atlet, nama, cabang, int(umur)
````


# Main menu

```python
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
````

# Hasil kode program

![Screenshot 2025-01-06 201537](https://github.com/user-attachments/assets/25eca468-21b6-4c4a-b529-bac5f6370bed)
![image](https://github.com/user-attachments/assets/3cf977d9-5eb8-4598-b14d-80f55980ec13)
