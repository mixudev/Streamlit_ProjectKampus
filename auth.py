import streamlit as st

def login():
    # Cek parameter URL agar login bertahan walaupun halaman di-refresh (F5)
    if "logged_in" in st.query_params and st.query_params["logged_in"] == "true":
        st.session_state.logged_in = True
    elif "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.write("")
        st.write("")
        st.write("")
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.markdown("""
            <div style="text-align: center; margin-bottom: 2rem;">
                <h1 style="font-size: 1.5rem; font-weight: bold; letter-spacing: -0.025em; text-transform: uppercase; margin-bottom: 0.25rem;">EduGrade</h1>
                <p style="font-size: 0.75rem; letter-spacing: 0.1em; opacity: 0.5; text-transform: uppercase;">Sistem Penilaian Mahasiswa</p>
            </div>
            """, unsafe_allow_html=True)
            
            with st.container(border=True):
                username = st.text_input("Nama Pengguna (Username)")
                password = st.text_input("Kata Sandi (Password)", type="password")
                st.write("")
                
                if st.button("MASUK SISTEM", use_container_width=True):
                    if username == "admin" and password == "admin":
                        st.session_state.logged_in = True
                        st.query_params["logged_in"] = "true" # Simpan ke URL
                        st.rerun()
                    else:
                        st.error("Gagal masuk: Nama Pengguna atau Kata Sandi salah.")
                        
            st.info("**Akun Demo:**  \nUsername: `admin`  \nPassword: `admin`")
                
        return False
    return True

def logout():
    st.session_state.logged_in = False
    if "logged_in" in st.query_params:
        del st.query_params["logged_in"]
    st.rerun()
