from datetime import datetime

Harga_bbm = {"Pertalite": 10000, "Pertamax": 13400, "Pertamax Turbo": 15500, "Solar": 6800}
Riwayat_pembelian = []

def tampilkan_menu():
    print("\n Selamat datang di Pom Bensin\n 1. Beli Bahan Bakar\n 2. Tampilkan Riwayat Pembelian\n 3. Update Pembelian\n 4. Hapus Pembelian\n 5. Metode Pembayaran\n 6. Tampilkan harga bbm\n 7. Cari riwayat pembelian\n 8. Tampilkan statistik\n 9. keluar ")

def tampilkan_bbm():
    print(" Pilihan Bahan Bakar : ")
    menu_bbm = list(Harga_bbm.keys())
    for i, bbm in enumerate(menu_bbm, start=1):
        print(f"{i}. {bbm}")

def beli_bbm():
    tampilkan_bbm()
    pilihan = int(input(" Silahkan anda memilih jenis bahan bakar : "))

    today = datetime.now().strftime("%Y-%m-%d")
    unpaid_transactions = [transaksi for transaksi in Riwayat_pembelian if transaksi.get("Status Pembayaran") is None and transaksi.get("Tanggal") != today]

    if unpaid_transactions:
        print("Anda memiliki transaksi sebelumnya yang belum dibayar pada waktu yang berbeda.")
        print("Silakan lakukan pembayaran terlebih dahulu.")
        bayar()

    if pilihan in range(1, len(Harga_bbm) + 1):
        jenis_bbm = list(Harga_bbm.keys())[pilihan - 1]
        liter = float(input(f" Masukkan jumlah liter {jenis_bbm}: "))

        total_harga = liter * Harga_bbm[jenis_bbm]

        tanggal_pembelian = input("Masukkan tanggal pembelian (YYYY-MM-DD): ")
        purchase_data = {"Jenis BBM": jenis_bbm, "Liter": liter, "Total Harga": total_harga, "Tanggal": tanggal_pembelian, "Status Pembayaran": None}

        Riwayat_pembelian.append(purchase_data)

        print(f" Terima kasih telah memesan {liter} liter {jenis_bbm} seharga Rp {total_harga} pada tanggal {tanggal_pembelian}")
    else:
        print(" Pilihan tidak valid. Silakan pilih sesuai menu yang disediakan.")
    

def tampilkan_riwayat_pembelian():
    print("Riwayat Pembelian:")
    for beli in Riwayat_pembelian:
        status_pembayaran = beli.get("Status Pembayaran")
        tanda_pembayaran = "Sudah Dibayar" if status_pembayaran == "Sudah Dibayar" else "Belum Dibayar"
        print(f" Jenis BBM: {beli['Jenis BBM']} {beli['Liter']} Liter Dengan harga: Rp. {beli['Total Harga']} - {tanda_pembayaran}")

def update_pembelian():
    tampilkan_riwayat_pembelian()
    if Riwayat_pembelian:
        index = int(input("Pilih indeks transaksi yang ingin diupdate (Mulai dari 0): "))
        if 0 <= index < len(Riwayat_pembelian):
            if Riwayat_pembelian[index].get("Status Pembayaran") is None:
                jenis_bbm = Riwayat_pembelian[index]["Jenis BBM"]
                liter = float(input(f"Masukkan jumlah liter {jenis_bbm} yang baru: "))
                total_harga = liter * Harga_bbm[jenis_bbm]
                Riwayat_pembelian[index]["Liter"] = liter
                Riwayat_pembelian[index]["Total Harga"] = total_harga
                print(f"Transaksi berhasil diupdate.")
            else:
                print("Transaksi sudah dibayar. Tidak dapat diupdate.")
        else:
            print("Indeks transaksi tidak cocok.")
    else:
        print("Belum ada riwayat pembelian.")

def hapus_pembelian():
    tampilkan_riwayat_pembelian()
    if Riwayat_pembelian:
        index = int(input("Pilih indeks transaksi yang ingin dihapus (Mulai dari 0): "))
        if 0 <= index < len(Riwayat_pembelian):
            if Riwayat_pembelian[index].get("Status Pembayaran") is None:
                del Riwayat_pembelian[index]
                print("Transaksi berhasil dihapus.")
            else:
                print("Transaksi sudah dibayar. Tidak dapat dihapus.")
        else:
            print("Indeks transaksi tidak cocok.")
    else:
        print("Belum ada riwayat pembelian.")

def bayar():
    tampilkan_riwayat_pembelian()

    if Riwayat_pembelian:
        unpaid_transactions = [transaksi for transaksi in Riwayat_pembelian if transaksi.get("Status Pembayaran") is None]

        if unpaid_transactions:
            print("Anda akan membayar untuk semua transaksi di atas.")
            print("Silahkan pilih metode pembayaran anda :")

            print("\nPilihan Pembayaran:")
            print("1. Tunai")
            print("2. ATM")

            metode_pembayaran = int(input("Silakan pilih metode pembayaran (1 atau 2): "))

            if metode_pembayaran == 1:
                total_harga_semua = sum(transaksi["Total Harga"] for transaksi in unpaid_transactions)
                print(f"\nPembayaran tunai sebesar Rp {total_harga_semua} diterima. Terima kasih!")

                for transaksi in unpaid_transactions:
                    transaksi["Status Pembayaran"] = "Sudah Dibayar"
                    transaksi["Metode Pembayaran"] = "Tunai"

            elif metode_pembayaran == 2:
                print("\nPilihan Bank:")
                print("1. Bank A (PPN 10%)")
                print("2. Bank B (PPN 8%)")

                bank_choice = int(input("Silakan pilih bank (1 atau 2): "))

                total_harga_semua = sum(transaksi["Total Harga"] for transaksi in unpaid_transactions)
                
                if bank_choice == 1:
                    ppn = 0.1
                elif bank_choice == 2:
                    ppn = 0.08
                else:
                    print("Pilihan bank tidak valid.")
                    return

                total_harga_dengan_ppn = total_harga_semua + (total_harga_semua * ppn)
                print(f"\nPembayaran dengan ATM Bank {'A' if bank_choice == 1 else 'B'} sebesar Rp {total_harga_dengan_ppn} diterima (Termasuk PPN {ppn * 100}%). Terima kasih!")

                for transaksi in unpaid_transactions:
                    transaksi["Status Pembayaran"] = "Sudah Dibayar"
                    transaksi["Metode Pembayaran"] = f"ATM Bank {'A' if bank_choice == 1 else 'B'}"

            else:
                print("Pilihan metode pembayaran tidak valid.")

        else:
            print("Semua transaksi sudah dibayar. Tidak ada yang perlu dibayar lagi.")
    else:
        print("Belum ada riwayat pembelian.")

def tampilkan_harga_bbm():
    print("\n Daftar Harga Bahan Bakar:")
    for bbm, harga in Harga_bbm.items():
        print(f" {bbm}: Rp {harga} per liter")

def cari_riwayat_pembelian():
    tanggal = input("Masukkan tanggal pembelian (YYYY-MM-DD): ")
    hasil_pencarian = [beli for beli in Riwayat_pembelian if beli.get("Tanggal") == tanggal]
    
    if hasil_pencarian:
        print("\nRiwayat Pembelian pada tanggal", tanggal, ":")
        for beli in hasil_pencarian:
            status_pembayaran = beli.get("Status Pembayaran")
            tanda_pembayaran = "Sudah Dibayar" if status_pembayaran == "Sudah Dibayar" else "Belum Dibayar"
            print(f" Jenis BBM: {beli['Jenis BBM']} {beli['Liter']} Liter Dengan harga: Rp. {beli['Total Harga']} - {tanda_pembayaran} pada tanggal {beli['Tanggal']}")
    else:
        print("Tidak ditemukan riwayat pembelian pada tanggal tersebut.")

def tampilkan_statistik():
    transaksi_yang_sudah_dibayar = [transaksi for transaksi in Riwayat_pembelian if transaksi.get("Status Pembayaran") == "Sudah Dibayar"]

    if transaksi_yang_sudah_dibayar:
        total_transaksi = len(transaksi_yang_sudah_dibayar)
        total_harga_semua = sum(transaksi["Total Harga"] for transaksi in transaksi_yang_sudah_dibayar)
        rata_rata_harga = total_harga_semua / total_transaksi

        print(f"\nStatistik Pembelian (Sudah Dibayar):")
        print(f" - Jumlah Transaksi: {total_transaksi}")
        print(f" - Total Pendapatan: Rp {total_harga_semua}")
        print(f" - Rata-rata Harga Transaksi: Rp {rata_rata_harga}")
    else:
        print("Belum ada riwayat pembelian yang sudah dibayar.")

while True:
    tampilkan_menu()
    pilihan_menu = int(input(" Silakan pilih menu yang telah disediakan : "))

    if pilihan_menu == 1:
        beli_bbm()
    elif pilihan_menu == 2:
        tampilkan_riwayat_pembelian()
    elif pilihan_menu == 3:
        update_pembelian()
    elif pilihan_menu == 4:
        hapus_pembelian()
    elif pilihan_menu == 5:
        bayar()
    elif pilihan_menu == 6:
        tampilkan_harga_bbm()
    elif pilihan_menu == 7:
        cari_riwayat_pembelian()
    elif pilihan_menu == 8:
        tampilkan_statistik()
    elif pilihan_menu == 9:
        if any(transaksi.get("Status Pembayaran") is None for transaksi in Riwayat_pembelian):
            print("\nAnda memiliki pembelian yang belum dibayar.")
            print("Pilihan:")
            print("1. Batalkan pembelian yang belum dibayar")
            print("2. Bayar pembelian yang belum dibayar")

            pilihan_keluar = int(input("Silakan pilih (1 atau 2): "))

            if pilihan_keluar == 1:
                Riwayat_pembelian = [transaksi for transaksi in Riwayat_pembelian if transaksi.get("Status Pembayaran") is not None]
                print("Pembelian yang belum dibayar telah dibatalkan. Terima kasih telah menggunakan layanan kami!")
                break
            elif pilihan_keluar == 2:
                bayar()
                print("Terima kasih telah menggunakan layanan kami.")
                break
            else:
                print("Pilihan tidak valid. Kembali ke menu utama.")
        else:
            print("Terima kasih telah menggunakan layanan kami.")
            break
    else:
        print("Pilihan tidak valid. Silakan pilih sesuai menu yang sudah disediakan.")
