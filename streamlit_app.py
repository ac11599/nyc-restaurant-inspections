# --- Package Imports ---
import streamlit as st
import pandas as pd
import sklearn
import joblib

# --- Setup ---
st.set_page_config(
    page_title="NYC Restaurant Inspections Dashboard 🌐",
    layout="centered",
    page_icon="🌐",)
st.sidebar.header("NYC Restaurant Inspections Dashboad 🌐")
page = st.sidebar.selectbox("Select Page", [
                            "Introduction 🗽",
                            "Explore Datasets 🔍",
                            # "What Drives Restaurant Risk? 📊",
                            "What Drives Restaurant Risk? 📊",
                            "Predictive Model Dashboard 🔮"])

# --- Introduction Page ---
if page == "Introduction 🗽":

    st.title("Introduction 🗽")

    st.header("Research Question")
    st.write("How does restaurant health inspection risk vary across neighborhoods in New York City, "
             "and what does that variation suggest about the relationship between neighborhood conditions "
             "and food safety outcomes?")

    st.header("Overview")

    st.write("Food safety inspections play an important role in protecting public health and maintaining "
             "restaurant quality standards throughout New York City. The NYC Department of Health and Mental Hygiene regularly inspects "
             "restaurants to evaluate compliance with food safety regulations and assigns inspection scores based on "
             "observed violations.")

    st.write("Inspection scores are calculated by assigning point values to violations identified during an "
             "inspection. Lower scores indicate better performance, while higher scores indicate more severe or "
             "numerous violations. Based on these scores, restaurants receive letter grades that are publicly displayed:")

    st.write("* Grade A: 0–13 points\n"
             "* Grade B: 14–27 points\n"
             "* Grade C: 28 or more points")

    st.write("Most restaurants are inspected at least once per year, although additional inspections may occur "
             "if violations are found or complaints are received. During inspections, health inspectors evaluate factors "
             "such as food handling practices, employee hygiene, sanitation, pest control, and facility maintenance.")

    st.write("This project explores datasets related to restaurant health and environmental conditions in New York City:")

    st.write("* [Restaurant Inspection Data](https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/43nn-pn8j/about_data) – Contains inspection scores, grades, violations, cuisine types, and restaurant characteristics.\n"
             "* [Rodent Inspection Data](https://data.cityofnewyork.us/Health/Rodent-Inspection/p937-wjvj/about_data) – Provides information about rodent activity and pest-related inspections throughout NYC.\n"
             "* [Income Data](https://data.cccnewyork.org/data/map/66/median-incomes) – Includes neighborhood-level socioeconomic indicators that may influence environmental conditions and business operations.\n"
             "* [311 Complaint Data](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2020-to-Present/erm2-nwe9/about_data) - Contains data on 311 complaints throughout New York City")

    st.write("Through exploratory analysis, data visualization, and predictive modeling, this dashboard "
             "investigates the relationships between these factors and identifies the variables that most strongly "
             "influence restaurant inspection outcomes.")

    st.write("The data used in this project covers the years 2023–2026. "
             "The only exception is the income data, which includes all available years.")

    st.write("The preliminary data exploration and analysis were conducted in Jupyter Notebook. "
             "The notebook is available in the GitHub repository associated with this project.")

# --- Explore Datasets Page ---
elif page == "Explore Datasets 🔍":
    dataset = st.sidebar.selectbox("Choose a dataset to explore:", [
        "Restaurant Inspections 🍽️",
        "Rodent Inspections 🐀",
        "Income Data 💰",
        "311 Complaints 📞"
    ])

    if dataset == "Restaurant Inspections 🍽️":
        st.title("Restaurant Inspections Analysis 🍽️")

        st.header("Summary Findings")
        st.write("Queens restaurants overwhelmingly perform well on inspections, with most scores landing "
                 "in the 10-30 range and the vast majority earning an A grade. Score clustering near the A/B cutoffs "
                 "suggests grading thresholds may influence outcomes, not just raw compliance. Inspection volume has "
                 "grown steadily since 2023, with a consistent seasonal dip in November and spike in December. "
                 "Chinese restaurants make up the largest share of inspections, but this reflects restaurant density "
                 "in Queens rather than targeted enforcement.")

        st.write("---")

        st.header("Key Metrics")

        tab1, tab2, tab3, tab4 = st.tabs(
            ["Inspection Score Distribution", "Grade Distribution", "Inspection Count Monthly", "Top Cuisines by Inspection Count"])

        with tab1:
            st.subheader("Inspection Score Distribution")
            st.image("figures/restaurant/inspection_score_distribution.png")
            st.write("Most Queens restaurants score between 10-30 (lower is better), "
                     "with a long tail of worse scores after that. There are two bumps in the data, "
                     "right around where the A and B grade cutoffs are")

        with tab2:
            st.subheader("Grade Distribution")
            st.image("figures/restaurant/grade_distribution.png")
            st.write("The vast majority of Queens restaurants get an A grade (~21,000), "
                     "far more than B and C combined. N, Z, and P (not yet graded, grade pending, pending) "
                     "are all pretty small by comparison. Matches what the score chart showed — most places cluster on the good end.")

        with tab3:
            st.subheader("Inspection Count Monthly")
            st.image("figures/restaurant/number_of_inspections_per_month.png")
            st.write("Inspections have trended up overall since 2023, from under 1,000/month to consistently over 2,000 by 2025. "
                     "There's a recurring dip each November (possibly holiday-related scheduling) and a sharp spike each December "
                     "(maybe a year-end push to hit inspection quotas). The steep drop at the very end (2026-07) is due to a "
                     "partial month of data.")

        with tab4:
            st.subheader("Top Cuisines by Inspection Count")
            st.image(
                "figures/restaurant/top_15_cuisine_types_by_number_of_inspections.png")
            st.write("Chinese restaurants are inspected most often (~9,600), followed by American and Latin American (~7,000 and ~6,600). "
                     "This tracks with prior data exploration showing Chinese restaurants are simply the most common cuisine type in Queens, "
                     "so the inspection counts likely just reflect restaurant density rather than targeted enforcement. "
                     "Counts drop off more gradually after the top 3, across Bakery, Caribbean, Pizza, and the rest.")
    elif dataset == "Rodent Inspections 🐀":
        st.title("Rodent Inspections Analysis 🐀")

        st.header("Summary Findings")
        st.write("Rodent inspections in Queens pass more often than they fail, but failures are still substantial — "
                 "over half of passes in count — and often result directly in bait treatment rather than just a failed flag. "
                 "The high volume of Initial inspections relative to Compliance and Treatments visits reflects this same "
                 "pattern, with many follow-up visits needed after failed checks. Inspection volume isn't steady over time: "
                 "two sharp spikes (Sept 2024, Aug 2025) drove both pass and fail counts up together, suggesting periods of "
                 "heightened citywide inspection activity.")

        st.write("It's worth noting that rodent inspections are largely complaint-driven, meaning the properties "
                 "being inspected are more likely to already have a rat issue. This helps explain why the failure rate "
                 "in this dataset appears high relative to citywide conditions overall.")

        st.write("---")

        st.header("Key Metrics")

        tab1, tab2, tab3 = st.tabs(
            ["Rodent Inspection Results", "Rodent Inspection Types", "Rodent Inspections Monthly"])

        with tab1:
            st.subheader("Rodent Inspection Results")
            st.image("figures/rodent/rodent_inspection_results.png")
            st.write("Most rodent inspections in Queens result in a Pass (~21,500), but failures aren't rare — "
                     "combined, 'Failed for Rat Activity,' 'Bait applied,' and 'Failed for Other Reason' add up to well "
                     "over half the pass count. 'Bait applied' sits close to 'Failed for Rat Activity' in count, suggesting "
                     "many failures lead directly to treatment action rather than just a flag.")

        with tab2:
            st.subheader("Rodent Inspection Types")
            st.image("figures/rodent/rodent_inspection_types.png")
            st.write("Most rodent inspections are Initial visits (~28,000), roughly double the combined "
                     "Compliance and Treatments visits. This tracks with the previous chart — since about half of "
                     "initial inspections fail, it makes sense to see a large volume of follow-up Compliance and "
                     "Treatments visits after the fact.")

        with tab3:
            st.subheader("Rodent Inspections Monthly")
            st.image("figures/rodent/failed_rodent_inspections_per_month.png")
            st.write("Failed rodent inspections stay fairly steady month to month, generally in the 300-600 range, "
                     "with two sharp spikes around September 2024 and August 2025.")

            st.write("\n")

            st.image("figures/rodent/pass_vs_fail_inspections_per_month.png")
            st.write("The same two months also show large spikes in passed inspections, 3-4x the surrounding months — "
                     "so both failed and passed counts rise together during these periods.")

            st.write("\n")

            st.write("These spikes likely reflect periods of heightened inspection activity overall, rather than a "
                     "sudden worsening of rodent conditions. Possible drivers include seasonal rat activity (rats are more "
                     "active in warmer months), targeted enforcement sweeps in specific neighborhoods, or a surge in 311 "
                     "complaints prompting a wave of inspections.")
    elif dataset == "Income Data 💰":
        st.title("Income Data Analysis 💰")

        st.header("Summary Findings")
        st.write("Median household income in Queens varies substantially by neighborhood, ranging from around "
                 "\\$69,000 in Flushing to over \\$115,000 in Queens Village — a gap that has generally persisted over time, "
                 "with denser, immigrant-heavy neighborhoods tending to sit at the lower end and more suburban, homeowner-heavy "
                 "neighborhoods at the higher end. Most neighborhoods have trended upward since 2005, though some (The "
                 "Rockaways, Elmhurst/Corona) show more volatility, possibly tied to smaller population bases or disruptive "
                 "events. At the household level, families earn more than the Queens average overall, and families without "
                 "children out-earn families with children, likely reflecting dual-income households with fewer dependent-"
                 "related costs.")

        st.write("---")

        st.header("Key Metrics")

        tab1, tab2, tab3 = st.tabs(
            ["Median Neighborhood Income", "Median Income by Household Type", "Top 5 vs Bottom 5 Neighborhoods by Income"])

        with tab1:
            st.subheader("Median Neighborhood Income")
            st.image(
                "figures/income/median_household_income_by_neighborhood_queens2024.png")
            st.write("Median household income varies widely across Queens neighborhoods, from around \\$69,000 in "
                     "Flushing to over \\$115,000 in Queens Village. Roughly half the neighborhoods fall below the Queens average.")

            st.write("\n")

            st.image(
                "figures/income/median_household_income_over_time_by_neighborhood_queens.png")
            st.write("Most neighborhoods show a general upward trend in median income from 2005 to 2024, though with "
                     "notable year-to-year volatility for some (like The Rockaways and Elmhurst/Corona). Queens Village and "
                     "Bayside consistently rank among the highest earners throughout the period.")
            st.write("The volatility in neighborhoods like The Rockaways and Elmhurst/Corona may reflect smaller "
                     "population bases, shifting immigration patterns, or disruptive events like COVID-19. "
                     "Queens Village and Bayside's consistently high incomes likely reflect their more suburban, homeowner-heavy "
                     "makeup compared to denser, more transient neighborhoods elsewhere in the borough.")

        with tab2:
            st.subheader("Median Income by Household Type")
            st.image(
                "figures/income/median_income_by_household_type_queens2024.png")
            st.write("Families have a higher median income (\\$94,000) than the overall Queens average (\\$85,000), "
                     "and families without children out-earn families with children (\\$96,000 vs \\$91,000) — likely reflecting "
                     "dual-income households with fewer dependent-related work interruptions or expenses.")

        with tab3:
            st.subheader("Top 5 vs Bottom 5 Neighborhoods by Income")
            st.image(
                "figures/income/top5_vs_bottom5_neighborhoods_by_median_income_queens2024.png")
            st.write("The gap between the top and bottom 5 neighborhoods is substantial — Queens Village "
                     "(\\$115,000) earns nearly 70% more than Flushing (\\$69,000). The bottom 5 are largely denser, "
                     "immigrant-heavy neighborhoods, while the top 5 skew more suburban.")
    elif dataset == "311 Complaints 📞":
        st.title("311 Complaints Analysis Page 📞")

        st.header("Summary Findings")
        st.write("311 complaints in Queens are dominated by parking and noise-related issues, with Illegal Parking "
                 "alone accounting for far more complaints than any other category. This is reflected in agency volume too — "
                 "NYPD receives the vast majority of complaints, well ahead of HPD, DSNY, and others, since parking, noise, "
                 "and vehicle issues all route through them. Complaint volume overall has trended upward since 2023, and "
                 "some categories show clear seasonal patterns, most notably HEAT/HOT WATER complaints spiking in winter "
                 "months and dropping off in summer.")
        st.write("---")

        st.header("Key Metrics")

        tab1, tab2, tab3 = st.tabs(
            ["Top Complaint Types", "Complaints by Agency", "Complaints Monthly"])

        with tab1:
            st.subheader("Top Complaint Types")
            st.image("figures/complaints/top_15_complaint_types.png")
            st.write("Illegal Parking is by far the most common 311 complaint in Queens (~575,000), more than "
                     "double the next highest category. Blocked Driveway and Noise - Residential follow closely behind "
                     "each other, and complaints drop off more gradually after that.")

        with tab2:
            st.subheader("Complaints by Agency")
            st.image("figures/complaints/complaints_by_agency.png")
            st.write("NYPD receives by far the most 311 complaints (~1.5M), more than 4x the next highest agency "
                     "(HPD). This tracks with the top complaint types chart — parking, noise, and vehicle complaints all "
                     "route to NYPD, which explains the outsized volume.")

        with tab3:
            st.subheader("Complaints Monthly")
            st.image("figures/complaints/total_complaints_per_month.png")
            st.write("Total 311 complaints trend upward overall since 2023, from ~43,000/month to consistently "
                     "over 75,000. The sharp drop at the very end (2026-07) is due to a partial month of data.")

            st.write("\n")

            st.image("figures/complaints/top_5_complaint_types_per_month.png")
            st.write("Illegal Parking stays the top complaint type nearly every month, with HEAT/HOT WATER showing "
                     "a strong seasonal pattern — spiking each winter and dropping off in summer, as expected.")

# --- What Drives Restaurant Risk? Page ---
elif page == "What Drives Restaurant Risk? 📊":

    st.title("What Drives Restaurant Risk? 📊")
    st.header("Research Question")
    st.write("How does restaurant health inspection risk vary across neighborhoods "
             "in New York City, and what does that variation suggest about the relationship between neighborhood "
             "conditions and food safety outcomes?")

    st.write("Each prior section explored one dataset on its own. Here, we bring income, rodent inspections, "
             "and 311 complaints together with restaurant grades to test whether they're related, and what that "
             "tells us about food safety risk across Queens neighborhoods.")

    st.header("Summary Findings")
    st.write("Restaurant inspection risk varies meaningfully across Queens neighborhoods, and that variation is "
             "most strongly tied to rodent inspection outcomes — neighborhoods with more rodent problems tend to have "
             "lower restaurant A-grade rates, pointing to shared conditions like building age or general sanitation "
             "infrastructure rather than food-safety-specific factors alone.")

    st.write("Income, somewhat surprisingly, shows only a weak relationship with restaurant grades. Several "
             "lower and mid-income neighborhoods (The Rockaways, Howard Beach) actually outperform higher-income areas, "
             "suggesting that neighborhood wealth alone doesn't determine food safety outcomes. 311 complaint activity "
             "tracks moderately with both rodent failures and lower restaurant grades, reinforcing the idea that these "
             "three datasets are picking up on overlapping neighborhood-level conditions rather than fully independent "
             "phenomena.")

    st.write("Taken together, this suggests restaurant inspection risk in Queens is shaped less by income "
             "directly, and more by shared physical/environmental neighborhood conditions — the kind that also drive "
             "rodent activity and resident complaints. A useful next step would be incorporating building age, housing "
             "density, or population data to normalize complaint counts and test these relationships more precisely.")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["Correlation Overview", "Risk Factors vs Restaurant Grades",
         "Neighborhood Risk Ranking", "Explore a Neighborhood"])

    with tab1:
        st.subheader("Correlation Overview")
        st.image("figures/integrated/correlation_heatmap.png")
        st.write("Restaurant A-grade rate correlates most strongly with rodent inspection failure rate (-0.58), "
                 "suggesting both reflect shared neighborhood-level sanitation conditions. Median income shows only a weak "
                 "relationship with restaurant grades (0.21), while 311 complaint volume shows a moderate negative "
                 "relationship with income (-0.57) and a moderate positive relationship with rodent failures (0.51).")

    with tab2:
        st.subheader("Risk Factors vs Restaurant Grades")

        st.image("figures/integrated/rodent_vs_restaurant_grade_rate.png")
        st.write("Rodent failure rate shows the clearest relationship with restaurant grades — neighborhoods "
                 "with more rodent problems tend to have lower A-grade rates, pointing to shared underlying conditions "
                 "like building age, density, or general sanitation infrastructure.")

        st.write("\n")

        st.image("figures/integrated/income_vs_restaurant_grade_rate.png")
        st.write("Income's relationship with restaurant grades is notably weak. Some lower-income neighborhoods "
                 "(The Rockaways, Howard Beach) actually have among the highest A-grade rates, while higher-income Queens "
                 "Village sits only in the middle — suggesting income alone doesn't determine food safety outcomes.")

        st.write("\n")

        st.image("figures/integrated/complaints_vs_restaurant_grade_rate.png")
        st.write("311 complaint volume shows a moderate negative relationship with restaurant grades. This makes "
                 "some intuitive sense — neighborhoods generating more complaints overall may also have more underlying "
                 "conditions that affect food safety, though complaint counts aren't normalized by population here.")

    with tab3:
        st.subheader("Neighborhood Risk Ranking")
        st.image("figures/integrated/restaurant_grade_rate_neighborhoods_ranked.png")
        st.write("Ranking neighborhoods by A-grade rate shows meaningful variation across Queens — from Flushing "
                 "at the low end (~53%) to Howard Beach at the high end (~77%). Notably, this ranking doesn't track cleanly "
                 "with income: Howard Beach and The Rockaways (lower/mid income) outperform Queens Village (highest income), "
                 "while Flushing (lowest income) does sit at the bottom, showing the relationship isn't purely deterministic.")

    with tab4:
        st.subheader("Explore a Neighborhood")

        merged = pd.read_csv("merged_neighborhood_summary.csv")

        selected = st.selectbox("Choose a neighborhood:",
                                sorted(merged['neighborhood']))
        row = merged[merged['neighborhood'] == selected].iloc[0]

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Median Income", f"${row['median_income']:,.0f}")
        col2.metric("A-Grade Rate", f"{row['pct_grade_a']*100:.1f}%")
        col3.metric("Rodent Fail Rate", f"{row['rodent_fail_rate']*100:.1f}%")
        col4.metric("311 Complaints", f"{row['complaint_count']:,}")

# --- Predictive Model Dashboard Page ---
elif page == "Predictive Model Dashboard 🔮":

    st.title("Predictive Model Dashboard 🔮")

    # Load everything once
    model = joblib.load('model/restaurant_score_model.pkl')
    model_columns = joblib.load('model/model_columns.pkl')
    cuisine_list = joblib.load('model/cuisine_list.pkl')
    neighborhood_list = joblib.load('model/neighborhood_list.pkl')
    neighborhood_stats = pd.read_csv('merged_neighborhood_summary.csv')

    st.header("Predictive Model: Restaurant Inspection Risk")
    st.write("Select a cuisine type, neighborhood, and month to predict an inspection score and estimated grade.")

    # User inputs
    col1, col2, col3 = st.columns(3)
    cuisine = col1.selectbox("Cuisine Type", cuisine_list)
    neighborhood = col2.selectbox("Neighborhood", neighborhood_list)
    month = col3.selectbox("Month", list(range(1, 13)), 
                            format_func=lambda x: pd.Timestamp(2024, x, 1).strftime('%B'))

    if st.button("Predict Inspection Score"):
        # Look up neighborhood stats
        stats_row = neighborhood_stats[neighborhood_stats['neighborhood'] == neighborhood].iloc[0]
        
        # Build input row, starting all zeros
        input_row = pd.DataFrame(0, index=[0], columns=model_columns)
        
        # Set numeric features
        input_row['month_num'] = month
        input_row['median_income'] = stats_row['median_income']
        input_row['rodent_fail_rate'] = stats_row['rodent_fail_rate']
        input_row['complaint_count'] = stats_row['complaint_count']
        
        # Set the correct one-hot columns to 1
        cuisine_col = f'cuisine_description_{cuisine}'
        neighborhood_col = f'neighborhood_{neighborhood}'
        
        if cuisine_col in input_row.columns:
            input_row[cuisine_col] = 1
        if neighborhood_col in input_row.columns:
            input_row[neighborhood_col] = 1
        
        # Predict
        predicted_score = model.predict(input_row)[0]
        
        # Convert to grade using NYC cutoffs
        if predicted_score <= 13:
            predicted_grade = "A"
        elif predicted_score <= 27:
            predicted_grade = "B"
        else:
            predicted_grade = "C"
        
        # Display results
        col1, col2 = st.columns(2)
        col1.metric("Predicted Score", f"{predicted_score:.1f}")
        col2.metric("Predicted Grade", predicted_grade)
        
        st.caption("Note: predictions are estimates based on historical patterns and may not reflect any individual restaurant's actual outcome. Model RMSE: ~15.9 points, R²: 0.29.")
