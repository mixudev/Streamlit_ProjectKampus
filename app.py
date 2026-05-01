import streamlit as st
from styles import apply_custom_css
from auth import login
from components import render_header, render_crud_interface, render_form_input, render_sidebar

st.set_page_config(
    page_title="EduGrade | Sistem Penilaian",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_custom_css()

if login():
    menu_selection = render_sidebar()
    render_header()
    
    if menu_selection == "Menu Utama":
        tab1, tab2 = st.tabs(["INPUT NILAI BARU", "DATA MAHASISWA"])
        
        with tab1:
            render_form_input()
            
        with tab2:
            render_crud_interface()
            
    elif menu_selection == "Informasi Sistem":
        st.markdown("""
        <div class="border border-solid theme-border p-6" style="border-width: 1px;">
            <h3 class="text-sm font-bold uppercase tracking-widest theme-text mb-4 border-b border-solid theme-border pb-2">Informasi & Aturan Sistem Penilaian</h3>
            <p class="text-sm theme-text mb-4 leading-relaxed">
            Selamat datang di panduan <b>EduGrade</b>. Sistem ini dibuat agar perhitungan nilai menjadi sepenuhnya otomatis, sehingga meminimalisir kesalahan perhitungan (<i>human error</i>). 
            Berikut adalah penjelasan mengenai cara kerja dan kriteria penilaian dari aplikasi ini:
            </p>
            <h4 class="text-sm font-bold theme-text mb-2 mt-6">1. Bagaimana Nilai Akhir Dihitung?</h4>
            <p class="text-sm theme-text mb-2 leading-relaxed">
            Setiap nilai yang Anda masukkan di formulir (Skala 0 sampai 100) tidak langsung dijumlahkan begitu saja. Setiap komponen memiliki "bobot" atau persentase pengaruhnya masing-masing terhadap Nilai Akhir:
            </p>
            <ul class="text-sm theme-text list-disc pl-5 mb-4 leading-relaxed">
                <li><strong>Nilai Kehadiran:</strong> Mempengaruhi 10% dari Nilai Akhir.</li>
                <li><strong>Nilai Tugas:</strong> Mempengaruhi 20% dari Nilai Akhir.</li>
                <li><strong>Nilai UTS (Ujian Tengah Semester):</strong> Mempengaruhi 30% dari Nilai Akhir.</li>
                <li><strong>Nilai UAS (Ujian Akhir Semester):</strong> Mempengaruhi paling besar, yaitu 40% dari Nilai Akhir.</li>
            </ul>
            <h4 class="text-sm font-bold theme-text mb-2 mt-6">2. Standar Predikat Huruf (Grade)</h4>
            <p class="text-sm theme-text mb-2 leading-relaxed">
            Setelah sistem selesai menjumlahkan semua komponen menjadi Nilai Akhir, sistem akan secara cerdas (<i>Rule-Based</i>) menentukan huruf mutu (Grade) dan kelulusan menggunakan pedoman berikut:
            </p>
            <div class="border border-solid theme-border p-4 theme-bg">
                <ul class="text-sm theme-text list-none pl-0 mb-0 leading-relaxed">
                    <li class="mb-1">✅ <strong>Grade A:</strong> Nilai Akhir 85 atau lebih &rarr; <i>(Lulus - Sangat Baik)</i></li>
                    <li class="mb-1">✅ <strong>Grade B:</strong> Nilai Akhir 70 sampai 84.9 &rarr; <i>(Lulus - Baik)</i></li>
                    <li class="mb-1">✅ <strong>Grade C:</strong> Nilai Akhir 55 sampai 69.9 &rarr; <i>(Lulus - Cukup)</i></li>
                    <li class="mb-1">❌ <strong>Grade D:</strong> Nilai Akhir 40 sampai 54.9 &rarr; <i>(Tidak Lulus - Kurang)</i></li>
                    <li class="mb-0">❌ <strong>Grade E:</strong> Nilai Akhir di bawah 40 &rarr; <i>(Tidak Lulus - Sangat Kurang)</i></li>
                </ul>
            </div>
            <p class="text-xs theme-text mt-6 opacity-60">
            * Aturan di atas dikelola di dalam "Knowledge Base" sistem dan beroperasi secara otomatis.
            </p>
        </div>
        """, unsafe_allow_html=True)