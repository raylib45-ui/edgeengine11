import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration for Dark Theme
st.set_page_config(page_title="Edge Engine", page_icon="⚡", layout="wide")

# Custom CSS styling to mimic the dark sports terminal UI
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .metric-card { background-color: #161b22; padding: 15px; border-radius: 8px; border: 1px solid #30363d; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# Top Navigation Bar Simulation
st.markdown("### ⚡ EDGE ENGINE v5")
nav_cols = st.columns([1, 1, 1, 1, 1, 1, 1, 1])
with nav_cols[0]: st.button("BATTERS")
with nav_cols[1]: st.button("PITCHERS")
with nav_cols[2]: st.button("K PROJ", type="primary")
with nav_cols[3]: st.button("HITTER FS")
with nav_cols[4]: st.button("TEAM PROJ")
with nav_cols[5]: st.button("NBA")
with nav_cols[6]: st.button("WNBA")
with nav_cols[7]: st.button("NFL")

st.divider()

# Filter Controls Row
filter_col1, filter_col2, filter_col3, filter_col4 = st.columns([1, 1, 1, 3])
with filter_col1: st.selectbox("Market", ["ALL", "OVER", "UNDER"])
with filter_col2: st.selectbox("Handedness", ["ALL", "RHP", "LHP"])
with filter_col3: st.text_input("Search pitcher...", placeholder="T. Skubal")

st.markdown("---")

# Pitcher Card Row
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="metric-card">
            <h4>T. Skubal <span style="font-size:12px; color:gray;">vs CLE</span></h4>
            <h2 style="color: #2ea043;">PROJ K: 7.8 <span style="font-size:14px; color:#58a6ff;">+1.3 vs line</span></h2>
            <p><b>Projected IP:</b> 6.1</p>
            <hr style="border-color: #30363d;">
            <p style="font-size:12px;">Last 7 starts trend: [🟩 🟩 🟨 🟩 🟩 🟩 🟩]</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="metric-card">
            <h4>Mason Adams <span style="font-size:12px; color:gray;">vs STL</span></h4>
            <h2 style="color: #2ea043;">PROJ K: 4.6 <span style="font-size:14px; color:#58a6ff;">+1.1 vs line</span></h2>
            <p><b>Projected IP:</b> 5.2</p>
            <hr style="border-color: #30363d;">
            <p style="font-size:12px;">Last 7 starts trend: [🟥 🟨 🟩 🟥 🟩 🟩 🟨]</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="metric-card">
            <h4>Braxton Ashcraft <span style="font-size:12px; color:gray;">vs LAA</span></h4>
            <h2 style="color: #da3633;">PROJ K: 6.2 <span style="font-size:14px; color:#f85149;">+0.7 vs line</span></h2>
            <p><b>Projected IP:</b> 5.5</p>
            <hr style="border-color: #30363d;">
            <p style="font-size:12px;">Last 7 starts trend: [🟩 🟥 🟩 🟩 🟥 🟩 🟩]</p>
        </div>
    """, unsafe_app_html=True)
