import json
import os

DB_FILE = "data.json"

def load_data():
    if not os.path.exists(DB_FILE):
        return []
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_student(nim, nama, absen, tugas, uts, uas, nilai_akhir, grade, keterangan):
    data = load_data()
    data.append({
        "NIM": nim,
        "Nama": nama,
        "Absen (10%)": absen,
        "Tugas (20%)": tugas,
        "UTS (30%)": uts,
        "UAS (40%)": uas,
        "Nilai Akhir": nilai_akhir,
        "Grade": grade,
        "Keterangan": keterangan
    })
    save_data(data)

def update_student(index, nim, nama, absen, tugas, uts, uas, nilai_akhir, grade, keterangan):
    data = load_data()
    if 0 <= index < len(data):
        data[index] = {
            "NIM": nim,
            "Nama": nama,
            "Absen (10%)": absen,
            "Tugas (20%)": tugas,
            "UTS (30%)": uts,
            "UAS (40%)": uas,
            "Nilai Akhir": nilai_akhir,
            "Grade": grade,
            "Keterangan": keterangan
        }
        save_data(data)

def delete_student(index):
    data = load_data()
    if 0 <= index < len(data):
        data.pop(index)
        save_data(data)
