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
        st.write(f"Status Code: {res.status_code}") # Debug status
        
        if res.status_code == 200:
            data = res.json()
            st.write(f"Data type received: {type(data)}") # Debug type
            
            if isinstance(data, list) and len(data) > 0:
                return pd.DataFrame(data)
            elif isinstance(data, dict):
                st.write(f"Dict keys: {list(data.keys())}") # Debug keys
                for k, v in data.items():
                    if isinstance(v, list) and len(v) > 0:
                        return pd.DataFrame(v)
        else:
            st.error(f"Server response text: {res.text}")
    except Exception as e:
        st.error(f"Connection Exception: {e}")
        
    return pd.DataFrame()
