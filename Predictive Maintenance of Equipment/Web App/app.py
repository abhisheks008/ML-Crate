import joblib
import streamlit as st

MODEL_PATH = "../Model/saved_models/05_adaboost-all_features.joblib"
loaded_model = joblib.load(MODEL_PATH)


def predict_failure(
    product_type,
    rotational_speed,
    torque,
    tool_wear,
    air_temp,
    process_temp,
):
    global loaded_model

    # Product type: ordinal mapping str -> int
    product_mapping = {"Low": 0, "Medium": 1, "High": 2}
    product_type = product_mapping[product_type]

    # Temperature: Kelvin -> Celsius, create temperature difference features
    air_temp = air_temp - 273.15
    process_temp = process_temp - 273.15
    temp_diff = process_temp - air_temp
    temp_diff_above_threshold = int(temp_diff > 8.5)

    # Create power features using rotational speed and torque
    power = (rotational_speed * 0.10472) * torque
    power_out_of_range = int(power <= 3500 or power >= 9000)

    # Create strain features using torque and tool wear
    strain = tool_wear * torque
    strain_below_11k = int(strain <= 11000)
    strain_above_12k = int(strain >= 12000)

    data = [
        [
            product_type,
            rotational_speed,
            torque,
            tool_wear,
            air_temp,
            process_temp,
            temp_diff,
            temp_diff_above_threshold,
            power,
            power_out_of_range,
            strain,
            strain_below_11k,
            strain_above_12k,
        ]
    ]

    prediction = loaded_model.predict(data).squeeze()
    proba = loaded_model.predict_proba(data).squeeze()[prediction]

    return prediction, proba


# App UI
st.title("Predictive Maintenance of Equipment :gear: :hammer_and_wrench:")

with st.form(key="inference"):
    st.subheader("Tool parameters")
    tool_col1, tool_col2 = st.columns(
        spec=[0.3, 0.7], gap="medium", vertical_alignment="center"
    )

    with tool_col1:
        product_type = st.radio(
            label="Product Type (Quality)",
            options=["Low", "Medium", "High"],
            horizontal=True,
        )

    with tool_col2:
        tool_wear = st.slider(
            label="Tool wear (min)",
            min_value=0,
            max_value=300,
            value=100,
            step=1,
        )

    st.subheader("Operational parameters")
    op_col1, op_col2 = st.columns(
        spec=[0.5, 0.5], gap="small", vertical_alignment="center"
    )

    with op_col1:
        rotational_speed = st.slider(
            label="Rotational speed [RPM]",
            min_value=1000,
            max_value=3000,
            value=2000,
            step=1,
        )

    with op_col2:
        torque = st.slider(
            label="Torque (Nm)",
            min_value=0.0,
            max_value=100.0,
            value=40.0,
            step=0.1,
        )

    st.subheader("Temperature parameters")
    temp_col1, temp_col2 = st.columns(
        spec=[0.5, 0.5], gap="small", vertical_alignment="center"
    )

    with temp_col1:
        air_temp = st.slider(
            label="Air temperature (Kelvin)",
            min_value=290.0,
            max_value=310.0,
            value=300.0,
            step=0.1,
        )

    with temp_col2:
        process_temp = st.slider(
            label="Process temperature (Kelvin)",
            min_value=290.0,
            max_value=310.0,
            value=300.0,
            step=0.1,
        )

    result_col1, result_col2 = st.columns(
        spec=[0.25, 0.75], gap="large", vertical_alignment="center"
    )
    with result_col1:
        submitted = st.form_submit_button(
            label="Predict machine failure :mag:",
            type="primary",
        )

    with result_col2:
        if submitted:
            prediction, proba = predict_failure(
                product_type,
                rotational_speed,
                torque,
                tool_wear,
                air_temp,
                process_temp,
            )

            if prediction:
                prediction = ":red[Yes]"
            else:
                prediction = ":green[No]"

            st.subheader(
                f"Prediction: {prediction} (Confidence: {proba*100:.2f}%)"
            )
