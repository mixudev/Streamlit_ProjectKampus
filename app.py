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
        with st.container(border=True):
            st.markdown("### Informasi & Aturan Sistem Penilaian")
            st.write("Selamat datang di panduan **EduGrade**. Sistem ini dibuat agar perhitungan nilai menjadi sepenuhnya otomatis, sehingga meminimalisir kesalahan perhitungan (*human error*). Berikut adalah penjelasan mengenai cara kerja dan kriteria penilaian dari aplikasi ini:")
            
            st.markdown("#### 1. Bagaimana Nilai Akhir Dihitung?")
            st.write("Setiap nilai yang Anda masukkan di formulir (Skala 0 sampai 100) tidak langsung dijumlahkan begitu saja. Setiap komponen memiliki \"bobot\" atau persentase pengaruhnya masing-masing terhadap Nilai Akhir:")
            st.markdown("""
            - **Nilai Kehadiran:** Mempengaruhi 10% dari Nilai Akhir.
            - **Nilai Tugas:** Mempengaruhi 20% dari Nilai Akhir.
            - **Nilai UTS (Ujian Tengah Semester):** Mempengaruhi 30% dari Nilai Akhir.
            - **Nilai UAS (Ujian Akhir Semester):** Mempengaruhi paling besar, yaitu 40% dari Nilai Akhir.
            """)
            
            st.markdown("#### 2. Standar Predikat Huruf (Grade)")
            st.write("Setelah sistem selesai menjumlahkan semua komponen menjadi Nilai Akhir, sistem akan secara cerdas (*Rule-Based*) menentukan huruf mutu (Grade) dan kelulusan menggunakan pedoman berikut:")
            
            with st.container(border=True):
                st.markdown("""
                - ✅ **Grade A:** Nilai Akhir 85 atau lebih &rarr; *(Lulus - Sangat Baik)*
                - ✅ **Grade B:** Nilai Akhir 70 sampai 84.9 &rarr; *(Lulus - Baik)*
                - ✅ **Grade C:** Nilai Akhir 55 sampai 69.9 &rarr; *(Lulus - Cukup)*
                - ❌ **Grade D:** Nilai Akhir 40 sampai 54.9 &rarr; *(Tidak Lulus - Kurang)*
                - ❌ **Grade E:** Nilai Akhir di bawah 40 &rarr; *(Tidak Lulus - Sangat Kurang)*
                """)
                
            st.caption("* Aturan di atas dikelola di dalam 'Knowledge Base' sistem dan beroperasi secara otomatis.")