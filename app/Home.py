import streamlit as st
import pandas as pd
from app_utils.iucn_api import get_species_status
from app_utils.gbif_api import get_species_occurrences

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
    
    # Show IUCN status
    status_data = get_species_status(species_name)
    if status_data and status_data.get("result"):
        category = status_data["result"][0].get("category", "N/A")
        st.markdown(f"🔴 **Conservation Status (IUCN):** {category}")
    else:
        st.markdown("⚠️ No IUCN data available.")

    # Show GBIF sightings
    gbif_data = get_species_occurrences(species_name)
    if gbif_data:
        num_sightings = gbif_data.get("count", 0)
        st.markdown(f"🗺️ **GBIF Sightings:** {num_sightings}")
    else:
        st.markdown("⚠️ No GBIF data available.")

    # Temporary testing of known species
    st.markdown("---")
    st.markdown("### 🔬 API Test Results")

    st.write("IUCN test for `Panthera leo`:")
    test_iucn = get_species_status("Panthera%20leo")
    st.json(test_iucn)

    st.write("GBIF test for `Elasmotherium`:")
    test_gbif = get_species_occurrences("Elasmotherium")
    st.json(test_gbif)


