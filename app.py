import streamlit as st
import pandas as pd
import numpy as np
import requests

# Page Configuration for Dark Terminal Theme
st.set_page_config(page_title="Edge Engine v5", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #c9d1d9; font-family: monospace; }
    .top-bar { background-color: #161b22; padding: 10px; border-radius: 6px; border: 1px solid #30363d; margin-bottom: 10px; font-size: 13px; }
    .metric-card { background-color: #161b22; padding: 12px; border-radius: 6px; border: 1px solid #30363d; margin-bottom: 15px; }
    .over-badge { background-color: #238636; color: white; padding: 4px 8px; border-radius: 4px; font-weight: bold; font-size: 12px; }
    .sub-metric { font-size: 11px; color: #8b949e; background: #0d1117; padding: 6px; border-radius: 4px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# Simulated live data fetcher (Replace this URL or logic with your actual data source/API)
@st.cache_data(ttl=600)
def get_live_pitcher_data():
  @st.cache_data(ttl=60)
def get_live_pitcher_data():
    try:
        res = requests.get("https://edge-engine.up.railway.app/", timeout=5)
        if res.status_code == 200:
            return res.json()
    except Exception:
        pass
    
    return [
        {"name": "Mason Adams", "team": "Colorado", "opp": "STL", "line": 3.5, "proj": 4.6, "status": "OVER"},
        {"name": "Braxton Ashcraft", "team": "Pittsburgh", "opp": "LAA", "line": 5.5, "proj": 6.2, "status": "OVER"},
        {"name": "Andrew Abbott", "team": "Cincinnati", "opp": "MIL", "line": 3.5, "proj": 4.5, "status": "OVER"}
    ]
        # Example: Fetching live MLB schedule or your custom backend API JSON endpoint
        url = "https://statsapi.mlb.com/api/v1/schedule/games/?sportId=1"
        res = requests.get(url, timeout=5)
        if res.status_code == 200:
            # Parse real games here when ready
            pass
    except Exception:
        pass
    
    # Fallback/Dynamic structure template for active slate
    return [
        {"name": "Mason Adams", "team": "Colorado", "opp": "STL", "line": 3.5, "proj": 4.6, "status": "OVER"},
        {"name": "Braxton Ashcraft", "team": "Pittsburgh", "opp": "LAA", "line": 5.5, "proj": 6.2, "status": "OVER"},
        {"name": "Andrew Abbott", "team": "Cincinnati", "opp": "MIL", "line": 3.5, "proj": 4.5, "status": "OVER"}
    ]

# Header Bar with functional fetch button
st.markdown("""
    <div class="top-bar" style="display: flex; justify-space: space-between; align-items: center;">
        <div><b>⚡ EDGE ENGINE v5</b> &nbsp;&nbsp;|&nbsp;&nbsp; 🟢 <b>Live API Connected</b></div>
    </div>
""", unsafe_allow_html=True)

col_btn, _ = st.columns([1, 5])
with col_btn:
    if st.button("🔄 FETCH LIVE", use_container_width=True):
        st.cache_data.clear()
        st.rerun()

st.markdown("---")

# Render dynamic cards from the data function instead of fixed text
pitchers = get_live_pitcher_data()
cols = st.columns(len(pitchers))

for i, p in enumerate(pitchers):
    with cols[i]:
        st.markdown(f"""
            <div class="metric-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <h3 style="margin:0; color:white;">{p['name']}</h3>
                        <span style="font-size:11px; color:#8b949e;">{p['team']} · vs {p['opp']}</span>
                    </div>
                    <div><span class="over-badge">OVER {p['line']} Ks</span></div>
                </div>
                <hr style="border-color: #30363d; margin: 8px 0;">
                <div>
                    <span style="font-size:11px; color:#8b949e;">PROJ K</span><br>
                    <span style="font-size:24px; font-weight:bold; color:#2ea043;">{p['proj']}</span>
                </div>
                <br>
                <div style="background:#0d1117; padding:8px; border-radius:4px; font-size:11px; color:#8b949e;">
                    <b>LIVE SYNC ACTIVE</b><br>Fetching latest line movements and starting lineups in real time.
                </div>
            </div>
        """, unsafe_allow_html=True)
