import joblib
import streamlit as st

MODEL_PATH = "../Model/saved_models/02_adaboost_Extended.joblib"
loaded_model = joblib.load(MODEL_PATH)


def predict_completion(
    course_category,
    device_type,
    num_videos,
    num_quizzes,
    quiz_scores,
    time_spent,
    completion_rate,
):
    global loaded_model

    # One-hot encoding Course Category
    course_Arts = 0
    course_Business = 0
    course_Health = 0
    course_Programming = 0
    course_Science = 0
    if course_category == "Business :chart_with_upwards_trend":
        course_Business = 1
    elif course_category == "Health :syringe:":
        course_Health = 1
    elif course_category == "Programming :computer:":
        course_Programming = 1
    elif course_category == "Science :test_tube:":
        course_Science = 1
    elif course_category == "Arts :lower_left_paintbrush:":
        course_Arts = 1
    else:
        pass

    # Device type mapping
    device_type_code = -1
    if device_type == "Desktop :desktop_computer:":
        device_type_code = 0
    elif device_type == "Mobile :iphone:":
        device_type_code = 1
    else:
        pass

    # Discretizing continuous features
    time_spent_above_threshold = 1 if time_spent > 20 else 0
    num_videos_above_threshold = 1 if num_videos > 5 else 0
    num_quizzes_above_threshold = 1 if num_quizzes > 3 else 0
    quiz_scores_above_threshold = 1 if quiz_scores > 68 else 0
    completion_above_threshold = 1 if completion_rate > 60 else 0

    data = [
        [
            time_spent,
            num_videos,
            num_quizzes,
            quiz_scores,
            completion_rate,
            device_type_code,
            course_Arts,
            course_Business,
            course_Health,
            course_Programming,
            course_Science,
            time_spent_above_threshold,
            num_videos_above_threshold,
            num_quizzes_above_threshold,
            quiz_scores_above_threshold,
            completion_above_threshold
        ]
    ]

    prediction = loaded_model.predict(data).squeeze()
    proba = loaded_model.predict_proba(data).squeeze()[prediction]

    return prediction, proba


# App UI
st.title(
    "Predicting Online Course Engagement :desktop_computer: :student: :iphone:"
)

with st.form(key="inference"):
    cat_1, cat_2 = st.columns(
        spec=[0.25, 0.75], gap="medium", vertical_alignment="center"
    )

    with cat_1:
        device_type = st.radio(
            label="Device Type",
            options=["Desktop :desktop_computer:", "Mobile :iphone:"],
            horizontal=True,
        )

    with cat_2:
        course_category = st.radio(
            label="Course Category",
            options=[
                "Business :chart_with_upwards_trend",
                "Health :syringe:",
                "Programming :computer:",
                "Science :test_tube:",
                "Arts :lower_left_paintbrush:",
            ],
            horizontal=True,
        )

    effort_1, effort_2 = st.columns(
        spec=[0.5, 0.5], gap="small", vertical_alignment="center"
    )

    with effort_1:
        num_videos = st.slider(
            label="Number of videos watched",
            min_value=0,
            max_value=20,
            value=5,
            step=1,
        )

    with effort_2:
        time_spent = st.slider(
            label="Time spent on course (hours)",
            min_value=0.0,
            max_value=100.0,
            value=50.0,
            step=0.1,
        )

    quiz_1, quiz_2 = st.columns(
        spec=[0.5, 0.5], gap="small", vertical_alignment="center"
    )

    with quiz_1:
        num_quizzes = st.slider(
            label="Number of quizzes taken",
            min_value=0,
            max_value=10,
            value=5,
            step=1,
        )

    with quiz_2:
        quiz_scores = st.slider(
            label="Quiz scores",
            min_value=0.0,
            max_value=100.0,
            value=50.0,
            step=0.1,
        )

    completion_rate = st.slider(
        label="Completion rate",
        min_value=0.0,
        max_value=100.0,
        value=50.0,
        step=0.1,
    )

    predict_col1, predict_col2 = st.columns(
        spec=[0.25, 0.75], gap="large", vertical_alignment="center"
    )
    with predict_col1:
        submitted = st.form_submit_button(
            label="Predict completion status :student:",
            type="primary",
        )

    with predict_col2:
        if submitted:
            prediction, proba = predict_completion(
                course_category,
                device_type,
                num_videos,
                num_quizzes,
                quiz_scores,
                time_spent,
                completion_rate,
            )

            if prediction:
                prediction = ":green[Completed!]"
            else:
                prediction = ":red[Not completed...]"

            st.subheader(
                f"Prediction: {prediction} (Confidence: {proba*100:.2f}%)"
            )
