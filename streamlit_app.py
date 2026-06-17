# --- Package Imports ---
import streamlit as st

# datasets
# https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/43nn-pn8j/about_data
# https://data.cityofnewyork.us/Health/Rodent-Inspection/p937-wjvj/about_data
# [insert income dataset here]

# --- Setup ---
st.set_page_config(
    page_title="NYC Restaurant Inspections Dashboard 🌐",
    layout="centered",
    page_icon="🌐",)
st.sidebar.title("NYC Restaurant Inspections 🌐")
page = st.sidebar.selectbox("Select Page", [
                            "Introduction 🍽️"])

# --- Introduction Page ---
if page == "Introduction 🍽️":

    st.title("Introduction 🍽️")



