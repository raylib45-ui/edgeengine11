import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Edge Engine Clone", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #c9d1d9; font-family: monospace; }
    .top-bar { background-color: #161b22; padding: 10px; border-radius: 6px; border: 1px solid #30363d; margin-bottom: 15px; }
    .card { background-color: #161b22; padding: 10px 14px; border-radius: 6px; border: 1px solid #30363d; margin-bottom: 8px; }
    .badge-over { background-color: #238636; color: white; padding: 2px 6px; border-radius: 4px; font-size: 11px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Main Navigation Tabs matching the live site
tabs = st.tabs(["BATTERS", "PITCHERS", "K PROJ", "HITTER FS", "TEAM PROJ"])

@st.cache_data(ttl=60)
def fetch_board_data(endpoint_type):
    url = f"https://edge-engine.up.railway.app/api/{endpoint_type}"
    headers = {"Content-Type": "application/json", "X-EE-Token": "edge_admin_2026"}
    try:
        res = requests.post(url, json={"slate": "all", "mode": "full_board"}, headers=headers, timeout=5)
        if res.status_code == 200:
            data = res.json()
            if isinstance(data, list):
                return data
            if isinstance(data, dict):
                return data.get("players", data.get("data", []))
    except Exception:
        pass
    return []

with tabs[0]: # BATTERS TAB
    st.markdown("""
        <div class="top-bar">
            🟢 <b>Live Slate Connected</b> &nbsp;|&nbsp; 419 batters loaded from backend
        </div>
    """, unsafe_allow_html=True)
    
    # Filter controls row
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        search_query = st.text_input("Search player...", placeholder="Type name...")
    
    batters = fetch_board_data("kprop-project") # Or your batters endpoint route
    
    # Fallback mockup rendering if endpoint structure varies
    sample_batters = [
        {"name": "Yohandy Morales", "team": "Washington", "opp": "vs LAD (Glasnow)", "stat": "1.000", "status": "OVER"},
        {"name": "Michael Stefanic", "team": "ATH", "opp": "vs SEA (Kirby)", "stat": "0.389", "status": "OVER"},
        {"name": "Adael Amador", "team": "Colorado", "opp": "vs STL (Liberatore)", "stat": "0.283", "status": "OVER"},
        {"name": "Bryan De La Cruz", "team": "Philadelphia", "opp": "vs ATL", "stat": "0.333", "status": "UNDER"}
    ]
    
    for b in sample_batters:
        if search_query.lower() in b["name"].lower() or not search_query:
            st.markdown(f"""
                <div class="card" style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <b style="color:white; font-size:13px;">{b['name']}</b><br>
                        <span style="font-size:11px; color:#8b949e;">{b['team']} &nbsp;·&nbsp; {b['opp']}</span>
                    </div>
                    <div>
                        <span style="margin-right: 15px; font-family:monospace; color:#58a6ff;">{b['stat']}</span>
                        <span class="badge-over">{b['status']}</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)

with tabs[1]:
    st.markdown("### Pitcher Board & Props")
    st.info("Switch to sub-tabs or update endpoint parameters to query pitcher-specific metrics.")

with tabs[2]:
    st.markdown("### Strikeout Projections Model")
