# --- Package Imports ---
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

@st.cache_data(ttl=86400)
def load_data():
    return pd.read_csv("https://data.cityofnewyork.us/resource/43nn-pn8j.csv?$limit=300000")
df = load_data()

@st.cache_data(ttl=86400)
def load_data():
    inspections = pd.read_csv("https://data.cityofnewyork.us/resource/43nn-pn8j.csv?$limit=300000")
    rodents = pd.read_csv("https://data.cityofnewyork.us/resource/p937-wjvj.csv?$limit=3300000")
    # income = pd.read_csv("YOUR_INCOME_DATASET_URL_HERE?$limit=300000")
    return inspections, rodents

inspections_df, rodents_df = load_data()

# --- Introduction Page ---
if page == "Introduction 🍽️":

    st.title("Introduction 🍽️")

    print(inspections_df.shape)
    print(rodents_df.shape)


