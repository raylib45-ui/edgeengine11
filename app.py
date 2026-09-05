import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration for Dark Terminal Theme
st.set_page_config(page_title="Edge Engine v5", page_icon="⚡", layout="wide")

# Custom CSS matching the dense sports terminal UI
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #c9d1d9; font-family: monospace; }
    .top-bar { background-color: #161b22; padding: 10px; border-radius: 6px; border: 1px solid #30363d; margin-bottom: 10px; font-size: 13px; }
    .metric-card { background-color: #161b22; padding: 12px; border-radius: 6px; border: 1px solid #30363d; margin-bottom: 15px; }
    .over-badge { background-color: #238636; color: white; padding: 4px 8px; border-radius: 4px; font-weight: bold; font-size: 12px; }
    .under-badge { background-color: #da3633; color: white; padding: 4px 8px; border-radius: 4px; font-weight: bold; font-size: 12px; }
    .sub-metric { font-size: 11px; color: #8b949e; background: #0d1117; padding: 6px; border-radius: 4px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# Header Bar
st.markdown("""
    <div class="top-bar" style="display: flex; justify-content: space-between; align-items: center;">
        <div><b>⚡ EDGE ENGINE v5</b> &nbsp;&nbsp;|&nbsp;&nbsp; 🟢 <b>419 batters - 30 pitchers - 15 games - 7:52:37 AM</b></div>
        <div><button style="background:#1f6feb; color:white; border:none; padding:4px 10px; border-radius:4px; font-weight:bold;">🔄 FETCH LIVE</button></div>
    </div>
""", unsafe_allow_html=True)

# Navigation & Filter Pill Bar
nav_col1, nav_col2, nav_col3, nav_col4, nav_col5, nav_col6 = st.columns([1, 1, 1, 1, 1, 3])
with nav_col1: st.button("BATTERS", use_container_width=True)
with nav_col2: st.button("PITCHERS", use_container_width=True)
with nav_col3: st.button("K PROJ", type="primary", use_container_width=True)
with nav_col4: st.button("HITTER FS", use_container_width=True)
with nav_col5: st.button("TEAM PROJ", use_container_width=True)

st.markdown("---")

# Filter Options Row
f1, f2, f3, f4 = st.columns([1, 1, 1, 3])
with f1: st.selectbox("Market Filter", ["ALL", "OVER", "UNDER"], label_visibility="collapsed")
with f2: st.selectbox("Handedness", ["ALL", "RHP", "LHP"], label_visibility="collapsed")
with f3: st.text_input("Search pitcher...", placeholder="Search pitcher...", label_visibility="collapsed")

st.markdown("---")

# Pitcher Grid Cards (Replicating Mason Adams & Braxton Ashcraft deep view)
card_col1, card_col2, card_col3 = st.columns(3)

with card_col1:
    st.markdown("""
        <div class="metric-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <h3 style="margin:0; color:white;">Mason Adams</h3>
                    <span style="font-size:11px; color:#8b949e;">Colorado · RHP · HOME vs STL · 0W-0L</span>
                </div>
                <div><span class="over-badge">OVER 3.5 Ks</span></div>
            </div>
            <hr style="border-color: #30363d; margin: 8px 0;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <span style="font-size:11px; color:#8b949e;">PROJ K</span><br>
                    <span style="font-size:24px; font-weight:bold; color:#2ea043;">4.6</span>
                    <span style="font-size:12px; background:#1f382b; color:#3fb950; padding:2px 4px; border-radius:3px;">+1.1 vs 3.5 line</span>
                </div>
                <div style="text-align: right; font-size:11px; color:#8b949e;">
                    EV 91.3 &nbsp;|&nbsp; HH% 45%<br>
                    BB% 13% &nbsp;|&nbsp; GB% 20%<br>
                    67% model &nbsp;|&nbsp; L10 100%
                </div>
            </div>
            <br>
            <div style="display:grid; grid-template-columns: repeat(4, 1fr); gap: 4px;">
                <div class="sub-metric">Putaway<br><b>-31%</b></div>
                <div class="sub-metric">Pit K%<br><b>20%</b></div>
                <div class="sub-metric">Opp K%<br><b>21.5%</b></div>
                <div class="sub-metric">Exp BF<br><b>20</b></div>
            </div>
            <hr style="border-color: #30363d; margin: 8px 0;">
            <div style="font-size:11px; color:#8b949e; margin-bottom:4px;"><b>EXACT MODEL 4.293K OVER +0.79</b></div>
            <table style="width:100%; font-size:11px; color:#c9d1d9; border-collapse: collapse;">
                <tr style="border-bottom: 1px solid #30363d; color:#8b949e;"><td>BATTER - PROJECTED</td><td>whiff</td><td>k%</td></tr>
                <tr><td>1. Herrera (RHP)</td><td>18%</td><td>19.3%</td></tr>
                <tr><td>2. Burleson (LHB)</td><td>17.1%</td><td>16.9%</td></tr>
                <tr><td>3. Walker (RHB)</td><td>24.9%</td><td>26.3%</td></tr>
                <tr><td>4. Church (LHB)</td><td>17.8%</td><td>18.3%</td></tr>
            </table>
            <hr style="border-color: #30363d; margin: 8px 0;">
            <div style="background:#0d1117; padding:8px; border-radius:4px; font-size:11px; color:#8b949e;">
                <b>MODEL LEANS OVER +1.1 vs 3.5</b><br>
                Rate and workload both contribute: +0.3K from a 24% K rate, -0.3K from 20 batters faced. He needs 4+. The model gives that 67%, which leaves 33% the other way...
            </div>
        </div>
    """, unsafe_allow_html=True)

with card_col2:
    st.markdown("""
        <div class="metric-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <h3 style="margin:0; color:white;">Braxton Ashcraft</h3>
                    <span style="font-size:11px; color:#8b949e;">Pittsburgh · RHP · HOME vs LAA · 14W-5L</span>
                </div>
                <div><span class="over-badge">OVER 5.5 Ks</span></div>
            </div>
            <hr style="border-color: #30363d; margin: 8px 0;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <span style="font-size:11px; color:#8b949e;">PROJ K</span><br>
                    <span style="font-size:24px; font-weight:bold; color:#2ea043;">6.2</span>
                    <span style="font-size:12px; background:#1f382b; color:#3fb950; padding:2px 4px; border-radius:3px;">+0.7 vs 5.5 line</span>
                </div>
                <div style="text-align: right; font-size:11px; color:#8b949e;">
                    EV 89.5 &nbsp;|&nbsp; HH% 42%<br>
                    BB% 6% &nbsp;|&nbsp; GB% 46%<br>
                    59% model &nbsp;|&nbsp; L10 30%
                </div>
            </div>
            <br>
            <div style="display:grid; grid-template-columns: repeat(4, 1fr); gap: 4px;">
                <div class="sub-metric">Putaway<br><b>-33%</b></div>
                <div class="sub-metric">Pit K%<br><b>21%</b></div>
                <div class="sub-metric">Opp K%<br><b>25.6%</b></div>
                <div class="sub-metric">Exp BF<br><b>23</b></div>
            </div>
            <hr style="border-color: #30363d; margin: 8px 0;">
            <div style="font-size:11px; color:#8b949e; margin-bottom:4px;"><b>EXACT MODEL 5.832K no play</b></div>
            <table style="width:100%; font-size:11px; color:#c9d1d9; border-collapse: collapse;">
                <tr style="border-bottom: 1px solid #30363d; color:#8b949e;"><td>BATTER - PROJECTED</td><td>whiff</td><td>k%</td></tr>
                <tr><td>1. Neto (RHB)</td><td>31%</td><td>32.0%</td></tr>
                <tr><td>2. Trout (RHB)</td><td>25.7%</td><td>26.6%</td></tr>
                <tr><td>3. Grissom (RHB)</td><td>17.7%</td><td>19.2%</td></tr>
                <tr><td>4. Peraza (RHB)</td><td>30%</td><td>30.0%</td></tr>
            </table>
            <hr style="border-color: #30363d; margin: 8px 0;">
            <div style="background:#0d1117; padding:8px; border-radius:4px; font-size:11px; color:#8b949e;">
                <b>MODEL LEANS OVER +0.7K vs 5.5</b><br>
                Driven by the arm, not the workload: his 25% K rate against this lineup is worth +0.6K over an average start...
            </div>
        </div>
    """, unsafe_allow_html=True)

with card_col3:
    st.markdown("""
        <div class="metric-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <h3 style="margin:0; color:white;">Andrew Abbott</h3>
                    <span style="font-size:11px; color:#8b949e;">Cincinnati · LHP · HOME vs MIL · 6W-10L</span>
                </div>
                <div><span class="over-badge">OVER 3.5 Ks</span></div>
            </div>
            <hr style="border-color: #30363d; margin: 8px 0;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <span style="font-size:11px; color:#8b949e;">PROJ K</span><br>
                    <span style="font-size:24px; font-weight:bold; color:#2ea043;">4.5</span>
                    <span style="font-size:12px; background:#1f382b; color:#3fb950; padding:2px 4px; border-radius:3px;">+1 vs 3.5 line</span>
                </div>
                <div style="text-align: right; font-size:11px; color:#8b949e;">
                    EV 88.4 &nbsp;|&nbsp; HH% 38%<br>
                    BB% 8% &nbsp;|&nbsp; GB% 37%<br>
                    67% model &nbsp;|&nbsp; L10 60%
                </div>
            </div>
            <br>
            <div style="display:grid; grid-template-columns: repeat(4, 1fr); gap: 4px;">
                <div class="sub-metric">Putaway<br><b>-30%</b></div>
                <div class="sub-metric">Pit K%<br><b>21%</b></div>
                <div class="sub-metric">Opp K%<br><b>21.0%</b></div>
                <div class="sub-metric">Exp BF<br><b>22</b></div>
            </div>
            <hr style="border-color: #30363d; margin: 8px 0;">
            <div style="font-size:11px; color:#8b949e; margin-bottom:4px;"><b>EXACT MODEL 3.933K no play</b></div>
            <table style="width:100%; font-size:11px; color:#c9d1d9; border-collapse: collapse;">
                <tr style="border-bottom: 1px solid #30363d; color:#8b949e;"><td>BATTER - PROJECTED</td><td>whiff</td><td>k%</td></tr>
                <tr><td>1. Turang (LHB)</td><td>25.3%</td><td>25.6%</td></tr>
                <tr><td>2. Contreras (RHB)</td><td>14.1%</td><td>15.6%</td></tr>
                <tr><td>3. Bauers (LHB)</td><td>25.0%</td><td>22.7%</td></tr>
                <tr><td>4. Chourio (RHB)</td><td>23.9%</td><td>23.1%</td></tr>
            </table>
            <hr style="border-color: #30363d; margin: 8px 0;">
            <div style="background:#0d1117; padding:8px; border-radius:4px; font-size:11px; color:#8b949e;">
                <b>MODEL LEANS OVER +1.0K vs 3.5</b><br>
                Driven by the arm, not the workload: his 18% K rate against this lineup is worth +1.0K over an average start...
            </div>
        </div>
    """, unsafe_allow_html=True)
