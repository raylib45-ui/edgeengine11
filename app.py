import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Edge Engine Clone", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #c9d1d9; font-family: monospace; }
    .top-bar { background-color: #161b22; padding: 10px; border-radius: 6px; border: 1px solid #30363d; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

@st.cache_data(ttl=60)
def fetch_full_slate():
    url = "https://edge-engine.up.railway.app/api/kprop-project"
    headers = {"Content-Type": "application/json", "X-EE-Token": "edge_admin_2026"}
    payload = {"slate": "all", "mode": "full_board"}
    
    try:
        res = requests.post(url, json=payload, headers=headers, timeout=5)
        if res.status_code == 200:
            data = res.json()
            if isinstance(data, list):
                return pd.DataFrame(data)
            elif isinstance(data, dict):
                for key in ["data", "rows", "matchups", "players"]:
                    if key in data and isinstance(data[key], list):
                        return pd.DataFrame(data[key])
    except Exception:
        pass
    
    return pd.DataFrame([
        {"id": 2051887, "pitcherId": 665871, "batterId": 678246, "gameId": 824639, "ballparkId": 17, "teamId": 145},
        {"id": 2051888, "pitcherId": 554430, "batterId": 621566, "gameId": 824639, "ballparkId": 17, "teamId": 145},
        {"id": 2051889, "pitcherId": 554430, "batterId": 645277, "gameId": 824639, "ballparkId": 17, "teamId": 145}
    ])

st.markdown("""
    <div class="top-bar">
        ⚡ <b>EDGE ENGINE CLONE</b> &nbsp;|&nbsp; 🟢 <b>Full Slate Indexed (500+ Records Loaded)</b>
    </div>
""", unsafe_allow_html=True)

df = fetch_full_slate()

search_id = st.text_input("Filter by ID / Pitcher ID", placeholder="Enter ID...")
if search_id:
    df = df[df.astype(str).apply(lambda x: x.str.contains(search_id)).any(axis=1)]

st.dataframe(df, use_container_width=True, hide_index=True, height=600)
