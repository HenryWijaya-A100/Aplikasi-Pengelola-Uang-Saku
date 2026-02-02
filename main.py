import json

def muat_data():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return {'saldo': 0, 'pemasukan': [], 'pengeluaran': []}

def simpan_data():
    with open('data.json', 'w') as f:
        json.dump({'saldo': saldo, 'pemasukan': pemasukan, 'pengeluaran': pengeluaran}, f)

data = muat_data()
saldo = data['saldo']
pemasukan = data['pemasukan']
pengeluaran = data['pengeluaran']

def tambah_pemasukan():
    global saldo
    jumlah = float(input("Masukkan jumlah pemasukan: "))
    saldo += jumlah
    pemasukan.append(jumlah)
    print("Pemasukan berhasil ditambahkan!")

def tambah_pengeluaran():
    global saldo
    jumlah = float(input("Masukkan jumlah pengeluaran: "))
    if saldo >= jumlah:
        saldo -= jumlah
        pengeluaran.append(jumlah)
        print("Pengeluaran berhasil ditambahkan!")
    else:
        print("Saldo tidak cukup!")

def lihat_saldo():
    print(f"Saldo saat ini: Rp {saldo}")

def laporan():
    total_pemasukan = sum(pemasukan)
    total_pengeluaran = sum(pengeluaran)
    print("=== Laporan Rekap ===")
    print(f"Total Pemasukan: Rp {total_pemasukan}")
    print(f"Total Pengeluaran: Rp {total_pengeluaran}")
    print(f"Saldo Akhir: Rp {saldo}")
    if pemasukan:
        print("\nDaftar Pemasukan:")
        for i, p in enumerate(pemasukan, 1):
            print(f"{i}. Rp {p}")
    if pengeluaran:
        print("\nDaftar Pengeluaran:")
        for i, p in enumerate(pengeluaran, 1):
            print(f"{i}. Rp {p}")

def menu():
    print("=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Laporan")
    print("5. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pemasukan()
    elif pilihan == "2":
        tambah_pengeluaran()
    elif pilihan == "3":
        lihat_saldo()
    elif pilihan == "4":
        laporan()
    elif pilihan == "5":
        simpan_data()
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid")