# Tugas Praktikum: Sistem Cerdas (Rule-Based System & CRUD)

**Studi Kasus yang Dipilih:** Sistem Penentuan Nilai Akhir Mahasiswa

Aplikasi ini merupakan implementasi *Rule-Based System* terintegrasi dengan fitur **Login** dan **CRUD Sederhana (Create, Read, Delete)**. Sistem ini akan secara otomatis menghitung nilai akhir mahasiswa berdasarkan proporsi komponen nilai, lalu menentukan Grade huruf (A-E) dan Keterangan Kelulusan menggunakan sekumpulan logika IF-THEN.

---

## 1. Fakta (Facts)

Berikut adalah kumpulan fakta yang menjadi dasar pijakan logika penentuan nilai mahasiswa:

1. **Fakta Komponen Penilaian:** Terdapat 4 variabel yang diinputkan untuk menentukan hasil evaluasi: Kehadiran/Absen (bobot 10%), Tugas (bobot 20%), Ujian Tengah Semester / UTS (bobot 30%), dan Ujian Akhir Semester / UAS (bobot 40%).
2. **Fakta Nilai Akhir:** Nilai akhir merupakan hasil penjumlahan dari setiap nilai komponen yang telah dikalikan dengan bobotnya.
3. **Fakta Grade (Huruf Mutu):** Nilai Akhir diklasifikasikan ke dalam 5 Grade mutu: A, B, C, D, dan E.
4. **Fakta Batas Nilai:** Skala rentang penilaian dibagi dengan batas minimal sebagai berikut: >= 85 (A), >= 70 (B), >= 55 (C), >= 40 (D), dan di bawah 40 (E).
5. **Fakta Keterangan Kelulusan:** Mahasiswa dengan predikat Grade A, B, dan C dinyatakan Lulus. Sedangkan mahasiswa dengan predikat Grade D dan E dinyatakan Tidak Lulus.

---

## 2. Aturan IF-THEN (Rules)

Berdasarkan fakta-fakta di atas, berikut adalah rancangan aturan (*rules*) IF-THEN yang diimplementasikan untuk menentukan Grade dan Status kelulusan mahasiswa:

*   **Rule 1 (Grade A)**
    *   **IF** `Nilai Akhir >= 85`
    *   **THEN** Grade = "A" **AND** Keterangan = "Lulus (Sangat Baik)"

*   **Rule 2 (Grade B)**
    *   **IF** `Nilai Akhir >= 70` **AND** `Nilai Akhir < 85`
    *   **THEN** Grade = "B" **AND** Keterangan = "Lulus (Baik)"

*   **Rule 3 (Grade C)**
    *   **IF** `Nilai Akhir >= 55` **AND** `Nilai Akhir < 70`
    *   **THEN** Grade = "C" **AND** Keterangan = "Lulus (Cukup)"

*   **Rule 4 (Grade D)**
    *   **IF** `Nilai Akhir >= 40` **AND** `Nilai Akhir < 55`
    *   **THEN** Grade = "D" **AND** Keterangan = "Tidak Lulus (Kurang)"

*   **Rule 5 (Grade E)**
    *   **IF** `Nilai Akhir < 40`
    *   **THEN** Grade = "E" **AND** Keterangan = "Tidak Lulus (Sangat Kurang)"

---

## 3. Dokumentasi Aplikasi (Streamlit)

Aplikasi dibangun menggunakan *framework* **Streamlit** (Python) dan menerapkan standar arsitektur Modular dengan fitur-fitur sesuai ketentuan tugas:

*   **Sistem Login:** Aplikasi diproteksi dengan halaman autentikasi. Hanya pengguna dengan kredensial yang valid yang dapat mengakses *dashboard* penilaian (misal *username*: admin, *password*: admin). Status login dikelola menggunakan `st.session_state`.
*   **CRUD Sederhana:**
    *   **Create:** Input Form untuk memasukkan NIM, Nama, dan komponen nilai.
    *   **Read:** Data mahasiswa dan hasil otomatisasi penentuan Grade ditampilkan di layar menggunakan komponen *dataframe* tabel. Data dibaca dari media penyimpanan.
    *   **Delete:** Fitur penghapusan baris data mahasiswa berdasarkan nomor urut baris (Index).
    *   *(Data disimpan di dalam file lokal `data.json` agar *persistent* atau tidak hilang saat Streamlit direstart).*
*   **Otomatisasi Keterangan:** Pemanggilan fungsi `tentukan_grade()` dari modul `knowledge_base` secara otomatis memberikan kesimpulan nilai ketika formulir di-*submit*, yang mana fungsi tersebut murni dibangun dari kumpulan logika IF-THEN.

### Cara Menjalankan
1.  Buka terminal/CMD di dalam *folder* root proyek aplikasi.
2.  Eksekusi perintah: `streamlit run app.py`
3.  Login dan kelola data nilai mahasiswa secara *real-time*.
