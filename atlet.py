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