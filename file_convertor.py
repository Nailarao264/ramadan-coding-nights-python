import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title= "file convertor",layout="wide") 
st.title("file convertor & cleaner") 
st.write("upload csv or excel files,")
# File upload section
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        # Detect file type and read data
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.write("### Preview of Uploaded File:")
        st.dataframe(df.head())

        # Data Cleaning Options
        st.write("### Data Cleaning Options:")
        remove_duplicates = st.checkbox("Remove Duplicates")
        fill_missing = st.checkbox("Fill Missing Values")

        if remove_duplicates:
            df = df.drop_duplicates()
            st.success("Duplicates removed!")

        if fill_missing:
            fill_value = st.text_input("Enter value to replace missing data:", "N/A")
            df = df.fillna(fill_value)
            st.success(f"Missing values replaced with '{fill_value}'")

        # File Conversion
        st.write("### Convert & Download")
        file_format = st.radio("Select file format:", ["CSV", "Excel"])

        def convert_file(df, format):
            output = BytesIO()
            if format == "CSV":
                df.to_csv(output, index=False)
                output.seek(0)
                return output, "converted_file.csv"
            else:
                with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
                    df.to_excel(writer, index=False, sheet_name="Sheet1")
                output.seek(0)
                return output, "converted_file.xlsx"

        if st.button("Download Converted File"):
            output, filename = convert_file(df, file_format)
            st.download_button(label="Download File", data=output, file_name=filename)

    except Exception as e:
        st.error(f"Error processing file: {e}")
