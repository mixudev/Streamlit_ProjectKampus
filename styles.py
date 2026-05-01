import streamlit as st

def apply_custom_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,300&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }

    .stApp { background-color: #F7F6F2; }
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { padding-top: 2rem; padding-bottom: 3rem; max-width: 740px; }

    /* ── Hero ── */
    .hero {
        background: #1A1A2E;
        border-radius: 20px;
        padding: 2.6rem 2.8rem;
        margin-bottom: 1.8rem;
        position: relative;
        overflow: hidden;
    }
    .hero::after {
        content: '';
        position: absolute;
        top: -80px; right: -80px;
        width: 260px; height: 260px;
        border-radius: 50%;
        background: rgba(99,179,237,0.06);
        pointer-events: none;
    }
    .hero-label {
        font-size: 0.68rem;
        font-weight: 600;
        letter-spacing: 0.18em;
        color: #63B3ED;
        text-transform: uppercase;
        margin-bottom: 0.55rem;
    }
    .hero-title {
        font-family: 'DM Serif Display', serif;
        font-size: 2.15rem;
        color: #FFFFFF;
        margin: 0 0 0.45rem 0;
        line-height: 1.15;
    }
    .hero-sub {
        font-size: 0.87rem;
        color: #A0AEC0;
        margin: 0;
        font-weight: 300;
        line-height: 1.6;
    }
    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        margin-top: 1.3rem;
        background: rgba(99,179,237,0.1);
        border: 1px solid rgba(99,179,237,0.22);
        color: #63B3ED;
        font-size: 0.7rem;
        font-weight: 500;
        letter-spacing: 0.04em;
        padding: 0.32rem 0.9rem;
        border-radius: 100px;
    }

    /* ── Card ── */
    .card {
        background: #FFFFFF;
        border-radius: 16px;
        padding: 1.8rem 2rem;
        margin-bottom: 1.2rem;
        border: 1px solid #E8E6E0;
        box-shadow: 0 2px 12px rgba(0,0,0,0.04);
    }
    .card-title {
        font-size: 0.68rem;
        font-weight: 600;
        letter-spacing: 0.14em;
        color: #9CA3AF;
        text-transform: uppercase;
        margin-bottom: 1.4rem;
        display: flex;
        align-items: center;
        gap: 0.45rem;
    }

    /* ── Selectbox ── */
    div[data-baseweb="select"] > div {
        background-color: #F7F6F2 !important;
        border: 1.5px solid #E2DED6 !important;
        border-radius: 10px !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.9rem !important;
        color: #1A1A2E !important;
    }
    div[data-baseweb="select"] > div:focus-within {
        border-color: #1A1A2E !important;
        box-shadow: 0 0 0 3px rgba(26,26,46,0.07) !important;
    }
    label {
        font-weight: 500 !important;
        font-size: 0.86rem !important;
        color: #374151 !important;
    }

    /* ── Button ── */
    .stButton > button {
        background: #1A1A2E !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.72rem 2rem !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.88rem !important;
        font-weight: 500 !important;
        letter-spacing: 0.02em !important;
        width: 100% !important;
        transition: background 0.2s, transform 0.15s, box-shadow 0.2s !important;
    }
    .stButton > button:hover {
        background: #2D2D4E !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 6px 20px rgba(26,26,46,0.22) !important;
    }
    .stButton > button:active { transform: translateY(0) !important; }

    /* ── Result ── */
    .result-header {
        display: flex;
        align-items: flex-start;
        gap: 1rem;
        margin-bottom: 1.4rem;
    }
    .result-icon-box {
        width: 54px; height: 54px;
        border-radius: 14px;
        display: flex; align-items: center; justify-content: center;
        flex-shrink: 0;
    }
    .ib-green  { background: #ECFDF5; }
    .ib-yellow { background: #FFFBEB; }
    .ib-red    { background: #FEF2F2; }

    .result-pill {
        display: inline-block;
        font-size: 0.65rem;
        font-weight: 600;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        padding: 0.22rem 0.7rem;
        border-radius: 100px;
        margin-bottom: 0.3rem;
    }
    .pill-green  { background: #D1FAE5; color: #065F46; }
    .pill-yellow { background: #FEF3C7; color: #92400E; }
    .pill-red    { background: #FEE2E2; color: #991B1B; }

    .result-name {
        font-family: 'DM Serif Display', serif;
        font-size: 1.45rem;
        color: #1A1A2E;
        line-height: 1.2;
        margin: 0;
    }

    .divider { border: none; border-top: 1px solid #EEECe8; margin: 1.2rem 0; }

    .grid-2 {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 0.85rem;
        margin-bottom: 0.85rem;
    }
    .info-box {
        background: #F7F6F2;
        border-radius: 11px;
        padding: 0.9rem 1rem;
    }
    .info-label {
        font-size: 0.65rem;
        font-weight: 600;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: #9CA3AF;
        margin-bottom: 0.3rem;
    }
    .info-value {
        font-size: 0.875rem;
        font-weight: 500;
        color: #1A1A2E;
        line-height: 1.5;
    }
    .info-box-full {
        background: #F7F6F2;
        border-radius: 11px;
        padding: 0.9rem 1rem;
        margin-bottom: 0.85rem;
    }

    .saran-wrap {
        border-left: 3px solid #1A1A2E;
        border-radius: 0 11px 11px 0;
        background: #F7F6F2;
        padding: 1rem 1.2rem;
    }
    .saran-label {
        font-size: 0.65rem;
        font-weight: 600;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: #6B7280;
        margin-bottom: 0.45rem;
    }
    .saran-text {
        font-size: 0.875rem;
        color: #374151;
        line-height: 1.7;
    }

    /* ── Disclaimer ── */
    .disclaimer {
        text-align: center;
        font-size: 0.74rem;
        color: #B0A99F;
        margin-top: 2.5rem;
        line-height: 1.7;
    }
    </style>
    """, unsafe_allow_html=True)
