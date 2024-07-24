import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize-matplotlib

# Load the data
file_path = '/mnt/data/202406_202406_연령별인구현황_월간 (2).csv'
data = pd.read_csv(file_path, encoding='cp949')

# Extract necessary columns and preprocess data
data.columns = data.columns.str.strip()
data = data.rename(columns={data.columns[0]: 'Region'})
age_columns = data.columns[3:]

# Define age range for middle school students (12-14 years old)
middle_school_ages = ['2024년06월_계_12세', '2024년06월_계_13세', '2024년06월_계_14세']

# Streamlit app
st.title("지역별 중학생 인구 비율")

# User input for region
region = st.selectbox('원하는 지역을 선택하세요:', data['Region'].unique())

# Filter data for the selected region
region_data = data[data['Region'] == region]

if not region_data.empty:
    total_population = region_data.iloc[0, 1]
    middle_school_population = region_data[middle_school_ages].sum(axis=1).values[0]
    
    # Calculate the proportion
    middle_school_percentage = (middle_school_population / total_population) * 100
    
    # Plotting
    labels = ['중학생 인구', '기타 인구']
    sizes = [middle_school_percentage, 100 - middle_school_percentage]
    colors = ['#ff9999','#66b3ff']
    explode = (0.1, 0)  # explode 1st slice
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)
else:
    st.write("선택한 지역의 데이터가 없습니다.")
