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
info = df[df["Species"] == species].squeeze()

st.markdown(f"""
- **Status:** {info['Status']}
- **Extinction Year:** {info['Extinction Year'] or 'N/A'}
- **Genome Available:** {info['Genome Available']}
- **Region:** {info['Region']}
- **Notes:** {info['Notes']}
""")

