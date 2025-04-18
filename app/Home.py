import streamlit as st
import pandas as pd

st.set_page_config(page_title="Species Revival Dashboard", layout="wide")

# Load the species list
@st.cache_data
def load_data():
    return pd.read_csv("data/species_list.csv")

df = load_data()

# App layout
st.title("🧬 Species Revival Dashboard")
st.sidebar.title("🔍 Explore")

# Sidebar species selection
species = st.sidebar.selectbox("Choose a species", df["Species Name"])

# Show selected species info
st.subheader(f"Species Profile: {species}")
info = df[df["Species Name"] == species].squeeze()

st.markdown(f"""
- **Species Name:** {info['Species Name']}
- **Status:** {info['Status']}
- **Year Extinct:** {info['Year Extinct']}
- **Region:** {info['Region']}
- **Genomic Data:** {info['Genomic Data']}
- **Notes:** {info['Notes']}
""")

