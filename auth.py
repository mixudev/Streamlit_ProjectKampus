import streamlit as st

def login():
    # Cek parameter URL agar login bertahan walaupun halaman di-refresh (F5)
    if "logged_in" in st.query_params and st.query_params["logged_in"] == "true":
        st.session_state.logged_in = True
    elif "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.markdown('<div class="mt-20"></div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.markdown("""
            <div class="text-center mb-6">
                <h1 class="text-2xl font-bold tracking-tight theme-text uppercase mb-1">EduGrade</h1>
                <p class="text-xs tracking-widest theme-text opacity-50 uppercase">Sistem Penilaian Mahasiswa</p>
            </div>
            """, unsafe_allow_html=True)
            
            with st.container():
                st.markdown('<div class="border border-solid theme-border p-6 theme-bg" style="border-width: 1px;">', unsafe_allow_html=True)
                username = st.text_input("Nama Pengguna (Username)")
                password = st.text_input("Kata Sandi (Password)", type="password")
                st.markdown("<div class='mt-6'></div>", unsafe_allow_html=True)
                
                if st.button("MASUK SISTEM", use_container_width=True):
                    if username == "admin" and password == "admin":
                        st.session_state.logged_in = True
                        st.query_params["logged_in"] = "true" # Simpan ke URL
                        st.rerun()
                    else:
                        st.error("Gagal masuk: Nama Pengguna atau Kata Sandi salah.")
                st.markdown('</div>', unsafe_allow_html=True)
                
        return False
    return True

def logout():
    st.session_state.logged_in = False
    if "logged_in" in st.query_params:
        del st.query_params["logged_in"]
    st.rerun()
