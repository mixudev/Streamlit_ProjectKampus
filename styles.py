import streamlit as st

def apply_custom_css():
    st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
<style>
/* Remove all rounded corners to make it sharp and small */
* {
    border-radius: 0px !important;
}
/* Make inputs small, sharp, and elegant */
.stTextInput > div > div > input, 
.stNumberInput > div > div > input {
    border: 1px solid var(--text-color) !important;
    padding: 0.25rem 0.5rem !important;
    font-size: 0.85rem !important;
    min-height: 32px !important;
    background-color: transparent !important;
    color: var(--text-color) !important;
    opacity: 0.8;
}
.stTextInput > div > div > input:focus, 
.stNumberInput > div > div > input:focus {
    border: 1px solid var(--primary-color) !important;
    box-shadow: none !important;
    opacity: 1;
}
/* Sharp, minimal Buttons */
.stButton > button {
    border: 1px solid var(--text-color) !important;
    background-color: transparent !important;
    color: var(--text-color) !important;
    padding: 0.25rem 1rem !important;
    font-size: 0.75rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.05em !important;
    text-transform: uppercase;
    min-height: 32px !important;
    transition: all 0.2s;
}
.stButton > button:hover {
    background-color: var(--text-color) !important;
    color: var(--background-color) !important;
    border-color: var(--text-color) !important;
}
/* Tabs minimal styling */
.stTabs [data-baseweb="tab"] {
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;
    font-size: 0.75rem !important;
    font-weight: 600 !important;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}
/* Hide default footer and Streamlit Watermark, but KEEP header for Theme Menu and Sidebar Toggle */
#MainMenu, footer { 
    visibility: hidden; 
}
header {
    background: transparent !important;
}
/* Utility classes mimicking tailwind where needed to support native Streamlit light/dark theming */
.theme-border { border-color: var(--text-color); opacity: 0.3; }
.theme-text { color: var(--text-color); }
.theme-bg { background-color: var(--background-color); }
</style>
""", unsafe_allow_html=True)
