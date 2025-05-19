
import streamlit as st
import pandas as pd
import numpy as np
import warnings

# 標題
st.title("Sports Performance Dashboard") #This function allows you to add the title of the app. 

# 讀取 CSV 檔案（請確認資料夾中有該檔案）
file_path = "bodyPerformance.csv"
df = pd.read_csv(file_path)

#st.header() This function is used to set header of a section. 

# 側邊欄篩選器
st.sidebar.header("篩選條件")

# 篩選性別選項
gender_options = ["All"] + df['gender'].unique().tolist()
selected_gender = st.sidebar.selectbox("選擇性別", gender_options)

# 篩選年齡範圍選項
min_age = int(df['age'].min())
max_age = int(df['age'].max())
selected_age_range = st.sidebar.slider("選擇年齡範圍", min_age, max_age, (min_age, max_age))

# 資料篩選邏輯
if selected_gender == "All":
    filtered_df = df[(df['age'] >= selected_age_range[0]) & (df['age'] <= selected_age_range[1])]
else:
    filtered_df = df[
        (df['gender'] == selected_gender) &
        (df['age'] >= selected_age_range[0]) &
        (df['age'] <= selected_age_range[1])
    ]

# 顯示結果
st.subheader("篩選後的資料") #This function is used to set sub-header of a section
st.dataframe(filtered_df)



