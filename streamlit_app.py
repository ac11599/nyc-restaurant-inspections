# --- Package Imports ---
import streamlit as st
import pandas as pd
import joblib

# --- Setup ---
st.set_page_config(
    page_title="NYC Restaurant Inspections Dashboard 🌐",
    layout="centered",
    page_icon="🌐",
)

st.sidebar.header("NYC Restaurant Inspections Dashboard 🌐")
# page = st.sidebar.selectbox(
#     "Select Page",
#     [
#         "Introduction 🗽",
#         "1. Restaurant Risk 🍽️",
#         "2. Risk Varies Across Queens 🗺️",
#         "3. What Do the Maps Show? 📍",
#         "4. Do Neighborhood Conditions Explain Risk? 📊",
#         "5. What Predicts Risk? 🔮",
#         "6. Policy & Conclusions 💡",
#         "Appendix: Explore Datasets 🔍",
#     ],
# )

page = st.sidebar.selectbox(
    "Select Page",
    [
        "Introduction 🗽",
        "1. Restaurant Risk 🍽️",
        "2. Risk Varies Across Queens 🗺️",
        "3. Do Neighborhood Conditions Explain Risk? 📊",
        "4. What Predicts Risk? 🔮",
        "5. Policy & Conclusions 💡",
        "Appendix A: Explore Datasets 🔍",
        "Appendix B: Maps 📍",
    ],
)

# --- Introduction Page ---
if page == "Introduction 🗽":
    st.title("NYC Restaurant Inspection Risk 🗽")

    st.header("Research Question")
    st.write(
        "**What explains differences in restaurant inspection risk across neighborhoods in New York City?** "
    )
    st.write(
        "I examine restaurant inspections alongside neighborhood income, rodent inspections, "
        "and 311 complaints to test what factors are associated with food-safety risk."
    )

    st.header("Overview and Importance")
    st.write(
        "Food safety inspections play an important role in protecting public health and maintaining "
        "restaurant quality standards throughout New York City. The NYC Department of Health and Mental Hygiene regularly inspects "
        "restaurants to evaluate compliance with food safety regulations and assigns inspection scores based on "
        "observed violations."
    )
    st.write(
        "Most restaurants are inspected at least once per year, although additional inspections may occur "
        "if violations are found or complaints are received. During inspections, health inspectors evaluate factors "
        "such as food handling practices, employee hygiene, sanitation, pest control, and facility maintenance."
    )
    st.write(
        "Restaurant inspection risk can vary for many reasons, from neighborhood conditions to characteristics of the restaurant "
        "itself. Identifying which factors are most useful for predicting risk can help support more targeted and effective "
        "food safety efforts."
    )

    st.header("How I Investigated It")
    st.write(
        "The analysis first looks at restaurant inspection risk, then examines how risk differs "
        "across neighborhoods and whether neighborhood conditions are related to those differences. "
        "Finally, it tests how well restaurant and neighborhood characteristics can predict "
        "the score of an individual inspection."
    )

    st.header("Data")
    col1, col2 = st.columns(2)
    col1.metric("Study Area", "Queens")
    col2.metric("Timeframe", "2023–2026")
    st.write("The project combines four sources: ")
    st.write(
        "* [Restaurant Inspection Data](https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/43nn-pn8j/about_data)\n"
        "* [Rodent Inspection Data](https://data.cityofnewyork.us/Health/Rodent-Inspection/p937-wjvj/about_data)\n"
        "* [Income Data](https://data.cccnewyork.org/data/map/66/median-incomes)\n"
        "* [311 Complaint Data](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2020-to-Present/erm2-nwe9/about_data)"
    )
    st.write(
        "The income data spans a longer period, while the other datasets focus on 2023–2026."
    )
    st.caption(
        "The preliminary data exploration and analysis were conducted in Jupyter Notebook. The notebook is available in the GitHub repository associated with this project."
    )

# --- Restaurant Risk Page ---
elif page == "1. Restaurant Risk 🍽️":
    st.title("1. What Does Restaurant Risk Look Like? 🍽️")

    st.write(
        "Before asking what explains risk, we first need to establish what the outcome looks like. "
    )
    st.write(
        "Inspection scores are calculated by assigning point values to violations identified during an "
        "inspection. Lower scores indicate better performance, while higher scores indicate more severe or "
        "numerous violations. Based on these scores, restaurants receive letter grades that are publicly displayed:"
    )

    st.write(
        "* Grade A: 0–13 points\n"
        "* Grade B: 14–27 points\n"
        "* Grade C: 28 or more points"
    )

    st.info(
        "**Key takeaway:** Most inspections are on the better-performing end of the distribution, "
        "but a meaningful tail of higher scores creates room for substantial variation in food-safety outcomes."
    )

    tab1, tab2 = st.tabs(["Inspection Scores", "Letter Grades"])

    with tab1:
        st.subheader("Inspection Score Distribution")
        st.image("figures/restaurant/inspection_score_distribution.png")
        st.write(
            "Most Queens restaurants score in roughly the 10–30 range, with a long tail of higher scores. "
            "The visible clustering near the A/B cutoffs also highlights that grade thresholds can shape how raw scores translate into public-facing grades."
        )

    with tab2:
        st.subheader("Grade Distribution")
        st.image("figures/restaurant/grade_distribution.png")
        st.write(
            "The vast majority of inspections receive an A, while B and C grades make up a much smaller share. "
            "So the central question is not whether most restaurants are safe enough to earn an A — it is why the risk profile still varies across places and restaurant types."
        )

    st.write("---")

    st.subheader("A Useful Context, Not a Main Finding")
    st.write(
        "Inspection volume has increased over the study period, and the number of inspections varies throughout the year. "
        "The detailed inspection-volume charts are in the appendix."
    )

    st.write("### The next question...")
    st.success(
        "If most restaurants earn an A, **what explains the differences in restaurant risk?**"
    )

# --- Neighborhood Variation Page ---
elif page == "2. Risk Varies Across Queens 🗺️":
    st.title("2. Risk Varies Across Queens 🗺️")

    st.write(
        "The first important pattern is geographic: restaurant outcomes are not uniform across Queens. "
        "I ranked neighborhoods by their A-grade rate to make that variation visible."
    )

    st.subheader("Restaurant A-Grade Rate by Neighborhood")
    st.image("figures/integrated/restaurant_grade_rate_neighborhoods_ranked.png")

    st.info(
        "**The spread is substantial:** the neighborhood ranking runs from roughly **71% A grades in Flushing** "
        "to roughly **86% in Howard Beach**."
    )

    st.write(
        "That geographic variation raises the obvious next question: do neighborhood conditions explain the differences? "
        "If they do, we would expect restaurant risk to line up with measures such as neighborhood income, rodent activity, or 311 complaints."
    )

    st.subheader("Explore a Neighborhood")
    merged = pd.read_csv("data/merged_neighborhood_summary.csv")
    selected = st.selectbox("Choose a neighborhood:", sorted(merged["neighborhood"]))
    row = merged[merged["neighborhood"] == selected].iloc[0]

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Median Income", f"${row['median_income']:,.0f}")
    col2.metric("A-Grade Rate", f"{row['pct_grade_a'] * 100:.1f}%")
    col3.metric("Rodent Fail Rate", f"{row['rodent_fail_rate'] * 100:.1f}%")
    col4.metric(
        "311 per 1k Residents",
        f"{row['complaints_per_1k_per_year']:,.1f}",
        help="Annualized 311 complaints per 1,000 residents, 2023-2026",
    )

    st.write("### The Next Question")
    st.success(
        "Neighborhoods differ in both restaurant inspection results and the conditions around them. "
        "**Are those differences in neighborhood conditions related to restaurant risk?**"
    )

# --- Maps Page (temporarily moved to Appendix) ---
# elif page == "3. What Do the Maps Show? 📍":
#     st.title("3. What Do the Maps Show? 📍")
elif page == "Appendix B: Maps 📍":
    st.title("Appendix B: What Do the Maps Show? 📍")

    st.write(
        "The neighborhood rankings show that restaurant inspection outcomes vary across Queens."
    )

    st.write(
        "The maps below show the geographic distribution of restaurant inspections, rodent inspection "
        "failures, and 311 complaints. Looking at these measures together helps us ask whether the "
        "same areas consistently stand out."
    )

    st.header("A Visual Check for Geographic Patterns")

    st.info(
        "**Key takeaway:** The maps show geographic differences in activity, but there is no obvious "
        "Queens-wide visual pattern that clearly explains restaurant inspection risk."
    )

    # --- Restaurant Inspections Map ---
    st.subheader("Restaurant Inspections")

    st.image(
        "figures/maps/restaurant_inspections.png",
        use_container_width=True,
    )

    st.write(
        "Restaurant inspections are distributed throughout Queens, with higher concentrations in some "
        "areas than others. However, there is no single obvious geographic pattern that clearly separates "
        "higher- and lower-risk areas."
    )

    st.caption(
        "Inspection volume reflects where restaurants and inspection activity are located. "
        "A higher number of inspections does not necessarily mean higher food-safety risk."
    )

    # --- Rodent Failures Map ---
    st.subheader("Rodent Inspection Failures")

    st.image(
        "figures/maps/failed_rodent_inspections.png",
        use_container_width=True,
    )

    st.write(
        "Rodent inspection failures also appear across multiple parts of Queens rather than being "
        "concentrated in one clearly defined area. Some areas show more failures than others, but "
        "the visual pattern alone is not strong enough to conclude that rodent conditions explain "
        "restaurant inspection risk."
    )

    st.caption(
        "Rodent inspections are not a random sample of properties and can be influenced by complaint "
        "activity and inspection patterns."
    )

    # --- 311 Complaints Map ---
    st.subheader("311 Complaints")

    st.image(
        "figures/maps/311_complaints.png",
        use_container_width=True,
    )

    st.write(
        "311 complaints are widespread across Queens as well. Some areas have noticeably more complaints, "
        "but raw complaint counts reflect more than neighborhood conditions. They can also reflect population, "
        "density, reporting behavior, and the number of people and businesses generating complaints."
    )

    st.caption(
        "Because these are raw complaint counts, they should not be interpreted as a direct measure "
        "of neighborhood risk."
    )

    # --- Combined Map ---
    st.subheader("All Three Measures Together")

    st.image(
        "figures/maps/restaurant_neighborhood_conditions.png",
        use_container_width=True,
    )

    st.write(
        "Putting the three measures together provides another useful check: do restaurant inspections, "
        "rodent failures, and 311 complaints consistently cluster in the same places?"
    )

    st.write(
        "Visually, the answer is not especially clear. There are areas where activity overlaps, but "
        "there is no obvious Queens-wide pattern in which all three measures consistently line up "
        "with restaurant inspection outcomes."
    )

    st.write("---")

    # --- What the Maps Tell Us ---
    st.header("What the Maps Tell Us — and What They Don't")

    st.write(
        "The maps provide an important first impression: **geographic differences exist, but they are "
        "not visually simple.**"
    )

    st.write(
        "That matters because it would be easy to look at one map and conclude that a particular area "
        "is higher risk. The combined maps suggest that the relationship between restaurant outcomes "
        "and neighborhood conditions is more complicated than that."
    )

    st.write(
        "The maps are therefore best treated as a starting point rather than a final answer. "
        "To understand whether these neighborhood conditions are actually related to restaurant outcomes, "
        "we need to move beyond visual inspection and test the relationships quantitatively."
    )

    st.success(
        "### The Next Question\n\n"
        "**If the geographic patterns are not obvious from the maps, are neighborhood conditions "
        "still statistically related to restaurant risk?**"
    )

# --- Neighborhood Conditions Page ---
# elif page == "4. Do Neighborhood Conditions Explain Risk? 📊":
#     st.title("4. Do Neighborhood Conditions Explain Risk? 📊")
elif page == "3. Do Neighborhood Conditions Explain Risk? 📊":
    st.title("3. Do Neighborhood Conditions Explain Risk? 📊")

    st.write(
        "We now bring neighborhood-level data into the restaurant analysis, focusing on a narrower question: "
        "**are neighborhood conditions associated with restaurant outcomes?**"
    )

    st.subheader("The Neighborhood-Level Correlations")
    st.image("figures/integrated/correlation_heatmap.png")

    col1, col2, col3 = st.columns(3)
    col1.metric("Income vs. A-grade rate", "+0.25")
    col2.metric("Rodent failures vs. A-grade rate", "−0.58")
    col3.metric("311 vs. A-grade rate", "-0.21")

    st.write(
        "Rodent inspection failure rate has the strongest neighborhood-level relationship with restaurant A-grade rate. "
        "Income and 311 complaints per resident both show weaker relationships. Income is much weaker than we might "
        "expect from a simple ‘wealthier neighborhood = safer restaurant’ story."
    )

    st.caption(
        "These correlations are based on only 14 neighborhoods, so they are suggestive rather than conclusive."
    )

    st.subheader("Rodent Conditions Show the Clearest Relationship")
    st.image("figures/integrated/rodent_vs_restaurant_grade_rate.png")
    st.write(
        "Neighborhoods with more rodent inspection failures tend to have lower A-grade rates. "
        "This could reflect shared underlying conditions such as building age, density, sanitation infrastructure, "
        "or differences in inspection activity. The correlation alone cannot distinguish among these explanations."
    )

    st.subheader("Income Is Much Less Predictive at the Neighborhood Level")
    st.image("figures/integrated/income_vs_restaurant_grade_rate.png")
    st.write(
        "Income shows only a weak relationship with restaurant grades. Some lower- or middle-income neighborhoods "
        "perform very well, while Queens Village — among the highest-income neighborhoods — sits closer to the middle of the restaurant ranking."
    )

    st.subheader("311 Complaint Rate")
    st.image("figures/integrated/complaints_vs_restaurant_grade_rate.png")
    st.write(
        "Neighborhoods with more 311 complaints per 1,000 residents tend to have slightly lower A-grade rates, "
        "but the relationship is weak. Most 311 complaints are about parking and noise, so this is only a rough "
        "measure of neighborhood conditions."
    )

    st.write("### But there is a catch")
    st.success(
        "These are neighborhood-level correlations. They tell us what moves together, "
        "**not which variables are most important or what causes what.** "
        "They also describe neighborhood averages, which may not hold for any individual restaurant."
    )
    

# --- Predictive Model Page ---
# elif page == "5. What Predicts Risk? 🔮":
#     st.title("5. What Predicts Risk? 🔮")
elif page == "4. What Predicts Risk? 🔮":
    st.title("4. What Predicts Risk? 🔮")

    # st.header("The Key Test")
    # st.write(
    #     "The neighborhood analysis gives us an important clue, but it does not tell us whether neighborhood conditions are the strongest signals. "
    #     "To test that, we built a model using cuisine type, neighborhood, inspection month, median income, rodent failure rate, and 311 complaint volume."
    # )

    # st.info(
    #     "Once these variables are considered together, the strongest predictive signals are **cuisine type and inspection month**, not neighborhood conditions."
    # )
    # st.info(
    #     "**Cuisine type is the strongest reported feature group, but this should not be interpreted as meaning that one cuisine is inherently higher risk "
    #     "than another.** "
    #     "Instead, cuisine type may be capturing differences in the ingredients, food preparation, and food-handling practices associated "
    #     "with different types of restaurants."
    # )

    # st.subheader("Model Performance")
    # col1, col2, col3 = st.columns([0.5, 1, 1.5])
    # col1.metric("R²", "0.29")
    # col2.metric("RMSE", "~15.9 points")
    # col3.metric("Outcome", "Inspection score")

    # st.write(
    #     "The model explains about 29% of the variation in inspection scores. That is a modest result: most of the variation in any individual inspection remains unexplained, "
    #     "which is consistent with the fact that inspection outcomes depend on day-of conditions and other restaurant-level factors that are not present in this dataset."
    # )

    # st.subheader("What Matters Most for Prediction?")
    # col1, col2, col3 = st.columns(3)
    # col1.metric("Cuisine type", "38%", delta="Strongest signal")
    # col2.metric("Inspection month", "32%", delta="Second strongest")
    # col3.metric("Neighborhood + conditions", "<25%", delta="Secondary")

    # st.write(
    #     "Cuisine type is the single strongest reported feature group, accounting for 38% of total importance. "
    #     "Inspection month is a close second at 32%. Neighborhood identity and the neighborhood-level conditions together are clearly secondary in the model."
    # )

    # st.write(
    #     "A more useful interpretation is that cuisine type may serve as a proxy for differences in the "
    #     "ingredients and food-handling processes that restaurants use. For example, a restaurant that regularly "
    #     "handles raw meat, poultry, or seafood may face different food-safety challenges than an establishment "
    #     "that primarily prepares coffee and other lower-risk items."
    # )

    # st.write(
    #     "These differences can involve factors such as temperature control, cross-contamination, storage, "
    #     "preparation, and handling procedures. The current model does not directly measure these factors, so "
    #     "we cannot determine whether they explain the cuisine-related feature importance."
    # )

    # st.success(
    #     "### The main finding\n\n"
    #     "**What food the restaurant serves, and when it gets inspected, matter more for prediction than what neighborhood it is in.**"
    # )

    # st.subheader("Why This Changes the Story")
    # st.write(
    #     "The earlier correlations could make neighborhood conditions look like the main explanation for restaurant risk. "
    #     "The model adds an important layer of context: neighborhood conditions still carry signal, but they are not the dominant predictive story after accounting for restaurant characteristics and inspection timing."
    # )

    # Update these from the notebook's final results table
    GB_R2, GB_RMSE, GB_MAE = 0.046, 14.71, 10.87
    MEAN_RMSE, MEDIAN_MAE = 15.08, 10.16

    st.header("The Key Test")
    st.write(
        "The neighborhood analysis shows patterns, but it doesn't tell us whether they help predict "
        "an individual restaurant's inspection score. To test that, we built a model using cuisine type, "
        "neighborhood, inspection month, median income, rodent failure rate, and 311 complaints per resident. "
        "We tested it only on restaurants it had never seen."
    )

    st.info(
        "**These factors explain very little about any single inspection.** The model barely beats "
        "a simple average guess, so none of these factors can reliably identify which restaurants will score poorly."
    )

    st.subheader("Model Performance")
    col1, col2, col3 = st.columns(3)
    col1.metric("R²", f"{GB_R2:.3f}")
    col2.metric("RMSE", f"{GB_RMSE:.1f} points")
    col3.metric("Guessing the average", f"{MEAN_RMSE:.1f} points")

    st.write(
        f"The model explains under 5% of the variation in inspection scores. Its typical error "
        f"(RMSE {GB_RMSE:.1f} points) is only about 2% better than always guessing the average score "
        f"({MEAN_RMSE:.1f}). On typical error (MAE), it does no better than guessing the median score "
        f"({GB_MAE:.1f} vs. {MEDIAN_MAE:.1f}). Inspection outcomes depend mostly on things not in this data, "
        "such as the restaurant's own practices and conditions on the day of the inspection."
    )

    st.subheader("Which Information Helped Most?")
    st.write(
        "We scrambled each type of information and measured how much worse the predictions got."
    )
    col1, col2, col3 = st.columns(3)
    col1.metric("Cuisine type", "+0.6 points")
    col2.metric("All neighborhood info", "+0.1 points")
    col3.metric("Inspection month", "+0.03 points")

    st.write(
        "Cuisine was the most useful clue, but even it improved predictions only slightly. "
        "Neighborhood and month added almost nothing. This should not be read as one cuisine being "
        "inherently riskier than another; cuisine may reflect differences in food preparation and handling."
    )

    st.success(
        "### The main finding\n\n"
        "**Neighborhood patterns exist, but neither neighborhood, cuisine, nor timing can predict which individual restaurants will do poorly.**"
    )

    st.subheader("Why This Changes the Story")
    st.write(
        "The earlier correlations show that neighborhoods with more rodent failures tend to have lower A-grade rates. "
        "But those are averages across many restaurants. Within any neighborhood, individual inspection scores vary widely, "
        "so neighborhood is a poor guide to any one restaurant."
    )




    st.subheader("Interactive Risk Prediction")
    st.write(
        "Choose a cuisine type, neighborhood, and inspection month to see the model's estimated inspection score and grade."
    )

    # Load model resources only on this page.
    model = joblib.load("model/restaurant_score_model.pkl")
    model_columns = joblib.load("model/model_columns.pkl")
    cuisine_list = joblib.load("model/cuisine_list.pkl")
    neighborhood_list = joblib.load("model/neighborhood_list.pkl")
    neighborhood_stats = pd.read_csv("data/merged_neighborhood_summary.csv")

    col1, col2, col3 = st.columns(3)
    cuisine = col1.selectbox("Cuisine Type", cuisine_list)
    neighborhood = col2.selectbox("Neighborhood", neighborhood_list)
    month = col3.selectbox(
        "Inspection Month",
        list(range(1, 13)),
        format_func=lambda x: pd.Timestamp(2024, x, 1).strftime("%B"),
    )

    if st.button("Predict Inspection Score"):
        stats_row = neighborhood_stats[
            neighborhood_stats["neighborhood"] == neighborhood
        ].iloc[0]

        input_row = pd.DataFrame(0, index=[0], columns=model_columns)
        input_row["month_num"] = month
        input_row["median_income"] = stats_row["median_income"]
        input_row["rodent_fail_rate"] = stats_row["rodent_fail_rate"]
        input_row["complaints_per_1k_per_year"] = stats_row["complaints_per_1k_per_year"]

        cuisine_col = f"cuisine_description_{cuisine}"
        neighborhood_col = f"neighborhood_{neighborhood}"

        if cuisine_col in input_row.columns:
            input_row[cuisine_col] = 1
        if neighborhood_col in input_row.columns:
            input_row[neighborhood_col] = 1

        predicted_score = model.predict(input_row)[0]

        if predicted_score <= 13:
            predicted_grade = "A"
        elif predicted_score <= 27:
            predicted_grade = "B"
        else:
            predicted_grade = "C"

        col1, col2 = st.columns(2)
        col1.metric("Predicted Score", f"{predicted_score:.1f}")
        col2.metric("Predicted Grade", predicted_grade)

        st.caption(
            f"Predictions cluster near the average score because these factors explain little. "
            f"Typical error is about {GB_RMSE:.0f} points (R² = {GB_R2:.3f})."
        )

    st.subheader("Correlation, Not Causation")
    st.write(
        "Neither the correlations nor the model establish causal relationships. For example, a neighborhood with more rodent failures "
        "may also have older buildings, denser development, or other shared conditions. Similarly, a cuisine category's "
        "predictive importance does not mean the cuisine itself causes worse inspection outcomes."
    )

    st.write(
        "That distinction is especially important when translating the model into policy: **use predictive signals as evidence for further investigation, "
        "not as proof that one community, cuisine, or neighborhood causes another outcome.**"
    )

# --- Policy & Conclusions Page ---
# elif page == "6. Policy & Conclusions 💡":
#     st.title("6. What Should We Do With the Finding? 💡")
elif page == "5. Policy & Conclusions 💡":
    st.title("5. What Should We Do With the Finding? 💡")

    st.header("Executive Summary")
    st.write(
        "Restaurant inspection results in Queens vary across neighborhoods, and neighborhoods with higher rodent "
        "inspection failure rates tend to have lower A-grade rates. But neighborhood, cuisine, and inspection month "
        "together explain under 5% of the variation in individual inspection scores."
    )

    st.header("So What?")
    st.write(
        "Neighborhood-level patterns are real, but they are too weak to identify which individual restaurants "
        "are higher risk. Targeting inspections by neighborhood, cuisine, or time of year alone would "
        "miss most of the variation."
    )

    st.subheader("Policy Recommendation")
    st.write(
        "**Recommendation:** Treat neighborhood conditions as context, and focus risk targeting on "
        "restaurant-level information."
    )
    st.write("**1. Use restaurant history.**")
    st.write(
        "A restaurant's own past scores and violation types are not in this analysis, but are the most "
        "promising next signals to test."
    )
    st.write("**2. Look at specific food-handling practices.**")
    st.write(
        "Cuisine was the most useful factor in the model, though only slightly. Examining practices such as "
        "raw meat handling and temperature control would be more informative than cuisine labels."
    )

    st.write("**Why this approach is preferable:**")
    st.write(
        "It focuses future targeting on characteristics that can be measured directly at the restaurant level, rather than assigning higher risk to a neighborhood or cuisine."
    )

    st.subheader("Limitations")
    st.write(
        "This analysis covers Queens restaurant inspections from 2023–2026, so the findings should not automatically be "
        "generalized to other boroughs. The neighborhood correlations rest on only 14 neighborhoods. "
        "The model explains under 5% of score variation, so most variation in an individual inspection remains unexplained. "
        "Some records could not be matched to a neighborhood by ZIP code and were left out. "
        "Finally, the analysis is observational and cannot establish causality."
    )

    st.header("Conclusion")
    st.write(
        "Returning to the original question, what explains differences in restaurant inspection risk across Queens neighborhoods? "
        "Neighborhood conditions, especially rodent failure rates, line up with differences in average A-grade rates. "
        "But those patterns don't carry down to individual inspections, where cuisine, neighborhood, and timing explain very little."
    )
    st.success(
        "**Bottom line:** Neighborhood patterns exist, but predicting which individual restaurants are higher risk "
        "requires restaurant-level information that this data doesn't include."
    )

# --- Appendix / Detailed Dataset Exploration ---
# elif page == "Appendix: Explore Datasets 🔍":
#     st.title("Appendix: Explore Datasets 🔍")
elif page == "Appendix A: Explore Datasets 🔍":
    st.title("Appendix A: Explore Datasets 🔍")

    st.write(
        "This section preserves the detailed exploratory analysis from the original dashboard. "
        "It is intentionally separated from the main story so that the presentation can stay focused while the underlying evidence remains available."
    )

    dataset = st.sidebar.selectbox(
        "Choose a dataset to explore:",
        [
            "Restaurant Inspections 🍽️",
            "Rodent Inspections 🐀",
            "Income Data 💰",
            "311 Complaints 📞",
        ],
    )

    if dataset == "Restaurant Inspections 🍽️":
        st.title("Restaurant Inspections Analysis 🍽️")
        st.header("Inspection Volume and Cuisine Context")

        tab1, tab2 = st.tabs(
            ["Inspection Count Monthly", "Top Cuisines by Inspection Count"]
        )

        with tab1:
            st.subheader("Inspection Count Monthly")
            st.image("figures/restaurant/number_of_inspections_per_month.png")
            st.write(
                "Inspections have trended upward overall since 2023, with a recurring November dip and December spike. "
                "The sharp drop at the very end (2026-07) reflects a partial month of data."
            )

        with tab2:
            st.subheader("Top Cuisines by Inspection Count")
            st.image(
                "figures/restaurant/top_20_cuisine_types_by_number_of_inspections.png"
            )
            st.write(
                "Chinese restaurants account for the largest number of inspections, followed by American and Latin American. "
                "Inspection counts are primarily useful here as a measure of restaurant prevalence, not as a direct measure of risk."
            )

    elif dataset == "Rodent Inspections 🐀":
        st.title("Rodent Inspections Analysis 🐀")
        st.write(
            "Rodent inspections are an important context variable because they provide a neighborhood-level indicator of pest-related conditions. "
            "They are also largely complaint-driven, so the inspected properties are not a random sample of all properties."
        )

        tab1, tab2 = st.tabs(
            ["Rodent Inspection Results", "Rodent Inspections Monthly"]
        )

        with tab1:
            st.subheader("Rodent Inspection Results")
            st.image("figures/rodent/rodent_inspection_results.png")
            st.write(
                "Most rodent inspections result in a pass, but failures and treatment actions are substantial. "
                "Because these inspections are often complaint-driven, the failure rate should not be interpreted as a citywide estimate of rodent prevalence."
            )

        with tab2:
            st.subheader("Rodent Inspections Monthly")
            st.image("figures/rodent/failed_rodent_inspections_per_month.png")
            st.write(
                "Failed rodent inspections are generally in the 300–600 range, with notable spikes around September 2024 and August 2025."
            )
            st.image("figures/rodent/pass_vs_fail_inspections_per_month.png")
            st.write(
                "Passed and failed inspections rise together in those periods, which suggests increased inspection activity rather than a simple one-directional change in rodent conditions."
            )

    elif dataset == "Income Data 💰":
        st.title("Income Data Analysis 💰")
        st.write(
            "Neighborhood median income varies substantially across Queens, providing useful context for testing whether neighborhood wealth is associated with restaurant outcomes."
        )

        tab1, tab2, tab3 = st.tabs(
            [
                "Median Neighborhood Income",
                "Median Income by Household Type",
                "Top 5 vs Bottom 5 Neighborhoods by Income",
            ]
        )

        with tab1:
            st.subheader("Median Neighborhood Income")
            st.image(
                "figures/income/median_household_income_by_neighborhood_queens2024.png"
            )
            st.write(
                "Median household income varies widely across neighborhoods, from around $69,000 in Flushing to over $115,000 in Queens Village."
            )
            st.image(
                "figures/income/median_household_income_over_time_by_neighborhood_queens.png"
            )
            st.write(
                "Most neighborhoods show a general upward income trend over time, although some show more year-to-year volatility than others."
            )

        with tab2:
            st.subheader("Median Income by Household Type")
            st.image("figures/income/median_income_by_household_type_queens2024.png")
            st.write(
                "Families have a higher median income than the overall Queens average, while families without children have a higher median than families with children."
            )

        with tab3:
            st.subheader("Top 5 vs Bottom 5 Neighborhoods by Income")
            st.image(
                "figures/income/top5_vs_bottom5_neighborhoods_by_median_income_queens2024.png"
            )
            st.write(
                "The income gap between the highest- and lowest-income neighborhoods is substantial, reinforcing that Queens contains large socioeconomic differences within a single borough."
            )

    elif dataset == "311 Complaints 📞":
        st.title("311 Complaints Analysis 📞")
        st.write(
            "311 complaints provide another neighborhood-level context variable, although raw counts combine population, activity, and reporting behavior and therefore should not be treated as a clean per-capita risk measure."
        )

        tab1, tab2 = st.tabs(["Top Complaint Types", "Complaints Monthly"])

        with tab1:
            st.subheader("Top Complaint Types")
            st.image("figures/complaints/top_15_complaint_types.png")
            st.write(
                "Illegal Parking is the most common complaint type by a wide margin, followed by other parking and noise-related complaints."
            )
            st.subheader("Complaints by Agency")
            st.image("figures/complaints/complaints_by_agency.png")
            st.write(
                "NYPD receives the largest volume of 311 complaints, consistent with the dominance of parking, noise, and vehicle-related requests."
            )

        with tab2:
            st.subheader("Complaints Monthly")
            st.image("figures/complaints/total_complaints_per_month.png")
            st.write(
                "Total 311 complaints trend upward overall, with a partial-month drop at the end of the study period."
            )
            st.image("figures/complaints/top_5_complaint_types_per_month.png")
            st.write(
                "Illegal Parking remains the leading complaint category in most months, while HEAT/HOT WATER shows a strong seasonal pattern."
            )
