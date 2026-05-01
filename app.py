import streamlit as st
from styles import apply_custom_css
from icons import SVG
from knowledge_base import diagnosa
from components import render_hero, render_result, render_footer

st.set_page_config(
    page_title="Sistem Diagnosa Awal",
    page_icon="⚕",
    layout="centered"
)

# ── CSS GLOBAL ────────────────────────────────────────────────────────────────
apply_custom_css()

# ── HERO ──────────────────────────────────────────────────────────────────────
render_hero()

# ── INPUT ─────────────────────────────────────────────────────────────────────
st.markdown(f'<div class="card"><div class="card-title">{SVG["pulse"]} Data Gejala Pasien</div>', unsafe_allow_html=True)

gejala_utama = st.selectbox(
    "Gejala Utama yang Dirasakan",
    ["Demam", "Batuk", "Nyeri Kepala", "Nyeri Perut", "Sesak Napas"],
)
col1, col2 = st.columns(2)
with col1:
    durasi = st.selectbox("Sudah Berapa Lama?", ["< 3 hari", "3–7 hari", "> 7 hari"])
with col2:
    usia_group = st.selectbox("Kelompok Usia", ["Anak (0–12 th)", "Remaja / Dewasa (13–59 th)", "Lansia (> 60 th)"])

st.markdown("</div><br>", unsafe_allow_html=True)

analisis = st.button("Analisis Gejala")

# ── HASIL ─────────────────────────────────────────────────────────────────────
if analisis:
    kondisi, tingkat, color, penanganan, saran = diagnosa(gejala_utama, durasi, usia_group)
    render_result(kondisi, tingkat, color, penanganan, saran, gejala_utama, durasi, usia_group)

# ── FOOTER ────────────────────────────────────────────────────────────────────
render_footer()