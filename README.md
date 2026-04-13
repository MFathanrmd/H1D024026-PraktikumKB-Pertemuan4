# H1D024026-PraktikumKB-Pertemuan4
LAPORAN PRAKTIKUM KECERDASAN BUATAN
SISTEM PAKAR (REPRESENTASI PENGETAHUAN & INFERENSI)

Nama       : Muhammad Fathan Ramdani
NIM        : H1D024026
Shif Awal  : A
Shif baru  : B

1. Deskripsi Program

Program ini merupakan implementasi sistem pakar untuk mendiagnosa kerusakan perangkat keras komputer atau laptop. Aplikasi dikembangkan menggunakan bahasa pemrograman Python dengan bantuan pustaka Tkinter sebagai antarmuka grafis.

Pengguna dapat memilih gejala yang dialami melalui checkbox, kemudian sistem akan menampilkan hasil diagnosa beserta solusi berdasarkan analisis gejala tersebut.

2. Struktur Kode dan Basis Pengetahuan
A. Basis Pengetahuan (Knowledge Base)
Basis pengetahuan disimpan dalam bentuk dictionary database_kerusakan. Setiap data berisi:
* Gejala: himpunan kode gejala
* Solusi: langkah penanganan

Contoh kerusakan yang digunakan antara lain RAM, Power Supply, Overheat, VGA, dan Hardisk/SSD.

B. Daftar Gejala (Working Memory)
Data semua_gejala digunakan untuk memetakan kode gejala ke deskripsi yang ditampilkan kepada pengguna. Data ini juga menjadi input utama dalam proses diagnosa.

C. Mesin Inferensi (Inference Engine)
Sistem menggunakan metode Forward Chaining. Proses diagnosa dilakukan dengan menghitung tingkat kecocokan antara gejala yang dipilih dengan basis pengetahuan.

Jika tingkat kecocokan memenuhi ambang batas tertentu (≥ 50%), maka kerusakan tersebut akan ditampilkan sebagai hasil diagnosa.

D. Antarmuka Pengguna (GUI)
Antarmuka dibuat menggunakan Tkinter dalam kelas SistemPakarGUI, yang berfungsi untuk:
* Menampilkan daftar gejala
* Menerima input pengguna
* Menampilkan hasil diagnosa melalui message box

3. Cara Menjalankan Program
Akses folder tugas melalui terminal, kemudian jalankan:
<img width="1258" height="285" alt="image" src="https://github.com/user-attachments/assets/f1a888dd-ddac-431f-bf48-03a608e4a50a" />

