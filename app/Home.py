import streamlit as st
st.set_page_config(page_title="Species Revival Dashboard", layout="wide")

import pandas as pd
from app_utils.wikidata_sparql import get_iucn_status_from_wikidata
from app_utils.gbif_api import get_species_occurrences

# Load the species list
@st.cache_data
def load_data():
    return pd.read_csv("data/species_list.csv")

df = load_data()

# App layout
st.title("🧬 Species Revival Dashboard")
st.sidebar.title("🔍 Explore")

# Sidebar species selection
species_name = st.sidebar.selectbox("🔍 Choose a species", df["Species Name"])

if species_name:
    st.subheader(f"📄 Profile: {species_name}")
    info = df[df["Species Name"] == species_name].squeeze()

    st.markdown(f"""
    - **Species Name:** {info['Species Name']}
    - **Status:** {info['Status']}
    - **Year Extinct:** {info['Year Extinct']}
    - **Region:** {info['Region']}
    - **Genomic Data:** {info['Genomic Data']}
    - **Notes:** {info['Notes']}
    """)

    # Clean the species name for API querying
    query_name = species_name.strip().replace(" ", "%20")
    st.write(f"🔍 Querying APIs for: {species_name}")


    # Show GBIF sightings
    gbif_data = get_species_occurrences(species_name)
    if gbif_data:
        num_sightings = gbif_data.get("count", 0)
        st.markdown(f"🗺️ **GBIF Sightings:** {num_sightings}")
    else:
        st.markdown("⚠️ No GBIF data available.")




