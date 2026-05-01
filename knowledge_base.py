def hitung_nilai(absen, tugas, uts, uas):
    # Rule perhitungan nilai akhir: 10% Absen, 20% Tugas, 30% UTS, 40% UAS
    nilai_akhir = (absen * 0.10) + (tugas * 0.20) + (uts * 0.30) + (uas * 0.40)
    return round(nilai_akhir, 2)

def tentukan_grade(nilai_akhir):
    # Rule Based System IF-THEN penentuan Grade
    if nilai_akhir >= 85:
        return "A", "Lulus (Sangat Baik)", "green"
    elif nilai_akhir >= 70:
        return "B", "Lulus (Baik)", "green"
    elif nilai_akhir >= 55:
        return "C", "Lulus (Cukup)", "yellow"
    elif nilai_akhir >= 40:
        return "D", "Tidak Lulus (Kurang)", "red"
    else:
        return "E", "Tidak Lulus (Sangat Kurang)", "red"
