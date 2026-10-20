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

root.mainloop()