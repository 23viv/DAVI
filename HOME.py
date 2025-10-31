import streamlit as st

st.set_page_config(page_title="DAVI", page_icon="🏠", layout="wide")

# --- Minimal centered design ---
st.markdown(
    """
    <style>
    body {
        background-color: #0e0e0e;
    }
    .main {
        text-align: center;
        color: white;
        padding-top: 15%;
        font-family: "Segoe UI", sans-serif;
    }
    .title {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 1rem;
        color: #bbb;
    }
    </style>

    <div class="main">
        <div class="title">📊 DAVI — Visualize Smarter, Not Harder</div>
        <div class="subtitle">
            Upload datasets • Compare columns • Explore patterns — your own mini Power BI.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
