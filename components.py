import streamlit as st
import pandas as pd
from crud import load_data, delete_student, update_student
from knowledge_base import hitung_nilai, tentukan_grade
from auth import logout

def render_sidebar():
    with st.sidebar:
        st.markdown("""
        <div class="mt-4 mb-8">
            <h2 class="text-lg font-bold uppercase tracking-widest theme-text m-0">EduGrade</h2>
            <p class="text-xs theme-text opacity-50 m-0 uppercase tracking-widest">Edisi Profesional</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<p class='text-xs font-bold uppercase tracking-widest theme-text opacity-50 mb-2'>Menu Navigasi</p>", unsafe_allow_html=True)
        
        menu = st.radio(
            "Navigasi",
            ["Menu Utama", "Informasi Sistem"],
            label_visibility="collapsed"
        )
        
        st.markdown("<div class='mt-24'></div>", unsafe_allow_html=True)
        st.markdown("<hr class='border-t border-solid theme-border my-4'>", unsafe_allow_html=True)
        if st.button("KELUAR SISTEM", use_container_width=True):
            logout()
            
        return menu

def render_header():
    st.markdown("""
    <div class="border border-solid theme-border p-4 mb-6" style="border-width: 1px;">
        <h1 class="text-lg font-bold tracking-tight uppercase theme-text mb-1">Beranda Penilaian</h1>
        <p class="text-xs theme-text opacity-75 m-0 uppercase tracking-wider">Modul Pemrosesan Nilai Otomatis</p>
    </div>
    """, unsafe_allow_html=True)

def render_form_input(form_key="input_nilai_utama"):
    st.markdown('<div class="border border-solid theme-border p-4" style="border-width: 1px;">', unsafe_allow_html=True)
    
    is_edit = "edit_idx" in st.session_state and st.session_state.edit_idx is not None
    data = load_data()
    
    if is_edit and st.session_state.edit_idx < len(data):
        st.markdown('<h3 class="text-xs font-bold uppercase tracking-widest theme-text mb-4 border-b border-solid theme-border pb-2">Edit Data Mahasiswa</h3>', unsafe_allow_html=True)
        edit_data = data[st.session_state.edit_idx]
        def_nim = edit_data.get("NIM", "")
        def_nama = edit_data.get("Nama", "")
        def_absen = float(edit_data.get("Absen (10%)", 0.0))
        def_tugas = float(edit_data.get("Tugas (20%)", 0.0))
        def_uts = float(edit_data.get("UTS (30%)", 0.0))
        def_uas = float(edit_data.get("UAS (40%)", 0.0))
        btn_label = "SIMPAN PERUBAHAN DATA"
        st.info("Anda sedang dalam mode Edit. Masukkan pembaruan data lalu simpan.")
    else:
        st.markdown('<h3 class="text-xs font-bold uppercase tracking-widest theme-text mb-4 border-b border-solid theme-border pb-2">Formulir Input Nilai</h3>', unsafe_allow_html=True)
        def_nim = ""
        def_nama = ""
        def_absen = 0.0
        def_tugas = 0.0
        def_uts = 0.0
        def_uas = 0.0
        btn_label = "SIMPAN & PROSES NILAI"
        st.markdown("<p class='text-sm theme-text opacity-90 mb-4'>Silakan masukkan identitas mahasiswa beserta nilai dari masing-masing komponen. Sistem akan menghitung Nilai Akhir dan menentukan Huruf Mutu (Grade) serta status kelulusan secara otomatis.</p>", unsafe_allow_html=True)

    with st.form(form_key, clear_on_submit=False):
        col1, col2 = st.columns(2)
        with col1:
            nim = st.text_input("NIM Mahasiswa", value=def_nim)
            nama = st.text_input("Nama Lengkap Mahasiswa", value=def_nama)
        with col2:
            absen = st.number_input("Nilai Kehadiran (0 - 100)", min_value=0.0, max_value=100.0, step=1.0, value=def_absen)
            tugas = st.number_input("Nilai Tugas (0 - 100)", min_value=0.0, max_value=100.0, step=1.0, value=def_tugas)
            
        st.markdown("<div class='mt-2'></div>", unsafe_allow_html=True)
        col3, col4 = st.columns(2)
        with col3:
            uts = st.number_input("Nilai UTS (0 - 100)", min_value=0.0, max_value=100.0, step=1.0, value=def_uts)
        with col4:
            uas = st.number_input("Nilai UAS (0 - 100)", min_value=0.0, max_value=100.0, step=1.0, value=def_uas)
            
        st.markdown("<div class='mt-4'></div>", unsafe_allow_html=True)
        
        submitted = st.form_submit_button(btn_label)
        
        if submitted:
            if not nim or not nama:
                st.error("Gagal: NIM dan Nama Mahasiswa wajib diisi!")
            else:
                from crud import add_student
                nilai_akhir = hitung_nilai(absen, tugas, uts, uas)
                grade, keterangan, color = tentukan_grade(nilai_akhir)
                
                if is_edit:
                    update_student(st.session_state.edit_idx, nim, nama, absen, tugas, uts, uas, nilai_akhir, grade, keterangan)
                    st.session_state.edit_idx = None
                    st.success(f"Berhasil! Data {nama} telah diperbarui.")
                else:
                    add_student(nim, nama, absen, tugas, uts, uas, nilai_akhir, grade, keterangan)
                    st.success(f"Berhasil! Data {nama} telah disimpan.")
                    
                st.markdown(f"""
                <div class="border border-solid theme-border p-4 theme-bg mt-2 mb-2">
                    <p class="theme-text m-0 mb-2"><strong>Detail Hasil Penilaian Akhir:</strong></p>
                    <ul class="theme-text mb-0 text-sm list-disc pl-5">
                        <li><strong>Nilai Akhir :</strong> {nilai_akhir}</li>
                        <li><strong>Huruf Mutu  :</strong> {grade}</li>
                        <li><strong>Status      :</strong> {keterangan}</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
                
    if is_edit:
        if st.button("BATAL EDIT", key=f"btn_cancel_{form_key}", use_container_width=True):
            st.session_state.edit_idx = None
            st.rerun()
                
    st.markdown("</div>", unsafe_allow_html=True)

def render_crud_interface():
    # Show edit form at the top of the table if we are editing from the table view
    if "edit_idx" in st.session_state and st.session_state.edit_idx is not None:
        render_form_input(form_key="input_nilai_edit")
        st.markdown("<div class='mt-6'></div>", unsafe_allow_html=True)

    st.markdown('<div class="border border-solid theme-border p-4" style="border-width: 1px;">', unsafe_allow_html=True)
    st.markdown('<h3 class="text-xs font-bold uppercase tracking-widest theme-text mb-4 border-b border-solid theme-border pb-2">Daftar Nilai Mahasiswa</h3>', unsafe_allow_html=True)
    data = load_data()
    
    if data:
        # Custom Table Header
        c1, c2, c3, c4, c5 = st.columns([1.5, 2.5, 1, 1, 1.5])
        c1.markdown("<span class='text-xs font-bold theme-text opacity-50 tracking-wider'>NIM</span>", unsafe_allow_html=True)
        c2.markdown("<span class='text-xs font-bold theme-text opacity-50 tracking-wider'>NAMA MAHASISWA</span>", unsafe_allow_html=True)
        c3.markdown("<span class='text-xs font-bold theme-text opacity-50 tracking-wider'>NILAI</span>", unsafe_allow_html=True)
        c4.markdown("<span class='text-xs font-bold theme-text opacity-50 tracking-wider'>GRADE</span>", unsafe_allow_html=True)
        c5.markdown("<span class='text-xs font-bold theme-text opacity-50 tracking-wider'>AKSI (EDIT/HAPUS)</span>", unsafe_allow_html=True)
        st.markdown("<hr class='border-t border-solid theme-border my-2'>", unsafe_allow_html=True)
        
        for idx, row in enumerate(data):
            c1, c2, c3, c4, c5 = st.columns([1.5, 2.5, 1, 1, 1.5])
            c1.markdown(f"<span class='text-sm theme-text'>{row['NIM']}</span>", unsafe_allow_html=True)
            c2.markdown(f"<span class='text-sm theme-text'>{row['Nama']}</span>", unsafe_allow_html=True)
            c3.markdown(f"<span class='text-sm font-bold theme-text'>{row['Nilai Akhir']}</span>", unsafe_allow_html=True)
            c4.markdown(f"<span class='text-sm font-bold theme-text'>{row['Grade']}</span>", unsafe_allow_html=True)
            
            with c5:
                # Action Buttons
                b1, b2 = st.columns(2)
                if b1.button("✏️", key=f"e_{idx}", help="Edit Data ini"):
                    st.session_state.edit_idx = idx
                    st.rerun()
                if b2.button("🗑️", key=f"d_{idx}", help="Hapus Data ini"):
                    delete_student(idx)
                    st.rerun()
                    
            st.markdown("<hr class='border-t border-solid theme-border my-2 opacity-30'>", unsafe_allow_html=True)
            
        st.markdown("<p class='text-xs theme-text opacity-50 mt-4'>* Tekan ✏️ untuk mengubah data atau 🗑️ untuk menghapus data secara permanen.</p>", unsafe_allow_html=True)
    else:
        st.info("Belum ada data mahasiswa yang tersimpan di dalam sistem.")
        
    st.markdown("</div>", unsafe_allow_html=True)
