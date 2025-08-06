# data buku
books = [
    {"isbn":"9786237121144", "judul":"Kumpulan Solusi Pemrograman Python", "pengarang":"Budi Raharjo", "jumlah":6, "terpinjam":0},
    {"isbn":"9786231800718", "judul":"Dasar-Dasar Pengembangan Perangkat Lunak dan Gim Vol. 2", "pengarang":"Okta Purnawirawan", "jumlah":15, "terpinjam":0},
    {"isbn":"9786026163905", "judul":"Analisis dan Perancangan Sistem Informasi", "pengarang":"Adi Sulistyo Nugroho", "jumlah":2, "terpinjam":1},
    {"isbn":"9786022912828", "judul":"Animal Farm", "pengarang":"George Orwell", "jumlah":4, "terpinjam":0}
]

# data peminjaman
records = [
    {"isbn":"9786022912828", "status":"Selesai", "tanggal_pinjam":"2025-03-21", "tanggal_kembali":"2025-03-28"},
    {"isbn":"9786026163905", "status":"Belum", "tanggal_pinjam":"2025-07-22", "tanggal_kembali":""},
]

def tampilkan_data():
    print("---=== DATA BUKU ===---")
    if not books:
        print("Tidak ada data buku.")
    for book in books:
            print(f"ISBN: {book['isbn']}, Judul: {book['judul']}, Pengarang: {book['pengarang']}, Jumlah: {book['jumlah']}, Terpinjam: {book['terpinjam']}")


    

def tambah_data():
    print("---===--=== Tambah Buku Baru ---===--===")
    isbn = input("Masukan kode ISBN: ")
    nama = input("Nama Buku: ")
    judul = input("Masukkan judul buku: ")
    pengarang = input("Masukkan pengarang buku: ")
    jumlah = int(input("Masukkan jumlah buku: "))
    terpinjam = int(input("Masukkan buku yang terpinjam: "))
    books.append = {"nama":nama, "isbn":isbn, "judul":judul, "pengarang":pengarang, "jumlah":jumlah, "terpinjam":terpinjam,}
    print("Data Buku Sudah ditambahkan")
    tampilkan_data()


def edit_data():
    print("---===--=== Edit Data Buku ---===--===")
    isbn = input("Masukan kode ISBN: ")
    for book in books:
        if book["isbn"] == isbn:
            book["judul"] = input("Masukkan judul buku: ")
            book["pengarang"] = input("Masukkan pengarang buku: ")
            book["jumlah"] = int(input("Masukkan jumlah buku: "))
            print ("Data Buku Sudah diubah")
            tampilkan_data()
        

def hapus_data():
    print("---===--=== Hapus Data Buku ---===--===")
    isbn = input("Masukan kode ISBN: ")
    for book in books:
        if book["isbn"] == isbn:
            books.remove(book)
            print("Data Buku Sudah dihapus")
            tampilkan_data()
    

def tampilkan_peminjaman():
    print("--=== Data Peminjaman ---===--===")
    print(tabulate(records, headers="keys", tablefmt="grid"))

def tampilkan_belum():
    print("--=== Data Buku Belum Dipinjam ---===--===")
    print(tabulate([record for record in records if recor['tanggal_kembali'] is None], headers="keys", tablefmt="grid"))
    

def peminjaman():
    print("---===--=== Peminjaman Buku ---===--===")
    tampilkan_data()
    isbn = input("Masukan kode ISBN: ")
    nama = input("Nama peminjam: ")
    for book in books:
        if book["isbn"] == isbn:
            if book["jumlah"] > book["terpinjam"]:
                book["jumlah"] -= 1
                book["terpinjam"] += 1
                records.append({"isbn":isbn, "nama":nama, "status": "Belum", "tanggal_pinjam":datetime.now0, "tanggal_kembali":None})
                print("Peminjaman Buku Berhasil")
                tampilkan_data()
                return
            else:
                print("Buku Sudah habis")
                return
        print("--------------")        

def pengembalian():
    print("---===--=== Pengembalian Buku ---===--===")
    isbn = input("Masukan kode ISBN: ")
    for book in books:
        if book["isbn"] == isbn:
            for record in records:
                if record["isbn"] == isbn and record["status"] == "Belum":
                    record["status"] = "Sudah"
                    record["tanggal_kembali"] = datetime.now()
                    book["terpinjam"] -= 1
                    book["jumlah"] += 1
                    print("Pengembalian Buku Berhasil")
                    tampilkan_peminjaman()
                    return
    

while ...:
    print("---=== MENU ===---")
    print("[1] Tampilkan Data")
    print("[2] Tambah Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("------------------")
    print("[5] Tampilkan Semua Peminjaman")
    print("[6] Tampilkan Peminjaman Belum Kembali")
    print("[7] Peminjaman")
    print("[8] Pengembalian")
    print("[X] Keluar")

    menu = input("Masukkan pilihan menu (1-8 atau x): ")

    if menu == "1":
        tampilkan_data()
        input("Menampikan data")

    elif menu == "2":
        tambah_data()
        input("Menambahkan data")
        
    elif menu == "3":
        edit_data()
        input("Mengedit data")

    elif menu == "4":
        hapus_data()
        input("Menghapus Data")

    elif menu == "5":
        tampilkan_peminjaman()
        input("Menampilkan Peminjaman")
        
    elif menu == "6":
        tampilkan_belum()
        input("Menampilkan Pinjaman Belum Kembali")

    elif menu == "7":
        peminjaman()
        input("Menampilkan Peminjaman")
        
    elif menu == "8":
        pengembalian()
        input("Menampilkan Pinjaman Belum Kembali")

    elif menu.lower() == "x":
        pengembalian()
        input("Terima Kasih Anda Sudah Menggunakan Perpustakaan Kami")

    else:
        print("Pilihan menu tidak valid. Silakan memilih menu yang tersedia.")




        