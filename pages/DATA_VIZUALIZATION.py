import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="📊 Data Visualization", page_icon="📈", layout="wide")
st.title("📈 Data Visualization Dashboard")

# Load data from session_state
if "df" not in st.session_state:
    st.warning("Please upload your data in the 'Data Overview' page first.")
else:
    df = pd.read_csv(st.session_state["df"]) if isinstance(st.session_state["df"], str) else pd.read_csv(st.session_state["df"])

    chart_type = st.selectbox("Select chart type", ["bar_chart", "line_chart", "scatter_plot", "pie_chart"])
    x_col = st.selectbox("Select X-axis", df.columns)
    y_col = None
    if chart_type != "pie_chart":
        y_col = st.selectbox("Select Y-axis", df.columns)

    colors = sns.color_palette("pastel")  # or try "coolwarm", "mako", etc.

    fig, ax = plt.subplots(figsize=(8, 5))

    if chart_type == "bar_chart":
        sns.barplot(data=df, x=x_col, y=y_col, palette=colors, ax=ax)

    elif chart_type == "line_chart":
        sns.lineplot(data=df, x=x_col, y=y_col, palette=colors, ax=ax)

    elif chart_type == "scatter_plot":
        sns.scatterplot(data=df, x=x_col, y=y_col, palette=colors, ax=ax)

    elif chart_type == "pie_chart":
        # For pie, pick one column (categorical) and show distribution
        pie_data = df[x_col].value_counts()
        ax.pie(pie_data, labels=pie_data.index, colors=colors[:len(pie_data)], autopct="%.0f%%")
        ax.set_title(f"Pie Chart of {x_col}")

    st.pyplot(fig)
