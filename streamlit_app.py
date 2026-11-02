import streamlit as st
import time
st.set_page_config(page_title="Pranav Beast", page_icon="🔥", layout="centered")
st.markdown("<h1 style='text-align: center; color: #FF0000;'>🔥 PRANAV BEAST 🔥</h1><h3 style='text-align: center;'>LONKHEDI | BALIDAN</h3>", unsafe_allow_html=True)
name = st.text_input("Tujha Nav:", "Pranav")
pushups = st.slider("Kiti Pushup?", 10, 200, 68)
st.subheader("⏱️ BEAST TIMER")
col1, col2 = st.columns(2)
with col1:
    if st.button("▶️ START 60s", use_container_width=True):
        ph = st.empty()
        for sec in range(60,0,-1):
            ph.metric("Time Left", f"{sec} sec")
            time.sleep(1)
        st.balloons()
with col2:
    lvl = pushups // 20
    st.metric("🔥 Beast Level", f"LEVEL {lvl}")
if st.button("💪 CHALU KAR", use_container_width=True):
    bar = st.progress(0)
    for i in range(pushups):
        time.sleep(0.02)
        bar.progress((i+1)/pushups)
    st.balloons()
    st.success(f"ZHALA! {pushups} DONE! 🔥")
st.divider()
st.subheader("💰 Support Kara")
upi_id = "9067516457@axl"
upi_link = f"upi://pay?pa={upi_id}&pn=Pranav&am=20&cu=INR&tn=Support"
st.link_button("☕
