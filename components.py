import streamlit as st
from icons import SVG

def render_hero():
    st.markdown(f"""
    <div class="hero">
        <div class="hero-label">Sistem Cerdas &mdash; Rule-Based Expert System</div>
        <h1 class="hero-title">Sistem Diagnosa<br>Kesehatan Awal</h1>
        <p class="hero-sub">Identifikasi kondisi kesehatan berdasarkan gejala utama menggunakan<br>kaidah IF-ELSE medis terstruktur.</p>
        <div class="hero-badge">{SVG["shield"]}&nbsp;Hanya untuk referensi awal &mdash; bukan pengganti dokter</div>
    </div>
    """, unsafe_allow_html=True)

def render_result(kondisi, tingkat, color, penanganan, saran, gejala_utama, durasi, usia_group):
    icon_svg  = SVG["check"] if color == "green" else (SVG["warn"] if color == "yellow" else SVG["alert"])
    pill_cls  = f"pill-{color}"
    ibox_cls  = f"ib-{color}"
    label_map = {"green": "Ringan", "yellow": "Perlu Perhatian", "red": "Segera Tangani"}

    st.markdown(f"""
<div class="card">
<div class="result-header">
<div class="result-icon-box {ibox_cls}">{icon_svg}</div>
<div>
<span class="result-pill {pill_cls}">{label_map[color]}</span>
<p class="result-name">{kondisi}</p>
</div>
</div>
<hr class="divider">
<div class="grid-2">
<div class="info-box">
<div class="info-label">Gejala</div>
<div class="info-value">{gejala_utama}</div>
</div>
<div class="info-box">
<div class="info-label">Durasi</div>
<div class="info-value">{durasi}</div>
</div>
<div class="info-box">
<div class="info-label">Kelompok Usia</div>
<div class="info-value">{usia_group}</div>
</div>
<div class="info-box">
<div class="info-label">Tingkat Urgensi</div>
<div class="info-value">{tingkat}</div>
</div>
</div>
<div class="info-box-full">
<div class="info-label">Penanganan Awal</div>
<div class="info-value" style="font-weight:400; color:#374151;">{penanganan}</div>
</div>
<div class="saran-wrap">
<div class="saran-label">Rekomendasi Lanjutan</div>
<div class="saran-text">{saran}</div>
</div>
</div>
""", unsafe_allow_html=True)

def render_footer():
    st.markdown("""
    <p class="disclaimer">
        Sistem ini memberikan informasi awal berdasarkan gejala yang dilaporkan secara mandiri.<br>
        Hasil analisis <strong>bukan diagnosis medis resmi</strong> dan tidak menggantikan pemeriksaan dokter.<br><br>
        &copy; Praktikum Sistem Cerdas &mdash; STMIK AMIKOM Surakarta
    </p>
    """, unsafe_allow_html=True)
