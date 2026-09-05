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
    headers = {
        "Content-Type": "application/json",
        "X-EE-Token": "edge_admin_2026"
    }
    payload = {"slate": "all", "mode": "full_board"}
    
    try:
        res = requests.post(url, json=payload, headers=headers, timeout=5)
        st.write(f"Status Code: {res.status_code}")
        
        if res.status_code == 200:
            data = res.json()
            st.write(f"Data type received: {type(data)}")
            
            if isinstance(data, list) and len(data) > 0:
                return pd.DataFrame(data)
            elif isinstance(data, dict):
                st.write(f"Dict keys: {list(data.keys())}")
                for k, v in data.items():
                    if isinstance(v, list) and len(v) > 0:
                        return pd.DataFrame(v)
        else:
            st.error(f"Server response text: {res.text}")
    except Exception as e:
        st.error(f"Connection Exception: {e}")
        
    return pd.DataFrame()

st.markdown("""
    <div class="top-bar">
        ⚡ <b>EDGE ENGINE CLONE</b> &nbsp;|&nbsp; 🟢 <b>Live API Connected</b>
    </div>
""", unsafe_allow_html=True)

df = fetch_full_slate()

if not df.empty:
    search_id = st.text_input("Filter Records", placeholder="Search ID, Pitcher ID, Batter ID...")
    if search_id:
        df = df[df.astype(str).apply(lambda x: x.str.contains(search_id, case=False)).any(axis=1)]
    
    st.markdown(f"**Loaded Records: {len(df)}**")
    st.dataframe(df, width="stretch", hide_index=True, height=600)
else:
    st.warning("Awaiting live array packet from Railway endpoint...")
