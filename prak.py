import tkinter as tk

# Fungsi untuk menampilkan hasil prediksi di window lain (Toplevel)

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

root.mainloop()