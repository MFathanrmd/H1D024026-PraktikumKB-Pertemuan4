# H1D024026-PraktikumKB-Pertemuan4
# LAPORAN PRAKTIKUM KECERDASAN BUATAN
# SISTEM PAKAR (REPRESENTASI PENGETAHUAN & INFERENSI)

Nama       : Muhammad Fathan Ramdani <br>
NIM        : H1D024026 <br>
Shif Awal  : A <br>
Shif baru  : B <br>

1. Deskripsi Program <br>
    ini merupakan implementasi sistem pakar untuk mendiagnosa kerusakan perangkat keras komputer atau laptop. Aplikasi dikembangkan menggunakan bahasa pemrograman Python dengan bantuan pustaka Tkinter sebagai antarmuka grafis.
    Pengguna dapat memilih gejala yang dialami melalui checkbox, kemudian sistem akan menampilkan hasil diagnosa beserta solusi berdasarkan analisis gejala tersebut.

2. Struktur Kode dan Basis Pengetahuan <br>
    A. Basis Pengetahuan (Knowledge Base) <br>
        Basis pengetahuan disimpan dalam bentuk dictionary database_kerusakan. Setiap data berisi:
        * Gejala: himpunan kode gejala
        * Solusi: langkah penanganan
    
    Contoh kerusakan yang digunakan antara lain RAM, Power Supply, Overheat, VGA, dan Hardisk/SSD.
    
    B. Daftar Gejala (Working Memory) <br>
      Data semua_gejala digunakan untuk memetakan kode gejala ke deskripsi yang ditampilkan kepada pengguna. Data ini juga menjadi input utama dalam proses diagnosa.
    
    C. Mesin Inferensi (Inference Engine) <br>
      Sistem menggunakan metode Forward Chaining. Proses diagnosa dilakukan dengan menghitung tingkat kecocokan antara gejala yang dipilih dengan basis pengetahuan.
    
      Jika tingkat kecocokan memenuhi ambang batas tertentu (≥ 50%), maka kerusakan tersebut akan ditampilkan sebagai hasil diagnosa.
    
    D. Antarmuka Pengguna (GUI) <br>
      Antarmuka dibuat menggunakan Tkinter dalam kelas SistemPakarGUI, yang berfungsi untuk:
      * Menampilkan daftar gejala
      * Menerima input pengguna
      * Menampilkan hasil diagnosa melalui message box

3. Cara Menjalankan Program <br>
  Akses folder tugas melalui terminal, kemudian jalankan:
  <img width="1258" height="285" alt="image" src="https://github.com/user-attachments/assets/f1a888dd-ddac-431f-bf48-03a608e4a50a" />

4. Hasil dan Visualisasi Output <br>
  Program menampilkan hasil dalam bentuk antarmuka grafis (GUI) yang memudahkan pengguna dalam melakukan diagnosa. Hasil eksekusi didokumentasikan melalui tangkapan layar sebagai bukti bahwa aplikasi berjalan dengan baik. <br>
  Tampilan Antarmuka Grafis (GUI) <br>
  Saat program dijalankan, muncul jendela berisi daftar gejala dalam bentuk checkbox. Pengguna memilih gejala yang sesuai, kemudian menekan tombol “Proses Diagnosa”.
Sistem akan menampilkan hasil berupa jenis kerusakan yang terdeteksi beserta solusi, disertai tingkat kecocokan berdasarkan gejala yang dipilih.
<img width="937" height="1032" alt="Screenshot 2026-04-13 200050" src="https://github.com/user-attachments/assets/7507a5ac-0d78-4568-8c87-eb086925a099" />


Tampilan Hasil Diagnosa <br>
Setelah tombol ditekan, sistem akan memproses fakta yang ada dan menampilkan hasil diagnosa
<img width="617" height="400" alt="Screenshot 2026-04-13 200025" src="https://github.com/user-attachments/assets/5f228308-f3a9-4a87-842d-77a9eef81d02" />



