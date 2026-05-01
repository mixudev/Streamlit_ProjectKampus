import streamlit as st
import pandas as pd
from crud import load_data, delete_student, update_student, add_student
from knowledge_base import hitung_nilai, tentukan_grade
from auth import logout

def render_sidebar():
    with st.sidebar:
        st.markdown("## 🎓 EduGrade\n**Edisi Profesional**")
        st.divider()
        menu = st.radio("Navigasi", ["Menu Utama", "Informasi Sistem"])
        st.write("")
        st.write("")
        if st.button("KELUAR SISTEM", use_container_width=True):
            logout()
        return menu

def render_header():
    with st.container(border=True):
        st.markdown("### Beranda Penilaian\nModul Pemrosesan Nilai Otomatis")

def render_form_input(form_key="input_nilai_utama"):
    is_edit = "edit_nim" in st.session_state and st.session_state.edit_nim is not None
    data = load_data()
    
    # Defaults
    def_nim = ""
    def_nama = ""
    def_absen = 0.0
    def_tugas = 0.0
    def_uts = 0.0
    def_uas = 0.0
    btn_label = "SIMPAN & PROSES NILAI"
    
    if is_edit:
        # Cari data mahasiswa berdasarkan NIM
        student_to_edit = next((s for s in data if s.get("NIM") == st.session_state.edit_nim), None)
        if student_to_edit:
            def_nim = student_to_edit.get("NIM", "")
            def_nama = student_to_edit.get("Nama", "")
            def_absen = float(student_to_edit.get("Absen (10%)", 0.0))
            def_tugas = float(student_to_edit.get("Tugas (20%)", 0.0))
            def_uts = float(student_to_edit.get("UTS (30%)", 0.0))
            def_uas = float(student_to_edit.get("UAS (40%)", 0.0))
            btn_label = "SIMPAN PERUBAHAN DATA"
        else:
            # Data tidak ditemukan, batalkan edit
            st.session_state.edit_nim = None
            st.rerun()

    with st.container(border=True):
        if is_edit:
            st.markdown("#### ✏️ Edit Data Mahasiswa")
            st.info("Anda sedang dalam mode Edit. Masukkan pembaruan data lalu simpan.")
        else:
            st.markdown("#### 📝 Formulir Input Nilai")
            st.caption("Silakan masukkan identitas mahasiswa beserta nilai dari masing-masing komponen. Sistem akan menghitung Nilai Akhir dan menentukan Huruf Mutu secara otomatis.")
            
        with st.form(form_key, clear_on_submit=not is_edit):
            col1, col2 = st.columns(2)
            with col1:
                nim = st.text_input("NIM Mahasiswa", value=def_nim, disabled=is_edit) # NIM tidak bisa diedit agar aman
                nama = st.text_input("Nama Lengkap Mahasiswa", value=def_nama)
            with col2:
                absen = st.number_input("Nilai Kehadiran (0 - 100)", min_value=0.0, max_value=100.0, step=1.0, value=def_absen)
                tugas = st.number_input("Nilai Tugas (0 - 100)", min_value=0.0, max_value=100.0, step=1.0, value=def_tugas)
                
            col3, col4 = st.columns(2)
            with col3:
                uts = st.number_input("Nilai UTS (0 - 100)", min_value=0.0, max_value=100.0, step=1.0, value=def_uts)
            with col4:
                uas = st.number_input("Nilai UAS (0 - 100)", min_value=0.0, max_value=100.0, step=1.0, value=def_uas)
                
            submitted = st.form_submit_button(btn_label, use_container_width=True)
            
            if submitted:
                if not nim or not nama:
                    st.error("Gagal: NIM dan Nama Mahasiswa wajib diisi!")
                else:
                    nilai_akhir = hitung_nilai(absen, tugas, uts, uas)
                    grade, keterangan, color = tentukan_grade(nilai_akhir)
                    
                    if is_edit:
                        update_student(st.session_state.edit_nim, nim, nama, absen, tugas, uts, uas, nilai_akhir, grade, keterangan)
                        st.session_state.edit_nim = None
                        st.success(f"Berhasil! Data {nama} telah diperbarui.")
                    else:
                        # Cek apakah NIM sudah ada
                        if any(s.get("NIM") == nim for s in data):
                            st.error("NIM tersebut sudah ada di sistem!")
                        else:
                            add_student(nim, nama, absen, tugas, uts, uas, nilai_akhir, grade, keterangan)
                            st.success(f"Berhasil! Data {nama} telah disimpan.")
                            
                        # Show metric
                        col_r1, col_r2, col_r3 = st.columns(3)
                        col_r1.metric("Nilai Akhir", nilai_akhir)
                        col_r2.metric("Huruf Mutu", grade)
                        col_r3.metric("Status", keterangan)
                    
        if is_edit:
            if st.button("BATAL EDIT", key=f"btn_cancel_{form_key}", use_container_width=True):
                st.session_state.edit_nim = None
                st.rerun()

def render_dashboard(data):
    if not data:
        return
        
    df = pd.DataFrame(data)
    
    st.markdown("#### 📊 Dashboard Analitik")
    col1, col2, col3 = st.columns(3)
    
    total_mhs = len(df)
    rata_rata = df["Nilai Akhir"].mean() if not df.empty else 0
    lulus_count = len(df[df["Grade"].isin(["A", "B", "C"])])
    
    with col1:
        st.metric("Total Mahasiswa", total_mhs)
    with col2:
        st.metric("Rata-rata Kelas", f"{rata_rata:.2f}")
    with col3:
        st.metric("Total Lulus", lulus_count)

def render_crud_interface():
    # Show edit form at the top if editing
    if "edit_nim" in st.session_state and st.session_state.edit_nim is not None:
        render_form_input(form_key="input_nilai_edit")
        st.write("")

    with st.container(border=True):
        data = load_data()
        
        if data:
            # Render Dashboard
            render_dashboard(data)
            st.divider()
            
            st.markdown("#### 📋 Daftar Nilai Mahasiswa")
            df = pd.DataFrame(data)
            
            # Display Data using Native st.dataframe
            st.dataframe(
                df,
                column_config={
                    "Absen (10%)": st.column_config.NumberColumn(format="%.1f"),
                    "Tugas (20%)": st.column_config.NumberColumn(format="%.1f"),
                    "UTS (30%)": st.column_config.NumberColumn(format="%.1f"),
                    "UAS (40%)": st.column_config.NumberColumn(format="%.1f"),
                    "Nilai Akhir": st.column_config.NumberColumn(format="%.2f"),
                },
                hide_index=True,
                use_container_width=True
            )
            
            st.markdown("##### Aksi Manajemen Data")
            col_search, col_action = st.columns([2, 1])
            with col_search:
                # Opsi Pilih NIM dari Dropdown untuk aman
                nims = df["NIM"].tolist()
                selected_nim = st.selectbox("Pilih NIM untuk Edit / Hapus", options=nims)
                
            with col_action:
                st.write("") # Spacer
                st.write("") # Spacer
                col_btn1, col_btn2 = st.columns(2)
                if col_btn1.button("✏️ Edit Data", use_container_width=True):
                    st.session_state.edit_nim = selected_nim
                    st.rerun()
                if col_btn2.button("🗑️ Hapus Data", use_container_width=True, type="primary"):
                    delete_student(selected_nim)
                    st.success(f"Data dengan NIM {selected_nim} berhasil dihapus.")
                    st.rerun()
        else:
            st.info("Belum ada data mahasiswa yang tersimpan di dalam sistem.")
