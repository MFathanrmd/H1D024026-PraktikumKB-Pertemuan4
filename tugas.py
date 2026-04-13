import tkinter as tk
from tkinter import messagebox

database_kerusakan = {
    "RAM Bermasalah": {
        "gejala": {"komputer_berbunyi_beep", "layar_blank_hitam", "sering_bluescreen"},
        "solusi": "Lepas RAM lalu bersihkan bagian pin dengan penghapus, kemudian pasang kembali dengan benar."
    },
    "Power Supply Rusak": {
        "gejala": {"mati_mendadak_saat_berat", "bau_hangus", "mati_total"},
        "solusi": "Periksa kabel dan catu daya. Jika perlu, ganti PSU dengan yang sesuai spesifikasi."
    },
    "Overheat (Panas Berlebih)": {
        "gejala": {"kipas_kencang", "mati_setelah_lama_menyala", "suhu_sangat_panas"},
        "solusi": "Bersihkan kipas dan heatsink, serta gunakan thermal paste baru."
    },
    "Kerusakan VGA": {
        "gejala": {"garis_layar", "warna_kacau", "gambar_pecah"},
        "solusi": "Update driver VGA atau periksa kondisi hardware VGA."
    },
    "Kerusakan Hardisk/SSD": {
        "gejala": {"booting_lambat", "bunyi_klik_disk", "pesan_boot_failure"},
        "solusi": "Segera backup data dan lakukan pengecekan disk atau ganti storage."
    }
}

semua_gejala = {
    "komputer_berbunyi_beep": "Komputer berbunyi beep berulang saat dinyalakan",
    "layar_blank_hitam": "Layar hanya menampilkan warna hitam",
    "sering_bluescreen": "Sering terjadi Blue Screen / crash",
    "mati_mendadak_saat_berat": "Mati tiba-tiba saat menjalankan program berat",
    "bau_hangus": "Tercium bau hangus dari dalam casing",
    "mati_total": "Tidak menyala sama sekali saat tombol power ditekan",
    "kipas_kencang": "Kipas berputar sangat kencang dan berisik",
    "mati_setelah_lama_menyala": "Mati setelah digunakan beberapa menit",
    "suhu_sangat_panas": "Perangkat terasa sangat panas",
    "garis_layar": "Muncul garis atau titik aneh di layar",
    "warna_kacau": "Warna layar tidak normal",
    "gambar_pecah": "Tampilan pecah saat digunakan",
    "booting_lambat": "Proses booting sangat lambat",
    "bunyi_klik_disk": "Ada bunyi klik dari hardisk",
    "pesan_boot_failure": "Muncul pesan gagal booting"
}

class SistemPakarGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Diagnosa Komputer")
        self.root.geometry("620x650")
        self.root.configure(bg="#f4f6f7")

        title = tk.Label(root, text="Aplikasi Diagnosa Kerusakan Komputer",
                         font=("Helvetica", 16, "bold"), bg="#f4f6f7")
        title.pack(pady=10)

        instruksi = tk.Label(root,
                             text="Pilih gejala yang sesuai dengan kondisi perangkat Anda:",
                             font=("Helvetica", 10), bg="#f4f6f7")
        instruksi.pack(pady=5)

        frame = tk.Frame(root, bg="#f4f6f7")
        frame.pack(fill="both", expand=True, padx=20, pady=10)

        canvas = tk.Canvas(frame, bg="#f4f6f7")
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)

        self.scroll_frame = tk.Frame(canvas, bg="#f4f6f7")

        self.scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.checkbox_vars = {}
        for kode, teks in semua_gejala.items():
            var = tk.BooleanVar()
            cb = tk.Checkbutton(self.scroll_frame, text=teks,
                                variable=var,
                                bg="#f4f6f7",
                                font=("Arial", 10),
                                anchor="w",
                                justify="left",
                                wraplength=520)
            cb.pack(anchor="w", pady=2)
            self.checkbox_vars[kode] = var

        # Tombol
        btn = tk.Button(root,
                        text="Proses Diagnosa",
                        command=self.diagnosa,
                        font=("Helvetica", 12, "bold"),
                        bg="#2ecc71",
                        fg="white")
        btn.pack(pady=15)

        footer = tk.Label(root, text="Sistem Diagnosa Sederhana",
                          font=("Arial", 8), bg="#f4f6f7")
        footer.pack()

        def diagnosa(self):
        gejala_user = set()

        for kode, var in self.checkbox_vars.items():
            if var.get():
                gejala_user.add(kode)

        hasil = []

        for nama, data in database_kerusakan.items():
            gejala_db = data["gejala"]

            cocok = gejala_db.intersection(gejala_user)
            skor = len(cocok) / len(gejala_db)

            if skor >= 0.5:
                hasil.append((nama, data["solusi"], skor))

        if hasil:
            teks = "Hasil analisa sistem:\n\n"
            for i, (penyakit, solusi, skor) in enumerate(hasil, 1):
                persen = int(skor * 100)
                teks += f"{i}. {penyakit} ({persen}%)\n"
                teks += f"   Solusi: {solusi}\n\n"

            messagebox.showinfo("Hasil Diagnosa", teks)

        else:
            messagebox.showwarning(
                "Hasil Diagnosa",
                "Gejala yang dipilih belum cukup untuk menentukan kerusakan secara pasti.\nSilakan lakukan pemeriksaan lebih lanjut."
            )


def main():
    root = tk.Tk()
    app = SistemPakarGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()