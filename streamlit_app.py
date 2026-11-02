import streamlit as st, time
st.set_page_config(page_title="Pranav Beast", page_icon="💪")
st.title("🔥 PRANAV BEAST 🔥")
st.write("50 Pushup Challenge")
name=st.text_input("Nav:", "Pranav")
n=st.slider("Kiti?",10,100,50)
if st.button("CHALU KAR"):
    b=st.progress(0)
    t=st.empty()
    for i in range(1,n+1):
        b.progress(int(i/n*100))
        t.write(f"{i}/{n} Done!")
        time.sleep(0.1)
    st.balloons()
    st.success(f"{name} DONE!")
