import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Initialize with letters

    if use_digits:
        characters += string.digits  # Add numbers

    if use_special:
        characters += string.punctuation  # Add special characters

    if not characters:
        return "Error: No characters selected"

    return ''.join(random.choice(characters) for _ in range(length))

st.title("My Password Generator")

length = st.slider("Select password length", min_value=6, max_value=32, value=12)
use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"**Generated Password:** `{password}`")
    st.write("---")

