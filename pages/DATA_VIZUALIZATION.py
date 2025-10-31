import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="DATA VISUALIZATION", page_icon="📊", layout="wide")

st.title("📊 Data Visualization Hub")

# ✅ Check if data exists
if "df" not in st.session_state:
    st.warning("⚠️ Please upload a dataset first in the Data Overview page.")
    st.stop()

df = st.session_state["df"]

# Sidebar controls
st.sidebar.header("⚙️ Visualization Controls")

# Column selections
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
categorical_cols = df.select_dtypes(exclude=["int64", "float64"]).columns.tolist()

chart_type = st.sidebar.selectbox(
    "Select chart type",
    ["Scatter Plot", "Line Plot", "Bar Plot", "Box Plot", "Histogram", "Pairplot", "Heatmap"]
)

x_col = st.sidebar.selectbox("X-axis", options=df.columns)
y_col = st.sidebar.selectbox("Y-axis", options=numeric_cols)
hue_col = st.sidebar.multiselect("Hue (optional)", options=categorical_cols)

# Color theme
sns.set_style("whitegrid")
plt.rcParams.update({'axes.titlesize': 14, 'axes.labelsize': 12})

st.subheader(f"📈 {chart_type}")

# Draw plot based on selection
fig, ax = plt.subplots(figsize=(10, 6))

if chart_type == "Scatter Plot":
    sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue_col[0] if hue_col else None, ax=ax)

elif chart_type == "Line Plot":
    sns.lineplot(data=df, x=x_col, y=y_col, hue=hue_col[0] if hue_col else None, ax=ax)

elif chart_type == "Bar Plot":
    sns.barplot(data=df, x=x_col, y=y_col, hue=hue_col[0] if hue_col else None, ax=ax)

elif chart_type == "Box Plot":
    sns.boxplot(data=df, x=x_col, y=y_col, hue=hue_col[0] if hue_col else None, ax=ax)

elif chart_type == "Histogram":
    sns.histplot(data=df, x=y_col, kde=True, ax=ax)

elif chart_type == "Pairplot":
    st.info("Generating Pairplot — might take a few seconds...")
    fig = sns.pairplot(df[numeric_cols])
    st.pyplot(fig)
    st.stop()

elif chart_type == "Heatmap":
    st.info("Showing Correlation Heatmap")
    corr = df[numeric_cols].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)

st.pyplot(fig)
