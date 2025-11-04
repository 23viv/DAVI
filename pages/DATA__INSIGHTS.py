import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Page setup
st.set_page_config(page_title="📉 Data Insights", page_icon="🧠", layout="wide")



st.title("🧠 Data Insights & Correlations")

# Check for data
if "df" not in st.session_state:
    st.warning("Please upload your dataset in the 'Data Overview' page first.")
else:
    df = st.session_state["df"]

    # ---- Missing Values ----
    st.subheader("🔍 Missing Values Overview")
    missing_data = df.isnull().sum()
    st.write(missing_data[missing_data > 0])

    if missing_data.sum() == 0:
        st.success("No missing values found! 🎉")
    
    st.subheader("👀 Data Preview")
    st.dataframe(df.head())


    # ---- Correlation Heatmap ----
    st.subheader("📊 Correlation Heatmap")

    numeric_df = df.select_dtypes(include=["number"])
    if not numeric_df.empty:
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.heatmap(numeric_df.corr(), annot=True, cmap="mako", fmt=".2f", ax=ax)
        st.pyplot(fig)
    else:
        st.info("No numeric columns available for correlation analysis.")


    # ---- Data Summary ----
    st.subheader("🧾 Summary Statistics")
    
    st.write(df.describe())
