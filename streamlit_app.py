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
st.sidebar.header("NYC Restaurant Inspections Dashboad 🌐")
page = st.sidebar.selectbox("Select Page", [
                            "Introduction 🗽", 
                            "Restaurant Inspections Analysis 🍽️",
                            "Rodent Inspections Analysis 🐀",
                            "Socioeconomic Analysis 💰",
                            "Integrated Analysis 📊",
                            "Predictive Model Dashboard 🔮"])

# --- Introduction Page ---
if page == "Introduction 🗽":

    st.title("Introduction 🗽")

    st.header("Research Question")
    st.write("How does restaurant health inspection risk vary across neighborhoods in New York City, " \
             "and what does that variation suggest about the relationship between neighborhood conditions " \
             "and food safety outcomes?")

    st.header("Overview")

    st.write("Food safety inspections play an important role in protecting public health and maintaining " \
    "restaurant quality standards throughout New York City. The NYC Department of Health regularly inspects " \
    "restaurants to evaluate compliance with food safety regulations and assigns inspection scores based on " \
    "observed violations.")

    st.write("Inspection scores are calculated by assigning point values to violations identified during an " \
    "inspection. Lower scores indicate better performance, while higher scores indicate more severe or " \
    "numerous violations. Based on these scores, restaurants receive letter grades that are publicly displayed:")

    st.write("* Grade A: 0–13 points\n" \
    "* Grade B: 14–27 points\n" \
    "* Grade C: 28 or more points")

    st.write("Most restaurants are inspected at least once per year, although additional inspections may occur " \
    "if violations are found or complaints are received. During inspections, health inspectors evaluate factors " \
    "such as food handling practices, employee hygiene, sanitation, pest control, and facility maintenance.")

    st.write("This project explores three datasets related to restaurant health and environmental conditions in New York City:")
    
    st.write("* Restaurant Inspection Data – Contains inspection scores, grades, violations, cuisine types, and restaurant characteristics.\n" \
    "* Rodent Inspection Data – Provides information about rodent activity and pest-related inspections throughout NYC.\n" \
    "* Income Data – Includes neighborhood-level socioeconomic indicators that may influence environmental conditions and business operations.")

    st.write("Through exploratory analysis, geographic visualization, and predictive modeling, this dashboard " \
            "investigates the relationships between these factors and identifies the variables that most strongly " \
            "influence restaurant inspection outcomes.")

# --- Restaurant Inspections Analysis Page ---
elif page == "Restaurant Inspections Analysis 🍽️":

    st.title("Restaurant Inspections Analysis 🍽️")

# --- Rodent Inspections Analysis Page ---
elif page == "Rodent Inspections Analysis 🐀":

    st.title("Rodent Inspections Analysis 🐀")

# --- Socioeconomic Analysis Page ---
elif page == "Socioeconomic Analysis 💰":

    st.title("Socioeconomic Analysis 💰")

# --- Integrated Analysis Page ---
elif page == "Integrated Analysis 📊":

    st.title("Integrated Analysis 📊")

# --- Predictive Model Dashboard Page ---
elif page == "Predictive Model Dashboard 🔮":

    st.title("Predictive Model Dashboard 🔮")
