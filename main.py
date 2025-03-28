class Kontak:
    def __init__(self):
        self.kontak = []

    def melihat_kontak(self):
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}, {item["nama"]}, {item["hp"]}, {item["email"]}')
        else:
            print("\nkontak masih kosong !! \n")
            return False
        return True

    def menambah_kontak(self):
        nama = input("masukkan nama kontak baru : ")
        hp = input("masukkan nomor kontak baru : ")
        email = input("masukkan email kontak baru : ")
        kontak_baru = {'nama': nama, 'hp': hp, 'email': email}
        self.kontak.append(kontak_baru)
        print("\nkontak baru berhasil di tambahkan ! \n")

    def menghapus_kontak(self):
        if not self.melihat_kontak():
            return
        else:
            i_hapus = int(input("\nmasukkan nomor kontak yang ingin di hapus : ")) - 1
            del self.kontak[i_hapus]
            print("kontak berhasil di hapus !")


kontak_kantor = Kontak()
kontak_keluarga = Kontak()

while True:
    print("-" * 35)
    print(f'{"Menu Utama":^35}')
    print("1. Menampilkan semua kontak")
    print("2. Menambah kontak baru")
    print("3. Menghapus kontak")
    print("4. keluar")
    print("-" * 35)
    pilihan = input("Masukkan pilihan anda (1,2,3) : ")

    if pilihan == '1':
        kontak_kantor.melihat_kontak()

    elif pilihan == '2':
        kontak_kantor.menambah_kontak()

    elif pilihan == '3':
        kontak_kantor.menghapus_kontak()

    elif pilihan == '4':
        break
    else:
        print("\npilihan yang anda masukkan tidak valid!!!\n")
