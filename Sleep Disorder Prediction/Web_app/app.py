import streamlit as st 
from streamlit_navigation_bar import st_navbar
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder


st.set_page_config(page_title="Snooze Monitor",page_icon="😴",layout="wide")

styles = {
     "nav": {
        "background-color": "#83c9ff",
    },
    "div": {
        "max-width": "32rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(49, 51, 63)",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "#7bf8ff",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}
selected_page = st_navbar(pages=["Predict","EDA"],styles=styles)

df=pd.read_csv('data.csv')

if selected_page=="Predict":
    st.title("Sleep Disorder Prediction")
    def preprocess_blood_pressure(bp_str):
        systolic, diastolic = bp_str.split('/')
        return float(systolic), float(diastolic)

    df[['Systolic Pressure', 'Diastolic Pressure']] = df['Blood Pressure'].apply(lambda x: pd.Series(preprocess_blood_pressure(x)))
    df.drop(columns=['Blood Pressure'], inplace=True)

    X = df.drop(columns=['Person ID','Gender','Age','Gender','Quality of Sleep','Occupation','Sleep Disorder'])
    y = df['Sleep Disorder']

    label_encoder1 = LabelEncoder()
    X['BMI Category']= label_encoder1.fit_transform(X['BMI Category'])

    bmi_mapping = {i: label for i, label in enumerate(label_encoder1.classes_)}


    label_encoder2= LabelEncoder()
    y = label_encoder2.fit_transform(y)

    label_mapping = {i: label for i, label in enumerate(label_encoder2.classes_)}

    model = DecisionTreeClassifier()
    model.fit(X,y)

    with st.sidebar:
        sleep=st.slider('Sleep Duration in hrs',value=6.5,min_value=4.0,max_value=10.0,step=0.5)
        phy=st.slider('Physical Activity Level',value=5,min_value=1,max_value=10)
        stress=st.slider('Stress Level',value=5,min_value=1,max_value=10)
        weight=st.number_input("Weight in Kgs",value=60.0,min_value=40.0,max_value=150.0,step=0.5)
        height=st.number_input("Height in cm",value=160.0,min_value=130.0,max_value=200.0,step=0.5)
        bmi=weight/((height/100)**2)
        if bmi<18.5: 
            bmi_label=0
            bmi_category="Under Weight"
            st.warning(bmi_category)
        elif 18.5<=bmi<=24.9: 
            bmi_label=1
            bmi_category="Healthy Weight"
            st.success(bmi_category)
            
        elif 25<=bmi<=30: 
            bmi_label=3
            bmi_category="Over Weight"
            st.info(bmi_category)
            
        else: 
            bmi_label=2
            bmi_category="Obese"
            st.error(bmi_category)
            
        
        heart=st.slider('Heart rate',value=70,min_value=60,max_value=120)
        steps=st.slider('Daily Walking Steps',value=6000,min_value=2000,max_value=12000,step=500)
        st.write("Enter Blood Pressure")
        col1,col2,col3=st.columns([0.3,0.2,0.3])
        with col1:
            sys=st.number_input(label="Systolic pressure",value=120,min_value=110,max_value=160)
        with col2: 
            st.write(" ")
            st.markdown("<h1 style='text-align: center;'>/</h1>", unsafe_allow_html=True)
        with col3:
            dia=st.number_input(label="Diastolic Pressure",value=80,min_value=60,max_value=100)
        user_input=[sleep,phy,stress,bmi_label,heart,steps,sys,dia]    
        user_df = pd.DataFrame([user_input], columns=['Sleep Duration', 'Physical Activity Level', 'Stress Level', 'BMI Category', 'Heart Rate', 'Daily Steps', "Sis","Dia"])
        user_df["BMI Category"]=bmi_category
        
        user_df["Blood Pressure"]=str(sys)+'/'+str(dia)
        user_df=user_df.drop(columns=["Sis","Dia"])
        
        user_input = np.array(user_input).reshape(1, -1)
        prediction = model.predict(user_input)
        
        # print(prediction)
        # print(f"Predicted Sleep Disorder: {label_mapping[prediction[0]]}")
    
    st.subheader("User Data")
    df_transposed = user_df.transpose().reset_index()
    df_transposed.columns = ['Metric', 'Value']
    df_transposed['Value'] = df_transposed['Value'].apply(lambda x: f"{x:.1f}" if isinstance(x, (int, float)) else x)
    st.table(df_transposed)
        
    pred_label=label_mapping[prediction[0]]
    if stress>7:
            pred_label="Insomnia"
            if sleep<5:
                pred_label="Sleep_Anemia"
    res_length=len(pred_label)
    width = 100
    font_size = 30
    if res_length>6:
        width=200
    padding_top = 5
    padding_bottom = 2
    style = f"background-color: grey; height: 60px; width: {width}px; border-radius: 5px; padding-top: {padding_top}px; padding-bottom: {padding_bottom}px; margin-left: 200px; text-align: center; margin-top:-50px;"

    label_style = "font-weight: bold; color: white; font-size: {font_size}px;"

    label_style = label_style.format(font_size=font_size)
    st.markdown(f"<span style='color: blue; font-size: 18px;'><p style='margin-top:30px;'><strong>Sleep Disorder Report:</strong></p></span><div style='{style}'><label style='{label_style}'>{pred_label}</label></div>", unsafe_allow_html=True)

else:
    st.title("Exploratory Data Analysis (EDA) - Sleep Health and Lifestyle Dataset")
    with st.expander("About the Dataset"):
        st.subheader("Dataset")
        st.table(df.head())
        st.markdown("Get complete dataset from [here](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset)")
        
    
    
    age_groups = []
    for i in range(min(df['Age']),max(df['Age']),5):
        age_group = f"{i}-{i+4}"
        age_groups.append(age_group)
    col1,col2=st.columns(2)
    with col1:
        gender_counts = df['Gender'].value_counts()
        custom_colors = ['#1f77b4', '#ff7f0e']
        fig = go.Figure(
            go.Pie(
                labels=gender_counts.index,
                values=gender_counts.values,
                hole=0.3,
                textinfo='percent+label',
            )
        )

        fig.update_layout(
            title='Gender Distribution',
            showlegend=False
        )

        st.plotly_chart(fig)
    
    with col2:
        bmi_count = df['BMI Category'].value_counts()
        custom_colors=['#0068c9','#ffabab','#83c9ff','#ff2b2b']
        fig = go.Figure(
            go.Pie(
                labels=bmi_count.index,
                values=bmi_count.values,
                hole=0.3,
                textinfo='percent+label',
                marker=dict(colors=custom_colors)
                )
        )

        fig.update_layout(
            title='BMI Categories Distribution',
            showlegend=False
        )

        st.plotly_chart(fig)
    
        
    occupation_counts = df['Occupation'].value_counts()
    fig = go.Figure(
        go.Bar(
            x=occupation_counts.index,
            y=occupation_counts.values
        )
    )
    fig.update_layout(
        title='Occupation Distribution',
        xaxis_title='Occupation',
        yaxis_title='Count',
        xaxis_tickangle=-45
    )
    st.plotly_chart(fig)
    
    
    heart_rates = []
    for i in range(min(df['Age']),max(df['Age']),5):
        age_group_df = df[(df['Age'] >= i) & (df['Age'] <= i+4)]
        heart_rate = age_group_df['Heart Rate'].mean()
        heart_rates.append(heart_rate)
    fig = go.Figure(
    go.Scatter(
        x=age_groups,
        y=heart_rates,
        mode='markers+lines',
        marker=dict(symbol='star')))

    fig.update_layout(
        title='Average Heart Rate by Age Group',
        xaxis_title='Age Group',
        yaxis_title='Average Heart Rate'
    )

    st.plotly_chart(fig)
    
    stress_level = []
    for i in range(min(df['Age']),max(df['Age']),5):
        age_group_df = df[(df['Age'] >= i) & (df['Age'] <= i+4)]
        x = age_group_df['Stress Level'].mean()
        stress_level.append(x)
    fig = go.Figure(
    go.Scatter(
        x=age_groups,
        y=stress_level,
        mode='markers+lines',
        marker=dict(symbol='star')))

    fig.update_layout(
        title='Average Stress Activity Level',
        xaxis_title='Age Group',
        yaxis_title='Average Stress Level'
    )

    st.plotly_chart(fig)
    
    
    gender_sleep_disorder_counts = df.groupby(['Gender', 'Sleep Disorder']).size().unstack()
    traces = []
    for sleep_disorder_status in gender_sleep_disorder_counts.columns:
        trace = go.Bar(
            x=gender_sleep_disorder_counts.index,
            y=gender_sleep_disorder_counts[sleep_disorder_status],
            name=sleep_disorder_status
        )
        traces.append(trace)

    layout = go.Layout(
        title='Distribution of Sleep Disorder by Gender',
        xaxis=dict(title='Gender'),
        yaxis=dict(title='Count'),
        barmode='group'
    )

    fig = go.Figure(data=traces, layout=layout)
    st.plotly_chart(fig)
    
    occupation_sleep_disorder_counts = df.groupby(['Occupation', 'Sleep Disorder']).size().unstack()

    traces = []
    for sleep_disorder_status in occupation_sleep_disorder_counts.columns:
        trace = go.Bar(
            x=occupation_sleep_disorder_counts.index,
            y=occupation_sleep_disorder_counts[sleep_disorder_status],
            name=sleep_disorder_status
        )
        traces.append(trace)

    layout = go.Layout(
        title='Occupation by Sleep Disorder',
        xaxis=dict(title='Occupation'),
        yaxis=dict(title='Count')
    )

    fig = go.Figure(data=traces, layout=layout)

    st.plotly_chart(fig)
    
    avg_stress_by_occupation = df.groupby('Occupation')['Stress Level'].mean().reset_index()

    color_scale = [[0, 'blue'], [0.25, 'green'], [0.5, 'yellow'], [0.75, 'orange'], [1, 'red']]

    fig1 = go.Figure(go.Bar(
        x=avg_stress_by_occupation['Stress Level'],
        y=avg_stress_by_occupation['Occupation'],
        marker=dict(color=avg_stress_by_occupation['Stress Level'],
                    coloraxis='coloraxis'),
        orientation='h',
        hoverinfo='x+y',
        textposition='inside',
        texttemplate='%{x:.2f}',
    ))

    fig1.update_layout(
        title='Average Stress Level by Occupation',
        yaxis=dict(title='Occupation', tickangle=-30),
        xaxis=dict(title='Average Stress Level'),
        bargap=0.15,
        font=dict(family='Arial', size=12, color='rgb(50, 50, 50)'),
        coloraxis=dict(colorscale=color_scale, cmin=1, cmax=10),
    )

    st.plotly_chart(fig1)
    
    
    fig = go.Figure()
    custom_colors={"Male":"#0068c9","Female":"#ff2b2b"}
    for gender, group in df.groupby('Gender'):
        fig.add_trace(go.Histogram(
            x=group['Stress Level'],
            histnorm='probability density',
            name=gender,
             marker=dict(color=custom_colors[gender]),
            opacity=0.8
        ))

    fig.update_layout(
        title='Stress Level by Gender',
        xaxis=dict(title='Stress Level'),
        yaxis=dict(title='Probability Density'),
        barmode='overlay'
    )

    st.plotly_chart(fig)