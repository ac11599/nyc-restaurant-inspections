# --- Package Imports ---
import streamlit as st

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
    
    st.write("* [Restaurant Inspection Data](https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/43nn-pn8j/about_data) – Contains inspection scores, grades, violations, cuisine types, and restaurant characteristics.\n" \
    "* [Rodent Inspection Data](https://data.cityofnewyork.us/Health/Rodent-Inspection/p937-wjvj/about_data) – Provides information about rodent activity and pest-related inspections throughout NYC.\n" \
    "* [Income Data](https://data.cccnewyork.org/data/map/66/median-incomes) – Includes neighborhood-level socioeconomic indicators that may influence environmental conditions and business operations.\n" \
    "* [311 Complaint Data](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2020-to-Present/erm2-nwe9/about_data) - Contains data on 311 complaints throughout New York City")

    st.write("Through exploratory analysis, data visualization, and predictive modeling, this dashboard " \
            "investigates the relationships between these factors and identifies the variables that most strongly " \
            "influence restaurant inspection outcomes.")

    st.write("The data used in this project covers the years 2023–2026. "
             "The only exception is the income data, which includes all available years.")

    st.write("The preliminary data exploration and analysis were conducted in Jupyter Notebook. "
             "The notebook is available in the GitHub repository associated with this project.")

# --- Restaurant Inspections Analysis Page ---
elif page == "Restaurant Inspections Analysis 🍽️":

    st.title("Restaurant Inspections Analysis 🍽️")

    st.header("Summary Findings")
    st.write("Queens restaurants overwhelmingly perform well on inspections, with most scores landing " \
    "in the 10-30 range and the vast majority earning an A grade. Score clustering near the A/B cutoffs " \
    "suggests grading thresholds may influence outcomes, not just raw compliance. Inspection volume has " \
    "grown steadily since 2023, with a consistent seasonal dip in November and spike in December. " \
    "Chinese restaurants make up the largest share of inspections, but this reflects restaurant density " \
    "in Queens rather than targeted enforcement.")

    st.write("---")

    st.header("Key Metrics")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["Inspection Score Distribution", "Grade Distribution", "Inspection Count Monthly", "Top Cuisines by Inspection Count"])

    with tab1:
        st.subheader("Inspection Score Distribution")
        st.image("figures/restaurant/inspection_score_distribution.png")
        st.write("Most Queens restaurants score between 10-30 (lower is better), " \
        "with a long tail of worse scores after that. There are two bumps in the data, " \
        "right around where the A and B grade cutoffs are")

    with tab2:
        st.subheader("Grade Distribution")
        st.image("figures/restaurant/grade_distribution.png")
        st.write("The vast majority of Queens restaurants get an A grade (~21,000), " \
        "far more than B and C combined. N, Z, and P (not yet graded, grade pending, pending) " \
        "are all pretty small by comparison. Matches what the score chart showed — most places cluster on the good end.")

    with tab3:
        st.subheader("Inspection Count Monthly")
        st.image("figures/restaurant/number_of_inspections_per_month.png")
        st.write("Inspections have trended up overall since 2023, from under 1,000/month to consistently over 2,000 by 2025. " \
        "There's a recurring dip each November (possibly holiday-related scheduling) and a sharp spike each December "
        "(maybe a year-end push to hit inspection quotas). The steep drop at the very end (2026-07) is due to a " \
        "partial month of data.")


    with tab4:
        st.subheader("Top Cuisines by Inspection Count")
        st.image("figures/restaurant/top_15_cuisine_types_by_number_of_inspections.png")
        st.write("Chinese restaurants are inspected most often (~9,600), followed by American and Latin American (~7,000 and ~6,600). " \
        "This tracks with prior data exploration showing Chinese restaurants are simply the most common cuisine type in Queens, " \
        "so the inspection counts likely just reflect restaurant density rather than targeted enforcement. " \
        "Counts drop off more gradually after the top 3, across Bakery, Caribbean, Pizza, and the rest.")

# --- Rodent Inspections Analysis Page ---
elif page == "Rodent Inspections Analysis 🐀":

    st.title("Rodent Inspections Analysis 🐀")

    st.header("Summary Findings")
    st.write("Rodent inspections in Queens pass more often than they fail, but failures are still substantial — " \
    "over half of passes in count — and often result directly in bait treatment rather than just a failed flag. " \
    "The high volume of Initial inspections relative to Compliance and Treatments visits reflects this same " \
    "pattern, with many follow-up visits needed after failed checks. Inspection volume isn't steady over time: " \
    "two sharp spikes (Sept 2024, Aug 2025) drove both pass and fail counts up together, suggesting periods of " \
    "heightened citywide inspection activity.")

    st.write("It's worth noting that rodent inspections are largely complaint-driven, meaning the properties " \
        "being inspected are more likely to already have a rat issue. This helps explain why the failure rate " \
        "in this dataset appears high relative to citywide conditions overall.")

    st.write("---")

    st.header("Key Metrics")

    tab1, tab2, tab3 = st.tabs(
        ["Rodent Inspection Results", "Rodent Inspection Types", "Rodent Inspections Monthly"])

    with tab1:
        st.subheader("Rodent Inspection Results")
        st.image("figures/rodent/rodent_inspection_results.png")
        st.write("Most rodent inspections in Queens result in a Pass (~21,500), but failures aren't rare — " \
        "combined, 'Failed for Rat Activity,' 'Bait applied,' and 'Failed for Other Reason' add up to well " \
        "over half the pass count. 'Bait applied' sits close to 'Failed for Rat Activity' in count, suggesting " \
        "many failures lead directly to treatment action rather than just a flag.")

    with tab2:
        st.subheader("Rodent Inspection Types")
        st.image("figures/rodent/rodent_inspection_types.png")
        st.write("Most rodent inspections are Initial visits (~28,000), roughly double the combined " \
        "Compliance and Treatments visits. This tracks with the previous chart — since about half of " \
        "initial inspections fail, it makes sense to see a large volume of follow-up Compliance and " \
        "Treatments visits after the fact.")

    with tab3:
        st.subheader("Rodent Inspections Monthly")
        st.image("figures/rodent/failed_rodent_inspections_per_month.png")
        st.write("Failed rodent inspections stay fairly steady month to month, generally in the 300-600 range, " \
        "with two sharp spikes around September 2024 and August 2025.")

        st.write("\n")

        st.image("figures/rodent/pass_vs_fail_inspections_per_month.png")
        st.write("The same two months also show large spikes in passed inspections, 3-4x the surrounding months — " \
        "so both failed and passed counts rise together during these periods.")

        st.write("\n")

        st.write("These spikes likely reflect periods of heightened inspection activity overall, rather than a " \
        "sudden worsening of rodent conditions. Possible drivers include seasonal rat activity (rats are more " \
        "active in warmer months), targeted enforcement sweeps in specific neighborhoods, or a surge in 311 " \
        "complaints prompting a wave of inspections.")

# --- Socioeconomic Analysis Page ---
elif page == "Income Data Analysis 💰":

    st.title("Income Data Analysis 💰")

    st.header("Summary Findings")
    st.write("Median household income in Queens varies substantially by neighborhood, ranging from around " \
    "\\$69,000 in Flushing to over \\$115,000 in Queens Village — a gap that has generally persisted over time, " \
    "with denser, immigrant-heavy neighborhoods tending to sit at the lower end and more suburban, homeowner-heavy " \
    "neighborhoods at the higher end. Most neighborhoods have trended upward since 2005, though some (The " \
    "Rockaways, Elmhurst/Corona) show more volatility, possibly tied to smaller population bases or disruptive " \
    "events. At the household level, families earn more than the Queens average overall, and families without " \
    "children out-earn families with children, likely reflecting dual-income households with fewer dependent-" \
    "related costs.")

    st.write("---")

    st.header("Key Metrics")

    tab1, tab2, tab3 = st.tabs(
        ["Median Neighborhood Income", "Median Income by Household Type", "Top 5 vs Bottom 5 Neighborhoods by Income"])

    with tab1:
        st.subheader("Median Neighborhood Income")
        st.image("figures/income/median_household_income_by_neighborhood_queens2024.png")
        st.write("Median household income varies widely across Queens neighborhoods, from around \\$69,000 in " \
        "Flushing to over \\$115,000 in Queens Village. Roughly half the neighborhoods fall below the Queens average.")
        
        st.write("\n")

        st.image("figures/income/median_household_income_over_time_by_neighborhood_queens.png")
        st.write("Most neighborhoods show a general upward trend in median income from 2005 to 2024, though with " \
        "notable year-to-year volatility for some (like The Rockaways and Elmhurst/Corona). Queens Village and " \
        "Bayside consistently rank among the highest earners throughout the period.")
        st.write("The volatility in neighborhoods like The Rockaways and Elmhurst/Corona may reflect smaller " \
        "population bases, shifting immigration patterns, or disruptive events like COVID-19. " \
        "Queens Village and Bayside's consistently high incomes likely reflect their more suburban, homeowner-heavy " \
        "makeup compared to denser, more transient neighborhoods elsewhere in the borough.")

    with tab2:
        st.subheader("Median Income by Household Type")
        st.image("figures/income/median_income_by_household_type_queens2024.png")
        st.write("Families have a higher median income (\\$94,000) than the overall Queens average (\\$85,000), " \
        "and families without children out-earn families with children (\\$96,000 vs \\$91,000) — likely reflecting " \
        "dual-income households with fewer dependent-related work interruptions or expenses.")

    with tab3:
        st.subheader("Top 5 vs Bottom 5 Neighborhoods by Income")
        st.image("figures/income/top5_vs_bottom5_neighborhoods_by_median_income_queens2024.png")
        st.write("The gap between the top and bottom 5 neighborhoods is substantial — Queens Village " \
        "(\\$115,000) earns nearly 70% more than Flushing (\\$69,000). The bottom 5 are largely denser, " \
        "immigrant-heavy neighborhoods, while the top 5 skew more suburban.")


# --- 311 Complaints Analysis Page ---
elif page == "311 Complaints Analysis Page 📞":
    
    st.title("311 Complaints Analysis Page 📞")

    st.header("Summary Findings")
    st.write("311 complaints in Queens are dominated by parking and noise-related issues, with Illegal Parking " \
    "alone accounting for far more complaints than any other category. This is reflected in agency volume too — " \
    "NYPD receives the vast majority of complaints, well ahead of HPD, DSNY, and others, since parking, noise, " \
    "and vehicle issues all route through them. Complaint volume overall has trended upward since 2023, and " \
    "some categories show clear seasonal patterns, most notably HEAT/HOT WATER complaints spiking in winter " \
    "months and dropping off in summer.")
    st.write("---")

    st.header("Key Metrics")

    tab1, tab2, tab3 = st.tabs(
        ["Top Complaint Types", "Complaints by Agency", "Complaints Monthly"])

    with tab1:
        st.subheader("Top Complaint Types")
        st.image("figures/complaints/top_15_complaint_types.png")
        st.write("Illegal Parking is by far the most common 311 complaint in Queens (~575,000), more than " \
        "double the next highest category. Blocked Driveway and Noise - Residential follow closely behind " \
        "each other, and complaints drop off more gradually after that.")

    with tab2:
        st.subheader("Complaints by Agency")
        st.image("figures/complaints/complaints_by_agency.png")
        st.write("NYPD receives by far the most 311 complaints (~1.5M), more than 4x the next highest agency " \
        "(HPD). This tracks with the top complaint types chart — parking, noise, and vehicle complaints all " \
        "route to NYPD, which explains the outsized volume.")

    with tab3:
        st.subheader("Complaints Monthly")
        st.image("figures/complaints/total_complaints_per_month.png")
        st.write("Total 311 complaints trend upward overall since 2023, from ~43,000/month to consistently " \
        "over 75,000. The sharp drop at the very end (2026-07) is due to a partial month of data.")

        st.write("\n")

        st.image("figures/complaints/top_5_complaint_types_per_month.png")
        st.write("Illegal Parking stays the top complaint type nearly every month, with HEAT/HOT WATER showing " \
        "a strong seasonal pattern — spiking each winter and dropping off in summer, as expected.")

# --- Integrated Analysis Page ---
elif page == "Integrated Analysis 📊":

    st.title("Integrated Analysis 📊")

# --- Predictive Model Dashboard Page ---
elif page == "Predictive Model Dashboard 🔮":

    st.title("Predictive Model Dashboard 🔮")
