import json

def muat_saldo():
    try:
        with open('saldo.json', 'r') as f:
            data = json.load(f)
            return data.get('saldo', 0)
    except FileNotFoundError:
        return 0

def simpan_saldo():
    with open('saldo.json', 'w') as f:
        json.dump({'saldo': saldo}, f)

saldo = muat_saldo()

def tambah_pemasukan():
    global saldo
    jumlah = float(input("Masukkan jumlah pemasukan: "))
    saldo += jumlah
    print("Pemasukan berhasil ditambahkan!")

def tambah_pengeluaran():
    global saldo
    jumlah = float(input("Masukkan jumlah pengeluaran: "))
    if saldo >= jumlah:
        saldo -= jumlah
        print("Pengeluaran berhasil ditambahkan!")
    else:
        print("Saldo tidak cukup!")

def lihat_saldo():
    print(f"Saldo saat ini: Rp {saldo}")

def menu():
    print("=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Keluar")

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
        simpan_saldo()
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid")