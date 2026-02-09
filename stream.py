import streamlit as st
import requests

st.title("Document to PDF Converter")

uploaded_file = st.file_uploader(
    "Choose a file",
    type=["txt", "docx"]
)

if uploaded_file is not None:
    st.write("File name:", uploaded_file.name)
    st.write("File type:", uploaded_file.type)

    if st.button("Convert to PDF"):
        with st.spinner("Converting..."):
            response = requests.post(
                "http://127.0.0.1:8000/convert",
                files={"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
            )

        if response.status_code == 200:
            st.success("Conversion successful")

            st.download_button(
                label="Download PDF",
                data=response.content,
                file_name="converted.pdf",
                mime="application/pdf"
            )
        else:
            st.error(response.json()["detail"])