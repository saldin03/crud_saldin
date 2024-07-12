from crud.lihat import lihat
from crud.create import create_record
from crud.update import update_record
from crud.delete import delete_record

def main():
    while True:
        print("\nMODIFIKASI DATABASE")
        print("-----------------------------------------")
        print("1. CREATE")
        print("2. READ")
        print("3. UPDATE")
        print("4. DELETE")
        print("5. EXIT")
        print("-----------------------------------------")

        pil = int(input("MASUKKAN PILIHAN: "))

        if pil == 1:
            nama = (input("Masukkan  nama: "))
            password = input("Masukkan password: ")
            create_record(nama, password )
            print("Data berhasil ditambahkan.")
            lihat()
        elif pil == 2:
            lihat()
        elif pil == 3:
            nama = (input("Masukkan nama baru : "))
            password = input("Masukkan password: ")
            update_record(nama, password)
            print("Data berhasil diupdate.")
            lihat()
        elif pil == 4:
            password = (input("Masukkan password yang mau dihapus: "))
            delete_record(password)
            print("Data berhasil dihapus.")
            lihat()
        elif pil == 5:
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak ada. Silakan coba lagi.")

if __name__ == "__main__":
    main()