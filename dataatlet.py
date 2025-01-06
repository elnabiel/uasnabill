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