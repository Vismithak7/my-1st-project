import streamlit as st 
st.set_page_config(page_title="love check!!",layout="centered")
                   
st.title("do you love me?")
st.write("honest answer required")

x = st.text_input("naanu do you love me? (yes/no)").lower()

if st.button("submit"):
    if x == 'yes':
        for _ in range(100):
            st.success("I luv uhh tooo babe <3!")
    elif x:
        for _ in range(100):
            st.error("I am sorry :( excuse me honey")
    else:
        ("please enter something to continue^w^")
        