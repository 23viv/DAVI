import streamlit as st
import pandas as pd


st.set_page_config(page_title="DATA OVERVIEW", page_icon="📄", layout="wide")
st.balloons()

st.title("📄 Data Overview")
uploaded_file = st.file_uploader("Upload your CSV file here", type=["csv"])

if uploaded_file is not None:
    st.success("File uploaded successfully!")
    
    df = pd.read_csv(uploaded_file)
    st.session_state["df"] = df

    st.subheader("👀 Data Preview")
    st.dataframe(df.head())

    st.subheader("📊 Basic Info")
    st.write(df.describe())

    st.subheader("🧾 Column Types")
    st.write(df.dtypes)

else:
    st.info("Please upload a CSV file to get started.")
