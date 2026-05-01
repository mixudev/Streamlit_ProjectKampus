def diagnosa(gejala, durasi, usia):
    # Returns: (kondisi, tingkat_label, urgency_color, penanganan, saran)
    G, D, U = gejala, durasi, usia

    if G == "Demam":
        if D == "< 3 hari":
            if U == "Anak (0–12 th)":
                return ("Demam Akut pada Anak", "Perlu Perhatian", "yellow",
                        "Kompres hangat, pastikan hidrasi cukup, pantau suhu setiap 4 jam. Berikan parasetamol sesuai dosis berat badan.",
                        "Jika suhu > 39°C atau muncul kejang, segera bawa ke IGD. Waspadai tanda dehidrasi: mulut kering, tidak buang air kecil.")
            elif U == "Lansia (> 60 th)":
                return ("Demam Akut pada Lansia", "Segera Tangani", "red",
                        "Segera konsultasi ke dokter. Lansia sangat rentan terhadap komplikasi infeksi meski gejala awalnya ringan.",
                        "Cek riwayat penyakit penyerta (diabetes, jantung). Jangan tunda pemeriksaan medis. Pastikan asupan cairan terjaga.")
            else:
                return ("Demam Akut Ringan", "Ringan", "green",
                        "Istirahat cukup, minum air putih 2–3 liter/hari. Konsumsi parasetamol jika perlu sesuai dosis.",
                        "Monitor suhu tubuh setiap 6 jam. Jika demam tidak turun dalam 3 hari, disertai ruam atau sesak napas, segera konsultasi dokter.")
        elif D == "3–7 hari":
            return ("Demam Berkepanjangan", "Perlu Perhatian", "yellow",
                    "Pemeriksaan darah lengkap diperlukan untuk menyingkirkan tifoid, dengue, atau infeksi lainnya.",
                    "Segera ke fasilitas kesehatan. Hindari antibiotik tanpa resep dokter. Catat riwayat bepergian dalam 2 minggu terakhir.")
        else:
            return ("Demam Kronik (> 7 hari)", "Segera Tangani", "red",
                    "Konsultasi dokter spesialis penyakit dalam. Diperlukan investigasi menyeluruh termasuk foto toraks dan kultur darah.",
                    "Demam kronik bisa mengindikasikan TB, endokarditis, atau keganasan. Jangan tunda rujukan ke spesialis.")

    elif G == "Batuk":
        if D == "< 3 hari":
            return ("Batuk Akut Ringan", "Ringan", "green",
                    "Minum air hangat dengan madu, istirahat cukup, hindari paparan debu dan asap rokok.",
                    "Gunakan obat batuk sesuai jenis: ekspektoran untuk batuk berdahak, antitusif untuk batuk kering. Jika disertai sesak, segera ke dokter.")
        elif D == "3–7 hari":
            if U == "Anak (0–12 th)":
                return ("Batuk Sub-Akut pada Anak", "Perlu Perhatian", "yellow",
                        "Periksa ke dokter anak untuk memastikan tidak ada infeksi saluran napas bawah atau pneumonia.",
                        "Waspadai: napas cepat, tarikan dinding dada, atau bibir kebiruan. Segera ke IGD jika tanda tersebut muncul.")
            else:
                return ("Batuk Sub-Akut", "Perlu Perhatian", "yellow",
                        "Konsultasi dokter umum. Kemungkinan infeksi saluran napas atas yang berlanjut atau post-nasal drip.",
                        "Hindari merokok. Jika dahak berwarna hijau/kuning atau disertai darah, segera periksakan diri.")
        else:
            return ("Batuk Kronik (> 7 hari)", "Segera Tangani", "red",
                    "Rujukan ke dokter spesialis paru diperlukan untuk skrining TB dan penyakit paru obstruktif.",
                    "Lakukan pemeriksaan sputum dan foto toraks. Jika ada kontak dengan pasien TB, sampaikan kepada dokter.")

    elif G == "Nyeri Kepala":
        if D == "< 3 hari":
            if U == "Lansia (> 60 th)":
                return ("Nyeri Kepala Akut pada Lansia", "Segera Tangani", "red",
                        "Segera konsultasi dokter. Nyeri kepala pada lansia perlu dievaluasi untuk menyingkirkan stroke atau perdarahan intrakranial.",
                        "Waspadai tanda stroke: kelemahan separuh badan, bicara pelo, penglihatan mendadak buram. Segera ke IGD.")
            elif U == "Anak (0–12 th)":
                return ("Nyeri Kepala pada Anak", "Perlu Perhatian", "yellow",
                        "Pastikan anak cukup minum, istirahat, dan tidak ada riwayat cedera kepala.",
                        "Jika disertai demam tinggi dan kaku leher, segera ke IGD (waspadai meningitis). Periksa ke dokter anak untuk evaluasi lebih lanjut.")
            else:
                return ("Tension Headache / Migrain", "Ringan", "green",
                        "Istirahat di ruangan tenang dan redup, kompres dingin di dahi, konsumsi analgesik ringan sesuai dosis.",
                        "Identifikasi dan hindari pemicu: stres, kurang tidur, kafein, atau layar terlalu lama. Jika nyeri seperti 'petir' mendadak, segera ke IGD.")
        elif D == "3–7 hari":
            return ("Nyeri Kepala Persisten", "Perlu Perhatian", "yellow",
                    "Konsultasi dokter untuk evaluasi. Hindari penggunaan analgesik berlebihan yang justru memperparah kondisi.",
                    "Catat pola nyeri: lokasi, intensitas, waktu, dan pemicu. Medication overuse headache dapat terjadi pada konsumsi obat > 10–15 hari/bulan.")
        else:
            return ("Nyeri Kepala Kronik", "Segera Tangani", "red",
                    "Rujuk ke dokter spesialis neurologi untuk evaluasi mendalam termasuk kemungkinan pencitraan otak.",
                    "Pemeriksaan MRI atau CT Scan kepala mungkin diperlukan. Jangan abaikan gejala yang berlangsung lebih dari seminggu.")

    elif G == "Nyeri Perut":
        if D == "< 3 hari":
            if U == "Anak (0–12 th)":
                return ("Nyeri Abdomen Akut pada Anak", "Perlu Perhatian", "yellow",
                        "Segera periksa ke dokter anak. Perlu disingkirkan kemungkinan apendisitis atau obstruksi.",
                        "Jangan berikan pereda nyeri kuat sebelum diperiksa dokter. Jika nyeri terpusat di kanan bawah perut, segera ke IGD.")
            else:
                return ("Dispepsia / Gastritis Akut", "Ringan", "green",
                        "Makan teratur dengan porsi kecil, hindari makanan pedas dan berlemak, konsumsi antasida jika diperlukan.",
                        "Jika nyeri sangat berat, perut terasa kaku seperti papan, atau disertai muntah darah, segera ke IGD tanpa menunggu.")
        elif D == "3–7 hari":
            return ("Nyeri Perut Sub-Akut", "Perlu Perhatian", "yellow",
                    "Pemeriksaan fisik dan laboratorium diperlukan untuk mengevaluasi organ abdomen secara menyeluruh.",
                    "Hindari self-medikasi. Konsultasikan ke dokter umum untuk pertimbangan USG abdomen jika diperlukan.")
        else:
            return ("Nyeri Perut Kronik", "Segera Tangani", "red",
                    "Rujukan ke dokter spesialis gastroenterologi atau penyakit dalam sangat dianjurkan.",
                    "Kemungkinan berhubungan dengan ulkus, penyakit Crohn, atau IBS. Endoskopi mungkin diperlukan untuk diagnosis definitif.")

    elif G == "Sesak Napas":
        if D == "< 3 hari":
            return ("Sesak Napas Akut", "Segera Tangani", "red",
                    "Segera ke IGD atau hubungi layanan gawat darurat (119). Duduk tegak dan longgarkan pakaian ketat.",
                    "Sesak napas adalah gejala gawat darurat. Jangan tunda. Beri tahu riwayat asma, jantung, atau alergi kepada petugas medis.")
        elif D == "3–7 hari":
            return ("Sesak Napas Persisten", "Segera Tangani", "red",
                    "Kunjungi dokter atau IGD segera. Diperlukan pemeriksaan saturasi oksigen, foto toraks, dan EKG.",
                    "Sesak beberapa hari membutuhkan evaluasi jantung dan paru menyeluruh. Hindari aktivitas fisik berat.")
        else:
            return ("Sesak Napas Kronik", "Segera Tangani", "red",
                    "Rujukan segera ke spesialis paru atau kardiologi. Jangan normalisasi sesak yang sudah berlangsung lama.",
                    "Kemungkinan PPOK, gagal jantung, atau asma tidak terkontrol. Pemeriksaan spirometri dan ekokardiografi diperlukan.")

    return ("Tidak dapat ditentukan", "–", "yellow",
            "Deskripsikan gejala lebih lengkap ke dokter.",
            "Konsultasikan langsung dengan tenaga medis.")
