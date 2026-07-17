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
                            "Income Data Analysis 💰",
                            "311 Complaints Analysis Page 📞",
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
    "restaurant quality standards throughout New York City. The NYC Department of Health and Mental Hygiene regularly inspects " \
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

    st.write("This project explores datasets related to restaurant health and environmental conditions in New York City:")
    
    st.write("* Restaurant Inspection Data – Contains inspection scores, grades, violations, cuisine types, and restaurant characteristics.\n" \
    "* Rodent Inspection Data – Provides information about rodent activity and pest-related inspections throughout NYC.\n" \
    "* Income Data – Includes neighborhood-level socioeconomic indicators that may influence environmental conditions and business operations.\n" \
    "* 311 Complaint Data - Contains data on 311 complaints throughout New York City")

    st.write("Through exploratory analysis, geographic visualization, and predictive modeling, this dashboard " \
            "investigates the relationships between these factors and identifies the variables that most strongly " \
            "influence restaurant inspection outcomes.")

# --- Restaurant Inspections Analysis Page ---
elif page == "Restaurant Inspections Analysis 🍽️":

    st.title("Restaurant Inspections Analysis 🍽️")

    st.header("Summary Findings")
    st.write("[insert summary findings]")

    st.write("---")

    st.header("Key Metrics")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["Inspection Score Distribution", "Grade Distribution", "Inspection Count Monthly", "Top Cuisines by Inspection Count"])

    with tab1:
        st.subheader("Inspection Score Distribution")
        st.image("figures/restaurant/inspection_score_distribution.png")
        st.write("[insert notes on figure]")

    with tab2:
        st.subheader("Grade Distribution")
        st.image("figures/restaurant/grade_distribution.png")
        st.write("[insert notes on figure]")

    with tab3:
        st.subheader("Inspection Count Monthly")
        st.image("figures/restaurant/number_of_inspections_per_month.png")
        st.write("[insert notes on figure]")

    with tab4:
        st.subheader("Top Cuisines by Inspection Count")
        st.image("figures/restaurant/top_15_cuisine_types_by_number_of_inspections.png")
        st.write("[insert notes on figure]")

# --- Rodent Inspections Analysis Page ---
elif page == "Rodent Inspections Analysis 🐀":

    st.title("Rodent Inspections Analysis 🐀")

    st.header("Summary Findings")
    st.write("[insert summary findings]")

    st.write("---")

    st.header("Key Metrics")

    tab1, tab2, tab3 = st.tabs(
        ["Rodent Inspection Results", "Rodent Inspection Types", "Rodent Inspections Monthly"])

    with tab1:
        st.subheader("Rodent Inspection Results")
        st.image("figures/rodent/rodent_inspection_results.png")
        st.write("[insert notes on figure]")

    with tab2:
        st.subheader("Rodent Inspection Types")
        st.image("figures/rodent/rodent_inspection_types.png")
        st.write("[insert notes on figure]")

    with tab3:
        st.subheader("Rodent Inspections Monthly")
        st.image("figures/rodent/failed_rodent_inspections_per_month.png")
        st.write("[insert notes on figure]")

        st.image("figures/rodent/pass_vs_fail_inspections_per_month.png")
        st.write("[insert notes on figure]")

# --- Socioeconomic Analysis Page ---
elif page == "Income Data Analysis 💰":

    st.title("Income Data Analysis 💰")

# --- 311 Complaints Analysis Page ---
elif page == "311 Complaints Analysis Page 📞":
    
    st.title("311 Complaints Analysis Page 📞")

    st.header("Summary Findings")
    st.write("[insert summary findings]")

    st.write("---")

    st.header("Key Metrics")

    tab1, tab2, tab3 = st.tabs(
        ["Top Complaint Types", "Complaints by Agency", "Complaints Monthly"])

    with tab1:
        st.subheader("Top Complaint Types")
        st.image("figures/complaints/top_15_complaint_types.png")
        st.write("[insert notes on figure]")

    with tab2:
        st.subheader("Complaints by Agency")
        st.image("figures/complaints/complaints_by_agency.png")
        st.write("[insert notes on figure]")

    with tab3:
        st.subheader("Complaints Monthly")
        st.image("figures/complaints/total_complaints_per_month.png")
        st.write("[insert notes on figure]")

        st.image("figures/complaints/top_5_complaint_types_per_month.png")
        st.write("[insert notes on figure]")

# --- Integrated Analysis Page ---
elif page == "Integrated Analysis 📊":

    st.title("Integrated Analysis 📊")

# --- Predictive Model Dashboard Page ---
elif page == "Predictive Model Dashboard 🔮":

    st.title("Predictive Model Dashboard 🔮")
