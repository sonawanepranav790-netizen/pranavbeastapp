
st.divider()
upi_id = "9067516457@axl"
upi_link = f"upi://pay?pa={upi_id}&pn=PranavBeast&am=20&cu=INR"
st.link_button("Support 20 Rs - UPI", upi_link)
st.write("UPI ID: 9067516457@axlimport streamlit as st
import time

st.set_page_config(page_title="Pranav Beast", layout="centered")
st.title("PRANAV BEAST")
st.subheader("LONKHEDI | BALIDAN")

name = st.text_input("Tujha Nav:", "Pranav")
pushups = st.slider("Kiti Pushup?", 10, 200, 68)
lvl = pushups // 20
st.metric("Beast Level", f"LEVEL {lvl}")

if st.button("START 60s Challenge"):
    ph = st.empty()
    for sec in range(60,0,-1):
        ph.metric("Time Left", f"{sec} sec")
        time.sleep(1)
    st.balloons()
    st.success("DONE!")

if st.button("CHALU KAR - BEAST MODE"):
    bar = st.progress(0)
    for i in range(pushups):
        time.sleep(0.02)
        bar.progress((i+1)/pushups)
    st.success(f"ZHALA! {pushups} DONE!")

st.divider()
upi_id = "9067516457@axl"
upi_link = f"upi://pay?pa={upi_id}&pn=PranavBeast&am=20&cu=INR"
st.link_button("Support 20 Rs - UPI", upi_link)
st.write("UPI ID: 9067516457@axl")

st.divider()
wa_link = "https://wa.me/919067516457?text=Hi Pranav Bhai Coaching Havi Ahe"
st.link_button("Coaching 299 - WhatsApp", wa_link)
