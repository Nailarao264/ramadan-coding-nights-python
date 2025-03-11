import streamlit as st

import random
import string

def generate_password(Length,use_digits,use_special):
    characters=string.ascii_letters

    if use_digits:
        characters+=string.digits # adds number 0,9

    if use_special:
        characters+=string.punctuation #(!,@,#)    

    return ''.join(random.choice(characters) for _ in range(length))
st.title("My Password Generator")

length=st.slider("select password length", min_value=6,max_value=32,value=12)
use_digits=st.checkbox("Include Digits")
use_special=st.checkbox("Include Special Character")

if st.button("Generate Password"):
    password=generate_password(length,use_digits,use_special)
    st.write(f"Generate Password :`{password}`")
    st.write("---------------------------------------")
