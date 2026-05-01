import streamlit as st

def apply_custom_css():
    st.markdown("""
<style>
/* Sembunyikan default footer */
footer { 
    visibility: hidden; 
}
/* Header transparan agar rapi */
header {
    background: transparent !important;
}
/* Styling tombol agar lebih modern */
.stButton > button {
    transition: all 0.3s ease;
    border-radius: 6px;
    font-weight: 600 !important;
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}
/* Menyesuaikan jarak tab */
.stTabs [data-baseweb="tab"] {
    font-weight: 600 !important;
}
</style>
""", unsafe_allow_html=True)
