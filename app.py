import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('employee_salary_prediction.pkl')

st.set_page_config(page_title='Employee Salary Predictor', page_icon='💼', layout= 'centered', initial_sidebar_state= 'expanded')

st.title('💼 Employee Salary Prediction')

st.markdown("""
<p style="
    font-size:20px;
    color:#2F3A4A;
    text-align:center;
    font-weight:500;
    margin-top:-10px;
    margin-bottom:35px;
">
Predict employee salaries based on experience, job role, company details, and work preferences
</p>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
    font-size:30px;
    color:#2F3A4A;
    text-align:left;
    font-weight:500;
    margin-top:-10px;
    margin-bottom:20px;
">
👤 Employee Information
</p>
""", unsafe_allow_html=True)



# Inputs

col1, col2 = st.columns(2 , gap= 'xxlarge')

with col1:

    work_year = st.number_input('📅 Work Year', 2020, 2030, 2026)



    experience_options = {
    "Entry Level (EN)" : "EN",
    "Mid Level (MI)" : "MI",
    "Senior Level (SE)" : "SE",
    "Executive Level (EX)" : "EX"
    }
    experience_level = st.selectbox(
    '👨‍💻 Experience Level',
    list(experience_options.keys())
    )



    employment_options={
    "Full Time (FT)" : "FT",
    "Part Time (PT)" : "PT",
    "Contract (CT)" : "CT",
    "Freelance (FL)" : "FL"
    }
    employment_type = st.selectbox(
    '💼 Employment Type',
    list(employment_options.keys())
    )




    remote_type = st.selectbox(
    '🏠 Remote Type',
    ['On-site', 'Remote', 'Hybrid']
        )


with col2:

    job_title = st.selectbox(
    '🧑‍💼 Job Title',
    ['Data Scientist', 'Data Analyst', 'ML Engineer', 'Data Engineer', 'Machine Learning Scientist', 'Big Data Engineer', 'Product Data Analyst', 'Lead Data Scientist', 'Business Data Analyst', 'Lead Data Engineer', 'Lead Data Analyst', 'Data Science Consultant', 'BI Data Analyst', 'Director of Data Science', 'Research Scientist', 'Data Engineering Manager', 'Machine Learning Infrastructure Engineer', 'AI Scientist', 'Computer Vision Engineer', 'Principal Data Scientist']
    )




    location_options={
     "United State (North America)" : "US",
    "Canada (North America)" : "CA",

    "India (Asia)" : "IN",
    "Japan (Asia)" : "JP",
    "Singapore (Asia)" : "SG",
    "China (Asia)" : "CN",

    "United Kingdom (Europe)" : "GB",
    "Germany (Europe)" : "DE",
    "France (Europe)" : "FR",
    "Spain (Europe)" : "ES",
    "Netherlands (Europe)" : "NL",

    "Others" : "HN , PK"
    }
    company_location = st.selectbox(
    '🌍 Company Location',
        list(location_options.keys())
    )




    size_options={
    "Small": "S", "Medium": "M", "Large": "L"
    }
    company_size = st.selectbox(
    '🏢 Company Size',
    list(size_options.keys())
    )



# Engineered features

experience_mapping = {
    "Entry Level (EN)": 0,
    "Mid Level (MI)": 4,
    "Senior Level (SE)": 7,
    "Executive Level (EX)": 12}
experience_years = experience_mapping[experience_level]



region_mapping = {
    'US': 'North America',
    'CA': 'North America',
    'IN': 'Asia',
    'GB': 'Europe',
    'DE': 'Europe'
}
company_region = region_mapping.get(company_location, 'Other')


company_size_mapping = {'Small': 1, 'Medium': 2, 'Large': 3}
company_size_score = company_size_mapping[company_size]


remote_mapping={
    "On-site":0, "Hybrid":50, "Remote":100
}
remote_ratio = remote_mapping[remote_type]

# Create dataframe
new_employee = pd.DataFrame({
    'work_year': [work_year],
    'experience_level': [experience_level],
    'employment_type': [employment_type],
    'job_title': [job_title],
    'employee_residence': [company_location],
    'remote_ratio': [remote_ratio],
    'remote_type': [remote_type],
    'company_location': [company_location],
    'company_size': [company_size],
    'experience_years': [experience_years],
    'company_region': [company_region],
    'company_size_score': [company_size_score]
})

# Predict
if st.button('🚀 Predict Salary'):
    prediction = model.predict(new_employee)


    st.markdown(f"""
<div style="
background: rgba(255,255,255,0.25);
backdrop-filter: blur(20px);
border-radius:25px;
padding:30px;
border:1px solid rgba(255,255,255,.3);
box-shadow:0 10px 30px rgba(0,0,0,.2);
text-align:center;
">

<h2 style="color:#2563EB;font-size:34px;">
💼 Estimated Salary
</h2>

<h1 style="
font-size:58px;
color:#111827;
">
${prediction[0]:,.0f}
</h1>

<p style="font-size:22px;">
per year
</p>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<style>
        [data-testid="stAppViewContainer"]{
            background-color:#B0E0E6;
            }
/* Main App */
.main{
    background-color: #89CFF0;
}

/* Title */
.title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color: #0E4C92;
}

/* Subtitle */
.subtitle{
    text-align:center;
    font-size:30px;
    color:grey;
    margin-bottom:30px;
}

/* Input Containers */
div[data-testid="stVerticalBlock"]{
    border-radius:12px;
    
}
            
/* Selectbox */
.stSelectbox div[data-baseweb="select"] {
    background-color: #f5f5f5;
    border-radius: 10px;
    border: 2px solid black;
    color: black;
    font-size:18px;
    font-weight:bold;
    width:350px
    
}
            
/* Input boxes */
.stNumberInput input {
    background-color: #f5f5f5;
    color: black;
    border-radius: 10px;
    border: 2px solid black;
    font-size: 18px;
    font-weight:bold;
}
            
/* Labels */
label {
    
    color: white !important;
    background-color: #1E3A8A;
    padding: 5px 10px;
    border-radius: 8px;
    width:350px
}
label p{
    font-size: 20px !important;
    font-weight: bold !important;
    text-align: center;
            }

/* Button */
.stButton>button{
    background-color:#0E4C92;
    color:white;
    height:100px;
    width:400px;
    border:none;
    border-radius:10px;
    font-size:50px !important;
    font-weight:bold;
}

.stButton>button:hover{
    background-color:#2563EB;
}

button p{
    font-size: 30px !important;
    font-weight: bold !important;
    text-align: center;
            }

/* Success Box */
div[data-testid="stAlert"]{
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)


with st.sidebar:

    st.title("📊 About")

    st.info("""
This application predicts employee salaries using a Random Forest Regressor.

Features:

✔ Professional UI

✔ Feature Engineering

✔ Machine Learning

✔ Streamlit Deployment
""")

    st.markdown("---")
    st.success("Developer")
    st.write("Anushka Sinha")


st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("🤖 Model\n\nRandom Forest")

with col2:
    st.info("📈 Accuracy\n\n95%")

with col3:
    st.info("🌎 Dataset\n\nAI Jobs Salary Dataset")


