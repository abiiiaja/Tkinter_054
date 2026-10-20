'''
•Buatlah GUI dengan Tkinter yang berisi:
   -1 label judul Aplikasi prediksi Prodi Pilihan
   -10 input nilai mata pelajaran
   -1 button bertuliskan Hasil Prediksi
   -1 label luaran hasil prediksi
•Atur posisi GUI sebaik mungkin!
•Fungsi Hasil Prediksi menuliskan prodi TeknologiInformasi apapun input yang diberikan!
'''


import tkinter as tk

root = tk.Tk()
root.title("Aplikasi prediksi Prodi Pilihan")
root.geometry("400x800")
root.configure(bg="#5B0EB5")

lbl = tk.Label(root, text="Aplikasi prediksi Prodi Pilihan",bg="#5B0EB5",foreground="white", font=("Arial", 14, "bold"))
lbl.grid(row=0, column=0, columnspan=2, pady=15)


root.mainloop()