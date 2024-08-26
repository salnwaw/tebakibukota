import tkinter as tk
from tkinter import simpledialog, messagebox

# Fungsi untuk menampilkan pilihan ganda dan mendapatkan jawaban pengguna
def tampilkan_pilihan(pertanyaan, pilihan):
    jawaban = simpledialog.askstring("Soal", f"{pertanyaan}\n\n{pilihan}")
    return jawaban

# Fungsi untuk memulai kuis
def mulai_kuis():
    global poin, chance
    poin = 0
    chance = 3

    while chance > 0:
        if poin < 75:
            tk.messagebox.showinfo("Informasi", f"Anda harus mencapai nilai 75 agar kuis berhenti. Anda punya {chance} kesempatan")
            mulai = simpledialog.askstring("Mulai Kuis", "Anda siap? (Ya/Tidak): ")

            if mulai.lower() == "ya":
                poin = 0  # Reset poin jika memulai ulang
                chance -= 1

                # Soal 1
                soal1 = tampilkan_pilihan(
                    "Apa ibukota Jawa Barat?",
                    "a) Sumedang\nb) Depok\nc) Karawang\nd) Bandung"
                )
                if soal1.lower() == "d":
                    poin += 25
                    tk.messagebox.showinfo("Hasil", f"Selamat anda mendapat 25 poin, poin anda {poin}")
                else:
                    tk.messagebox.showinfo("Hasil", f"Maaf jawaban anda salah, poin anda {poin}")

                # Soal 2
                soal2 = tampilkan_pilihan(
                    "Apa ibukota Papua?",
                    "a) Batam\nb) Jayapura\nc) Merauke\nd) Nias"
                )
                if soal2.lower() == "b":
                    poin += 25
                    tk.messagebox.showinfo("Hasil", f"Selamat anda mendapat 25 poin, poin anda {poin}")
                else:
                    tk.messagebox.showinfo("Hasil", f"Maaf jawaban anda salah, poin anda {poin}")

                # Soal 3
                soal3 = tampilkan_pilihan(
                    "Apa ibukota Bali?",
                    "a) Denpasar\nb) Badung\nc) Buleleng\nd) Ciamis"
                )
                if soal3.lower() == "c":
                    poin += 25
                    tk.messagebox.showinfo("Hasil", f"Selamat anda mendapat 25 poin, poin anda {poin}")
                else:
                    tk.messagebox.showinfo("Hasil", f"Maaf jawaban anda salah, poin anda {poin}")

                # Soal 4
                soal4 = tampilkan_pilihan(
                    "Apa ibukota Sumatera Barat?",
                    "a) Solok\nb) Padang\nc) Bukittinggi\nd) Pariaman"
                )
                if soal4.lower() == "b":
                    poin += 25
                    tk.messagebox.showinfo("Hasil", f"Selamat anda mendapat 25 poin, poin anda {poin}")
                else:
                    tk.messagebox.showinfo("Hasil", f"Maaf jawaban anda salah, poin anda {poin}")

            elif mulai.lower() == "tidak":
                break
            else:
                tk.messagebox.showinfo("Informasi", "Maaf, silakan jawab dengan 'Ya' atau 'Tidak'")

        else:
            tk.messagebox.showinfo("Selesai", f"Selamat {nama}, anda sudah selesai, poin terakhir anda adalah {poin}")
            if poin >= 75:
                tk.messagebox.showinfo("Lulus", "Anda dinyatakan lulus")
            else:
                tk.messagebox.showinfo("Tidak Lulus", "Anda dinyatakan tidak lulus")
            break

    tk.messagebox.showinfo("Terima Kasih", "Baiklah, terima kasih :D!")

# Program utama
root = tk.Tk()
root.withdraw()  # Menyembunyikan jendela utama

# Input nama pengguna
nama = simpledialog.askstring("Input", "Masukkan nama:")
poin = 0
chance = 3

tk.messagebox.showinfo("Selamat Datang", f"Halo {nama}, selamat datang :>!")
tk.messagebox.showinfo("Informasi", "Anda akan diminta menjawab soal, dan mendapat poin bila benar")

# Mulai kuis
mulai_kuis()
