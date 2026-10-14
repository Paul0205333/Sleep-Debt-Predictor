import streamlit as st
import pandas as pd
import joblib

# ============================================
# PAGE CONFIGURATION
# ============================================

st.set_page_config(
    page_title="Sleep Debt Assessment",
    page_icon="🌙",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================
# LOAD TRAINED MODEL
# ============================================

@st.cache_resource
def load_model():
    return joblib.load("models/sleep_debt_model.pkl")

model = load_model()

# ============================================
# CUSTOM CSS
# ============================================

st.markdown("""
<style>
    .stApp {
        background-color: #F7F8F6;
        color: #202820;
    }

    .block-container {
        max-width: 900px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3 {
        color: #202820;
        letter-spacing: -0.7px;
    }

    .eyebrow {
        color: #52735E;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 2px;
        margin-bottom: 0.5rem;
    }

    .subtitle {
        color: #737B74;
        font-size: 1rem;
        line-height: 1.7;
        margin-bottom: 1.5rem;
    }

    .section-heading {
        font-size: 1.05rem;
        font-weight: 650;
        color: #28372C;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid #E3E8E1;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    div[data-testid="stForm"] {
        background: #FFFFFF;
        border: 1px solid #E5E9E3;
        border-radius: 18px;
        padding: 1.4rem;
    }

    div[data-testid="stMetric"] {
        background: #FFFFFF;
        border: 1px solid #E5E9E3;
        border-radius: 16px;
        padding: 1.2rem;
    }

    div[data-testid="stMetricLabel"] {
        color: #737B74;
        font-size: 0.85rem;
    }

    div[data-testid="stMetricValue"] {
        color: #315C49;
        font-weight: 700;
    }

    .stButton > button,
    div[data-testid="stFormSubmitButton"] > button {
        background-color: #315C49;
        color: white;
        border: none;
        border-radius: 10px;
        min-height: 3rem;
        font-weight: 600;
        width: 100%;
        transition: background-color 0.2s ease;
    }

    .stButton > button:hover,
    div[data-testid="stFormSubmitButton"] > button:hover {
        background-color: #244735;
        color: white;
        border: none;
    }

    div[data-testid="stAlert"] {
        border-radius: 12px;
    }

    .footer {
        text-align: center;
        color: #899089;
        font-size: 0.78rem;
        margin-top: 2.5rem;
    }

    hr {
        border-color: #E3E8E1;
    }

    /* Slider accent color */
    .stSlider [data-baseweb="slider"] div[role="slider"] {
        background-color: #315C49 !important;
        border: 2px solid #315C49 !important;
    }

    /* Slider filled track */
    .stSlider [data-baseweb="slider"] > div > div {
        background-color: #315C49 !important;
    }

    /* Slider labels */
    .stSlider label {
        color: #28372C !important;
        font-weight: 600 !important;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# HEADER
# ============================================

st.markdown(
    '<div class="eyebrow">SLEEP / DEBT</div>',
    unsafe_allow_html=True
)

st.title("Sleep Debt Assessment")

st.markdown(
    """
    <div class="subtitle">
        Understand your sleep patterns through a machine-learning
        prediction based on your sleep habits and lifestyle.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ============================================
# INPUT FORM
# ============================================

with st.form("sleep_assessment_form"):

    # SLEEP METRICS
    st.markdown(
        '<div class="section-heading">01 &nbsp; Sleep Metrics</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        total_sleep_hours = st.slider(
            "Total Sleep Hours",
            min_value=0.0,
            max_value=12.0,
            value=7.0,
            step=0.1,
            help="Total hours slept during the relevant sleep period."
        )

        sleep_latency_min = st.slider(
            "Sleep Latency (minutes)",
            min_value=0.0,
            max_value=180.0,
            value=15.0,
            step=1.0,
            help="How long it takes to fall asleep."
        )

        deep_sleep_pct = st.slider(
            "Deep Sleep (%)",
            min_value=0.0,
            max_value=100.0,
            value=20.0,
            step=1.0
        )

    with col2:
        morning_alarm_snoozes = st.slider(
            "Morning Alarm Snoozes",
            min_value=0,
            max_value=20,
            value=1,
            step=1
        )

        bedtime_phone_minutes = st.slider(
            "Bedtime Phone Use (minutes)",
            min_value=0,
            max_value=300,
            value=30,
            step=1
        )

        caffeine_post_5pm_mg = st.slider(
            "Caffeine After 5 PM (mg)",
            min_value=0.0,
            max_value=600.0,
            value=0.0,
            step=10.0
        )

    st.markdown(
        '<div class="section-heading">02 &nbsp; Screen Habits</div>',
        unsafe_allow_html=True
    )

    col3, col4 = st.columns(2)

    with col3:
        blue_light_filter_active = st.selectbox(
            "Blue Light Filter",
            options=[1, 0],
            format_func=lambda x: "Enabled" if x == 1 else "Disabled"
        )

    with col4:
        screen_brightness_pct = st.slider(
            "Screen Brightness (%)",
            min_value=0.0,
            max_value=100.0,
            value=50.0,
            step=1.0
        )

    # LIFESTYLE
    st.markdown(
        '<div class="section-heading">03 &nbsp; Lifestyle</div>',
        unsafe_allow_html=True
    )

    col5, col6 = st.columns(2)

    with col5:
        chronotype = st.selectbox(
            "Chronotype",
            [
                "Intermediate",
                "Night Owl",
                "Morning Lark"
            ]
        )

        occupation_type = st.selectbox(
            "Occupation Type",
            [
                "Student",
                "Remote Tech",
                "Healthcare / Shift Worker"
            ]
        )

    with col6:
        primary_bedtime_app = st.selectbox(
            "Primary Bedtime App",
            [
                "YouTube",
                "TikTok / Reels",
                "Instagram / Reddit",
                "Streaming (Netflix/Hulu)",
                "Messaging / Chat",
                "News / Reading"
            ]
        )

    st.markdown("<br>", unsafe_allow_html=True)

    submitted = st.form_submit_button(
        "Generate Sleep Assessment",
        use_container_width=True
    )

# ============================================
# PREDICTION AND CONFIDENCE
# ============================================

if submitted:

    input_data = pd.DataFrame({
        "total_sleep_hours": [total_sleep_hours],
        "morning_alarm_snoozes": [morning_alarm_snoozes],
        "bedtime_phone_minutes": [bedtime_phone_minutes],
        "sleep_latency_min": [sleep_latency_min],
        "blue_light_filter_active": [blue_light_filter_active],
        "screen_brightness_pct": [screen_brightness_pct],
        "caffeine_post_5pm_mg": [caffeine_post_5pm_mg],
        "deep_sleep_pct": [deep_sleep_pct],
        "chronotype": [chronotype],
        "occupation_type": [occupation_type],
        "primary_bedtime_app": [primary_bedtime_app]
    })

    try:
        prediction = model.predict(input_data)[0]

        # Initialize variables
        confidence = None
        category_probabilities = None

        # Get model probabilities when supported
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(input_data)[0]

            # Get class labels
            classes = getattr(model, "classes_", None)

            # Support sklearn Pipeline models
            if classes is None and hasattr(model, "named_steps"):
                final_estimator = list(
                    model.named_steps.values()
                )[-1]
                classes = getattr(final_estimator, "classes_", None)

            # Store probabilities for every category
            if classes is not None and len(classes) == len(probabilities):
                category_probabilities = pd.DataFrame({
                    "Sleep Debt Category": classes,
                    "Probability": probabilities,
                    "Probability (%)": [
                        f"{p:.1%}" for p in probabilities
                    ]
                })

                # Find the probability for the predicted category
                matching_indices = [
                    i for i, class_label in enumerate(classes)
                    if class_label == prediction
                ]

                if matching_indices:
                    confidence = float(
                        probabilities[matching_indices[0]]
                    )

        # ========================================
        # RESULTS
        # ========================================

        st.divider()

        st.markdown(
            '<div class="eyebrow">ASSESSMENT RESULTS</div>',
            unsafe_allow_html=True
        )

        st.subheader("Your Prediction")

        metric_col1, metric_col2 = st.columns(2)

        with metric_col1:
            st.metric(
                label="Predicted Sleep Debt Category",
                value=str(prediction)
            )

        with metric_col2:
            if confidence is not None:
                st.metric(
                    label="Model Confidence",
                    value=f"{confidence:.1%}"
                )
            else:
                st.metric(
                    label="Model Confidence",
                    value="Unavailable"
                )

        if confidence is not None:
            st.caption(
                "Confidence represents the model's estimated probability "
                "for the predicted category. It is not a guarantee of "
                "prediction accuracy."
            )
        else:
            st.info(
                "This model does not expose a usable class probability. "
                "A confidence percentage cannot be displayed reliably. "
                "The predicted category is still available above."
            )

        with st.expander("View submitted sleep information"):
            st.dataframe(
                input_data.T.rename(columns={0: "Your Input"}),
                use_container_width=True
            )

        with st.expander("View Category Probabilities"):

            if category_probabilities is not None:

                st.caption(
                    "Probabilities are generated by the trained model "
                    "for the submitted sleep information."
                )

                # Display categories ranked by probability
                display_probabilities = (
                    category_probabilities
                    .sort_values("Probability", ascending=False)
                    .reset_index(drop=True)
                )

                st.dataframe(
                    display_probabilities[
                        ["Sleep Debt Category", "Probability (%)"]
                    ],
                    hide_index=True,
                    use_container_width=True
                )

                # Visual comparison of category probabilities
                chart_data = display_probabilities.set_index(
                    "Sleep Debt Category"
                )[["Probability"]]

                st.bar_chart(chart_data)

            else:
                st.info(
                    "Category probabilities are unavailable because "
                    "the model does not expose predict_proba()."
                )

    except Exception as e:
        st.error(
            "The prediction could not be generated. "
            "Check that the model and input features are compatible."
        )
        st.exception(e)

# ============================================
# FOOTER
# ============================================

st.markdown(
    """
    <div class="footer">
        SLEEP / DEBT &nbsp;·&nbsp; MACHINE LEARNING ASSESSMENT
        <br><br>
        Predictions are estimates generated by a trained model
        and are not medical diagnoses.
    </div>
    """,
    unsafe_allow_html=True
)