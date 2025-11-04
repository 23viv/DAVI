import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="📊 Data Visualization", page_icon="📈", layout="wide")
st.title("📈 Data Visualization Dashboard")

# Load data from session_state
if "df" not in st.session_state:
    st.warning("⚠️ Please upload your data in the 'Data Overview' page first.")
    st.stop()

df = st.session_state["df"]

# If df is a file path string, read it as CSV
if isinstance(df, str):
    try:
        df = pd.read_csv(df)
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        st.stop()

# Sidebar
st.sidebar.header("🎨 Visualization Settings")

chart_type = st.sidebar.selectbox("Select Chart Type", ["Bar Chart", "Line Chart", "Scatter Plot", "Pie Chart"])
x_col = st.sidebar.selectbox("Select X-axis", df.columns)

# For non-pie charts, need a Y-axis too
if chart_type != "Pie Chart":
    y_col = st.sidebar.selectbox("Select Y-axis", df.columns)
else:
    y_col = None

colors = sns.color_palette("pastel")
fig, ax = plt.subplots(figsize=(8, 5))

# Chart logic
if chart_type == "Bar Chart":
    sns.barplot(data=df, x=x_col, y=y_col, palette=colors, ax=ax)
    ax.set_title(f"Bar Chart of {y_col} vs {x_col}")

elif chart_type == "Line Chart":
    sns.lineplot(data=df, x=x_col, y=y_col, ax=ax, color=sns.color_palette("tab10")[0])
    ax.set_title(f"Line Chart of {y_col} vs {x_col}")

elif chart_type == "Scatter Plot":
    sns.scatterplot(data=df, x=x_col, y=y_col, color=sns.color_palette("tab10")[1], ax=ax)
    ax.set_title(f"Scatter Plot of {y_col} vs {x_col}")

elif chart_type == "Pie Chart":
    pie_data = df[x_col].value_counts()
    ax.pie(pie_data, labels=pie_data.index, colors=colors[:len(pie_data)], autopct="%.1f%%")
    ax.set_title(f"Pie Chart of {x_col}")

else:
    st.error("Unknown chart type selected!")

# Display chart
st.pyplot(fig)
