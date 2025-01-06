class InputForm:
    @staticmethod
    def input_data():
        id_atlet = input("Masukkan ID Atlet: ")
        nama = input("Masukkan Nama Atlet: ")
        cabang = input("Masukkan Cabang Olahraga: ")
        umur = input("Masukkan Umur Atlet: ")
        return id_atlet, nama, cabang, int(umur)