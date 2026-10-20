import tkinter as tk

# Fungsi untuk menampilkan hasil prediksi di window lain (Toplevel)
def hasil_prediksi():
    # Membuat window baru (popup)
    top = tk.Toplevel(root)
    top.title("Hasil Prediksi")
    top.geometry("320x200")
    top.configure(bg="#5B0EB5")
   
    # Mengatur agar window baru fokus di atas window utama
    top.transient(root)
    top.grab_set()
   
    # Label keterangan di window baru
    lbl_info = tk.Label(top, text="Prodi Prediksi Anda:", fg="white", bg="#5B0EB5", font=("Arial", 11))
    lbl_info.pack(pady=(25, 5))
   
    # Label hasil (selalu Teknologi Informasi apapun inputnya)
    lbl_hasil_value = tk.Label(top, text="Teknologi Informasi", fg="#00FFC8", bg="#5B0EB5", font=("Arial", 14, "bold"))
    lbl_hasil_value.pack(pady=5)
   
    # Tombol untuk menutup window hasil
    btn_tutup = tk.Button(top, text="Tutup", command=top.destroy, bg="white", fg="#5B0EB5", font=("Arial", 10, "bold"), padx=10)
    btn_tutup.pack(pady=15)




root = tk.Tk()
root.title("Aplikasi prediksi Prodi Pilihan")
root.geometry("450x850")
root.configure(bg="#5B0EB5")

# Agar frame di dalam root berada di tengah secara vertikal dan horizontal
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Frame utama sebagai wadah agar tetap di tengah saat di-resize
main_frame = tk.Frame(root, bg="#5B0EB5")
main_frame.grid(row=0, column=0)

# 1 Label Judul
lbl = tk.Label(main_frame, text="Aplikasi prediksi Prodi Pilihan", bg="#5B0EB5", fg="white", font=("Arial", 14, "bold"))
lbl.grid(row=0, column=0, columnspan=2, pady=(0, 15))

entry_list = []
for i in range(1, 11):
    label_mapel = tk.Label(main_frame, text=f"Nilai Mata Pelajaran {i}:", fg="white", bg="#5B0EB5", font=("Arial", 10, "bold"))
    label_mapel.grid(row=i, column=0, sticky="e", padx=10, pady=5)
   
    entry_mapel = tk.Entry(main_frame, width=25)
    entry_mapel.grid(row=i, column=1, sticky="w", padx=10, pady=5)
    entry_list.append(entry_mapel)

btn_hasil = tk.Button(main_frame, text="Hasil Prediksi", command=hasil_prediksi, bg="white", fg="#5B0EB5", font=("Arial", 10, "bold"))
btn_hasil.grid(row=11, column=0, columnspan=2, pady=15)

root.mainloop()